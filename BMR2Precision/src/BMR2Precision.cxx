
#include <stdio.h>
#include <StdHepIter.h>
#include <TLorentzVector.h>
#include <TGraph.h>
#include <TLatex.h>
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom.h>
#include <TH2D.h>
#include <exception> 
#include <TLegend.h>
#include <TStyle.h>
using namespace EVENT;

#include <dirent.h>
static bool endsWith(const std::string& str, const std::string& suffix)
{
            return str.size() >= suffix.size() && 0 == str.compare(str.size()-suffix.size(), suffix.size(), suffix);
}

std::vector<std::string> files(char const *path, char const *ext) {
   std::vector<std::string> result;
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir (path)) != NULL) {
        /* print all the files and directories within directory */
        while ((ent = readdir (dir)) != NULL) {
            if(endsWith(ent->d_name, ext)) {
                result.push_back(std::string(path) + "/"+ ent->d_name);
		std::string aaa=std::string(path) + "/"+ ent->d_name;
		    printf("ratio %s\n", aaa.c_str());
            } 
        }
        closedir (dir);
    } else {
        throw "someting wrong!\n";
    }
    return result;
}

std::vector<TLorentzVector> Read(std::vector<std::string> const &files) {

    std::vector<TLorentzVector> data;
    StdHepIter iter(files);
    double nEvt = 0;
    double nPas = 0;
    for(LCCollection * col; (col = iter.getCollection()); ) {

    TLorentzVector v4(0,0,0,0);
    bool isS = false;
    bool isS2 = false;
    bool isB = false;
    bool isB2 = false;
    int  IsS2 = 0;
    int  IsS3=0;
    for(int i = 0; i < (int)col->getNumberOfElements(); ++i) {
        MCParticle *mcp = (MCParticle*)col->getElementAt(i);
           
             if(mcp->getPDG() == 25 && mcp->getDaughters().size() > 0 ) {
             //if(mcp->getPDG() == 25 && mcp->getDaughters().size() > 0 ) {
                isS = true;
             }


		int pdg = mcp->getPDG();
	    if((!isS)&&mcp->getParents().size()==0&&(abs(pdg) == 12 || abs(pdg) == 14 || abs(pdg) == 16))isB=true;
        if(isS)isB=false;
        if(mcp->getParents().size()==0&&(pdg==1 || pdg==2 || pdg==3 || pdg==4 || pdg==5))  {
             //if(mcp->getPDG() == 25 && mcp->getDaughters().size() > 0 ) {
                IsS2 = IsS2 + 1;
        }
//        if(mcp->getParents().size()==0&&abs(pdg)==13)  {
//             //if(mcp->getPDG() == 25 && mcp->getDaughters().size() > 0 ) {
//                IsS2 = IsS2 + 1;
//        }
        if((mcp->getParents().size()==0)&&pdg==-1||pdg==-2||pdg==-3||pdg==-4||pdg==-5)  {
             //if(mcp->getPDG() == 25 && mcp->getDaughters().size() > 0 ) {
                IsS3 = IsS3 + 1;
        }
		//if(mcp->getParents().size()==0&&abs(pdg)<10)isS2=true;
	     //if(mcp->getParents().size()==0&&pdg == 15)isB=true;
//	     if(mcp->getParents().size()==0&&(abs(pdg) == 12 || abs(pdg) == 14 || abs(pdg) == 16))isB=true;

	     MCParticle *par=mcp;
	     if(par->getParents().size()>0){
	     	do{
	     		par=par->getParents()[0];
	     	}while(par->getParents().size()>0);
	     }

	     float parpdg=par->getPDG();

	     //if(pdg==25)isS = false;
             if(mcp->getGeneratorStatus() == 1 && (abs(parpdg)<10||parpdg==22)) { //stable;
             //if(mcp->getGeneratorStatus() == 1) { //stable;
               //if(abs(pdg) != 12 && abs(pdg) != 14 && abs(pdg) != 16) {
                    double e = mcp->getEnergy();
                    double const *p = mcp->getMomentum();
                    TLorentzVector thisV4(p[0], p[1], p[2], e);
                    v4 += thisV4;
                //}
             }
    } // for elements
//    printf("IsS2: %i\n",IsS2);
    
        if((isS)&&(IsS2==1)&&(IsS2==1)||isB){
                nPas +=1;
                data.push_back(v4);
        }
        nEvt += 1;
    }  // for collection
    printf("nEvt %f\n", nEvt);
    printf("ratio %f\n", nPas/nEvt);
    return data;

}


struct Book {

    int fN;
    std::string fName;
    Book(char const *fileName) {
        fName = fileName;
        fN = 0;
    }

    void Add(TCanvas &cvs) {

	    cvs.SetWindowSize(500,500);
        if(fN == 0) cvs.Print((fName + ".pdf(").c_str());
        else cvs.Print((fName + ".pdf").c_str());
        fN += 1;
    }

    ~Book() {
        TCanvas cvs;
	    cvs.SetWindowSize(500,500);
        TH1D h;
        h.SetTitle(fName.c_str());
        cvs.Print((fName + ".pdf)").c_str());
    }
};




struct DataSet {

    double fSqrts;
    double fXsection;
    TH1D *fMass;
    TH1D *fRecoil;
    TH2D *fRecoilTheta;
    double fBMR;
    double fNum;
    std::string fLabel;
    int fEnlarge;
    DataSet(std::string label, double sqrts, double xsec) {
        fLabel = label;
        fSqrts = sqrts;
        fXsection = xsec;
        fMass = new TH1D("","", 200, 0, 200);
        fRecoil = new TH1D(Form("fRecoil_%s", fLabel.c_str()),"fRecoil", 300, 0, 300);
        fRecoilTheta = new TH2D("","", 200, 0, 200, 20, -1, 1);
        fNum = 0;
        fEnlarge = 1;
    }
   
    ~DataSet() {
        delete fMass;
        delete fRecoil;
    } 
    void Read(std::vector<TLorentzVector> const &data, double BMR) {
            fBMR = BMR;
            for(int i = 0; i < (int)data.size(); ++i) {
                for(int  r = 0; r < fEnlarge; ++r) {
                TLorentzVector v4 = data[i];
                TLorentzVector inc(0, 0, 0, fSqrts);
                v4 = v4 * (1 + BMR*gRandom->Gaus());
                fMass->Fill(v4.M());
                fRecoil->Fill((v4-inc).M());
                //printf("M %f\n", v4.E());
                fNum += 1;
                }
            }   
            Print();
   }   

    
    void Print() {
  
        bool draw = false; 
        if(draw) {
                TCanvas cvs;
	    cvs.SetWindowSize(500,500);
                fRecoil->Draw("");
                char b[1024];
                sprintf(b, "%s_recoil_BMR%f_sqrts%f", fLabel.c_str(), fBMR, fSqrts);
                cvs.Print((std::string(b) + ".png").c_str()); 
                cvs.Print((std::string(b) + ".pdf").c_str()); 
        }
           
    
    }    



    double Precision(DataSet &bkg, double L, Book *book = NULL) {
            gStyle->SetOptStat(0);
            gStyle->SetOptTitle(0);
	gStyle->SetCanvasDefH(600);
	  	gStyle->SetCanvasDefW(600);
	  gStyle->SetLabelSize(0.04,"xyz");
	  gStyle->SetTitleSize(0.05,"xyz");
	  gStyle->SetTitleOffset(1.4,"yz");
	  gStyle->SetTitleOffset(1.2,"x");

  gStyle->SetPadBottomMargin(0.15);
  gStyle->SetPadTopMargin(0.05);
  gStyle->SetPadRightMargin(0.05);
  gStyle->SetPadLeftMargin(0.15);

            {
                char b[1024];
                sprintf(b, "%s+%s_mass_BMR%f_sqrts%f", fLabel.c_str(), bkg.fLabel.c_str(), fBMR, fSqrts);
                TCanvas cvs;
	    cvs.SetWindowSize(500,500);
                bkg.fMass->SetTitle(b);
                fMass->SetLineColor(kRed); 
                bkg.fMass->SetLineColor(kGreen); 
               
                bkg.fMass->Draw("");
                bkg.fMass->SetStats(0);
                fMass->Draw("SAME");
                
                TLegend leg(0.7, 0.7, 0.89, 0.89);
                leg.AddEntry(fMass, "ZH qqtautau", "l");
                leg.AddEntry(bkg.fMass, "ZZ qqtautau", "l");
                leg.SetBorderSize(0);
                leg.SetFillColor(0);
                leg.Draw();
                cvs.Print((std::string(b) + ".png").c_str()); 
                cvs.Print((std::string(b) + ".pdf").c_str());
                if(book) book->Add(cvs); 
            } 
 
    
            gStyle->SetOptStat(0);
	  {
                char b[1024];
                sprintf(b, "%s+%s_recoil_BMR%f_sqrts%f", fLabel.c_str(), bkg.fLabel.c_str(), fBMR, fSqrts);
                TCanvas cvs;
	    cvs.SetWindowSize(500,500);
                bkg.fRecoil->SetTitle(b);
                bkg.fRecoil->SetStats(0);
                fRecoil->SetStats(0);
                bkg.fRecoil->SetLineColor(kGreen);
                fRecoil->SetLineColor(kRed);
		bkg.fRecoil->GetXaxis()->SetTitle("M_{qq}^{rec}[GeV]");
		bkg.fRecoil->GetXaxis()->CenterTitle();
		bkg.fRecoil->GetYaxis()->SetTitle("Events/1GeV");
		bkg.fRecoil->GetYaxis()->CenterTitle();
		//tautau: before cut 48266/609672; with ratio: 16257/10307
		//inv: before cut 76613/1254904;
		fRecoil->Scale(812./fNum);
		fRecoil->SetEntries(812);
		bkg.fRecoil->Scale(1254904./bkg.fNum);
		bkg.fRecoil->SetEntries(1254904.);
                 
                bkg.fRecoil->Draw("");
                fRecoil->Draw("SAME");
                
                TLegend leg(0.75, 0.75, 0.92, 0.92);
                leg.AddEntry(fRecoil, "ZH qq+tautau", "l");
                leg.AddEntry(bkg.fRecoil, "ZZ qq+tautau", "l");
                leg.SetBorderSize(0);
                leg.SetFillColor(0);
                leg.SetFillStyle(0);
                leg.Draw(); 
                
	TLatex * prelim = new TLatex(0.94,0.92, "CEPC Preliminary");
	prelim->SetNDC();
	prelim->SetTextFont(42);
	prelim->SetTextSize(0.040);
	prelim->SetTextAlign(33);
	prelim->Draw();
                cvs.Print((std::string(b) + ".C").c_str()); 
                cvs.Print((std::string(b) + ".pdf").c_str());
                if(book) book->Add(cvs); 
 
        } 
  



        double prec = 0;
        double S = 0; 
        double B = 0;
        double X = 0;
        double sumS = 0;
        double sumB = 0;
            double p_m2=0;
	    //printf("%f sig %f, %f bkg %f\n",fRecoil->GetEntries(),fRecoil->Integral(),bkg.fRecoil->GetEntries(),bkg.fRecoil->Integral());
        for(int i = 1; i <= fRecoil->GetNbinsX(); ++i) {
            double s = fRecoil->GetBinContent(i);
            double b = bkg.fRecoil->GetBinContent(i);
            //s = s * 48266./fNum; 
            //s = s * 16257./fNum; 
            //s = s * fXsection*L/fNum; 
            //b = b * 609672./bkg.fNum; 
            //b = b * 52307./bkg.fNum; 
            //b = b * bkg.fXsection*L/bkg.fNum; 

            if(b == 0) p_m2 = s;
            else p_m2 = (s*s)/(s+b); 
            prec += p_m2;
       //     if(s != 0 || b != 0) {
       //         S += s*s/(s+b);
       //         B += b*b/(s+b);
       //         X += s*b/(s+b);
       //         sumS += s;
       //         sumB += b;
       //     }

		//if(p_m2>0)printf("%ith bin, s= %f , b=%f, bin acc = %f\n",i, s,b,sqrt(s+b)/s);
        }
        printf("S/B = %f\n", sumS/sumB);
        //B += 1./(0.00375*0.00375);
        //B += 1./(0.00375*0.00375);
        //chi2 = S ds^2 + B db^2 + 2X ds db
        //chi2 =  {ds, db} {{sigma s^2, rho sigma s sigma b},{ rho sigma s sigma b, sigma b^2}}^-1 {ds, db}^T
        //prec = sqrt(S/(S*B-X*X));
        prec = 1./sqrt(prec);
        return prec; 
    }


   
};


std::vector<std::string> at_most(std::vector<std::string> vs, size_t n) {
    if(vs.size() > n) vs.resize(n);
    return vs;
}


void DrawPrecisionVsBMR() {



    double sqrts[] = {240};
    char const *sigPath[] = {
	    "/cefs/higgs/tanyuhang/BMR2Precision/stdhep/ffh_inv"
    };
    char const *bkgPath[] = {
	    "/cefs/higgs/tanyuhang/BMR2Precision/stdhep/bkg"
    };
    double sigXsec[] = {
	    136.81*0.00106
    };
    double bkgXsec[] = {
	    224.09
    };
    char b[1024];
    for(int s = 0; s < (int)(sizeof(sqrts)/sizeof(double)); ++s) {
    sprintf(b, "PrecisionVsBMRBook_sqrts%f", sqrts[s]);

    Book precisionVsBMRBook(b);
    std::vector<double> xs;
    std::vector<double> ys;
    std::vector<double> ysp;

    std::vector<TLorentzVector> sigData = Read(at_most(files(sigPath[s], ".stdhep"),10));
    std::vector<TLorentzVector> bkgData = Read(at_most(files(bkgPath[s], ".stdhep"),10));
    for(double BMR = 0; BMR < 0.4000001; BMR += 0.01) {
        DataSet sig("sig", 240, sigXsec[s]);
        DataSet bkg("bkg", 240, bkgXsec[s]);
        sig.Read(sigData, BMR);
        bkg.Read(bkgData, BMR);
        
        Book *book = NULL;
    //    if(fabs(BMR)<0.0001 || fabs(BMR - 0.05)<0.0001 || fabs(BMR - 0.2) < 0.0001) book = &precisionVsBMRBook;
        double pre = sig.Precision(bkg, 5600, book);
        printf("Pre  %f\n", pre);
        
        xs.push_back(BMR*100);
        ys.push_back(pre*100); 
        ysp.push_back(pre*100); 
    }
    
    TGraph gr(xs.size(), xs.data(), ys.data());
    gr.SetTitle("");
    gr.GetXaxis()->SetTitle("BMR[%]");
    gr.GetXaxis()->CenterTitle();
    gr.GetYaxis()->SetTitle("Accuracy[%]");
    gr.GetYaxis()->SetTitleOffset(1.4);
    gr.GetYaxis()->CenterTitle();
    TGraph grp(xs.size(), xs.data(), ysp.data());
    {
            TCanvas cvs;
	    cvs.SetWindowSize(500,500);
            gr.Draw("ACP");

	TLatex * prelim = new TLatex(0.94,0.92, "CEPC Preliminary");
	prelim->SetNDC();
	prelim->SetTextFont(42);
	prelim->SetTextSize(0.040);
	prelim->SetTextAlign(33);
	prelim->Draw();
            cvs.Print("PrecisionvsBMR_240GeV.pdf");
            cvs.Print("PrecisionvsBMR_240GeV.C");
            precisionVsBMRBook.Add(cvs);    
    }
    }

}



int main() {

    DrawPrecisionVsBMR();
    //DrawPrecisionVsSqrts(0);

    return 0;
}
