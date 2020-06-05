#!/usr/bin/env bash

# Unset MARLIN_DLL


unset MARLIN_DLL
source /cvmfs/cepc.ihep.ac.cn/software/cepcenv/setup.sh
cepcenv -r /cvmfs/cepc.ihep.ac.cn/software/cepcsoft use 0.1.0-rc9
# Set Variables for MARLIN Execution
shopt -s expand_aliases
#source /besfs/groups/higgs/Software/v01-17-05_slc6/init_ilcsoft.sh
#source $PWD/init_ilcsoft.sh

# FastJet
#export MARLIN_DLL=$PWD/MarlinFastJet/v00-02/lib/libMarlinFastJet.so:$MARLIN_DLL

# Add MARLIN Library Path 
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
export MARLIN_DLL=$PWD/lib/libhig2inv.so:$MARLIN_DLL

# For Condor Job Submit
export PATH=/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin:$PATH


# PyROOT 
export PYTHONPATH=$ROOTSYS/lib:$PYTHONPATH

#SET ROOT
#export ROOTSYS="/afs/ihep.ac.cn/soft/common/ROOT/root-6.12.04"
#export PATH="$ROOTSYS/bin:$PATH"
#export LD_LIBRARY_PATH="$ROOTSYS/lib:$LD_LIBRARY_PATH"
