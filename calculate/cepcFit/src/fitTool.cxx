#include "fitTool.h"
#include "CEPCCDRstyle.h"  
fitTool::fitTool() {   
  // Default values for the minimizer
  _minAlgo = "Minuit2";
  _minTolerance = 1E-06;
  _minStrat = 2;
  _nllOffset = true;
  _nCPU = 1;
  _optConst = 2;
  _printLevel = 2;
  _useHESSE = true;
  _useMINOS = true;
  _useSIMPLEX = false; 
  _saveWS= false;
}
using namespace std;
using namespace RooFit;
using namespace RooStats;

int fitTool::profileToData(ModelConfig *mc, RooAbsData *data){
	// ----------------------------------------------------------------------------------------------------- 
	RooAbsPdf *pdf=mc->GetPdf();
	RooWorkspace *ws=mc->GetWS();
//	
	TStopwatch timer1;

	RooAbsReal *nll = pdf->createNLL(*data, NumCPU(_nCPU));

	nll->enableOffsetting(1);

	
	RooMinimizer minim(*nll);
	minim.setStrategy( _minStrat );
	minim.setPrintLevel( _printLevel-1 );
	minim.setProfile(); /* print out time */
	minim.setEps( _minTolerance/0.001  );
	minim.setOffsetting( _nllOffset );

	if (_optConst > 0) minim.optimizeConst( _optConst );

	int status = 0;
	// Perform fit with MIGRAD
	status += minim.minimize( _minAlgo );

	if ( _useHESSE ) 

	{
		cout << endl << "Starting fit with HESSE..." << endl;
		status += minim.hesse();
		minim.save("hesse","")->Print();
	}

	if ( _useMINOS ) 

	{
		cout << endl << "Starting fit with MINOS..." << endl;
		status += minim.minos( *mc->GetParametersOfInterest() );
	}

	if ( _outputFile != "" )
	{ 
		cout << endl << "Saving results to " << _outputFile << endl;
		// Create output file and save fit results
		TFile *tout = new TFile( _outputFile, "RECREATE" );
		tout->cd();
		RooFitResult *result = minim.save("fitResult","Fit Results"); 
		result->Write();
		
		// Get important values to save
		double nllVal = nll->getVal();
		TString str_nll = Form("NLL value is %.12f", nllVal);
		cout << endl << str_nll << endl;
		std::map<std::string, double> muMap;

		for (RooLinkedListIter it = mc->GetParametersOfInterest()->iterator(); RooRealVar* POI = dynamic_cast<RooRealVar*>(it.Next());) 
		{
		    muMap[POI->GetName()] = POI->getVal();
	    }
		
		// Save values to TTree
		TTree *nllTree = new TTree("nllscan", "nllscan");
		nllTree->Branch( "status", &status);
		nllTree->Branch( "nll", &nllVal);
		for (RooLinkedListIter it = mc->GetParametersOfInterest()->iterator(); RooRealVar* POI = dynamic_cast<RooRealVar*>(it.Next());) 
		{
		    nllTree->Branch( POI->GetName(), &(muMap[POI->GetName()]) );
		}
		nllTree->Fill();
		nllTree->Write();
	}


	//likelihood  diagram

	for (RooLinkedListIter it = mc->GetParametersOfInterest()->iterator(); RooRealVar* POI = dynamic_cast<RooRealVar*>(it.Next());) 
	{
		SetCEPCCDRStyle();
		Float_t err= (fabs(POI->getAsymErrorHi()) + fabs(POI->getAsymErrorLo()))/2;
		Float_t mean_value = POI->getValV();
		TCanvas *canvas = new TCanvas("c1", "c1",800,800);
		canvas->SetMargin(0.16, 0.04, 0.11, 0.02);
        RooPlot* frame;
	    frame=POI->frame(100);
	    nll->plotOn(frame,ShiftToZero()) ;
        frame->SetMaximum(3.5);
        frame->SetMinimum(0);
	    frame->SetAxisRange(0,4); 
//		frame->SetTitle("");
//		frame->Scale(2);
		frame->GetXaxis()->CenterTitle();
		frame->GetYaxis()->CenterTitle();
        //frame->GetXaxis()->SetLabelFont(42);  
        //frame->GetXaxis()->SetTitleSize(0.04);
        //frame->GetXaxis()->SetTitleOffset(1.2);
        //frame->GetXaxis()->SetTitleFont(42);
        //frame->GetYaxis()->SetLabelFont(42);
        //frame->GetYaxis()->SetTitleSize(0.05);
        //frame->GetYaxis()->SetTitleOffset(1.2);
        //frame->GetYaxis()->SetTitleFont(42);
		frame->SetXTitle("#mu");
		frame->SetYTitle("-#Delta log(L)");
	    frame->Draw();
		auto l1 = new TLine(0,2,4,2);
        l1->SetLineColor(kGreen); 
		l1->SetLineWidth(2); 
		l1->SetLineStyle(10);      
		l1->Draw("");
		auto l2 = new TLine(0,0.5,4,0.5);
        l2->SetLineColor(kGreen); 
		l2->SetLineWidth(2); 
		l2->SetLineStyle(10);      
		l2->Draw("");
		TLatex latex;
		latex.SetTextAlign(11); 
		latex.SetTextSize(0.04);
		latex.DrawLatex(3.5,2.1,"2#sigma");
		latex.DrawLatex(3.5,0.6,"#sigma");
        //auto *tt = new TText(3.5,2.2,"2#sigma");
        //tt->SetTextAlign(11); 
		//tt->SetTextSize(0.03);
		//tt->SetTextColorAlpha(kBlue);
		//auto *tt2 = new TText(3.5,0.7,"#sigma");
        //tt2->SetTextAlign(11); 
		//tt2->SetTextSize(0.03);
		////tt->SetTextColorAlpha(kBlue);
        //tt2->Draw();
		

		//tex->DrawLatexNDC(3.5, 2.2, "2#sigma");
        //tex->DrawLatexNDC(3.5, 0.7, "#sigma");

	    canvas->SaveAs("../../fig/likelihood.pdf");
		canvas->SaveAs("../../fig/likelihood.C");
	    delete canvas;
	    delete frame;
	}

	    return status;
	
	}


