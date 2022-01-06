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
karhunenLoveDigits64Dimensionscsv = CSVReader(
    FileName=["karhunenLoveDigits64Dimensions.csv"]
)
karhunenLoveDigits64Dimensionscsv.HaveHeaders = 0

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(Input=karhunenLoveDigits64Dimensionscsv)
tTKDimensionReduction1.InputColumns = [
    "Field 1",
    "Field 10",
    "Field 11",
    "Field 12",
    "Field 13",
    "Field 14",
    "Field 15",
    "Field 16",
    "Field 17",
    "Field 18",
    "Field 19",
    "Field 2",
    "Field 20",
    "Field 21",
    "Field 22",
    "Field 23",
    "Field 24",
    "Field 25",
    "Field 26",
    "Field 27",
    "Field 28",
    "Field 29",
    "Field 3",
    "Field 30",
    "Field 31",
    "Field 32",
    "Field 33",
    "Field 34",
    "Field 35",
    "Field 36",
    "Field 37",
    "Field 38",
    "Field 39",
    "Field 4",
    "Field 40",
    "Field 41",
    "Field 42",
    "Field 43",
    "Field 44",
    "Field 45",
    "Field 46",
    "Field 47",
    "Field 48",
    "Field 49",
    "Field 5",
    "Field 50",
    "Field 51",
    "Field 52",
    "Field 53",
    "Field 54",
    "Field 55",
    "Field 56",
    "Field 57",
    "Field 58",
    "Field 59",
    "Field 6",
    "Field 60",
    "Field 61",
    "Field 62",
    "Field 63",
    "Field 64",
    "Field 7",
    "Field 8",
    "Field 9",
]
tTKDimensionReduction1.Method = "t-distributed Stochastic Neighbor Embedding"

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints1.XColumn = "Component_0"
tableToPoints1.YColumn = "Component_1"
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ["POINTS", "ignore arrays"]
gaussianResampling1.ResamplingGrid = [256, 256, 3]
gaussianResampling1.SplatAccumulationMode = "Sum"

# create a new 'Slice'
slice1 = Slice(Input=gaussianResampling1)
slice1.SliceType = "Plane"

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "Persistence"]
ThresholdBetween(threshold1, 10.0, 999999999)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=slice1, Constraints=threshold1
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(
    Input=OutputPort(tTKMorseSmaleComplex1, 3)
)
tTKIdentifierRandomizer1.ScalarField = ["POINTS", "AscendingManifold"]

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(
    SourceDataArrays=tTKIdentifierRandomizer1, DestinationMesh=tableToPoints1
)
resampleWithDataset1.PassPointArrays = 1

SaveData("OutputClustering.csv", resampleWithDataset1)
