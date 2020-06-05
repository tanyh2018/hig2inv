#!/usr/bin/env python
"""
Common tools   (slightly modified from the one used in J/psi->invi.)
"""

__author__ = "SHI Xin <shixin@ihep.ac.cn>"
__copyright__ = "Copyright (c) SHI Xin"
__created__ = "[2016-06-28 Tue 09:17]" 

import sys 
import os
import shutil  
import subprocess
import ROOT 


# ---------------------------------------------
# Function 
# ---------------------------------------------

def check_and_join(filepath, filename, mode=''):
    if not os.access(filepath, os.F_OK):
        sys.stdout.write('creating dir %s ...' % filepath)
        os.makedirs(filepath)
        sys.stdout.write(' OK.\n')
        
    file_ = os.path.join(filepath, filename)
    if os.access(file_, os.F_OK) :
        tmpfile = make_tmpfile(file_)
        shutil.copy2(file_, tmpfile)
        if mode == 'w':
            os.remove(file_)

    return file_

def check_outfile_path(outfile):
    path, tail = os.path.split(outfile)
    if path != '' and not os.access(path, os.F_OK) :
        sys.stdout.write('Creating dir %s ...\n'  % path)
        os.makedirs(path)


def convert_size_from_str(size_str):
    c_1GB = 1024*1024*1024
    factor = eval(size_str.split('G')[0])
    return factor*c_1GB


def duration(seconds): 
    seconds = long(round(seconds))
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365.242199)
 
    minutes = long(minutes)
    hours = long(hours)
    days = long(days)
    years = long(years)
 
    duration = []
    if years > 0:
        duration.append('%d year' % years + 's'*(years != 1))
    else:
        if days > 0:
            duration.append('%d day' % days + 's'*(days != 1))
        if hours > 0:
            duration.append('%d hour' % hours + 's'*(hours != 1))
        if minutes > 0:
            duration.append('%d minute' % minutes + 's'*(minutes != 1))
        if seconds > 0:
            duration.append('%d second' % seconds + 's'*(seconds != 1))
    return ' '.join(duration)


def group_files_by_size(name_list, size_max='20G'):
    size_max = convert_size_from_str(size_max)
    groups = []
    group = []    
    size_sum = 0

    for name in name_list:
        size = os.path.getsize(name)
        if size_sum < size_max:
            group.append(name)
            size_sum += float(size)
        else:
            groups.append(group)
            group = []
            size_sum = 0
            group.append(name)            
            size_sum += float(size)

        if name == name_list[-1]:
            groups.append(group)

    return groups

def proc_cmd(cmd, test=False, verbose=1, procdir=None, shell=False):
    if test:
        sys.stdout.write(cmd+'\n')
        return 

    # No need to add quote in the cmd! 
    cwd = os.getcwd()
    if procdir is not None:
        os.chdir(procdir)
    
    args = cmd.split()

    if isinstance(cmd, list) or shell:
        args = cmd 

    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, shell=shell)
    stdout = process.communicate()[0]

    if 'error' in stdout:
        sys.stdout.write(stdout)
        
    if procdir is not None:
        os.chdir(cwd)

    return stdout


def save_list_into_file(file_list, dst):
    nfiles = len(file_list)
    
    path, tail = os.path.split(dst)
    if path != '' and not os.access(path, os.F_OK) :
        sys.stdout.write('Creating dir %s ...\n'  % path)
        os.makedirs(path)
                
    fo = open(dst, 'w')
#    fo.write('EventCnvSvc.digiRootInputFile = {\n')

    n = 0
    for f in file_list:
        n = n+1
        fo.write('%s \n' % f)
#        if n<nfiles:
#            fo.write('"%s",\n' % f)
#        else:
#            fo.write('"%s"\n};\n' % f)

    fo.close()
    sys.stdout.write('Saved as: %s\n' %dst)

    
def set_root_style(stat=0, grid=0, PadTopMargin=0.08,
                   PadLeftMargin=0.15):
    # must be used in the beginning
    ROOT.gROOT.SetBatch(1)
    ROOT.gROOT.Reset()
    CEPCStyle()
def CEPCStyle():
    
    CEPCCDRStyle = ROOT.TStyle("CEPCCDRStyle","Style for CEPC CDR by Kaili")
    CEPCCDRStyle.SetCanvasBorderMode(0)
    CEPCCDRStyle.SetCanvasColor(0)
    CEPCCDRStyle.SetCanvasDefH(800) #Height of canvas
    CEPCCDRStyle.SetCanvasDefW(800) #Width of canvas
    CEPCCDRStyle.SetCanvasDefX(0)   #POsition on screen
    CEPCCDRStyle.SetCanvasDefY(0)
	# For the Pad:
    CEPCCDRStyle.SetPadBorderMode(0)
    # CEPCCDRStyle->SetPadBorderSize(Width_t size = 1)
    CEPCCDRStyle.SetPadColor(0)
    CEPCCDRStyle.SetGridStyle(3)
    CEPCCDRStyle.SetGridWidth(1)

    # For the frame:
    CEPCCDRStyle.SetFrameBorderMode(0)
    CEPCCDRStyle.SetFrameBorderSize(1)
    CEPCCDRStyle.SetFrameFillColor(0)
    CEPCCDRStyle.SetFrameFillStyle(0)
    CEPCCDRStyle.SetFrameLineColor(1)
    CEPCCDRStyle.SetFrameLineStyle(1)
    CEPCCDRStyle.SetFrameLineWidth(2)

    # For the histo:
    # CEPCCDRStyle->SetHistFillColor(1)
    # CEPCCDRStyle->SetHistFillStyle(0)
    # CEPCCDRStyle->SetHistLineColor(1)
    CEPCCDRStyle.SetHistLineStyle(0)
    # CEPCCDRStyle->SetHistLineWidth(2)
    # CEPCCDRStyle->SetLegoInnerR(0.8)
    # CEPCCDRStyle->SetNumberContours(Int_t number = 20)

    CEPCCDRStyle.SetEndErrorSize(2)
    #CEPCCDRStyle->SetErrorMarker(20)
    #CEPCCDRStyle->SetErrorX(0.)

    CEPCCDRStyle.SetMarkerStyle(20)

    #For the fit/function:
    CEPCCDRStyle.SetOptFit(0)
    CEPCCDRStyle.SetFitFormat("5.4g")
    CEPCCDRStyle.SetFuncColor(2)
    CEPCCDRStyle.SetFuncStyle(1)
    CEPCCDRStyle.SetFuncWidth(2)

    #For the date:
    CEPCCDRStyle.SetOptDate(0)
    # CEPCCDRStyle->SetDateX(Float_t x = 0.01)
    # CEPCCDRStyle->SetDateY(Float_t y = 0.01)

    # For the statistics box:
    CEPCCDRStyle.SetOptFile(0)
    CEPCCDRStyle.SetOptStat(0) 		# To display the mean and RMS:   SetOptStat("mr")
    CEPCCDRStyle.SetStatColor(0)
    CEPCCDRStyle.SetStatTextColor(1)
    CEPCCDRStyle.SetStatFormat("6.4g")
    CEPCCDRStyle.SetStatBorderSize(1)
    CEPCCDRStyle.SetStatH(0.1)
    CEPCCDRStyle.SetStatW(0.15)
    # CEPCCDRStyle->SetStatStyle(Style_t style = 1001)
    # CEPCCDRStyle->SetStatX(Float_t x = 0)
    # CEPCCDRStyle->SetStatY(Float_t y = 0)

    # Margins:
    # canvas->SetMargin(0.16, 0.04, 0.11, 0.02) # left, right, bottom, top
    CEPCCDRStyle.SetPadLeftMargin(0.16)
    CEPCCDRStyle.SetPadRightMargin(0.04)
    CEPCCDRStyle.SetPadBottomMargin(0.11)
    CEPCCDRStyle.SetPadTopMargin(0.02)

    # For the Global title:

    CEPCCDRStyle.SetOptTitle(0)
    CEPCCDRStyle.SetTitleFont(43)
    CEPCCDRStyle.SetTitleColor(1)
    CEPCCDRStyle.SetTitleTextColor(1)
    CEPCCDRStyle.SetTitleFillColor(0)
    CEPCCDRStyle.SetTitleFontSize(36)


    # For the axis titles:

    CEPCCDRStyle.SetTitleColor(1, "XYZ")
    CEPCCDRStyle.SetTitleFont(43, "XYZ")
    CEPCCDRStyle.SetTitleSize(36, "XYZ")

    CEPCCDRStyle.SetTitleXOffset(0.9)
    CEPCCDRStyle.SetTitleYOffset(1.0)
    # CEPCCDRStyle->SetTitleOffset(1.1, "Y") # Another way to set the Offset

    # For the axis labels:

    CEPCCDRStyle.SetLabelColor(1, "XYZ")
    CEPCCDRStyle.SetLabelFont(43, "XYZ")
    CEPCCDRStyle.SetLabelOffset(0.005, "XYZ")
    CEPCCDRStyle.SetLabelSize(34, "XYZ")

    # For the axis:

    CEPCCDRStyle.SetAxisColor(1, "XYZ")
    CEPCCDRStyle.SetStripDecimals(1)
    CEPCCDRStyle.SetTickLength(0.02, "XYZ")
    CEPCCDRStyle.SetNdivisions(508, "XYZ")    
    CEPCCDRStyle.SetPadTickX(1)  
    CEPCCDRStyle.SetPadTickY(1)
    # CEPCCDRStyle->SetPadTickZ(1)

    # Change for log plots:
    CEPCCDRStyle.SetOptLogx(0)
    CEPCCDRStyle.SetOptLogy(0)
    CEPCCDRStyle.SetOptLogz(0)

    # Postscript options:
    CEPCCDRStyle.SetPaperSize(20.,20.)
    # CEPCCDRStyle->SetLineScalePS(Float_t scale = 3)
    # CEPCCDRStyle->SetLineStyleString(Int_t i, const char* text)
    # CEPCCDRStyle->SetHeaderPS(const char* header)
    # CEPCCDRStyle->SetTitlePS(const char* pstitle)

    # CEPCCDRStyle->SetBarOffset(Float_t baroff = 0.5)
    # CEPCCDRStyle->SetBarWidth(Float_t barwidth = 0.5)
    # CEPCCDRStyle->SetPaintTextFormat(const char* format = "g")
    # CEPCCDRStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0)
    # CEPCCDRStyle->SetTimeOffset(Double_t toffset)
    # CEPCCDRStyle->SetHistMinimumZero(kTRUE)

    CEPCCDRStyle.SetHatchesLineWidth(5)
    CEPCCDRStyle.SetHatchesSpacing(0.05)

    # CEPCCDRStyle->SetCanvasPreferGL(kTRUE) # ok in Mac or lxslc6, not in local windows/linux.

    CEPCCDRStyle.cd()
# ---------------------------------------------
# Class 
# ---------------------------------------------

class UserFile(object):
    '''Class to handle file  '''
    def __init__(self, filename=None, data=None):
        self.data = []
        if data != None:
            self.data = data
            
        if filename:
            self.input(filename)
            self.file = filename

    def append(self, content):
        self.data.append(content)

    def input(self, filename, verbose=0):
        fi = open(filename, 'r')
        for line in fi:
            self.data.append(line)
        fi.close()

    def input_data(self, data):
        self.data = data
        
        
class BossLogFile(UserFile):
    "Handle BOSS log file"

    def __init__(self, filename=None):
        self.terminated = False
        UserFile.__init__(self, filename)
        self.parse()
        
    def parse(self):
        "parse BOSS log file" 
        line_no = -1
        for line in self.data:
            line_no += 1
            line = line.strip()
            if 'INFO Application Manager Terminated successfully' in line:
                self.terminated = True

class EventsLogFile(UserFile):
    "Handle Events log file"

    def __init__(self, filename=None):
        self.terminated = False
        UserFile.__init__(self, filename)
        self.parse()
        
    def parse(self):
        "parse Events log file" 
        line_no = -1
        for line in self.data:
            line_no += 1
            line = line.strip()
            if 'Done ' in line:
                self.terminated = True
