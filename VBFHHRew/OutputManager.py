import ROOT
import collections
import fnmatch
import array
import uproot

from VBFReweightModules import inputSample, VBFReweight, printProgressBar

A13tev = [2.09078, 10.1517, 0.282307, 0.101205, 1.33191, -8.51168, -1.37309, 2.82636, 1.45767, -4.91761, -0.675197, 1.86189, 0.321422, -0.836276, -0.568156]
 
def functionGF(kl,kt,c2,cg,c2g,A):
  return A[0]*kt**4 + A[1]*c2**2 + (A[2]*kt**2 + A[3]*cg**2)*kl**2 + A[4]*c2g**2 + ( A[5]*c2 + A[6]*kt*kl )*kt**2  + (A[7]*kt*kl + A[8]*cg*kl )*c2 + A[9]*c2*c2g  + (A[10]*cg*kl + A[11]*c2g)*kt**2+ (A[12]*kl*cg + A[13]*c2g )*kt*kl + A[14]*cg*c2g*kl
 
class OutputManager:
    """ Handles the input from AnalysisHelper and manages the output to a file
    to be used for datacards and analysis"""
    def __init__(self):
        self.histos      = []
        self.variables   = ["MX"]

    # VBF Reweighting
    # Inputs:
    # - inputSigs  : name of 6 input samples
    # - target_kl  : vector of kl target values (float or int)
    # - target_cv  : vector of cv target values (float or int)
    # - target_c2v : vector of c2v target values (float or int)
    # - target BF can be used to weight to the final state BF

    def makeVBFrew(self, inputSigs, target_kl, target_cv, target_c2v, target_bf):

        print "-- VBF reweighting --"
        print "Input samples:", inputSigs
        #print "Input samples:", inputSigs[0]
        print "Target kl    :", target_kl
        print "Target cv    :", target_cv
        print "Target c2v   :", target_c2v
        print "BF:", target_bf

        #f = ROOT.TFile.Open(inputSigs[0])
        #treename = 'bbggSelectionTree'
        #tree = f.Get(treename)
        #for evt in tree:
        #    MX = evt.MX
        #    print "MX", MX   

        totIterations = len(target_kl) * len(target_cv) * len(target_c2v) * len(self.variables)
        nIteration = 0

        # Loop on variables and selections to reweight all the histograms
        for var in self.variables:

# this is what I've seen in Soumya mail. To be checked
#sample A: CV = 1    , C2V = 1   , klambda = 1    xs = 0.0015929203539823008  * BR(HH->bbgg)  
#sample B: CV = 1    , C2V = 2   , klambda = 1    xs = 0.013923303834808259   * BR(HH->bbgg) 
#sample C: CV = 1    , C2V = 1   , klambda = 2    xs = 0.0012979351032448377  * BR(HH->bbgg)  
#sample D: CV = 1    , C2V = 1   , klambda = 0    xs = 0.004277286135693214   * BR(HH->bbgg) 
#sample E: CV = 0.5  , C2V = 1   , klambda = 1    xs = 0.010412979351032449   * BR(HH->bbgg) 
#sample F: CV = 1.5  , C2V = 1   , klambda = 1    xs = 0.06339233038348081    * BR(HH->bbgg)

                # Create a list of inputSamples
            inputList = [
                inputSample(  1., 1., 1., 0.001499 ), # node 1
                inputSample(  1., 1., 0., 0.003947 ), # node 2
                inputSample(  1., 1., 2., 0.001243 ), # node 3
                inputSample(  1., 2., 1., 0.012719 ), # node 4
                inputSample( 1.5, 1., 1., 0.057943 ), # node 5
#                inputSample(  1,  0., 2.,   0.0178 ), # node 19
                inputSample(0.5, 1., 1.,   0.009579 ), # node 6 ---> calculated from Francesco code 
            ]

                # Instantiate a VBFReweight object
            VBFreweighter = VBFReweight(inputList)


            f=open("outKLweight.txt", "w+")
                # Get the modeled histogram for each (cv,c2v,kl) target point

            for cv in target_cv:
                for c2v in target_c2v:
                    for kl in target_kl:
                            
                        modeled_xs, coefficients = VBFreweighter.modelSignal(cv,c2v,kl,target_bf)

                        print '\n ====== kl ',kl, " ikl, ", int((6+kl)/0.2+1),' and the branch weight name would be KL'+str(int((6+kl)/0.2+1)) + '\n c2v ', c2v, ' cv ', cv, ': sigma = ', "{0:.3f}".format(modeled_xs*1000), ' fb, sigma*BF = ',"{0:.3f}".format(modeled_xs*target_bf*1000) 
                        print 'coeffs ', "{0:.5f}".format(coefficients[0]*1000), ' ',"{0:.5f}".format(coefficients[1]*1000), "{0:.5f}".format(coefficients[2]*1000), "{0:.5f}".format(coefficients[3]*1000), "{0:.5f}".format(coefficients[4]*1000), "{0:.5f}".format(coefficients[5]*1000), " fb"

                        print 'Norm coeffs ', "{0:.5f}".format(coefficients[0]/modeled_xs), ' ',"{0:.5f}".format(coefficients[1]/modeled_xs), "{0:.5f}".format(coefficients[2]/modeled_xs), "{0:.5f}".format(coefficients[3]/modeled_xs), "{0:.5f}".format(coefficients[4]/modeled_xs), "{0:.5f}".format(coefficients[5]/modeled_xs), " for 1 fb"
                        xsec = 31.05*0.0026*functionGF(kl, 1.0, 0.0, 0.0, 0.0, A13tev)
                        #xsec = 1.726*0.0026*functionGF(kl, 1.0, 0.0, 0.0, 0.0, A13tev)
                        print 'xsec ggHHH ', "{0:.5f}".format(xsec)  

 
                        f.write("%f %f %f %f %f %f %f\n" % ( (6+kl)/0.2+1, coefficients[0]/modeled_xs, coefficients[1]/modeled_xs, coefficients[2]/modeled_xs, coefficients[3]/modeled_xs, coefficients[4]/modeled_xs, coefficients[5]/modeled_xs ))                         
 
#                        print 'total_xs ', modeled_xs
#                        print 'total_xs*bf ', modeled_xs*target_bf

            f.close()     

