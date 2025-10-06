#!/usr/bin/env python

import sys

from paraview.simple import *

if len(sys.argv) == 2:
    dim = int(sys.argv[1])
else:
    dim = 128

# create a new 'XML Image Data Reader'
backpack = XMLImageDataReader(FileName=["backpack.vti"])

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=backpack)
resampleToImage1.SamplingDimensions = [dim, dim, dim]
resampleToImage1.SamplingBounds = [0.0, 511.0, 0.0, 511.0, 0.0, 372.0]

tTKArrayPreconditioning = TTKArrayPreconditioning(Input=resampleToImage1)
tTKArrayPreconditioning.PointDataArrays = ["ImageFile"]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKArrayPreconditioning)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "ImageFile"]
tTKPersistenceDiagram1.Backend = "Distributed Discrete Morse Sandwich"

# remove the dummy pairs representing the diagonal
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairType']
threshold1.UpperThreshold = 0.0
threshold1.ThresholdMethod = 'Above Upper Threshold'

UpdatePipeline()

# To save the output to disk, uncomment the line below.
# SaveData('diagram.pvtu', proxy=threshold1)

# WARNING: due to a reported ParaView issue, when saving the output to disk in
# MPI mode, pvbatch will execute the pipeline twice in a row (instead of one).
