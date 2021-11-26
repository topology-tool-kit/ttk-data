from paraview.simple import *

# create a new 'CSV Reader'
clusteringcsv = CSVReader(FileName=['clustering4.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clusteringcsv)
tableToPoints1.XColumn = 'X'
tableToPoints1.YColumn = 'Y'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling1.ResamplingGrid = [256, 256, 3]
gaussianResampling1.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice1 = Slice(Input=gaussianResampling1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.0187499550000001, 0.0313220950000002, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'SplatterValues']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold0 = Threshold(Input=threshold1)
persistenceThreshold0.Scalars = ['CELLS', 'Persistence']
persistenceThreshold0.ThresholdRange = [10.0, 9999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=slice1,
    Constraints=persistenceThreshold0)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'SplatterValues']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'SplatterValues']

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(SourceDataArrays=OutputPort(tTKMorseSmaleComplex1,3),
    DestinationMesh=tableToPoints1)
resampleWithDataset1.CellLocator = 'Static Cell Locator'

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1,1))
threshold2.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'Threshold'
threshold12 = Threshold(Input=tTKPersistenceDiagram1)
threshold12.Scalars = ['CELLS', 'PairIdentifier']
threshold12.ThresholdRange = [-1.0, -0.1]

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 10
#tTKGeometrySmoother1.InputMaskField = [None, '']

# save the output(s)
SaveData('data4Resampled.csv', resampleWithDataset1)
