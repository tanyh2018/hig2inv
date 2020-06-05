#!/usr/bin/env python
"""  
Plot summary histograms  
"""

__author__ = "Tanyh <tanyuhang@ihep.ac.cn>"
__copyright__ = "Copyright (c) Tanyh"
__created__ = "[2016-07-25 Mon 09:22]"

import os 
import sys 
import copy
import ROOT 
from tools import check_outfile_path, set_root_style,CEPCStyle
from ROOT import TLine,TArrow

def main(): 
    set_root_style(stat=0, grid=0)
  #  ROOT.gStyle.SetPadLeftMargin(0.15)
    processname = sys.argv[1]
    sample = sys.argv[1:]
    CEPCStyle()
    fs = get_files_from_sample(sample,processname)
    c = ROOT.TCanvas('c', 'c', 200, 10, 700, 500)
    
 #   ROOT.gStyle.SetOptStat(0)
 #   ROOT.gStyle.SetOptTitle(0)
    c.SetTopMargin(0.05)

    if  processname == "qqH":
        #draw_after_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_cut_TauTauM(sample, c, fs, processname)
        #draw_after_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_cut_dijet_e(sample, c, fs, processname)
       # draw_after_cut_dijet_m(sample, c, fs, processname)
        draw_after_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_cut_dijet_p(sample, c, fs, processname)
        #draw_after_cut_vis(sample, c, fs, processname)
        #draw_after_cut_cos_miss(sample, c, fs, processname)	
        #draw after first cut
        draw_after_first_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_first_cut_TauTauM(sample, c, fs, processname)
        #draw_after_first_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_first_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_first_cut_dijet_e(sample, c, fs, processname)
        #draw_after_first_cut_dijet_m(sample, c, fs, processname)
        #draw_after_first_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_first_cut_dijet_p(sample, c, fs, processname)
        #draw_after_first_cut_vis(sample, c, fs, processname)
        #draw_after_first_cut_cos_miss(sample, c, fs, processname)
        #draw after second cut
        #draw_after_second_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_second_cut_TauTauM(sample, c, fs, processname)
        #draw_after_second_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_second_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_second_cut_dijet_e(sample, c, fs, processname)
        #draw_after_second_cut_dijet_m(sample, c, fs, processname)
        #draw_after_second_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_second_cut_dijet_p(sample, c, fs, processname)
        draw_after_second_cut_vis(sample, c, fs, processname)
        #draw_after_second_cut_cos_miss(sample, c, fs, processname)	
        #draw after third cut
        #draw_after_third_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_third_cut_TauTauM(sample, c, fs, processname)
        #draw_after_third_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_third_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_third_cut_dijet_e(sample, c, fs, processname)
        draw_after_third_cut_dijet_m(sample, c, fs, processname)
        #draw_after_third_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_third_cut_dijet_p(sample, c, fs, processname)
        #draw_after_third_cut_vis(sample, c, fs, processname)
        #draw_after_third_cut_cos_miss(sample, c, fs, processname)	
        #draw after fourth cut
        #draw_after_fourth_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_fourth_cut_TauTauM(sample, c, fs, processname)
        #draw_after_fourth_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_fourth_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_fourth_cut_dijet_e(sample, c, fs, processname)
        #draw_after_fourth_cut_dijet_m(sample, c, fs, processname)
        #draw_after_fourth_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_fourth_cut_dijet_p(sample, c, fs, processname)
        #draw_after_fourth_cut_vis(sample, c, fs, processname)
        #draw_after_fourth_cut_cos_miss(sample, c, fs, processname)			
        ##draw after fifth cut
        #draw_after_fifth_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_fifth_cut_TauTauM(sample, c, fs, processname)
        #draw_after_fifth_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_fifth_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_fifth_cut_dijet_e(sample, c, fs, processname)
        #draw_after_fifth_cut_dijet_m(sample, c, fs, processname)
        #draw_after_fifth_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_fifth_cut_dijet_p(sample, c, fs, processname)
        #draw_after_fifth_cut_vis(sample, c, fs, processname)
        #draw_after_fifth_cut_cos_miss(sample, c, fs, processname)			
        ##draw after sixth cut
        #draw_after_sixth_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_sixth_cut_TauTauM(sample, c, fs, processname)
        #draw_after_sixth_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_sixth_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_sixth_cut_dijet_e(sample, c, fs, processname)
        #draw_after_sixth_cut_dijet_m(sample, c, fs, processname)
        #draw_after_sixth_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_sixth_cut_dijet_p(sample, c, fs, processname)
        #draw_after_sixth_cut_vis(sample, c, fs, processname)
        #draw_after_sixth_cut_cos_miss(sample, c, fs, processname)			
        ##draw after seventh cut
        #draw_after_seventh_cut_dijet_Pt(sample, c, fs, processname)
        #draw_after_seventh_cut_TauTauM(sample, c, fs, processname)
        #draw_after_seventh_cut_dijet_ang(sample, c, fs, processname)
        #draw_after_seventh_cut_dijet_phi(sample, c, fs, processname)
        #draw_after_seventh_cut_dijet_e(sample, c, fs, processname)
        #draw_after_seventh_cut_dijet_m(sample, c, fs, processname)
        #draw_after_seventh_cut_dijet_rec_m(sample, c, fs, processname)
        #draw_after_seventh_cut_dijet_p(sample, c, fs, processname)
        #draw_after_seventh_cut_vis(sample, c, fs, processname)
        #draw_after_seventh_cut_cos_miss(sample, c, fs, processname)	
        
    else:
#After first cut
        #draw_after_first_cut_Pt(sample, c, fs, processname)
        #draw_after_first_cut_vdt(sample, c, fs, processname)
        #draw_after_first_cut_theta(sample, c, fs, processname)
        #draw_after_first_cut_vis(sample, c, fs, processname)
        #draw_after_first_cut_Mmumu(sample, c, fs, processname)
        draw_after_first_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_first_cut_ep(sample, c, fs, processname)
#After second cut
        #draw_after_second_cut_Pt(sample, c, fs, processname)
        #draw_after_second_cut_vdt(sample, c, fs, processname)
        #draw_after_second_cut_theta(sample, c, fs, processname)
        #draw_after_second_cut_vis(sample, c, fs, processname)
        draw_after_second_cut_Mmumu(sample, c, fs, processname)
        #draw_after_second_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_second_cut_ep(sample, c, fs, processname)
#After third cut
        draw_after_third_cut_Pt(sample, c, fs, processname)
        draw_after_third_cut_vdt(sample, c, fs, processname)
        #draw_after_third_cut_theta(sample, c, fs, processname)
        #draw_after_third_cut_vis(sample, c, fs, processname)
        #draw_after_third_cut_Mmumu(sample, c, fs, processname)
        #draw_after_third_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_third_cut_ep(sample, c, fs, processname)	
#After fourth cut
        #draw_after_fourth_cut_Pt(sample, c, fs, processname)
        #draw_after_fourth_cut_vdt(sample, c, fs, processname)
        #draw_after_fourth_cut_theta(sample, c, fs, processname)
        #draw_after_fourth_cut_vis(sample, c, fs, processname)
        #draw_after_fourth_cut_Mmumu(sample, c, fs, processname)
        #draw_after_fourth_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_fourth_cut_ep(sample, c, fs, processname)
#After fifth cut
        #draw_after_fifth_cut_Pt(sample, c, fs, processname)
        #draw_after_fifth_cut_vdt(sample, c, fs, processname)
        #draw_after_fifth_cut_theta(sample, c, fs, processname)
        draw_after_fifth_cut_vis(sample, c, fs, processname)
        #draw_after_fifth_cut_Mmumu(sample, c, fs, processname)
        #draw_after_fifth_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_fifth_cut_ep(sample, c, fs, processname)
#After sixth cut
        #draw_after_sixth_cut_Pt(sample, c, fs, processname)
        draw_after_sixth_cut_vdt(sample, c, fs, processname)
        #draw_after_sixth_cut_theta(sample, c, fs, processname)
        #draw_after_sixth_cut_vis(sample, c, fs, processname)
        #draw_after_sixth_cut_Mmumu(sample, c, fs, processname)
        #draw_after_sixth_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_sixth_cut_ep(sample, c, fs, processname)
#After seventh cut
        #draw_after_seventh_cut_Pt(sample, c, fs, processname)
        #draw_after_seventh_cut_vdt(sample, c, fs, processname)
        #draw_after_seventh_cut_theta(sample, c, fs, processname)
        #draw_after_seventh_cut_vis(sample, c, fs, processname)
        #draw_after_seventh_cut_Mmumu(sample, c, fs, processname)
        #draw_after_seventh_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_seventh_cut_ep(sample, c, fs, processname)					
#After all cut
        #draw_after_cut_Pt(sample, c, fs, processname)
        #draw_after_cut_vdt(sample, c, fs, processname)
        #draw_after_cut_theta(sample, c, fs, processname)
        #draw_after_cut_vis(sample, c, fs, processname)
        #draw_after_cut_Mmumu(sample, c, fs, processname)
        draw_after_cut_Mrecoil(sample, c, fs, processname)
        #draw_after_cut_ep(sample, c, fs, processname)



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

    if 'szorsw' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/sz_sw.root'))

    if 'zzorww' in sample:
        fs.append(ROOT.TFile('run/'+processname+'/'+'total/hist/zzorww.root'))	       
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
    print fs

    return fs

def get_common_objects_to_draw(fs, hname, leg):
    hs = []

    FormatLegend(leg)

    for f in fs:
        h = f.Get(hname)
        if fs.index(f) == 0:        
            h.SetLineColor(2)
            h.SetLineWidth(2)

        elif fs.index(f) == 1:
            h.SetLineColor(22)
            h.SetLineWidth(2)

        elif fs.index(f) == 2:
            h.SetLineColor(5)
            h.SetLineWidth(2)

        elif fs.index(f) == 3:
            h.SetLineColor(42)
            h.SetLineWidth(2)

        elif fs.index(f) == 4:
            h.SetLineColor(6)
            h.SetLineWidth(2)

        elif fs.index(f) == 5:
            h.SetLineColor(7)
            h.SetLineWidth(2)
 
        elif fs.index(f) == 6:     
            h.SetLineColor(14)
            h.SetLineWidth(2)

        elif fs.index(f) == 7:
            h.SetLineColor(3)
            h.SetLineWidth(2)

        elif fs.index(f) == 8:      
            h.SetLineColor(47)
            h.SetLineWidth(2)

        elif fs.index(f) == 9:      
            h.SetLineColor(33)
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

#    if sample in ['bkg_add_sig']:
#        leg.AddEntry(h, "bkg_add_sig")

    if sample in ['mumuH_inv','eeH_inv','qqH_inv']:
        leg.AddEntry(h, "signal","L")

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
#    else:
#        raise NameError(sample)

    return leg

#After first cut

def  draw_after_first_cut_Pt(sample, c, fs, processname):
    hname = 'after_first_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after first cut)')
                h.SetMaximum(30000)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after first cut)')
                #ROOT.gPad.SetYy(1)
                h.SetMaximum(1000000)
    
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_first_cut_vdt(sample, c, fs, processname):
    hname = 'after_first_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after first cut)')
                h.SetMaximum(20000)
            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after first cut)')
                h.SetMaximum(120000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_first_cut_theta(sample, c, fs, processname):
    hname = 'after_first_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after first cut)')
                h.SetMaximum(10000)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after first cut)')
#                h.SetMaximum(10)

            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_first_cut_vis(sample, c, fs, processname):
    hname = 'after_first_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(20000)
            if processname == "eeH": 

                h.SetMaximum(320000) 
  
            if processname == "qqH": 
                h.SetMaximum(10000)           
            h.SetXTitle('Visible Energy (GeV)(after first cuts)')
            h.SetYTitle('Events/(0.5GeV)')
#            #h.GetXaxis().SetRangeUser(90,120)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_first_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_first_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after first cut)')
                h.SetMaximum(20000)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after first cut)')
                h.SetMaximum(50000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_first_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_first_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.68, 0.62, 0.87, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":

                h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(before cut: 120GeV<M_{recoil}^{#mu^{+}#mu^{-}}<150GeV)')
                h.SetMaximum(1e7)
                h.SetMinimum(30)
                h.GetXaxis().SetRangeUser(0,250)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(before cut: 120GeV<M_{recoil}^{e^{+}e^{-}}<170GeV)')
                h.SetMaximum(1e10)
                h.SetMinimum(1e2)
            #ROOT.gPad.SetLogy(1)
            h.SetYTitle('Events/(0.5GeV)')
 
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    if processname == "mumuH":    
        arrow1 = TArrow(120,1e5,120,1e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(150,1e5,150,1e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(120,1e7,120,1e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(170,1e7,170,1e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_first_cut_ep(sample, c, fs, processname):
    hname = 'after_first_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('E/P(after first cut)')
            h.SetYTitle('Events')
            h.SetMaximum(20000)
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After second cut

def  draw_after_second_cut_Pt(sample, c, fs, processname):
    hname = 'after_second_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after second cut)')
                h.SetMaximum(3000)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after second cut)')
                h.SetMaximum(60000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_second_cut_vdt(sample, c, fs, processname):
    hname = 'after_second_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after second cut)')
                h.SetMaximum(2500)
            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after second cut)')
                h.SetMaximum(50000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_second_cut_theta(sample, c, fs, processname):
    hname = 'after_second_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after second cut)')
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after second cut)')
                h.SetMaximum(60000)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_second_cut_vis(sample, c, fs, processname):
    hname = 'after_second_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(10000)
            if processname == "eeH": 
                h.SetMaximum(60000)   
            if processname == "qqH":
                h.GetXaxis().SetRangeUser(70,140) 
                h.SetMaximum(5e5)
                h.SetMinimum(5e2)             
            h.SetXTitle('E_{visible}(GeV)(before cut: 90GeV<E_{visible}<117GeV)')
            h.SetYTitle('Events/(0.5GeV)')
#            #h.GetXaxis().SetRangeUser(90,120)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')
    if processname=="qqH":
        arrow1 = TArrow(90,1e5,90,2e3,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(117,1e5,117,2e3,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)


def draw_after_second_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_second_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(before cut: 85GeV<M_{#mu^{+}#mu^{-}}<97GeV)')
                h.SetMaximum(4e5)
                #h.GetXaxis().SetRangeUser(0,125)                
                h.SetMinimum(1e2)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(before cut: 71GeV<M_{e^{+}e^{-}}<99GeV)')
                h.SetMaximum(1e7)
                h.SetMinimum(1e2)
            h.SetYTitle('Events/(0.5GeV)')
#            ROOT.gPad.SetLogy(1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(85,2e4,85,2e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(97,2e4,97,2e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(71,1e5,71,2e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(99,1e5,99,2e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        arrow2.Draw()
        #arrow2.SetLineStyle(8)
    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_second_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_second_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after second cut)')
                h.SetMaximum(11000)
                #h.GetXaxis().SetRangeUser(120,150)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after second cut)')
                h.SetMaximum(15000)
                #h.GetXaxis().SetRangeUser(120,170)
            h.SetYTitle('Events/(0.5GeV)')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_second_cut_ep(sample, c, fs, processname):
    hname = 'after_second_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(4000)
            if processname == "eeH":
                h.SetMaximum(40000)
            h.SetXTitle('E/P(after second cut)')
            h.SetYTitle('Events')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After third cut

def  draw_after_third_cut_Pt(sample, c, fs, processname):
    hname = 'after_third_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{T}^{#mu^{+}#mu^{-}}(GeV)(before cut: 12GeV<P_{T}^{#mu^{+}#mu^{-}})')
                h.SetMaximum(1e6)
                h.SetMinimum(10)
            if processname == "eeH":
                h.SetXTitle('P_{T}^{e^{+}e^{-}}(GeV)(before cut: 12GeV<P_{T}^{e^{+}e^{-}}<55GeV)')
                h.SetMaximum(1e7)
                h.SetMinimum(40)
            h.SetYTitle('Events/(0.5GeV)')
            #h.GetXaxis().SetLabelSize(0.02)
            #h.GetXaxis().SetRangeUser(0,75)
            #h.GetYaxis().SetLabelSize(0.02)

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(12,1e5,12,100,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        arrow1.Draw()
        arrow2 = TArrow(12,1e3,30,1e3,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(12,1e5,12,1e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        arrow1.Draw()
        arrow2 = TArrow(55,1e5,55,1e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)


def draw_after_third_cut_vdt(sample, c, fs, processname):
    hname = 'after_third_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after third cut)')
                h.SetMaximum(2000)
            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after third cut)')
                h.SetMaximum(30000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_third_cut_theta(sample, c, fs, processname):
    hname = 'after_third_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after third cut)')
                h.SetMaximum(3000)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after third cut)')
                h.SetMaximum(30000)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_third_cut_vis(sample, c, fs, processname):
    hname = 'after_third_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(10000)
            if processname == "eeH": 
                h.SetMaximum(8000)   
            if processname == "qqH": 
                h.SetMaximum(10000)           
            h.SetXTitle('Visible Energy (GeV)(after third cut)')
            h.SetYTitle('Events/(0.5GeV)')
            #h.GetXaxis().SetRangeUser(90,120)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_third_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_third_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after third cut)')
                h.SetMaximum(25000)
                #h.GetXaxis().SetRangeUser(80,100)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after third cut)')
                h.SetMaximum(60000)
                #h.GetXaxis().SetRangeUser(70,100)
            h.SetYTitle('Events/(0.5GeV)')


            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_third_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_third_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                  h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after third cut)')
                  h.SetMaximum(10000)
                  #h.GetXaxis().SetRangeUser(120,150)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after third cut)')
                h.SetMaximum(40000)
                #h.GetXaxis().SetRangeUser(120,150)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_third_cut_ep(sample, c, fs, processname):
    hname = 'after_third_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(4000)
            if processname == "eeH":
                h.SetMaximum(15000)
            h.SetXTitle('E/P(after third cut)')
            h.SetYTitle('Events')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After fourth cut 

def  draw_after_fourth_cut_Pt(sample, c, fs, processname):
    hname = 'after_fourth_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after fourth cut)')
                h.SetMaximum(3000)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after fourth cut)')
                h.SetMaximum(30000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fourth_cut_vdt(sample, c, fs, processname):
    hname = 'after_fourth_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after fourth cut)')
                h.SetMaximum(600)
            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after fourth cut)')
                h.SetMaximum(10000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fourth_cut_theta(sample, c, fs, processname):
    hname = 'after_fourth_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after fourth cut)')
                h.SetMaximum(1200)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after fourth cut)')
                h.SetMaximum(10000)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fourth_cut_vis(sample, c, fs, processname):
    hname = 'after_fourth_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(3000)
            if processname == "eeH": 
                h.SetMaximum(3000)   
            if processname == "qqH": 
                h.SetMaximum(10000)           
            h.SetXTitle('Visible Energy (GeV)(after fourth cut)')
            h.SetYTitle('Events/(0.5GeV)')
            #h.GetXaxis().SetRangeUser(90,120)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fourth_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_fourth_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after fourth cut)')
                h.SetMaximum(10000)
                #h.GetXaxis().SetRangeUser(80,100)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after fourth cut)')
                h.SetMaximum(40000)
                #h.GetXaxis().SetRangeUser(70,100)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_fourth_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_fourth_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after fourth cut)')
                h.SetMaximum(8000)
                #h.GetXaxis().SetRangeUser(120,150)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after fourth cut)')
                h.SetMaximum(25000)
                #h.GetXaxis().SetRangeUser(120,170)
            h.SetYTitle('Events/(0.5GeV)')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_fourth_cut_ep(sample, c, fs, processname):
    hname = 'after_fourth_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(4000)
            if processname == "eeH":
                h.SetMaximum(15000)
            h.SetXTitle('E/P(after fourth cut)')
            h.SetYTitle('Events')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After fifth cut

def  draw_after_fifth_cut_Pt(sample, c, fs, processname):
    hname = 'after_fifth_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after fifth cut)')
                h.SetMaximum(2000)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after fifth cut)')
                h.SetMaximum(20000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fifth_cut_vdt(sample, c, fs, processname):
    hname = 'after_fifth_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after fifth cut)')
                h.SetMaximum(1200)
            if processname == "eeH":
                h.SetXTitle('|the recoil mass of visible minus tau (GeV)(after fifth cut)')
                h.SetMaximum(3000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fifth_cut_theta(sample, c, fs, processname):
    hname = 'after_fifth_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after fifth cut)')
                h.SetMaximum(1500)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after fifth cut)')
                h.SetMaximum(6000)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fifth_cut_vis(sample, c, fs, processname):
    hname = 'after_fifth_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(4000) 
#                h.SetMinimum(7e1)
                h.SetXTitle('E_{visible}(GeV)(before cut: 102GeV<E_{visible}<107GeV)')
                h.SetYTitle('Events/(0.5GeV)')  
            if processname == "eeH": 
                h.SetMaximum(5e4) 
                h.SetMinimum(1.5e2)
                h.SetXTitle('E_{visible}(GeV)(before cut: 101GeV<E_{visible}<107GeV)')
                h.SetYTitle('Events/(0.5GeV)')
                h.GetXaxis().SetRangeUser(80,250)  
            if processname == "qqH": 
                h.SetMaximum(20000)           

            ROOT.gPad.SetLogy(1)
            h.GetXaxis().SetRangeUser(85,250)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')
    if processname == "mumuH":    
        arrow1 = TArrow(102,2000,102,300,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(107,2000,107,300,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        #arrow2.SetLineStyle(8)
        arrow2.Draw()
    if processname == "eeH":
        arrow1 = TArrow(101,1e4,101,5e2,0.01)
        arrow1.SetLineColor(4)
        arrow1.SetLineWidth(2)
        #arrow1.SetLineStyle(8)
        arrow1.Draw()
        arrow2 = TArrow(107,1e4,107,5e2,0.01)
        arrow2.SetLineColor(4)
        arrow2.SetLineWidth(2)
        arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)


def draw_after_fifth_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_fifth_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after fifth cut)')
                h.SetMaximum(8000)
                #h.GetXaxis().SetRangeUser(84,98)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after fifth cut)')
                h.SetMaximum(15000)
                #h.GetXaxis().SetRangeUser(70,100)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_fifth_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_fifth_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after fifth cut)')
                h.SetMaximum(8000)
                #h.GetXaxis().SetRangeUser(120,150)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after fifth cut)')
                h.SetMaximum(8000)
                #h.GetXaxis().SetRangeUser(120,170)
            h.SetYTitle('Events/(0.5GeV)')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_fifth_cut_ep(sample, c, fs, processname):
    hname = 'after_fifth_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(4000)
            if processname == "eeH":
                h.SetMaximum(4000)
            h.SetXTitle('E/P(after fifth cut)')
            h.SetYTitle('Events')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After sixth cut

def  draw_after_sixth_cut_Pt(sample, c, fs, processname):
    hname = 'after_sixth_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after sixth cut)')
                h.SetMaximum(1500)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after sixth cut)')
                h.SetMaximum(600)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_sixth_cut_vdt(sample, c, fs, processname):
    hname = 'after_sixth_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after sixth cut)')
                h.SetMaximum(500)
            if processname == "eeH":
                h.GetXaxis().SetRangeUser(160,250)
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after sixth cut)')
                h.SetMaximum(600)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_sixth_cut_theta(sample, c, fs, processname):
    hname = 'after_sixth_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after sixth cut)')
                h.SetMaximum(1200)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after sixth cut)')
                h.SetMaximum(300)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_sixth_cut_vis(sample, c, fs, processname):
    hname = 'after_sixth_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(3000)
                #h.GetXaxis().SetRangeUser(90,120)
            if processname == "eeH": 
                h.SetMaximum(1000)
                #h.GetXaxis().SetRangeUser(102,120)   
            if processname == "qqH": 
                h.SetMaximum(10000)           
            h.SetXTitle('Visible Energy (GeV)(after sixth cut)')
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_sixth_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_sixth_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after sixth cut)')
                h.SetMaximum(8000)
                #h.GetXaxis().SetRangeUser(80,100)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after sixth cut)')
                h.SetMaximum(1000)
                #h.GetXaxis().SetRangeUser(70,100)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_sixth_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_sixth_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                  h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after sixth cut)')
                  #h.GetXaxis().SetRangeUser(120,150)
                  h.SetMaximum(6000)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after sixth cut)')
                h.SetMaximum(2000)
                #h.GetXaxis().SetRangeUser(120,170)
            h.SetYTitle('Events/(0.5GeV)')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_sixth_cut_ep(sample, c, fs, processname):
    hname = 'after_sixth_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(1200)
            if processname == "eeH":
                h.SetMaximum(500)

            h.SetXTitle('E/P(after sixth cut)')
            h.SetYTitle('Events')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After seventh cut 

def  draw_after_seventh_cut_Pt(sample, c, fs, processname):
    hname = 'after_seventh_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after seventh cut)')
                h.SetMaximum(500)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after seventh cut)')
                h.SetMaximum(600)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_seventh_cut_vdt(sample, c, fs, processname):
    hname = 'after_seventh_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after seventh cut)')
                h.SetMaximum(100)
            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after seventh cut)')
                h.SetMaximum(300)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_seventh_cut_theta(sample, c, fs, processname):
    hname = 'after_seventh_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after seventh cut)')
                h.SetMaximum(300)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after seventh cut)')
                h.SetMaximum(300)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_seventh_cut_vis(sample, c, fs, processname):
    hname = 'after_seventh_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(3000)
                #h.GetXaxis().SetRangeUser(102,107)
            if processname == "eeH": 
                h.SetMaximum(1000)
                #h.GetXaxis().SetRangeUser(102,120)     
            if processname == "qqH": 
                h.SetMaximum(10000)           
            h.SetXTitle('Visible Energy (GeV)(after seventh cut)')
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_seventh_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_seventh_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after seventh cut)')
                h.SetMaximum(2000)
                #h.GetXaxis().SetRangeUser(80,100)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after seventh cut)')
                h.SetMaximum(1000)
                #h.GetXaxis().SetRangeUser(70,100)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_seventh_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_seventh_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after seventh cut)')
                h.SetMaximum(4000)
                #h.GetXaxis().SetRangeUser(120,150)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after seventh cut)')
                h.SetMaximum(1200)
                #h.GetXaxis().SetRangeUser(120,170)
            h.SetYTitle('Events/(0.5GeV)')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_seventh_cut_ep(sample, c, fs, processname):
    hname = 'after_seventh_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(800)
            if processname == "eeH":
                #h.GetXaxis().SetRangeUser(1.7,2.5)
                h.SetMaximum(500)
            h.SetXTitle('E/P(after seventh cut)')
            h.SetYTitle('Events')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
#After all cuts

def  draw_after_cut_Pt(sample, c, fs, processname):
    hname = 'after_cut_Pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_Pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('P_{t}^{#mu^{+}#mu^{-}} (GeV)(after all cuts)')
                h.SetMaximum(1000)
            if processname == "eeH":
                h.SetXTitle('P_{t}^{e^{+}e^{-}} (GeV)(after all cuts)')
                h.SetMaximum(600)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_cut_vdt(sample, c, fs, processname):
    hname = 'after_cut_vdt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_vdt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:
            if processname == "mumuH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after all cuts)')
                h.SetMaximum(2400)

            if processname == "eeH":
                h.SetXTitle('the recoil mass of visible minus tau (GeV)(after all cuts)')
                h.SetMaximum(300)
            #h.GetXaxis().SetRangeUser(230,240)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_cut_theta(sample, c, fs, processname):
    hname = 'after_cut_theta'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_theta.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('#Delta#phi_{#mu^{+}#mu^{-}}(after all cuts)')
                h.SetMaximum(150)
            if processname == "eeH":
                h.SetXTitle('#Delta#phi_{e^{+}e^{-}}(after all cuts)')
                h.SetMaximum(300)
            h.SetYTitle('Events')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_cut_vis(sample, c, fs, processname):
    hname = 'after_cut_vis'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_vis.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetMaximum(3000)
                #h.GetXaxis().SetRangeUser(102,107)
            if processname == "eeH": 
                h.SetMaximum(600)  
                #h.GetXaxis().SetRangeUser(102,120) 
            if processname == "qqH": 
                h.SetMaximum(10000)           
            h.SetXTitle('Visible Energy (GeV)(after all cuts)')
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_cut_Mmumu(sample, c, fs, processname):
    hname = 'after_cut_Mmumu'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_Mmumu.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                h.SetXTitle('M_{#mu^{+}#mu^{-}}(GeV)(after all cuts)')
                h.SetMaximum(2000)
                #h.GetXaxis().SetRangeUser(80,100)
            if processname == "eeH":
                h.SetXTitle('M_{e^{+}e^{-}}(GeV)(after all cuts)')
                h.SetMaximum(1000)
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def  draw_after_cut_Mrecoil(sample, c, fs, processname):
    hname = 'after_cut_Mrecoil'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_Mrecoil.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            if processname == "mumuH":
                  h.SetXTitle('M_{recoil}^{#mu^{+}#mu^{-}}(GeV)(after all cuts)')
                  h.SetMaximum(5000)
                  #h.GetXaxis().SetRangeUser(120,135)
            if processname == "eeH":
                h.SetXTitle('M_{recoil}^{e^{+}e^{-}}(GeV)(after all cuts)')
                h.SetMaximum(1300)
            h.SetYTitle('Events/(0.5GeV)')

            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def  draw_after_cut_ep(sample, c, fs, processname):
    hname = 'after_cut_ep'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_ep.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('E/P')
            h.SetYTitle('Events')
            h.SetMaximum(800)
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


def draw_after_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after all cuts)')	
            h.SetMaximum(14000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the  mass of  tau (GeV)(after all cuts)')
            h.SetMaximum(2000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after all cuts)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after all cuts)')
            h.SetMaximum(5000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after all cuts)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after all cuts)')
            h.SetMaximum(13000)
#            h.GetXaxis().SetRangeUser(85,120)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            #h.GetXaxis().SetRangeUser(85,102)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after all cuts)')
            h.SetMaximum(9800)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #h.GetXaxis().SetRangeUser(100,150)
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after all cuts)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after all cuts)')
            h.SetMaximum(3000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

#after first cut
def draw_after_first_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_first_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{T}^{visible}(GeV)(before cut:18GeV<P_{T}^{visible}<60GeV)')	
            h.SetMaximum(1e7)
            h.SetMinimum(6e2)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')
            ROOT.gPad.SetLogy(1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')
    arrow1 = TArrow(18,1e6,18,5e3,0.01)
    arrow1.SetLineColor(4)
    arrow1.SetLineWidth(3)
    arrow1.Draw()
    arrow2 = TArrow(60,1e6,60,5e3,0.01)
    arrow2.SetLineColor(4)
    arrow2.SetLineWidth(3)
    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)

def draw_after_first_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_first_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the mass of tau (GeV)(after first cut)')
            h.SetMaximum(40000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_first_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_first_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after first cut)')
            h.SetMaximum(400000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_first_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_first_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after first cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_first_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_first_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after first cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(240000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_first_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_first_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after first cut)')
            h.SetMaximum(300000)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_first_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_first_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after first cut)')
            h.SetMaximum(200000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_first_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_first_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after first cut)')
            h.SetMaximum(200000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_first_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_first_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_first_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after first cut)')
            h.SetMaximum(60000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

#after second cut
def draw_after_second_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_second_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after second cut)')	
            h.SetMaximum(140000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_second_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_second_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the mass of tau (GeV)(after second cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_second_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_second_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after second cut)')
            h.SetMaximum(200000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_second_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_second_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after second cut)')
            h.SetMaximum(50000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_second_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_second_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after second cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(120000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_second_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_second_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after second cut)')
            h.SetMaximum(60000)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_second_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_second_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after second cut)')
            h.SetMaximum(150000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_second_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_second_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after second cut)')
            h.SetMaximum(100000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_second_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_second_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_second_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after second cut)')
            h.SetMaximum(120000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

   
#after third cut 
def draw_after_third_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_third_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after third cut)')	
            h.SetMaximum(28000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_third_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_third_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the mass of tau (GeV)(after third cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_third_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_third_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after third cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_third_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_third_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after third cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_third_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_third_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after third cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_third_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_third_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.31, 0.62, 0.5, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(before cut: 85GeV<M_{visible}<102GeV)')
            h.SetMaximum(30000)
            h.SetMinimum(100)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')
    arrow1 = TArrow(85,20000,85,4000,0.01)
    arrow1.SetLineColor(4) 
    arrow1.SetLineWidth(3)
    arrow1.Draw()
    arrow2 = TArrow(102,20000,102,4000,0.01)
    arrow2.SetLineColor(4)
    arrow2.SetLineWidth(3)
    arrow2.Draw()
    leg.Draw()
    c.SaveAs(figfile)

def draw_after_third_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_third_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after third cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_third_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_third_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after third cut)')
            h.SetMaximum(30000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_third_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_third_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_third_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after third cut)')
            h.SetMaximum(30000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


#after fourth cut
def draw_after_fourth_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_fourth_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after fourth cut)')	
            h.SetMaximum(14000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fourth_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_fourth_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the mass of tau (GeV)(after fourth cut)')
            h.SetMaximum(2000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fourth_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_fourth_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after fourth cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_fourth_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_fourth_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after fourth cut)')
            h.SetMaximum(5000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_fourth_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_fourth_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after fourth cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_fourth_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_fourth_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after fourth cut)')
            h.SetMaximum(15000)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fourth_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_fourth_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after fourth cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fourth_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_fourth_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after fourth cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_fourth_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_fourth_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fourth_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after fourth cut)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

#after fifth cut
def draw_after_fifth_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_fifth_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after fourth cut)')	
            h.SetMaximum(14000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fifth_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_fifth_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the  mass of  tau (GeV)(after fifth cut)')
            h.SetMaximum(2000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fifth_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_fifth_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after fifth cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_fifth_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_fifth_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after fifth cut)')
            h.SetMaximum(5000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_fifth_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_fifth_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after fifth cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_fifth_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_fifth_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after fifth cut)')
            h.SetMaximum(15000)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fifth_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_fifth_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after fifth cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_fifth_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_fifth_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after fifth cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_fifth_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_fifth_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_fifth_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after fifth cut)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)


    #after sixth cut 
def draw_after_sixth_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_sixth_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after sixth cut)')	
            h.SetMaximum(14000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_sixth_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_sixth_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the  mass of tau (GeV)(after sixth cut)')
            h.SetMaximum(2000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_sixth_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_sixth_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after sixth cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_sixth_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_sixth_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after sixth cut)')
            h.SetMaximum(5000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_sixth_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_sixth_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after sixth cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_sixth_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_sixth_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after sixth cut)')
            h.SetMaximum(15000)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_sixth_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_sixth_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after sixth cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_sixth_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_sixth_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after sixth cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_sixth_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_sixth_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_sixth_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after sixth cut)')
            h.SetMaximum(6000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

#after seventh cut
def draw_after_seventh_cut_dijet_Pt(sample, c, fs, processname):
    
    hname = 'after_seventh_cut_dijet_pt'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_dijet_pt.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:

            h.SetXTitle('P_{t}^{visible}(GeV)(after seventh cut)')	
            h.SetMaximum(14000)
#            h.SetMinimum(0.00000000000001)		
            h.SetYTitle('Events/(0.5GeV)')

            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_seventh_cut_TauTauM(sample, c, fs, processname):

    hname = 'after_seventh_cut_TauTauM'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_TauTauM.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('the mass of tau (GeV)(after seventh cut)')
            h.SetMaximum(2000)
#            h.SetMinimum(0.0000001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_seventh_cut_dijet_ang(sample, c, fs, processname):
    hname = 'after_seventh_cut_dijet_dang'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_dijet_dang.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('|#angle_{dijet}|(after seventh cut)')
            h.SetMaximum(20000)
#            h.SetMinimum(0.000001)

            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	
def draw_after_seventh_cut_dijet_phi(sample, c, fs, processname):
    hname = 'after_seventh_cut_dijet_dphi'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_dijet_dphi.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('#Delta#phi_{dijet}(after seventh cut)')
            h.SetMaximum(5000)
#            h.SetMinimum(0)
            h.SetYTitle('Events')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
def draw_after_seventh_cut_dijet_e(sample, c, fs, processname):

    hname = 'after_seventh_cut_dijet_e'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_dijet_e.pdf'

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('Energy of dijet (GeV)(after seventh cut)')
            h.SetYTitle('Events/(0.5GeV)')
            h.SetMaximum(12000)
#            h.SetMinimum(0.000001)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)	

def draw_after_seventh_cut_dijet_m(sample, c, fs, processname):

    hname = 'after_seventh_cut_dijet_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_dijet_m.pdf'
    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 1:
            h.SetXTitle('M_{visible}(GeV)(after seventh cut)')
            h.SetMaximum(15000)
#            h.SetMinimum(0.0001)
            h.SetYTitle('Events/(0.5GeV)')
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 1:
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_seventh_cut_dijet_rec_m(sample, c, fs, processname):	
    hname = 'after_seventh_cut_m_dijet_rec_m'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_m_dijet_rec_m.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('M_{recoil}^{visible}(GeV)(after seventh cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)

def draw_after_seventh_cut_dijet_p(sample, c, fs, processname):	
    hname = 'after_seventh_cut_dijet_p'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_m_dijet_p.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('P_{visible}(GeV)(after seventh cut)')
            h.SetMaximum(10000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events/(0.5GeV)')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
            h.Draw('same')

    leg.Draw()
    c.SaveAs(figfile)
    
def draw_after_seventh_cut_cos_miss(sample, c, fs, processname):	
    hname = 'after_seventh_cut_cos_miss'
    figfile = 'fig/'+processname+'/'+'after/hig2inv_after_seventh_cut_cos_miss.pdf'
    check_outfile_path(figfile)

    leg = ROOT.TLegend(0.71, 0.62, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg)

    for h in hs:
        histrogram_set(h)
        if hs.index(h) == 0:

            h.SetXTitle('|cos#theta_{miss}|(after seventh cut)')
            h.SetMaximum(3000)
#            h.SetMinimum(0.00000000000001)
            h.SetYTitle('Events')
            #            h.GetYaxis().SetRange(0,400)
            # Plot title?
#            gPad.SetLogy();
            #            h.SetMinimum(0.1)
            h.Draw()
    for h in hs:
        histrogram_set(h)
        if not hs.index(h) == 0:
            #            h.GetYaxis().SetRangeUser(0,1000)
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
