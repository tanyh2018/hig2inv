#!/usr/bin/env python
"""
Irradiation flux
"""

__author__ = "Tanyh <tanyuhang@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyh"
__created__ = "[2019-04-28 ]"  

import sys
import os 
#Formula  flux=current*time/e*Proton beam cross section
current =40*10**(-9)   #A
time=3600         # 1h
e=1.6*10**(-19)   #
area_unit=2*2  #cm^2
factor=0.71
Aim=6*10**(15)
Irra_dose=current*time/(e*area_unit)
print Irra_dose
Aim_time=Aim/(factor*Irra_dose)
print Aim_time
