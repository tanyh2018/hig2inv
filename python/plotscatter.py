 #!/usr/bin/env python
import sys
import os
import math
import ROOT
Mylist=[[0,1.67E+12],[4E+14,1.52E+12],[8E+14,1.40E12],[1.5E+15,1.22E12],[3E+15,8.97E11]]
x=0
y=0
i=0
n=5
h2 = ROOT.TH2F('h2','h2',100,0,4E+15,100,0,2E+12)
#TH2F * h2 = new TH2F("h2","h2 title",8,0,4,8,0,4)
c = ROOT.TCanvas('c', 'c', 200, 10, 700, 500)
for i in range(len(Mylist)):
    x=Mylist[i][0]
    y=Mylist[i][1]
    h2.Fill(x,y)
h2.Draw("ALP")
h2.GetXaxis().SetTitle("Fluence (Neq/cm^2)")
h2.GetYaxis().SetTitle("Integral of doping profile")
h2.SetLineWidth(2)
h2.SetMarkerStyle(21)
h2.GetXaxis().CenterTitle()
h2.GetYaxis().CenterTitle()
h2.Draw("")
c.SaveAs("a.pdf")