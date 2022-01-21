#!/usr/bin/env python
from paraview.simple import *

# paraview 5.9 VS 5.10 compatibility ===========================================
def ThresholdBetween(threshold, lower, upper):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [lower, upper]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Between"
        threshold.LowerThreshold = lower
        threshold.UpperThreshold = upper
# end of comphatibility ========================================================

# create a new 'PNG Series Reader'
tributepng = PNGSeriesReader(FileNames=['tribute.png'])

# create a new 'Calculator'
calculator1 = Calculator(Input=tributepng)
calculator1.ResultArrayName = 'originalData'
calculator1.Function = 'sqrt(PNGImage_X*PNGImage_X+PNGImage_Y*PNGImage_Y)'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'originalData']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
ThresholdBetween(threshold1, -0.1, 999999999)

# create a new 'Threshold'
minimumPairs = Threshold(Input=threshold1)
minimumPairs.Scalars = ['CELLS', 'PairType']
ThresholdBetween(minimumPairs, -1.0, 0.0)

# create a new 'Threshold'
maximumPairs = Threshold(Input=threshold1)
maximumPairs.Scalars = ['CELLS', 'PairType']
ThresholdBetween(maximumPairs, 1.0, 1.0)

# create a new 'Calculator'
calculator2 = Calculator(Input=maximumPairs)
calculator2.ResultArrayName = 'Birth'
calculator2.Function = 'coordsX'

# create a new 'Threshold'
birthThreshold = Threshold(Input=calculator2)
birthThreshold.Scalars = ['POINTS', 'Birth']
ThresholdBetween(birthThreshold, 257.390747070312, 297.0)

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[minimumPairs, birthThreshold])

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=appendDatasets1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
ThresholdBetween(persistenceThreshold, 8.5, 999999999)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=calculator1, Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'originalData']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex2.ScalarField = ['POINTS', 'originalData']

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer2 = TTKIdentifierRandomizer(Input=OutputPort(tTKMorseSmaleComplex2,3))
tTKIdentifierRandomizer2.ScalarField = ['POINTS', 'AscendingManifold']

# save the output
SaveData('tribute_segmentation.vti', tTKIdentifierRandomizer2)
