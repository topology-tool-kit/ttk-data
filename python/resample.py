#!/usr/bin/env python

# Resample a VTI dataset.
# Julien Tierny <julien.tierny@sorbonne-universite.fr>, 2023.
# argv[1]: input file
# argv[2]: xDim
# argv[3]: yDim
# argv[4]: zDim
# argv[5]: output file


import sys

from paraview.simple import *

if len(sys.argv) == 6:
    inputFile = sys.argv[1]
    xDim = int(sys.argv[2])
    yDim = int(sys.argv[3])
    zDim = int(sys.argv[4])
    outputFile = sys.argv[5]
else:
    print("Missing mandatory argument!")
    print("Usage:")
    print(" $ python resample.py <input VTI> <xDim> <yDim> <zDim> <output VTI>")
    sys.exit()

print("Re-sampling `", inputFile, "` to ", xDim, "x", yDim, "x", zDim, "...")

inputData = XMLImageDataReader(FileName=[inputFile])
resample = ResampleToImage(Input=inputData)
resample.SamplingDimensions = [xDim, yDim, zDim]
SaveData(outputFile, resample)
