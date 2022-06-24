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

# create a new 'XML Image Data Reader'
uncertainStartingVortexvti = XMLImageDataReader(
    FileName=["uncertainStartingVortex.vti"]
)

# create a new 'TTK MandatoryCriticalPoints'
tTKMandatoryCriticalPoints1 = TTKMandatoryCriticalPoints(
    Input=uncertainStartingVortexvti
)
tTKMandatoryCriticalPoints1.LowerBoundField = ["POINTS", "lowerBoundField"]
tTKMandatoryCriticalPoints1.UpperBoundField = ["POINTS", "upperBoundField"]
tTKMandatoryCriticalPoints1.NormalizedThreshold = 0.02

# create a new 'Threshold' for the Minimas
threshold6 = Threshold(Input=tTKMandatoryCriticalPoints1)
threshold6.Scalars = ["POINTS", "MinimumComponents"]
ThresholdBetween(threshold6, 0.0, 2.0)

# create a new 'Threshold' for the maximas
threshold5 = Threshold(Input=OutputPort(tTKMandatoryCriticalPoints1, 3))
threshold5.Scalars = ["POINTS", "MaximumComponents"]
ThresholdBetween(threshold5, 0.0, 8.0)

# create a new 'Random Attributes'
randomAttributes1 = RandomAttributes(Input=uncertainStartingVortexvti)
randomAttributes1.DataType = "Double"
randomAttributes1.ComponentRange = [0.0, 0.999]
randomAttributes1.GeneratePointScalars = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=randomAttributes1)
calculator1.ResultArrayName = "realization0"
calculator1.Function = (
    "lowerBoundField+(upperBoundField-lowerBoundField)*RandomPointScalars"
)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "realization0"]
tTKPersistenceDiagram1.Backend = "FTM (IEEE TPSD 2019)"

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ["CELLS", "PairIdentifier"]
ThresholdBetween(threshold2, 0.0, 185374.0)

# create a new 'Threshold'
persistenceThreshold1 = Threshold(Input=threshold2)
persistenceThreshold1.Scalars = ["CELLS", "Persistence"]
ThresholdBetween(persistenceThreshold1, 0.05, 1.75475390406744)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=calculator1, Constraints=persistenceThreshold1
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "realization0"]

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(
    Input=tTKTopologicalSimplification1
)
tTKScalarFieldCriticalPoints1.ScalarField = ["POINTS", "realization0"]

SaveData("PersistenceDiagram.vtu", tTKPersistenceDiagram1)
SaveData("CriticalPoints.vtp", tTKScalarFieldCriticalPoints1)
SaveData("MandatoryCriticalMinima.csv", OutputPort(tTKMandatoryCriticalPoints1, 0))
SaveData("MandatoryCriticalMaxima.csv", OutputPort(tTKMandatoryCriticalPoints1, 3))
