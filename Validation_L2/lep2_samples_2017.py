import ROOT 

#   name                              index   scale     legend              input tokens (sample name in the previous step)
the_samples_dict = {
#    'Data':                           [0,      1.,     'Data',    ['Run2017_MET_MiniAOD', 'Run2017_Ele_ReMiniAOD','Run2017_Mu_ReMiniAOD','Run2017_DoubleEle_ReMiniAOD','Run2017_DoubleMu_ReMiniAOD']],
    'data_obs':                          [0,      1.,       'data_obs',             ['Run2017_DoubleMu_ReMiniAOD', 'Run2017_DoubleEle_ReMiniAOD']],
#    'data':                               [0,      1.,       'Data',        ['Run2018_DoubleEle','Run2018_DoubleMu','Run2018_Ele','Run2018_MET','Run2018_Mu']],
    'ZH125_Znn_powheg':                   [-12504, 1., 'VH',      ['ZH125_ZNuNu_powheg']],
    'ggZH125_Znn_powheg':                 [-12505, 1., 'VH',              ['ggZH125_ZNuNu_powheg']],
    'ZH125_ZLL_powheg':                   [-12502, 1., 'VH',      ['ZH125_ZLL_powheg']],
#    'ggZH125_ZLL_powheg':                 [-12503, 1., 'VH',              ['ggZH125_ZLL_powheg']],
    'WH125_WplusLNu_powheg':              [-12500, 1., 'VH',      ['WplusH125_powheg']],
    'WH125_WminusLNu_powheg':             [-12501, 1., 'VH',      ['WminusH125_powheg']],
    'TT_DiLep':                           [202,    1., 'TT',          ['TT_DiLep']],
    'TT_SingleLep':                       [203,    1., 'TT',          ['TT_SingleLep']],
    'TT_AllHadronic':                     [212,    1., 'TT',          ['TT_AllHadronic']],
    'TToLeptons_s':                       [16,     1., 's_Top',       ['ST_s-c_4f_lep_PSw']],
    'TToLeptons_t':                       [18,     1., 's_Top',       ['ST_t-c_top_4f_inc']],
#    'TBarToLeptons_t':                    [19,     1., 's_Top',       ['ST_t-c_antitop_4f_inc']],
    'T_tW':                               [20,     1., 's_Top',       ['ST_tW_top_5f_inc_PSw']],
    'Tbar_tW':                            [21,     1., 's_Top',       ['ST_tW_antitop_5f_inc']],
    'Z':                            [11000,  1., 'Zj0b',        ['DYToLL_madgraph']],
    'Z_bb_HT100To200':                    [11102,  1., 'Zj2b',        ['DYToLL_HT100to200_madgraph']],
    'Z_bb_HT200To400':                    [11202,  1., 'Zj2b',        ['DYToLL_HT200to400_madgraph']],
    'Z_bb_HT400To600':                    [11302,  1., 'Zj2b',        ['DYToLL_HT400to600_madgraph']],
    'Z_bb_HT600To800':                    [11402,  1., 'Zj2b',        ['DYToLL_HT600to800_madgraph']],
    'Z_bb_HT800To1200':                   [11502,  1., 'Zj2b',        ['DYToLL_HT800to1200_madgraph']],
    'Z_bb_HT1200To2500':                  [11602,  1., 'Zj2b',        ['DYToLL_HT1200to2500_madgraph']],
    'Z_bb_HT2500ToInf':                   [11702,  1., 'Zj2b',        ['DYToLL_HT2500toInf_madgraph']],
    'Z_udcsg_LowMHT100To200':             [12500,  1., 'Zj0b',        ['DYToLL_M4to50_HT100to200_madgraph']],
    'Z_udcsg_LowMHT200To400':             [12600,  1., 'Zj0b',        ['DYToLL_M4to50_HT200to400_madgraph']],
    'Z_bb_LowMHT400To600':                [12702,  1., 'Zj2b',        ['DYToLL_M4to50_HT400to600_madgraph']],
    'Z_udcsg_LowMHT600ToInf':             [12800,  1., 'Zj0b',        ['DYToLL_M4to50_HT600toInf_madgraph']],
    'DYBJets-Pt100To200_udcsg':           [12100,  1., 'Zj0b',        ['DYBJets-Pt100To200']],
    'DYBJets-Pt200ToInf_udcsg':           [12200,  1., 'Zj0b',        ['DYBJets-Pt200ToInf']],
    'DYJets-BGenFilter-Pt100To200_udcsg': [14100,  1., 'Zj0b',        ['DYJets-BGenFilter-Pt100To200']],
    'DYJets-BGenFilter-Pt200ToInf_udcsg': [14200,  1., 'Zj0b',        ['DYJets-BGenFilter-Pt200ToInf']],
    'W':                            [4000,   1., 'Wj',        ['WJets_madgraph']],
    'W_HT100To200':                 [4100,   1., 'Wj',        ['WJets-HT100To200']],
    'W_HT200To400':                 [4200,   1., 'Wj',        ['WJets-HT200To400']],
    'W_HT400To600':                 [4300,   1., 'Wj',        ['WJets-HT400To600']],
    'W_HT800To1200':                [4500,   1., 'Wj',        ['WJets-HT800To1200']],
    'W_HT1200To2500':               [4600,   1., 'Wj',        ['WJets-HT1200To2500']],
    'W_HT2500ToInf':                [4700,   1., 'Wj',        ['WJets-HT2500ToInf']],
    'W_bb_100to200':                  [5000,   1., 'Wj',        ['WBJets-Pt100To200']],
    'W_bb_200toInf':                  [5102,   1., 'Wj',        ['WBJets-Pt200ToInf']],
    'W_bgen100to200':               [5300,   1., 'Wj',        ['WJets_BGenFilter-Pt100To200']],
    'W_bgen200toInf':               [5400,   1., 'Wj',        ['WJets_BGenFilter-Pt200ToInf']],
    'ZZ_2L2Q_nlo_lf':                     [34600,  1., 'ZZ',        ['ZZ_2L2Q_nlo']],
#    'WZ_1L1Nu2Q_lf':                      [3200,   1., 'VVLF',        ['WZ_1L1Nu2Q']],
#    'WZ_1L1Nu2Q_b':                       [3201,   1., 'VVHF',        ['WZ_1L1Nu2Q']],
#    'WZ_1L1Nu2Q_bb':                      [3202,   1., 'VVHF',        ['WZ_1L1Nu2Q']],
    'WW_1L1Nu2Q_lf':                      [3400,   1., 'WW',        ['WW_1L1Nu2Q']],


#            'QCD_HT200to300':   [2, 1., 'QCD', ['QCD_HT200to300']],
#            'QCD_HT300to500':   [3, 1., 'QCD', ['QCD_HT300to500']],
#            'QCD_HT500to700':   [4, 1., 'QCD', ['QCD_HT500to700']],
#            'QCD_HT700to1000':  [5, 1., 'QCD', ['QCD_HT700to1000']],
#            'QCD_HT1000to1500': [6, 1., 'QCD', ['QCD_HT1000to1500']],
#            'QCD_HT1500to2000': [7, 1., 'QCD', ['QCD_HT1500to2000']],
#            'QCD_HT2000toInf':  [8, 1., 'QCD', ['QCD_HT2000toInf']],
}

#	bkg_files_list.append([get_DY2B_bkg(),	'DY2B',	ROOT.kBlue])
#	bkg_files_list.append([get_DY2LL_bkg(),	'DY2LL',ROOT.kGreen])
	#bkg_files_list.append([get_ST_bkg(),	'ST',	ROOT.kMagenta])
#	bkg_files_list.append([get_TT_bkg(),	'TT',	ROOT.kCyan])
#	bkg_files_list.append([get_ZZ_bkg(),	'ZZ',	ROOT.kYellow])
	#bkg_files_list.append([get_WW_bkg(),	'WW',	ROOT.kOrange])


sample_colors = [
        ['TT',               ROOT.kCyan],
        ['s_Top',            	ROOT.kMagenta],
        ['Wj',             ROOT.kGreen+2],
        ['Zj0b',             ROOT.kGreen],
        ['Zj2b',             ROOT.kBlue],
        ['ZZ',    ROOT.kYellow],
        ['WW',             ROOT.kYellow+3],
        ['VH',             ROOT.kYellow+4],
]

def get_bkg(name):
	f_list = []
        
        print(name) 

        for x in the_samples_dict:
#            print(the_samples_dict[x])
            if the_samples_dict[x][2] == name:
                print '  '
                print(the_samples_dict[x][3])
                f_list = f_list + the_samples_dict[x][3]

#        print(f_list)
        i = 0
        while i < len(f_list):
                f_list[i]='skimmed_'+f_list[i]+'.root'
                i += 1


        print 'Done'
	return f_list

#import lep2_samples_2017 
#reload(lep2_samples_2017)
#import lep2_samples_2017 as toto
#toto.get_bkg('ggZnnH')
