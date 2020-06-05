#!/usr/bin/env python
"""  
Plot summary histograms 
"""
  
__author__ = "Tanyh <shixin@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyh"
__created__ = "[2016-07-25 Mon 09:22]"

import os
import sys
import copy
import ROOT
from ROOT import TLine,TArrow
from tools import check_outfile_path, set_root_style,CEPCStyle


def main():  
    set_root_style(stat=0, grid=0) 
#    ROOT.gStyle.SetPadLeftMargin(0.15)
    processname = sys.argv[1]
    sample = sys.argv[2:]
    CEPCStyle()
    fs = get_files_from_sample(sample,processname)
    c = ROOT.TCanvas('c', 'c', 200, 10, 700, 500)
    c.SetTopMargin(0.05)
    if processname == "qqH":
        draw_before_cut_dijet_Pt(sample, c, fs, processname)
        #draw_before_cut_TauTauM(sample, c, fs, processname)
        #draw_before_cut_dijet_ang(sample, c, fs, processname)
        #draw_before_cut_dijet_phi(sample, c, fs, processname)
        draw_before_cut_dijet_e(sample, c, fs, processname)
        draw_before_cut_dijet_m(sample, c, fs, processname)
        draw_before_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_before_cut_dijet_p(sample, c, fs, processname)	
        draw_before_cut_vis(sample, c, fs, processname)
        #draw_before_cut_cos_miss(sample, c, fs, processname)						
#    draw_before_cut_n_moun(sample, c, fs, processname)
#	draw_before_cut_n_photon(sample, c, fs, processname)
    else:
        draw_before_cut_Pt(sample, c, fs, processname)
        draw_before_cut_vdt(sample, c, fs, processname)
        draw_before_cut_theta(sample, c, fs, processname)
        draw_before_cut_vis(sample, c, fs, processname)
        draw_before_cut_Mmumu(sample, c, fs, processname)
        draw_before_cut_Mrecoil(sample, c, fs, processname)
        #draw_before_cut_ep(sample, c, fs, processname)



def get_files_from_sample(sample,processname):
    fs = []       
    if 'signal' in sample:
        if processname == "mumuH":
            fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/mumuH_inv.root'))
        if processname == "eeH":
            fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/eeH_inv.root'))	
        if processname == "qqH":
            fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/qqH_inv.root'))	

    if 'ZZ' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/ZZ.root'))

    if 'WW' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/WW.root'))

    if 'single_z' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/single_z.root'))

    if 'single_w' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/single_w.root'))

    if 'zzorww' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/zzorww.root'))	

    if 'szorsw' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/sz_sw.root'))	
        
    if '2f' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/2f.root'))

    if 'XH_visible' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/XH_visible.root'))

    if processname == "eeH":
        if 'eeH_visible' in sample:
            fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/eeH_visible.root'))

    if processname == "qqH":
        if 'qqH_visible' in sample:
            fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/qqH_visible.root'))

    if processname == "mumuH":
        if 'mumuH_visible' in sample:
            fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/mumuH_visible.root'))


    return fs

def get_common_objects_to_draw(fs, hname, leg, processname):
    hs = []
    FormatLegend(leg)
    for f in fs:
#       print f
        h = f.Get(hname)
        if fs.index(f) == 0:
#            if processname == "eeH":				
#                h.Scale(1.0/19712.0)
#            if processname == "mumuH":
#                h.Scale(1.0/18956.0)
#            if processname == "qqH":
#                h.Scale(1.0/383068.0)                 
            h.SetLineColor(2)
            h.SetLineWidth(2)

        elif fs.index(f) == 1:
#            h.Scale(1.0/6389430.0)
            h.SetLineColor(22)
            h.SetLineWidth(2)

        elif fs.index(f) == 2:
#            h.Scale(1.0/50826214.0)
            h.SetLineColor(5)
            h.SetLineWidth(2)

        elif fs.index(f) == 3:
#            h.Scale(1.0/9072951.0)
            h.SetLineColor(42)
            h.SetLineWidth(2)

        elif fs.index(f) == 4:
#            h.Scale(1.0/19517400.0)
            h.SetLineColor(6)
            h.SetLineWidth(2)

        elif fs.index(f) == 5:
#            h.Scale(1.0/20440840.0)  
            h.SetLineColor(7)
            h.SetLineWidth(2)
 
        elif fs.index(f) == 6:
#            h.Scale(1.0/1397088.0)     
            h.SetLineColor(14)
            h.SetLineWidth(2)

        elif fs.index(f) == 7:
#            h.Scale(1.0/801152072.0)
            h.SetLineColor(3)
            h.SetLineWidth(2)

        elif fs.index(f) == 8:      
            h.SetLineColor(33)
            h.SetLineWidth(2)

        elif fs.index(f) == 9:      
            h.SetLineColor(29)
            h.SetLineWidth(2)

        else:
            print "Sample name misses, please check that!"
            sys.exit() 		

        leg = leg_add_entry_hist(leg, f, h)
        hs.append(h)

    return  hs, leg


def leg_add_entry_hist(leg, f, h):
    sample = f.GetName()
    sample = sample.split('/')[-1]
    sample = sample.split('.root')[0]


    if sample in ['mumuH_inv','eeH_inv','qqH_inv']:
        leg.AddEntry(h, "signal")

    elif sample in ['ZZ']:
        leg.AddEntry(h, "ZZ","L")

    elif sample in ['WW']:
        leg.AddEntry(h, "WW","L")

    elif sample in ['sz_sw']:
        leg.AddEntry(h, "szorsw","L")

    elif sample in ['single_z']:
        leg.AddEntry(h, "single_z","L")

    elif sample in ['single_w']:
        leg.AddEntry(h, "single_w","L")

    elif sample in ['zzorww']:
        leg.AddEntry(h, "zzorww","L")

    elif sample in ['2f']:
        leg.AddEntry(h, "2fbkg","L")

    elif sample in ['XH_visible']:
        leg.AddEntry(h, "XH_visible","L")

    elif sample in ['qqH_visible']:
        leg.AddEntry(h, "qqH_visible","L")    
    elif sample in ['eeH_visible']:
        leg.AddEntry(h, "eeH_visible","L")    
    elif sample in ['mumuH_visible']:
        leg.AddEntry(h, "mumuH_visible","L")    
    else:
        raise NameError(sample)

    return leg

def  draw_before_cut_Pt(sample, c, fs, processname):
    hname = 'before_cut_Pt'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            if processname == "mumuH":
                h.SetXTitle('P_{T}^{#mu^{+}#mu^{-}} (GeV)')
                h.GetXaxis().SetRangeUser(0,70)
                h.SetMaximum(1)
                h.SetMinimum(0.00000000000001)	
            if processname == "eeH":
                h.SetXTitle('P_{T}^{e^{+}e^{-}} (GeV)')
                h.GetXaxis().SetRangeUser(0,100)	
                h.SetMaximum(0.06)
                h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h) 
        if not hs.index(h) == 6:
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(12,0.4,12,0.1,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        arrow1.Draw()
        arrow2 = TArrow(12,0.2,24,0.2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(12,0.04,12,0.01,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        arrow1.Draw()
        arrow2 = TArrow(55,0.04,55,0.01,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)


def draw_before_cut_vdt(sample, c, fs, processname):
    hname = 'before_cut_vdt'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        ROOT.gPad.SetLogy(1)
        if hs.index(h) == 6:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)')
                h.SetMaximum(0.04)
                h.SetMinimum(0.0000001)
            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)')
                h.SetMaximum(1000000)
                h.SetMinimum(10)
                
            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_before_cut_theta(sample, c, fs, processname):
    hname = 'before_cut_theta'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}')
                h.SetMaximum(0.02)
                h.SetMinimum(0.000001)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}')
                h.SetMaximum(0.04)
                h.SetMinimum(0)
            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_before_cut_vis(sample, c, fs, processname):
    hname = 'before_cut_vis'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            h.SetXTitle('Visible Energy (GeV)(raw data)')
            h.SetYTitle('Normalized to 1')
            if processname == "mumuH": 
                h.SetMaximum(0.2)
                h.GetXaxis().SetRangeUser(0,300)
            if processname == "eeH":
                h.SetMaximum(0.06)
                h.GetXaxis().SetRangeUser(0,300)
            if processname == "qqH": 
                h.SetMaximum(0.06)
                h.GetXaxis().SetRangeUser(0,300)                                                          
            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(102,0.08,102,0.01,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(107,0.08,107,0.01,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(103,0.03,103,0.005,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(120,0.03,120,0.005,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)


def draw_before_cut_Mmumu(sample, c, fs, processname):
    hname = 'before_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)
#    ROOT.gPad.SetLogy(1)
    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            if processname == "mumuH":
                h.GetXaxis().SetRangeUser(0,120)
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)')
                h.SetMaximum(1)
                h.SetMinimum(0.0001)
            if processname == "eeH":
                h.GetXaxis().SetRangeUser(0,250)
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)')
                h.SetMaximum(0.05)
                h.SetMinimum(0.0001)
            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(85,0.4,85,0.1,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(97,0.4,97,0.1,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(71,0.03,71,0.005,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(99,0.03,99,0.005,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)


def  draw_before_cut_Mrecoil(sample, c, fs, processname):
    hname = 'before_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            if processname == "mumuH":
                h.GetXaxis().SetRangeUser(0,250)
                h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(before all cuts: 120GeV<M_{recoil}^{#mu^{+}#mu^{-}}<150GeV)')
                h.SetMaximum(1e4)
                h.SetMinimum(10)
            if processname == "eeH":
                h.GetXaxis().SetRangeUser(0,250)
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(before all cuts: 120GeV<M_{recoil}^{e^{+}e^{-}}<170GeV)')
                h.SetMaximum(1e4)
                h.SetMinimum(10)
#            ROOT.gPad.SetLogy(1)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
 #           gPad.SetLogy()
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            #            h.GetYaxis().SetLimits(0,1000)
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(120,1e6,120,1e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(150,1e6,150,1e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    #if processname == "eeH":
    #    arrow1 = TArrow(120,1e7,120,1e2,0.01)
    #    arrow1.SetLineColor(4)
    #    arrow1.SetLineWidth(2)
    #    #arrow1.SetLineStyle(8)
    #    arrow1.Draw()
    #    arrow2 = TArrow(170,1e7,170,1e2,0.01)
    #    arrow2.SetLineColor(4)
    #    arrow2.SetLineWidth(2)
    #    #arrow2.SetLineStyle(8)
    #    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)
    c.Print("test.C")
def  draw_before_cut_ep(sample, c, fs, processname):

    hname = 'before_cut_ep'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:

            h.SetXTitle('E/P')
            h.SetYTitle('Events/(1Gev)')
            h.SetMaximum(0.03)
            h.SetMinimum(0.00000000000001)
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            #            h.GetYaxis().SetLimits(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_before_cut_dijet_Pt(sample, c, fs, processname):

    hname = 'before_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:

            h.SetXTitle('P_{T}^{visible}(GeV)(raw data)')	
            h.SetMaximum(0.09)
            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Normalized to 1')
            h.GetXaxis().SetRangeUser(0,110)

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')
    arrow1 = TArrow(30,0.04,30,0.015,0.01)
    arrow1.SetLineColor(4)
    arrow1.SetLineWidth(3)
    arrow1.Draw()
    arrow2 = TArrow(60,0.04,60,0.015,0.01)
    arrow2.SetLineColor(4)
    arrow2.SetLineWidth(3)
    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)

def draw_before_cut_TauTauM(sample, c, fs, processname):

    hname = 'before_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            h.SetXTitle('the mass of Candidate tau (GeV)(raw data)')
            h.SetMaximum(0.03)
            h.SetMinimum(0.0000001)
            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_before_cut_dijet_ang(sample, c, fs, processname):
    hname = 'before_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            h.SetXTitle('|#angle_{dijet}|(raw data)')
            h.SetMaximum(0.1)
            h.SetMinimum(0.000001)

            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_before_cut_dijet_phi(sample, c, fs, processname):
    hname = 'before_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            h.SetXTitle('#Delta#phi_{dijet}(raw data)')
            h.SetMaximum(0.25)
            h.SetMinimum(0)
            h.SetYTitle('Normalized to 1')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_before_cut_dijet_e(sample, c, fs, processname):

    hname = 'before_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            h.SetXTitle('Visible Energy (GeV)(raw data)')
            h.SetYTitle('Normalized to 1')
            h.GetXaxis().SetRangeUser(0,300)
            h.SetMaximum(0.06)
            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')
    arrow1 = TArrow(90,0.03,90,0.01,0.01)
    arrow1.SetLineColor(4)
    arrow1.SetLineWidth(3)
    arrow1.Draw()
    arrow2 = TArrow(117,0.03,117,0.01,0.01)
    arrow2.SetLineColor(4)
    arrow2.SetLineWidth(3)
    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)	

def draw_before_cut_dijet_m(sample, c, fs, processname):

    hname = 'before_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:
            h.SetXTitle('M_{visible}(GeV)(raw data)')
            h.SetMaximum(0.04)
            h.SetMinimum(0.0001)
            h.SetYTitle('Normalized to 1')
            h.GetXaxis().SetRangeUser(0,300)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            h.Draw('same')
    arrow1 = TArrow(85,0.02,85,0.005,0.01)
    arrow1.SetLineColor(4)
    arrow1.SetLineWidth(3)
    arrow1.Draw()
    arrow2 = TArrow(102,0.02,102,0.005,0.01)
    arrow2.SetLineColor(4)
    arrow2.SetLineWidth(3)
    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)

def draw_before_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'before_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)
    CEPCStyle()
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(before cut:100GeV<M_{recoil}^{visible}<150GeV)')
            h.SetMaximum(1e9)
            h.SetMinimum(3e2)
            h.SetYTitle('Events/(0.5GeV)')
            h.GetXaxis().SetRangeUser(0,250)
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            ROOT.gPad.SetLogy(1)
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            #            h.GetYaxis().SetLimits(0,1000)
            h.Draw('same')
    arrow1 = TArrow(100,1e7,100,1e3,0.01)
    arrow1.SetLineColor(4)
    arrow1.SetLineWidth(3)
    arrow1.Draw()
    arrow2 = TArrow(150,1e7,150,1e3,0.01)
    arrow2.SetLineColor(4)
    arrow2.SetLineWidth(3)
    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)
    c.SaveAs('fig/qqH/before/recoil_dijet.C')
def draw_before_cut_dijet_p(sample, c, fs, processname):	
    hname = 'before_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 6:

            h.SetXTitle('P_{visible}(GeV)(raw data)')
            h.SetMaximum(0.05)
            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Normalized to 1')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            gPad.SetLogy()
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 6:
            #            h.GetYaxis().SetLimits(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_before_cut_cos_miss(sample, c, fs, processname):	
    hname = 'before_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'before/hig2inv_before_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('cos#theta_{miss}(raw data)')
            h.SetMaximum(0.06)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy()
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetLimits(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def histrogram_set(h):
#    ci = TColor::GetColor("#000099")
#    h.SetLineColor(ci)
    h.GetXaxis().CenterTitle()
    h.GetXaxis().SetLabelFont(42)  
    h.GetXaxis().SetTitleSize(0.04)
    h.GetXaxis().SetTitleOffset(1.2)
    h.GetXaxis().SetTitleFont(42)
    h.GetYaxis().CenterTitle()
    h.GetYaxis().SetLabelFont(42)
    h.GetYaxis().SetTitleSize(0.05)
    h.GetYaxis().SetTitleOffset(1.2)
    h.GetYaxis().SetTitleFont(42)
    h.GetZaxis().SetLabelFont(42)
    h.GetZaxis().SetTitleSize(0.04)
    h.GetZaxis().SetTitleOffset(1.2)
    h.GetZaxis().SetTitleFont(42)



def FormatLegend(leg):

    leg.SetBorderSize(0)
    leg.SetTextFont(43)
    leg.SetTextSize(15)
    leg.SetFillStyle(0)
    leg.SetFillColor(0)
    leg.SetLineColor(0)
    
if __name__ == '__main__':
    main()
