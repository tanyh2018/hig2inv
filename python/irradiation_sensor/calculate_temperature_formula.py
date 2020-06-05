#!/usr/bin/env python
"""
From formula to get temperature 
"""

__author__ = "Tanyh <tanyuhang@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyh"
__created__ = "[2019-04-28 ]"

import sys
import os 
import math

n_charge=1
meta_charge=1.6*10**(-19)
mass_e=9.1*10**(-31)
c=3*10**8  #m/s
v_proton=math.sqrt(0.3672*c*c)

N_proton_volume=2.32*10**6/28*6.02*10**23   #m-3
I_si=1.12    #ev   Equivalent ionization point of silicon
I_si_unit=1.6*10**(-19)
Z=14     #Atomic number
m_B=Z*(math.log(2*mass_e*v_proton*v_proton/I_si_unit)-v_proton*v_proton/(c*c))
dE_dx=4*math.pi/(mass_e*c*c)*meta_charge**2/(4*math.pi*8.854*10**(-12))*N_proton_volume*m_B/(v_proton**2)*m_B
dE_dx_unit=dE_dx/(1.6*10**(-13)*5*10**15)*1.6*10**(-10)/(10**6)   #GeV/m->J/um
#dE_dx=1.359   #MeV/mm
print dE_dx_unit
#dE_dx_unit=dE_dx*1.6*10**(-13)/(10**3)    #J/um
C_si=0.7    #J/(g.K)
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