#!/usr/bin/env bash 

# MarlinFastJet
source /cvmfs/cepc.ihep.ac.cn/software/cepcenv/setup.sh
cepcenv -r /cvmfs/cepc.ihep.ac.cn/software/cepcsoft use 0.1.0-rc9

#cd ./MarlinFastJet/v00-02
#rm -fr build
#mkdir build
#cd build
#cmake ..
##cmake -C ../ILCSoft.cmake.mod ..
#make install 
#cd ../../../


# IsolatedLeptonFinder && Higgs2zz

rm -fr build
mkdir build
cd build
#cmake -C /afs/ihep.ac.cn/soft/common/gcc/v01-17-05/ILCSoft.cmake .. 
cmake ..
make install
cd ..

