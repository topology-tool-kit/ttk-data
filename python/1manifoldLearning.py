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

# create a new 'CSV Reader'
pointCloudcsv = CSVReader(FileName=["pointCloud.csv"])

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(
    Input=pointCloudcsv, ModulePath="default"
)
tTKDimensionReduction1.InputColumns = ["Points:0", "Points:1", "Points:2"]
tTKDimensionReduction1.UseAllCores = 0

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints2.XColumn = "Component_0"
tableToPoints2.YColumn = "Component_1"
tableToPoints2.a2DPoints = 1

# create a new 'Gaussian Resampling'
gaussianResampling2 = GaussianResampling(Input=tableToPoints2)
gaussianResampling2.ResampleField = ["POINTS", "ignore arrays"]
gaussianResampling2.ResamplingGrid = [128, 64, 3]
gaussianResampling2.SplatAccumulationMode = "Sum"

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(Input=gaussianResampling2)
pythonCalculator1.Expression = 'numpy.round_(inputs[0].PointData["SplatterValues"], 6)'
pythonCalculator1.ArrayName = 'SplatterValues'

# create a new 'Slice'
slice1 = Slice(Input=pythonCalculator1)
slice1.SliceType = "Plane"

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
ThresholdBetween(threshold1, -0.1, 999999999)

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
ThresholdBetween(persistenceThreshold, 3.0, 999999999)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=slice1, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1, 1))
threshold2.Scalars = ["CELLS", "SeparatrixType"]
ThresholdBetween(threshold2, 1.0, 1.0)

# create a new 'Threshold'
threshold3 = Threshold(Input=threshold2)
threshold3.Scalars = ["CELLS", "NumberOfCriticalPointsOnBoundary"]

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold3)
tTKGeometrySmoother1.IterationNumber = 100

SaveData("OutputArc.vtu", tTKGeometrySmoother1)
