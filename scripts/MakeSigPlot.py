#!/usr/bin/env python

from ROOT import *
from HiggsAnalysis.bbggLimits2018.SigPlotter import *
import sys, getopt, os

def main(argv):
	gSystem.Load("libHiggsAnalysisCombinedLimit.so")

	wfile = ""
	cat = -1
	obs = ""
	lumi = ""
	doBands = 1
	analysis = ""
	bins = []
	xmax = {'mgg':140, 'mjj': 190}
        xmin = {'mgg':110, 'mjj': 70}
	outpath = "."

	try:
		opts, args = getopt.getopt(argv,"p:w:c:o:l:a:b:d",["outpath=","workspace=", "cat=", "observable=","lumi=","analysis=","bins=","dummy="])
	except getopt.GetoptError:
		print 'MakeBkgPlot.py -w <workspace file> -c <cat> -o <obs1,obs2,obs3> -l <lumi> -a <analysis title> -b <binobs1,binobs2>'
		sys.exit(2)
	for opt, arg in opts:
		print "opt ", opt, " arg", arg
		if opt == "-w":
			wfile = arg
		if opt == "-c":
			cat = arg
		if opt == "-o":
			obs = str(arg).split(',')
			if 'mjj' not in obs and 'mgg' not in obs:
				print 'Observable must be either mjj or mgg'
				sys.exit(2)
		if opt == "-b":
			arr = str(arg).split(',')
			for b in arr: bins.append(int(b))
		if opt == "-l":
			lumi = arg
		if opt == "-a":
			analysis = arg
		if opt == "-p":
			print "arg ", arg
			outpath = arg

	if wfile == "" or cat == -1 or obs == "" or lumi == "" or analysis == "" or outpath == "":
		print 'MakeBkgPlot.py -w <workspace file> -c <cat> -o <observable> -l <lumi> -a <analysis title>'
		sys.exit(2)


	Label = "cat"+str(cat)

	wroot = TFile(wfile, "READ")
	workspace = wroot.Get("w_all")

	print cat

	for i,ob in enumerate(obs):
		print "Start" 
#		data2D = workspace.data("Hig_vh_cat"+str(cat))
#		data2D = workspace.data("Hig_vbf_cat"+str(cat))
		data2D = workspace.data("Hig_ggh_cat"+str(cat))
#		data2D = workspace.data("Hig_tth_cat"+str(cat))
#		data2D = workspace.data("Hig_bbh_cat"+str(cat))
		data2D.Print()
#		pdf = workspace.pdf(ob+"Hig_vh_cat"+str(cat)+"_CMS_hig_vh_cat"+str(cat))
#		pdf = workspace.pdf(ob+"Hig_vbf_cat"+str(cat)+"_CMS_hig_vbf_cat"+str(cat))
		pdf = workspace.pdf(ob+"Hig_ggh_cat"+str(cat)+"_CMS_hig_ggh_cat"+str(cat))
#		pdf = workspace.pdf(ob+"Hig_tth_cat"+str(cat)+"_CMS_hig_tth_cat"+str(cat))
#		pdf = workspace.pdf(ob+"Hig_bbh_cat"+str(cat)+"_CMS_hig_bbh_cat"+str(cat))
		print ob+"Sig_cat"+str(cat)+"_CMS_sig_cat"+str(cat)
		pdf.Print()
		var = workspace.var(ob)
		data = data2D.reduce(RooArgSet(var))

		print "outpath = ", outpath

		label = "m_{jj} [GeV]"
		if 'mgg' in ob:
			label = "m_{#gamma#gamma} [GeV]"
#		MakeSigPlot(data, pdf, var, label, lumi, cat, analysis, doBands, Label+"_Hig_vh_fit_"+ob+"_cat"+str(cat), bins[i], xmin[ob], xmax[ob], outpath)
#		MakeSigPlot(data, pdf, var, label, lumi, cat, analysis, doBands, Label+"_Hig_vbf_fit_"+ob+"_cat"+str(cat), bins[i], xmin[ob], xmax[ob], outpath)
		MakeSigPlot(data, pdf, var, label, lumi, cat, analysis, doBands, Label+"_Hig_ggh_fit_"+ob+"_cat"+str(cat), bins[i], xmin[ob], xmax[ob], outpath)	
#		MakeSigPlot(data, pdf, var, label, lumi, cat, analysis, doBands, Label+"_Hig_tth_fit_"+ob+"_cat"+str(cat), bins[i], xmin[ob], xmax[ob], outpath)
#		MakeSigPlot(data, pdf, var, label, lumi, cat, analysis, doBands, Label+"_Hig_bbh_fit_"+ob+"_cat"+str(cat), bins[i], xmin[ob], xmax[ob], outpath)

if __name__ == "__main__":
	main(sys.argv[1:])

