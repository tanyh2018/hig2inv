#!/usr/bin/env python
"""
From srim to get temperature 
"""

__author__ = "Tanyh <tanyuhang@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyh"
__created__ = "[2019-04-28 ]"

import sys
import os 
import math
dE_dx=1.359   #MeV/mm
dE_dx_unit=dE_dx*1.6*10**(-13)/(10**3)    #J/um
C_si=0.7    #J/(g.K)
print dE_dx_unit
#sensor mass
sensor_depth=50.0  #um
sensor_size=23*26*50*10**(-4)
sensor_density=2.32   #g/cm-3
sensor_mass=sensor_size*sensor_density      #g

C_sensor=sensor_mass*C_si

#Conversion efficiency
Conversion_eff=1.0
#number of particle
N_proton=6*10**15   #24 hours
T=dE_dx_unit*sensor_depth*Conversion_eff*N_proton/C_sensor
print  "the increase tempareture:"  
print   T    #13 C