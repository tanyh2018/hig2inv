#!/usr/bin/env python
"""
Plot signal-bg histograms 
"""

__author__ = "Tanyh"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2018-10-12 Friday 10:53]" 

import sys,os,copy
import ROOT 
from tools import check_outfile_path, set_root_style

def main():

    args = sys.argv[1:]
    tab = open(args[0] , 'r' )

    c = ROOT.TCanvas('c', 'c', 200, 10, 700, 500)

    draw_after_cut_n_photon(tab, 'after_cut_n_photon', c)
    draw_after_cut_Pt(tab, 'after_cut_Pt', c) 
    draw_after_cut_Pz(tab, 'after_cut_Pz', c) 
    draw_after_cut_theta(tab, 'after_cut_theta', c) 
    draw_after_cut_vis(tab, 'after_cut_vis', c)
    draw_after_cut_Mmumu(tab, 'after_cut_Mmumu', c)
    draw_after_cut_Mrecoil(tab, 'after_cut_Mrecoil', c)
 

def plot_bkg_diagram(tab,pic,hc):
    i = 1
    for s_line in tab :
        if not s_line.startswith('#'):
            l = [x.strip() for x in s_line.split(',')]
            dname = l[0]
            event_exp = float(l[3])
            print dname
            if os.path.exists('./run/bg/hist' + '/' + dname + '/' + 'ana_File_merged_1.root'):
                exec ("sample%s = ROOT.TFile('./run/bg/hist' + '/' + dname + '/' + 'ana_File_merged_1.root')"%i)               
                exec ("h%s=sample%s.Get('hevtflw')"%(i,i))
                exec ("event_ana = h%s.GetBinContent(1)"%i)
                if event_ana != 0:
                    sc = event_exp / event_ana
                    if sc < 1000:
                        print ("%s:%s"%(dname,sc))
                        exec ("tem%s=sample%s.Get(pic)"%(i,i))
                        exec ("a%s=copy.copy(tem%s)"%(i,i))
                        exec ("a%s.Scale(sc)"%i)
                        exec ("event_tem=a%s.GetBinContent(1)"%i)                      
                        exec ("a%s.SetFillColor(ROOT.kOrange)"%i)
                        exec ("a%s.SetLineColor(ROOT.kOrange)"%i)
                        exec ("hc.Add(a%s)"%i) 
        i = i+1
    return hc
def plot_sig_diagram(hc):

    signal_sample =  ROOT.TFile('./run/e2E2h_invi/hist/ana_File_merged_1.root')
    b = signal_sample.Get(pic)
    b.Scale(0.054)
    b.SetFillColor(ROOT.kRed)
    b.SetLineColor(ROOT.kRed) 
    hc.Add(b)
	reture hc

def draw_after_cut_n_photon(tab, pic, c):
	
    figfile = './fig/after/hig2inv_after_cut_n_photon.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc","draw_after_cut_n_photon")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

def draw_after_cut_Pt(tab, pic, c):
	
    figfile = 'fig/after/hig2inv_after_cut_Pt.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc","draw_after_cut_Pt")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

def draw_after_cut_Pz(tab, pic, c):
	
    figfile = './fig/after/hig2inv_after_cut_Pz.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc","draw_after_cut_Pz")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

def draw_after_cut_theta(tab, pic, c):
	
    figfile = './fig/after/hig2inv_after_cut_theta.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc","draw_after_cut_theta")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

def draw_after_cut_vis(tab, pic, c):
	
    figfile = './fig/after/higinv_after_cut_vis.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc","draw_after_cut_vis")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

def  draw_after_cut_Mmumu(tab, pic, c):
	
    figfile = './fig/after/hig2inv_after_cut_Mmumu.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc"," draw_after_cut_Mmumu")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

def draw_after_cut_Mrecoil(tab, pic, c):

    figfile = './fig/after/hig2inv_after_cut_Mrecoil.pdf'
    check_outfile_path(figfile)
    hc = ROOT.THStack("hc","draw_after_cut_Mrecoil")
    hc = plot_sig_diagram(hc)
    hc = plot_bkg_diagram(tab,pic,hc) 
    hc.Draw()
    c.SaveAs(figfile) 

if __name__ == '__main__':
    main()
