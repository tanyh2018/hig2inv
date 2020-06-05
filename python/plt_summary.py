#!/usr/bin/env python
"""
Plot signal-bg histograms 
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2018-09-26 Wed 10:53]" 

import sys,os,copy
import ROOT 
from tools import check_outfile_path, set_root_style

def main():

    args = sys.argv[1:]
    tab = open(args[0] , 'r' )

    c = ROOT.TCanvas('c', 'c', 200, 10, 700, 500)

    draw_signal_bg_dimuon(tab, 'after_cut_Mrecoil', c)


def draw_signal_bg_dimuon(tab, pic, c):

    figfile = './fig/signal_bg%s.pdf'%pic
    check_outfile_path(figfile)

    hc = ROOT.THStack("hc","signal_bg")

    signal_sample =  ROOT.TFile('./run/e2E2h_invi/hist/ana_File_merged_1.root')
    b1 = signal_sample.Get(pic)
    b = copy.copy(b1)
    b.Scale(0.0054)
    b.SetFillColor(ROOT.kRed)
    b.SetLineColor(ROOT.kRed) 
    hc.Add(b)

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
        
    hc.Draw()
    c.SaveAs(figfile) 

if __name__ == '__main__':
    main()
