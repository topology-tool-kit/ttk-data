#!/usr/bin/env python
from paraview.simple import *

# create a new 'PNG Series Reader'
tributepng = PNGSeriesReader(FileNames=["tribute.png"])

# create a new 'Calculator'
calculator1 = Calculator(Input=tributepng)
calculator1.ResultArrayName = "originalData"
calculator1.Function = "-sqrt(PNGImage_X*PNGImage_X+PNGImage_Y*PNGImage_Y)"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "originalData"]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = -0.1
threshold1.UpperThreshold = 999999999

# create a new 'Threshold'
minimumPairs = Threshold(Input=threshold1)
minimumPairs.Scalars = ["CELLS", "PairType"]
minimumPairs.ThresholdMethod = "Between"
minimumPairs.LowerThreshold = -1.0
minimumPairs.UpperThreshold = 0.0

# create a new 'Calculator'
calculator6 = Calculator(Input=minimumPairs)
calculator6.AttributeType = "Cell Data"
calculator6.ResultArrayName = "Death"
calculator6.Function = "Birth+Persistence"

# create a new 'Threshold'
deathThreshold = Threshold(Input=calculator6)
deathThreshold.Scalars = ["CELLS", "Death"]
deathThreshold.LowerThreshold = -297.0
deathThreshold.UpperThreshold = -257.391

# create a new 'Threshold'
maximumPairs = Threshold(Input=threshold1)
maximumPairs.Scalars = ["POINTS", "CriticalType"]
maximumPairs.LowerThreshold = 3.0
maximumPairs.UpperThreshold = 3.0
maximumPairs.AllScalars = 0

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[deathThreshold, maximumPairs])

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=appendDatasets1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdMethod = "Between"
persistenceThreshold.LowerThreshold = 8.5
persistenceThreshold.UpperThreshold = 999999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=calculator1, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "originalData"]

# create a new 'Calculator'
calculator7 = Calculator(Input=tTKTopologicalSimplification1)
calculator7.ResultArrayName = "originalData"
calculator7.Function = "-originalData"

# create a new 'Calculator'
calculator8 = Calculator(Input=calculator7)
calculator8.ResultArrayName = "originalData_Order"
calculator8.Function = "-originalData_Order"

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=calculator8)
tTKMorseSmaleComplex2.ScalarField = ["POINTS", "originalData_Order"]

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer2 = TTKIdentifierRandomizer(
    Input=OutputPort(tTKMorseSmaleComplex2, 3)
)
tTKIdentifierRandomizer2.ScalarField = ["POINTS", "AscendingManifold"]

# save the output
SaveData("tribute_segmentation.vti", tTKIdentifierRandomizer2)
