void fit() 
{
   gStyle->SetOptTitle(0);
   gStyle->SetPadLeftMargin(0.17);
   gStyle->SetPadBottomMargin(0.17);

   gSystem->Load("libRooFit");
   using namespace RooFit;
   TString rootfile;
   rootfile = "./BDT_output/Hinv_bkg_e2e2h_selected_BDT.root";
    
   TString  epsname;  
   epsname="./fig/fithiggs.pdf";
   
   TCanvas *myC = new TCanvas("myC", "", 10,10,800,600);
   
   myC->Divide(1,1);
   myC->cd(1); 
   
   TFile *f = new TFile(rootfile);
   TTree *t = (TTree *)f->Get("tree");
   
   Float_t m_m_recoil;
   t->SetBranchAddress("m_m_recoil", &m_m_recoil);
   
   TH1F* histData=new TH1F("Recoil mass of Z boson","Recoil mass of Z boson",80,120,145);
   histData->SetLineColor(2);
   histData->SetLineWidth(2);
   //double nsum = t->GetEntries; 
   for(int i=0; i<t->GetEntries(); i++)
   { 
      t->GetEntry(i);
      histData->Fill(m_m_recoil);
   }
   
   RooRealVar x("m_m_recoil","m_m_recoil",120,145);
   TChain *chain2 = new TChain("tree");
   chain2->Add("/cefs/higgs/tanyuhang/hig2inv/BDT_output/Hinv_sig_e2e2h_BDT.root");
   TTree* t2mcsig = chain2;
   TH1F *h2=new TH1F("m_m_recoil1","m_m_recoil1",80,120,145);
   t2mcsig->Draw("m_m_recoil>>h2");
   TH1D *pKsm_4c =(TH1D*)gDirectory->Get("h2"); 
   RooDataHist a0side ("data1"  , "data1" , x, pKsm_4c);
   RooHistPdf sig("sig","sigshape", x, a0side, 0);
   

   //Signal: CBshape function
   RooRealVar mean("mean_CB","mean_CB",125.4);
   RooRealVar sigma("sgm_CB","sgm_CB",1.06);
   RooRealVar alpha("alpha_CB","alpha_CB",-1.04);
   RooRealVar n("n","n",1.1);
   RooCBShape cb("sig","sig p.d.f.",x,mean,sigma,alpha,n);

   //Siganl: B-W function 
   RooRealVar mean0("mean0","Mean of Gaussian",126,120,130);
   RooRealVar sigma0("sigma0","Width of Gaussian",2.6,2.0,3.0) ;
   RooBreitWigner  breithtwigner2("breithtwigner2","breithtwigner2",x,mean0,sigma0);
   
   //Signal: Gauss function
   //RooRealVar mean0("mean0", "mean0", 125.9,124,128);
   //RooRealVar sigma0("sigma0", "sigma0",1.85,0.2,5);
   //RooGaussian gauss0("gauss0"," gauss fit ",x, mean0, sigma0);

   RooRealVar mean2("mean2", "mean2", 136.1, 130.0, 140.0);
   RooRealVar sigma2("sigma2", "sigma2",2.87,1.50,3.50);
   RooGaussian gauss2("gauss2"," gauss fit ",x, mean2, sigma2);
 
   //Background: Chebychev and Polynomial function
   //RooRealVar co1("co1","coefficienct #1",0.13,-1., 1.);
   //RooRealVar co2("co2","coefficienct #2",0,-999., 999.);
   //RooRealVar co3("co3","coefficienct #3",0,-999., 999.);
   //RooRealVar co4("co4","coefficienct #4",0,-999., 999.);
   //RooRealVar co5("co5","coefficienct #5",0,-999., 999.);
   //RooChebychev bkg("bkg", "bkg p.d.f", x, RooArgList(co1));
   //RooChebychev bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2));
   //RooChebychev bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3));
   //RooPolynomial bkg("bkg", "bkg p.d.f", x, RooArgList(co1,co2,co3,co4));

   RooRealVar mean1("mean1", "mean1", 126., 125., 130.);
   RooRealVar sigma1("sigma1", "sigma1",1.9,0.2,5.0);
   RooGaussian gauss1("gauss1"," gauss fit ",x, mean1, sigma1);

   RooRealVar fira("fira", "fira",0.79,0.,1.);
   RooAddPdf bkg("bkg","bkg",RooArgList(breithtwigner2,gauss2),fira);
   Double_t mentr = (Double_t)histData->GetEntries();
   Double_t msig = mentr;
   Double_t mbkg = mentr;

   RooRealVar nsig("nsig", "signal elow number",0, msig);
   RooRealVar nbkg("nbkg", "background number",0, mbkg);
   RooRealVar nbkg("nbkg", "background number",0, mbkg);
  // RooRealVar nbkg("nbkg", "background number",0, mbkg);
   //RooAddPdf sum("sum", "sum", RooArgList(breithtwigner2,bkg), RooArgList(nsig,nbkg));
   //RooAddPdf sum("sum", "sum", RooArgList(gauss0,bkg), RooArgList(nsig,nbkg));
   RooAddPdf sum("sum", "sum", RooArgList(bkg), RooArgList(nbkg));
   //RooAddPdf sum("sum", "sum", RooArgList(cb,bkg), RooArgList(nsig,nbkg));
   
   RooDataHist data("data","dada",x,histData);
   
   sum.fitTo(data,Extended(kTRUE));
   RooPlot *xframe=x.frame();
   
   data.plotOn(xframe);
   sum.plotOn(xframe);
   sum.plotOn(xframe,Components(bkg),LineStyle(2), LineColor(3));
   //sum.plotOn(xframe,Components(cb),LineStyle(2), LineColor(2));
   //sum.plotOn(xframe,Components(cb),LineStyle(2), LineColor(2));
   //sum.plotOn(xframe,Components(bkg),LineStyle(2), LineColor(3));
  //gPad->SetLogy();
   //xframe->SetMaximum(10000);
   //xframe->SetMinimum(10);
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
   xaxis->SetTitle("M_{Recoil}(GeV/c^{2})");
   yaxis->SetTitle("Events/(0.3Gev/C^{2})");
   xaxis->CenterTitle();
   yaxis->CenterTitle();
   xaxis->SetNdivisions(505);
   yaxis->SetNdivisions(505);
   xframe->Draw();

  double xmin = 120; 
  double xmax = 145;
  TH1F *hsig =new TH1F("hsig", "", 100, xmin, xmax);
  TH1F *hbkg =new TH1F("hbkg", "", 100, xmin, xmax);
  TH1F *hJpsi=new TH1F("hJpsi", "", 100, xmin, xmax);
  hsig->SetLineColor(2);     hsig->SetLineStyle(2);   hsig->SetLineWidth(1);
  hbkg->SetLineColor(3);     hbkg->SetLineStyle(2);   hbkg->SetLineWidth(1);
  hJpsi->SetLineColor(6);     hJpsi->SetLineStyle(9);   hJpsi->SetLineWidth(3);
  TLegend *leg = new TLegend(0.2, 0.78, 0.4, 0.93);
    leg->AddEntry(hsig,"#signal","L");
    leg->AddEntry(hbkg,"#background","L");
	//leg->AddEntry(hJpsi,"sum","L")
  //  leg->AddEntry(hJpsi,"#Sigma(1940)","L");
    leg->SetFillColor(0);
  //  leg->SetBorderSize(1);
    //leg->Draw();
     
  
   myC->Print(epsname);  
 
}
