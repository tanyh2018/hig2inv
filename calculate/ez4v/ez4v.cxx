"""
##get information from ee mumu and qq
"""

__author__ = "Tan Yuhang <tanyuhang@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyuhang"
__created__ = "[2019-03-04 ]"

#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <string>

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"

#if not defined(__CINT__) || defined(__MAKECINT__)
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"
#endif

void mm_ntuple(TString a,TString b);
void ez4v()
{

  mm_ntuple("eeH_inv.root",   "ez4v_sig.root");
  mm_ntuple("total_bkg.root", "ez4v_bkg.root");

}

void mm_ntuple(TString a,TString b)
{

  TFile *f       = new TFile(a);
  TFile *target  = new TFile(b,"RECREATE");
  TTree *data = (TTree *)f->Get("tree");


  Double_t VisMass,  MisMass;
  Float_t  VisMassf, MisMassf;
  Float_t      weight;

  Int_t   MCtau=0;
  Int_t   Tau,nTauP,nTauM;
  weight=1;

  Float_t g1CosPolar,g2CosPolar, g1E, g2E, g1rcCos, g2rcCos, ggE, ggM, rcM, g1PTrans, g2PTrans, ggPTrans, rcCosPolar, g1g2cos;
  Float_t LD0, LZ0, NLD0, NLZ0;


   data->SetBranchAddress("m_m_recoil",      &MisMassf);
   data->SetBranchAddress("m_m_dimu",        &VisMassf);


  Int_t nentries = data->GetEntries();



  TTree *output=new TTree("HiggsTree","HiggsTree");
  output->Branch("Mass_invar"    ,&MisMassf,         "Mass_invar/F");
  output->Branch("Mass_Z"        ,&VisMassf,         "Mass_vis/F");
  output->Branch("weight"        ,&weight,           "weight/F");

double sum=0;
 
  for (Long64_t ievt=0; ievt<nentries;ievt++)
 {
     data->GetEntry(ievt);

     if (b.Contains("s")) weight=0.00212;
     if (b.Contains("b")) weight=1;
     sum+=weight;


     output->Fill();
  }

 cout<<a<<"->begin:"<<nentries<<endl;
 cout<<"after:"<<output->GetEntries()<<endl;
  cout<<"sum weight:"<<sum<<endl;
 output->Write("",TObject::kOverwrite);
 target->Close();
 f->Close();


}