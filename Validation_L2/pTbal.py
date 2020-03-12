
#!/usr/bin/env python
import ROOT 
import math
import numpy as np
import os
import lep2_samples_2017 as samples
import os,sys,json,time,re

def get_empty_hist(name, title):
	hist = ROOT.TH1D(name, title, 25, 0, 2)
	return hist

def get_hist(path2input, filename, lep, data = 0):

	ROOT.gInterpreter.ProcessLine('#include "../interface/lester_mt2_bisect.h"')
        ROOT.gSystem.Load("libHiggsAnalysisbbggLimits2018")
        biss = ROOT.asymm_mt2_lester_bisect()

	if lep == 'mu':
		lep_type = 0
	elif lep == 'el':
		lep_type = 1
	else:
		lep_type = -1

	input_file = ROOT.TFile(path2input + filename, 'READ')
	input_tree = input_file.Get('Events')	
	hist = get_empty_hist('hist', '')
        hist.Sumw2()

        bjet1_DeepCSV	= np.empty(1, dtype='float32')  
	bjet1_PtReg	= np.empty(1, dtype='float32')  
	bjet1_eta	= np.empty(1, dtype='float32') 
	bjet1_phi	= np.empty(1, dtype='float32')   
	bjet1_mass	= np.empty(1, dtype='float32')

        bjet2_DeepCSV	= np.empty(1, dtype='float32')  
	bjet2_PtReg	= np.empty(1, dtype='float32')  
	bjet2_eta	= np.empty(1, dtype='float32') 
	bjet2_phi	= np.empty(1, dtype='float32')   
	bjet2_mass	= np.empty(1, dtype='float32')

	input_tree.SetBranchAddress("bjet1_DeepCSV", bjet1_DeepCSV)
	input_tree.SetBranchAddress("bjet1_PtReg", bjet1_PtReg)
	input_tree.SetBranchAddress("bjet1_eta"	, bjet1_eta)
	input_tree.SetBranchAddress("bjet1_phi"	, bjet1_phi)
	input_tree.SetBranchAddress("bjet1_mass", bjet1_mass)
	
	input_tree.SetBranchAddress("bjet2_DeepCSV", bjet2_DeepCSV)
	input_tree.SetBranchAddress("bjet2_PtReg", bjet2_PtReg)
	input_tree.SetBranchAddress("bjet2_eta"	, bjet2_eta)
	input_tree.SetBranchAddress("bjet2_phi"	, bjet2_phi)
	input_tree.SetBranchAddress("bjet2_mass", bjet2_mass)

	lep1_pt		= np.empty(1, dtype='float32')  
	lep1_eta	= np.empty(1, dtype='float32') 
	lep1_phi	= np.empty(1, dtype='float32')   
	lep1_mass	= np.empty(1, dtype='float32')

	lep2_pt		= np.empty(1, dtype='float32')  
	lep2_eta	= np.empty(1, dtype='float32') 
	lep2_phi	= np.empty(1, dtype='float32')   
	lep2_mass	= np.empty(1, dtype='float32')

	input_tree.SetBranchAddress("lep1_pt"	, lep1_pt)
	input_tree.SetBranchAddress("lep1_eta"	, lep1_eta)
	input_tree.SetBranchAddress("lep1_phi"	, lep1_phi)
	input_tree.SetBranchAddress("lep1_mass"	, lep1_mass)
	
	input_tree.SetBranchAddress("lep2_pt"	, lep2_pt)
	input_tree.SetBranchAddress("lep2_eta"	, lep2_eta)
	input_tree.SetBranchAddress("lep2_phi"	, lep2_phi)
	input_tree.SetBranchAddress("lep2_mass"	, lep2_mass)

	MET_Pt	= np.empty(1, dtype='float32')
	MET_phi	= np.empty(1, dtype='float32')
	weight	= np.empty(1, dtype='float32')	
	H_mass 	= np.empty(1, dtype='float32')	
	Vtype	= np.empty(1, dtype='int32')	
	
	
	input_tree.SetBranchAddress("MET_Pt"	, MET_Pt)
	input_tree.SetBranchAddress("MET_phi"	, MET_phi)
	input_tree.SetBranchAddress("weight"	, weight)
	input_tree.SetBranchAddress("Vtype"		, Vtype)
	input_tree.SetBranchAddress("H_mass"	, H_mass)


	n_events = input_tree.GetEntries()
	n_events_v_cat = 0
	for event in range(0, n_events):
		input_tree.GetEntry(event)
		bp1 = ROOT.TLorentzVector()
		bp1.SetPtEtaPhiM(bjet1_PtReg[0],bjet1_eta[0],bjet1_phi[0],bjet1_mass[0])
		
		bp2 = ROOT.TLorentzVector()
		bp2.SetPtEtaPhiM(bjet2_PtReg[0],bjet2_eta[0],bjet2_phi[0],bjet2_mass[0])
		
		ep1 = ROOT.TLorentzVector()
		ep1.SetPtEtaPhiM(lep1_pt[0],lep1_eta[0],lep1_phi[0],lep1_mass[0])
		
		ep2 = ROOT.TLorentzVector()
		ep2.SetPtEtaPhiM(lep2_pt[0],lep2_eta[0],lep2_phi[0],lep2_mass[0])

                


		bp = bp1 + bp2
		ep = ep1 + ep2


		ej11 = bp1 + ep1
		ej12 = bp1 + ep2
		ej21 = bp2 + ep1
		ej22 = bp2 + ep2

                mVisA =  ej11.M()
                pxA = ej11.Px()
                pyA = ej11.Py()

                mVisB =  ej22.M()
                pxB = ej22.Px()
                pyB = ej22.Py()

                if mVisA + mVisB > ej12.M() + ej21.M():
                        mVisA =  ej12.M()
                        pxA = ej12.Px()
                        pyA = ej12.Py()

                        mVisB =  ej21.M()
                        pxB = ej21.Px()
                        pyB = ej21.Py()
#                        print "mVisA = ", mVisA, " mVisB = ", mVisB

#                mVisA =  bp1.M()
#                pxA = bp1.Px()
#                pyA = bp1.Py()

#                mVisB =  bp2.M()
#                pxB = bp2.Px()
#                pyB = bp2.Py()
                pxMiss = MET_Pt*math.cos(MET_phi)#+ep1.Px()+ep2.Px()
                pyMiss = MET_Pt*math.sin(MET_phi)#+ep1.Py()+ep2.Py()
#                print "ep1.Px() = ", ep1.Px()
                chiA = 0.1; # hypothesised mass of invisible on side A.  Must be >=0.
                chiB = 0.1; # hypothesised mass of invisible on side B.  Must be >=0.

                desiredPrecisionOnMt2 = 0; # Must be >=0.  If 0 alg aims for machine precision.  if >0, MT2 computed to supplied absolute precision. # asymm_mt2_lester_bisect::disableCopyrightMessage(

                MT2 =  biss.get_mT2(
                        mVisA, pxA, pyA,
                        mVisB, pxB, pyB,
                        pxMiss, pyMiss,
                        chiA, chiB,
                        desiredPrecisionOnMt2)

#                print "here is MT2!!! = ", MT2








		bb_pt = bp.Pt()
		ee_pt = ep.Pt()
		bb_phi = bp.Phi()
		ee_phi = ep.Phi()	
		ee_m = ep.M()
		d_phi = abs(ROOT.TVector2.Phi_mpi_pi(bb_phi - ee_phi))
                dPhi_jj = abs(ROOT.TVector2.Phi_mpi_pi(bjet2_phi[0] - bjet1_phi[0]))
                dEta_jj = abs(bjet2_eta[0]-bjet1_eta[0])
                dR_jj = math.sqrt(dEta_jj*dEta_jj+dPhi_jj*dPhi_jj)
                
                if lep == 'lep':
#                hist.Fill(H_mass[0],(Vtype[0] == lep_type)*(dEta_jj<1.6)*(dR_jj>0.5)*(dR_jj < 3.2)*weight[0]*(bjet2_PtReg[0]>30)*(bjet2_DeepCSV>0.2)*(bjet1_DeepCSV>0.5)*(lep2_pt < 130)*(lep1_pt > 40)*(ee_m > 87)*(ee_m < 95))
                        hist.Fill(bb_pt/ee_pt,(dEta_jj<1.6)*(dR_jj>0.5)*(dR_jj < 3.2)*weight[0]*(bjet2_PtReg[0]>30)*(bjet2_DeepCSV>0.2)*(bjet1_DeepCSV>0.5)*(lep2_pt < 130)*(lep1_pt > 40))#*((MT2 > 170) + (MT2 < 110)))
                else:
                        hist.Fill(bb_pt/ee_pt,(Vtype[0] == lep_type)*(dEta_jj<1.6)*(dR_jj>0.5)*(dR_jj < 3.2)*weight[0]*(bjet2_PtReg[0]>30)*(bjet2_DeepCSV>0.2)*(bjet1_DeepCSV>0.5)*(lep2_pt < 130)*(lep1_pt > 40)*((MT2 > 170) + (MT2 < 120)))  

#                hist.Fill(H_mass[0],(ee_m > 88)*(ee_m < 93)*(Vtype[0] == lep_type)*weight[0])
#		if data == 0: 
#			hist.Fill(H_mass[0],(ee_m > 88)*(ee_m < 93)*(Vtype[0] == lep_type)*weight[0])
#		else:
#			hist.Fill(H_mass[0],weight[0]*(ee_m > 88)*(ee_m < 93))

	hist.SetDirectory(0)
	return hist
def draw(lep):

	c1 = ROOT.TCanvas('mbb','mbb')
	c1.cd()
	ROOT.gStyle.SetOptStat(0)	
	
	leg = ROOT.TLegend(0.7,0.5,0.85,0.85)
	leg.SetBorderSize(1)
	leg.SetTextSize(.04)

	filename_mu = 'skimmed_Run2017_DoubleMu_ReMiniAOD.root'
	filename_e = 'skimmed_Run2017_DoubleEle_ReMiniAOD.root'
	filename_l = 'skimmed_Run2017_DoubleLep_ReMiniAOD.root'
	path2input = "skim_bkg/"
	if lep == 'mu':
		filename = filename_mu
	elif lep == 'el':
		filename = filename_e
        else:
                filename = filename_l

	h_data = get_hist(path2input, filename, lep, data = 1 )
	h_data.SetMarkerStyle(8)
	h_data.SetMarkerColor(1)
	h_data.SetLineColor(1)
	h_data.GetXaxis().SetTitle('pT_bal')	
	h_data.Draw('PE')
        h_data.SetMinimum(0)
	leg.AddEntry(h_data,'Data','lep')
	hstack = ROOT.THStack('hs1','')
	buf_hist =  get_empty_hist('buf_hist', '')
	h_list = []
	bkg_files_list = []

        for smpl in samples.sample_colors:
                bkg_files_list.append([samples.get_bkg(smpl[0]), smpl[0], smpl[1]])
#	bkg_files_list.append([get_DY2B_bkg(),	'DY2B',	ROOT.kBlue])
#	bkg_files_list.append([get_DY2LL_bkg(),	'DY2LL',ROOT.kGreen])
	#bkg_files_list.append([get_ST_bkg(),	'ST',	ROOT.kMagenta])
#	bkg_files_list.append([get_TT_bkg(),	'TT',	ROOT.kCyan])
#	bkg_files_list.append([get_ZZ_bkg(),	'ZZ',	ROOT.kYellow])
	#bkg_files_list.append([get_WW_bkg(),	'WW',	ROOT.kOrange])
	
	for i, bkg_type in enumerate(bkg_files_list):
		buf_hist =  get_empty_hist('', '')	
		for bkg_item in bkg_type[0]:
                        print bkg_item 
			hist = get_hist(path2input, bkg_item, lep, data = 0)
                        C_corr = 1
#			if bkg_type[1] == 'DY2B':
#				C_corr = 2.9
#			else:
#				C_corr = 1
                        buf_hist.Add(hist, C_corr)
		        buf_hist.SetFillColor(bkg_files_list[i][2])
		        buf_hist.SetLineColor(1)
		        print buf_hist.GetEntries(), " hist int ", hist.Integral(), " tot int ", buf_hist.Integral()
                h_list.append(buf_hist)
	h_data_extrac_MC = get_empty_hist('data-MC','d-MC')
	h_data_extrac_MC.Add(h_data)
	
	for i, hist in enumerate(h_list):
		leg.AddEntry(hist,bkg_files_list[i][1],'f')
		hstack.Add(hist)
		if bkg_files_list[i][1] != 'ZZ':
			h_data_extrac_MC.Add(hist,-1)
	
	hstack.Draw('hist same')
	h_data.Draw('PE same')
	leg.Draw()
	c1.Update()
	c1.Modified()
#        c1.SaveAs(lep+'_mbb_detajj.root')
        c1.SaveAs(lep+'_pTbal.png')

	text = raw_input()
if __name__ == '__main__':
	draw('lep') # use 'mu' for drawing muon hist and 'el' for electron 'lep' for all leptons




