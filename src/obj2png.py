# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 00:40:00 2018

@author: Peter M. Clausen, pclausen

MIT License

Copyright (c) 2018 pclausen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import argparse
import ObjFile
import sys
import os
import glob

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Obj to png using MatPlotLib')

    parser.add_argument("-i", "--infiles",
              dest='objfiles',
              nargs='+',              
              help="File or files to be converted to png")

    parser.add_argument("-o", "--outfile",
              dest='outfile',
              help="Output file(s). Default: infile.png")

    parser.add_argument("-a", "--azimuth",
              dest='azim',
              type=float,
              help="Azimuth angle of view in degrees.")

    parser.add_argument("-e", "--elevation",
              dest='elevation',
              type=float,
              help="Elevation angle of view in degrees.")

    parser.add_argument("-q", "--quality",
              dest='quality',
              help="Image quality (HIGH,MEDIUM,LOW).  Default: LOW")

    parser.add_argument("-s", "--scale",
              dest='scale',
              type=float,
              help="Scale picture by descreasing boundaries. Lower than 1. gives a larger object.")

    parser.add_argument("-v", "--view",
              dest='view',
              action='store_true',
              help="View instead of creating picture file.")

    parser.add_argument("-A", "--Animate",
              dest='animate',
              action='store_true',
              help="Animate instead of creating picture file as animation, from elevation -180:180 and azim -180:180")

    args = parser.parse_args()

    print (args)
    
    objfiles=args.objfiles
    if '*' in objfiles[0]:
        objfiles=glob.glob(objfiles[0])
    
    res={'HIGH':1200,'MEDIUM':600,'LOW':300}
    dpi=None
    if args.quality:
        if type(args.quality)==int:
            dpi=args.quality
        elif args.quality.upper() in res:
            dpi=res[args.quality.upper()]

    azim=None
    if args.azim is not None:
        azim=args.azim

    elevation=None
    if args.elevation is not None:
        elevation=args.elevation

    scale=None
    if args.scale:
        scale=args.scale

    animate=None
    if args.animate:
        animate=args.animate
        
    for objfile in objfiles:
        
        if os.path.isfile(objfile) and '.obj' in objfile:
            outfile = objfile.replace('.obj','.png')
            if args.outfile:
                outfile=args.outfile
            if args.view:
                outfile=None
            else:
                print('Converting %s to %s'%(objfile, outfile))
            ob = ObjFile.ObjFile(objfile)
            ob.Plot(outfile,elevation=elevation,azim=azim,dpi=dpi,scale=scale,animate=animate)
        else:
            print('File %s not found or not file type .obj'%objfile)
            sys.exit(1)
    
    
    
    