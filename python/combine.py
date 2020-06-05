#!/usr/bin/env python
""" 
Combine the results of three channel
"""
 
__author__ = "Tanyh <tanyh@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyh"
__created__ = "[2019-01-14 Mon 09:22]"

import os
import sys
import math
import ROOT

def main():
    BR=1 #assuming
    BRR= 0.00106 #Real
    meanmu=1.000  #mean value of muon channel
    meane=1.000
    meanq=1.000
    d_mu_mu=98
    d_mu_e=403   # sigma*BR
    d_mu_q=93

    d_mu_mu_m=math.sqrt(meanmu)*d_mu_mu    #modified mu precision or sigma
    d_mu_e_m=math.sqrt(meane)*d_mu_e
    d_mu_q_m=math.sqrt(meanq)*d_mu_q

    print "After modified the muon BR = %.2f %%, sigma*BR= %.2f %%, upper limit=%.2f %%" %(BR*100,d_mu_mu_m,(BRR+2*d_mu_mu_m*BRR/100)*100)
    print "After modified the ee   BR = %.2f %%, sigma*BR= %.2f %%, upper limit=%.2f %%" %(BR*100,d_mu_e_m,(BRR+2*d_mu_e_m*BRR/100)*100)
    print "After modified the qq   BR = %.2f %%, sigma*BR= %.2f %%, upper limit=%.2f %%" %(BR*100,d_mu_q_m,(BRR+2*d_mu_q_m*BRR/100)*100)

    d_combine_mu =math.sqrt(1/(1/(d_mu_mu_m*d_mu_mu_m)+1/(d_mu_e_m*d_mu_e_m)+1/(d_mu_q_m*d_mu_q_m)))
    print "Combine result BR = %.2f %%, sigma*BR= %.2f %%, upper limit=%.2f %%" %(BR*100,d_combine_mu,(BRR+2*d_combine_mu*BRR/100)*100)
if __name__ == '__main__':
    main()
