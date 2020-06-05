#!/bin/bash

if [[ $1 == 0 ]]; then
cd ./run/mumuH/bg/hist

elif [[ $1 == 1 ]]; then
cd ./run/eeH/bg/hist
else
cd ./run/qqH/bg/hist
echo 1
fi

hadd ../../total/hist/2f.root e1e1/* e2e2/* e3e3/* qq/* nn/* 
hadd ../../total/hist/ZZ.root  zz_*/* 
hadd ../../total/hist/WW.root  ww*/*
hadd ../../total/hist/single_z.root sze_*/*  sznu*/*
hadd ../../total/hist/sz_sw.root    szeorsw*/*
hadd ../../total/hist/single_w.root sw_*/*
hadd ../../total/hist/zzorww.root zzorww*/*
if [[ $1 == 0 ]]; then
hadd ../../total/hist/XH_visible.root Z_eH/* Z_nuH/* Z_qH/* Z_tauH/* 
hadd ../../total/hist/mumuH_visible.root Z_muH/*
elif [[ $1 == 1 ]]; then
hadd ../../total/hist/XH_visible.root  Z_muH/* Z_nuH/* Z_qH/* Z_tauH/* 
hadd ../../total/hist/eeH_visible.root Z_eH/*
else
hadd ../../total/hist/XH_visible.root Z_muH/* Z_nuH/* Z_eH/* Z_tauH/* 
hadd ../../total/hist/qqH_visible.root Z_qH/*
fi
hadd ../../total/hist/total_bkg.root ../../total/hist/*
#cd ../plot
#hadd ../../total/plot/2f.root e1e1/* e2e2/* e3e3/* qq/*  nn/* 
#hadd ../../total/plot/ZZ.root  zz_*/* 
#hadd ../../total/plot/WW.root  ww*/*
#hadd ../../total/plot/single_z.root sz*/*
#hadd ../../total/plot/single_w.root sw*/*
#hadd ../../total/plot/zzorww.root zzorww*/*
#if [[ $1 == 0 ]]; then
#hadd ../../total/plot/XH_visible.root Z_eH/* Z_nuH/* Z_qH/* Z_tauH/* 
#hadd ../../total/plot/mumuH_visible.root Z_muH/*
#elif [[ $1 == 1 ]]; then
#hadd ../../total/plot/XH_visible.root  Z_muH/* Z_nuH/* Z_qH/* Z_tauH/* 
#hadd ../../total/plot/eeH_visible.root Z_eH/*
#else
#hadd ../../total/plot/XH_visible.root Z_muH/* Z_nuH/* Z_eH/* Z_tauH/* 
#hadd ../../total/plot/qqH_visible.root Z_qH/*
#fi
#hadd ../../total/hist/total_bkg.root ../../total/hist/*
#hadd ../../total/plot/total_bkg.root ../../total/plot/*
#cd ../../total 
#if [[ $1 == 0 ]]; then
#hadd bkg_add_sig.root ./hist/total_bkg.root ../e2E2h_invi/hist/e2E2h_invi/ana_File_merged_scale_1.root 
#elif [[ $1 == 1 ]]; then
#hadd bkg_add_sig.root ./hist/total_bkg.root ../eeh_invi/hist/eeh_invi/ana_File_merged_scale_1.root
#else
#hadd bkg_add_sig.root ./hist/total_bkg.root ../qqh_invi/hist/qqh_invi/ana_File_merged_scale_1.root
#hadd bkg_add_sig.root ./plot/total_bkg.root ../qqh_invi/hist/qqh_invi/ana_File_merged_scale_1.root
#fi