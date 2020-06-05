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
from tools import check_outfile_path, set_root_style


def main():  
    set_root_style(stat=0, grid=0)
    ROOT.gStyle.SetPadLeftMargin(0.15)
    processname = sys.argv[1]
    sample = sys.argv[2:]

    fs = get_files_from_sample(sample,processname)
    c = ROOT.TCanvas('c', 'c', 200, 10, 700, 500)
    draw_before_cut_n_moun(sample, c, fs, processname)



def get_files_from_sample(sample,processname):
    fs = []       

    if 'ffH_inv' in sample:
        fs.append(ROOT.TFile('ana_mu_e2e2_H_inv.root'))

    if 'e2e2h_X' in sample:
        fs.append(ROOT.TFile('ana_mu_e2e2_x.root'))

    if 'aa' in sample:
        fs.append(ROOT.TFile('ana_mu_e2e2_H_inv.root'))
    print fs

    return fs

def get_common_objects_to_draw(fs, hname, leg, processname):
    hs = []

    leg.SetTextSize(0.)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetLineWidth(0)
    leg.SetShadowColor(0)

    for f in fs:
        h = f.Get(hname)
        if fs.index(f) == 0:  
            h.Scale(1.0/4970.0)             
            h.SetLineColor(2)
            h.SetLineWidth(1)
            h.SetMarkerStyle(1)

        elif fs.index(f) == 1:
            h.Scale(1.0/964.0)
            h.SetLineColor(22)
            h.SetLineWidth(1)
            h.SetMarkerStyle(1)

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
    print sample

    if sample in ['mumuH_inv','eeH_inv','qqH_inv']:
        leg.AddEntry(h, "signal")

    elif sample in ['ana_mu_e2e2_H_inv']:
        leg.AddEntry(h, "ffH_inv")

    elif sample in ['ana_mu_e2e2_x']:
        leg.AddEntry(h, "e2e2h_X")

    elif sample in ['sz_sw']:
        leg.AddEntry(h, "szorsw")

    elif sample in ['single_z']:
        leg.AddEntry(h, "single_z")

    elif sample in ['single_w']:
        leg.AddEntry(h, "single_w")

    elif sample in ['zzorww']:
        leg.AddEntry(h, "zzorww")

    elif sample in ['2f']:
        leg.AddEntry(h, "2fbkg")
    elif sample in ['ZH_visible']:
        leg.AddEntry(h, "ZH_visible") 
    else:
        raise NameError(sample)

    return leg


def draw_before_cut_n_moun(sample, c, fs, processname):
    hname = 'before_cut_theta'
    figfile = 'test.pdf'

    leg = ROOT.TLegend(0.7, 0.71, 0.9, 0.91)
    hs, leg = get_common_objects_to_draw(fs, hname, leg, processname)
    for h in hs:
        if hs.index(h) == 1:
            h.SetYTitle('Normalized to 1')
            h.GetXaxis().SetLabelSize(0.02)
            h.GetYaxis().SetLabelSize(0.02)
            h.GetXaxis().CenterTitle()
            h.GetYaxis().CenterTitle()
            h.SetMarkerStyle(1)
            h.Draw()
    for h in hs:
        h.Draw('same')
    leg.Draw()
    c.SaveAs(figfile)


if __name__ == '__main__':
    main()
