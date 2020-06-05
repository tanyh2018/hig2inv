#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "RooPlot.h"
void fitsigbkg() 
{
   gStyle->SetOptTitle(0);
   gStyle->SetPadLeftMargin(0.17);
   gStyle->SetPadBottomMargin(0.17);
 
   gSystem->Load("libRooFit");
   using namespace RooFit;
   TString rootfile;
   rootfile = "./run/total/bkg_add_sig.root";
    
   TString  epsname;  
   epsname="./fig/fithiggsb.pdf";
   
   TCanvas *myC = new TCanvas("myC", "", 10,10,800,600); 
   
   myC->Divide(1,1);
   myC->cd(1); 
   
   TFile *f = new TFile(rootfile);
   TTree *t = (TTree *)f->Get("tree");
   
   Float_t m_m_recoil;
   t->SetBranchAddress("m_m_recoil", &m_m_recoil);
   
   TH1F* histData=new TH1F("Recoil mass of Z boson","Recoil mass of Z boson",48,123,135);
   histData->SetLineColor(1);
   histData->SetLineWidth(1);
   
   for(int i=0; i<t->GetEntries(); i++)
   { 
      t->GetEntry(i);
      histData->Fill(m_m_recoil);
   }
   
   RooRealVar x("m_m_recoil","m_m_recoil",120,140);
  // TChain *chain2 = new TChain("tree");
  // chain2->Add("/cefs/higgs/tanyuhang/hig2inv/run/e2E2h_invi/hist/e2E2h_invi/ana_File_merged_1.root");
  // TTree* sigtree = chain2;
  // TH1F *h2=new TH1F("m_m_recoil1","m_m_recoil1",100,120,145);
  // sigtree->Draw("m_m_recoil>>h2");
  // TH1D *sigdata =(TH1D*)gDirectory->Get("h2"); 
  // RooDataHist data1 ("data1"  , "data1" , x, sigdata);
  // RooHistPdf sigh("sig","sigshape", x, data1, 0);
//
  // RooRealVar y("m_m_recoil","m_m_recoil",120,145);
  // TChain *chain3 = new TChain("tree");
  // chain3->Add("/cefs/higgs/tanyuhang/hig2inv/run/total/hist/all_bkg_merge.root");
  // TTree* bkgtree = chain3;
  // TH1F *h3=new TH1F("m_m_recoil2","m_m_recoil2",100,120,145);
  // bkgtree->Draw("m_m_recoil>>h3");
  // TH1D *bkgdata =(TH1D*)gDirectory->Get("h3"); 
  // RooDataHist data2 ("data2"  , "data2" , y, bkgdata);
  // RooHistPdf bkgh("bkg1","bkgshape", y, data2, 0);
   

   //Signal: CBshape function
   RooRealVar mean("mean_CB","mean_CB",125.2,125,126);
   RooRealVar sigma("sgm_CB","sgm_CB",0.59,0.,0.80);
   RooRealVar alpha("alpha_CB","alpha_CB",-1.28,-10.,1.);
   RooRealVar n("n","n",1.28,0.,2.0);
   RooCBShape cb("sig1","sig1 p.d.f.",x,mean,sigma,alpha,n);

   //Siganl: B-W function 
   RooRealVar mean1("mean1","Mean of Gaussian",126,110,130);
   RooRealVar sigma1("sigma1","Width of Gaussian",8.7,0,10);
   RooBreitWigner  breithtwigner2("breithtwigner2","breithtwigner2",x,mean1,sigma1);
   //Argus background
   RooRealVar fira1("fira1", "fira1",0.773);
   RooRealVar argpar("argpar","argus shape parameter",-4.329) ;
   RooArgusBG argus("argus","Argus PDF",x,RooConst(136.8),argpar,fira1) ;
   
   //Signal: Gauss function
   RooRealVar mean0("mean0", "mean0", 126, 110, 130);
   RooRealVar sigma0("sigma0", "sigma0",4.3,0,10);
   RooGaussian gauss0("gauss0"," gauss fit ",x, mean0, sigma0);

   RooRealVar mean2("mean2", "mean2", 125.4, 124.5, 125.5);
   RooRealVar sigma2("sigma2", "sigma2",0.7,0.01,1);
   RooGaussian gauss2("gauss2"," gauss fit ",x, mean2, sigma2);
 
   //Background: Chebychev and Polynomial function
   RooRealVar co1("co1","coefficienct #1",-0.480871);
   RooRealVar co2("co2","coefficienct #2",-0.297093);
   RooRealVar co3("co3","coefficienct #3",-0.149663);
   RooRealVar co4("co4","coefficienct #4",0,-999., 999.);
   //RooRealVar co5("co5","coefficienct #5",0,-999., 999.);
   //RooChebychev bkg("bkg", "bkg p.d.f", x, RooArgList(co1));
   RooChebychev bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));

   //RooRealVar mean1("mean1", "mean1", 126.2, 125, 130);
   //RooRealVar sigma1("sigma1", "sigma1",1.9,0.20,10);
   //RooGaussian gauss1("gauss1"," gauss fit ",x, mean1, sigma1);

   RooRealVar fira("fira", "fira",30,-999,999);
   //RooAddPdf sig("sig","sig",RooArgList(sigh),fira);
   Double_t mentr = (Double_t)histData->GetEntries();
   Double_t msig = mentr;
   Double_t mbkg = mentr;

   RooRealVar nsig("nsig", "signal elow number",0, msig);
   RooRealVar nbkg("nbkg", "background number",4907,6445);
  // RooRealVar nbkg("nbkg", "background number",0, mbkg);
   //RooAddPdf sum("sum", "sum", RooArgList(breithtwigner2,bkg), RooArgList(nsig,nbkg));
   //RooAddPdf sum("sum", "sum", RooArgList(gauss0,bkg), RooArgList(nsig,nbkg));
   RooAddPdf sum("sum", "sum", RooArgList(cb,bkg), RooArgList(nsig,nbkg));
   //RooAddPdf sum("sum", "sum", RooArgList(cb,bkg), RooArgList(nsig,nbkg));
   
   RooDataHist data("data","dada",x,histData);
   sum.fitTo(data,Extended(kTRUE));
   RooPlot *xframe=x.frame();
   
   data.plotOn(xframe);
   sum.plotOn(xframe);
   //sum.plotOn(xframe,Components(cb),DrawOption("F"),FillColor(kRed),MoveToBack());
   //sum.plotOn(xframe,Components(bkg),DrawOption("F"),FillColor(kOrange));
   sum.plotOn(xframe,Components(cb),LineStyle(2), LineColor(2));
   sum.plotOn(xframe,Components(bkg),LineStyle(2), LineColor(3));
   //gPad->SetLogy();
  // xframe->SetMaximum(60000);
   //xframe->SetMinimum(350);
   nsig.Print();
   nbkg.Print(); 

   TAxis *yaxis= xframe->GetYaxis();
   TAxis *xaxis= xframe->GetXaxis();

   xaxis->SetTitleFont(22);
   yaxis->SetTitleFont(22);
   xaxis->SetTitleOffset(1.2);
   yaxis->SetTitleOffset(1.2);
   xaxis->SetTitleSize(0.06);
   yaxis->SetTitleSize(0.06);
   xaxis->SetLabelSize(0.05);
   yaxis->SetLabelSize(0.05);
   xaxis->SetTitle("M_{Recoil}^{#mu^{+}#mu^{-}}(GeV/c^{2})");
   yaxis->SetTitle("Events/(0.5Gev/C^{2})");
   xaxis->CenterTitle();
   yaxis->CenterTitle();
   xaxis->SetNdivisions(505);
   yaxis->SetNdivisions(505);
   xframe->Draw();

  double xmin = 120; 
  double xmax = 145;
  TH1F *hsig =new TH1F("hsig", "", 100, xmin, xmax);
  TH1F *hbkg =new TH1F("hbkg", "", 100, xmin, xmax);
  TH1F *hJpsi=new TH1F("hsum", "", 100, xmin, xmax);
  hsig->SetLineColor(2);     hsig->SetLineStyle(2);   hsig->SetLineWidth(1);
  hbkg->SetLineColor(3);     hbkg->SetLineStyle(2);   hbkg->SetLineWidth(1);
 hsum->SetLineColor(4);     hsum->SetLineStyle(1);   hsum->SetLineWidth(3);
  TLegend *leg = new TLegend(0.7, 0.75, 0.9, 0.90);
    leg->AddEntry(hsig,"#signal","L");
    leg->AddEntry(hbkg,"#bkg","L");
    leg->AddEntry(hsum,"#signal+bkg","L");
  //  leg->AddEntry(hJpsi,"#Sigma(1940)","L");
    leg->SetFillColor(0);
    leg->SetBorderSize(1);
    leg->Draw();
     
     
  
   myC->Print(epsname); 
}