#!/usr/bin/env python
from paraview.simple import *

# create a new 'PNG Series Reader'
tributepng = PNGSeriesReader(FileNames=['tribute.png'])

# create a new 'Calculator'
calculator1 = Calculator(Input=tributepng)
calculator1.ResultArrayName = 'originalData'
calculator1.Function = 'sqrt(PNGImage_X*PNGImage_X+PNGImage_Y*PNGImage_Y)'

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=calculator1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'originalData']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.LowerThreshold = -0.1
threshold1.UpperThreshold = 3560.0

# create a new 'Threshold'
minimumPairs = Threshold(Input=threshold1)
minimumPairs.Scalars = ['CELLS', 'PairType']
minimumPairs.LowerThreshold = -1.0

# create a new 'Threshold'
maximumPairs = Threshold(Input=threshold1)
maximumPairs.Scalars = ['CELLS', 'PairType']
maximumPairs.LowerThreshold = 1.0
maximumPairs.UpperThreshold = 1.0

# create a new 'Calculator'
calculator2 = Calculator(Input=maximumPairs)
calculator2.ResultArrayName = 'Birth'
calculator2.Function = 'coordsX'

# create a new 'Threshold'
birthThreshold = Threshold(Input=calculator2)
birthThreshold.Scalars = ['POINTS', 'Birth']
birthThreshold.LowerThreshold = 257.390747070312
birthThreshold.UpperThreshold = 297.0

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[minimumPairs, birthThreshold])

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=appendDatasets1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.LowerThreshold = 8.5
persistenceThreshold.UpperThreshold = 102.106426713382

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1, Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'originalData']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex2.ScalarField = ['POINTS', 'originalData']
tTKMorseSmaleComplex2.OffsetField = ['POINTS', 'OutputOffsetScalarField']

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer2 = TTKIdentifierRandomizer(Input=OutputPort(tTKMorseSmaleComplex2,3))
tTKIdentifierRandomizer2.ScalarField = ['POINTS', 'AscendingManifold']

# save the output
SaveData('tribute_segmentation.vtu', tTKIdentifierRandomizer2)
