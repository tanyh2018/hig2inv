#!/usr/bin/env python
#Check whether jobs can work.
import sys
import os
import re
def main():
    args=sys.argv[1:]
    infile=args[0]
    i = 1
    j = 1
    for root, dirs, files in os.walk(infile):
        for f in files:
            bf = f.split('_')[0]
            if bf =='log':

                filename = root+'/'+f
                fout_script = open(filename,'rw')
                str='Myhig2inv'
                if not (re.compile(str) == 'NONE'):
#                    print ('Run %d successful\n'%i)
                    i=i+1
                else:
                    print ('Run %d fild:%s\n' %(j,f))
                    j=j+1
    print ('The successful numbers are %d \n'%(i-1))
    print ('the fialed numbers are %d \n' %(j-1))
             
                
if __name__ == '__main__':
    main()