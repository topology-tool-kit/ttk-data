#!/usr/bin/env python

from paraview.simple import *

if len(sys.argv) == 2:
        dim = int(sys.argv[1])
else:
        dim = 128

# create a new 'XML Image Data Reader'
backpack = XMLImageDataReader(FileName=['backpack.vti'])

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=backpack)
resampleToImage1.SamplingDimensions = [dim, dim, dim]
resampleToImage1.SamplingBounds = [0.0, 511.0, 0.0, 511.0, 0.0, 372.0]

tTKArrayPreconditioning = TTKArrayPreconditioning(Input=resampleToImage1)
tTKArrayPreconditioning.PointDataArrays = ['ImageFile']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKArrayPreconditioning)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'ImageFile']
tTKPersistenceDiagram1.Backend = 'Distributed Discrete Morse Sandwich'

SaveData('diagram.pvtu', proxy=tTKPersistenceDiagram1)
