import paraview

#### import the simple module from the paraview
from paraview.simple import *

if len(sys.argv) == 2:
        dim = int(sys.argv[1])
else:
        dim = 128

# create a new 'XML Image Data Reader'
backpack = XMLImageDataReader(registrationName='backpack.vti', FileName=['backpack.vti'])

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=backpack)
resampleToImage1.SamplingDimensions = [dim, dim, dim]
resampleToImage1.SamplingBounds = [0.0, 511.0, 0.0, 511.0, 0.0, 372.0]

tTKArrayPreconditioning = TTKArrayPreconditioning(registrationName='TTKArrayPreconditioning5', Input=resampleToImage1)
tTKArrayPreconditioning.PointDataArrays = ['ImageFile']
tTKArrayPreconditioning.GlobalOrderArray = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=tTKArrayPreconditioning)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'ImageFile']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'ImageFile']
tTKPersistenceDiagram1.Backend = 'Distributed Discrete Morse Sandwich'

SaveData('diagram.pvtu', proxy=tTKPersistenceDiagram1)