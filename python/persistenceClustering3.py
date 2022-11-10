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
clusteringcsv = CSVReader(FileName=["clustering3.csv"])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clusteringcsv)
tableToPoints1.XColumn = "X"
tableToPoints1.YColumn = "Y"
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
tTKPersistenceDiagram1.IgnoreBoundary = False

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
ThresholdBetween(threshold1, -0.1, 999999999)

# create a new 'Threshold'
persistenceThreshold0 = Threshold(Input=threshold1)
persistenceThreshold0.Scalars = ["CELLS", "Persistence"]
ThresholdBetween(persistenceThreshold0, 10.0, 999999999)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=slice1, Constraints=persistenceThreshold0
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(
    SourceDataArrays=OutputPort(tTKMorseSmaleComplex1, 3),
    DestinationMesh=tableToPoints1,
)

# save the output(s)
SaveData("OutputClustering.csv", resampleWithDataset1)
