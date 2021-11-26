from paraview.simple import *

# create a new 'XML Image Data Reader'
builtInExamplevti = XMLImageDataReader(FileName=['BuiltInExample2.vti'])

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=builtInExamplevti)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'log(Rho)']
tTKMorseSmaleComplex1.Ascending2Separatrices = 1
tTKMorseSmaleComplex1.Descending2Separatrices = 1

# Generate spheres for the critical points using 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=tTKMorseSmaleComplex1)
tTKIcospheresFromPoints1.Radius = 1.5

# Generate bigger spheres for the critical points using 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(Input=tTKMorseSmaleComplex1)
tTKIcospheresFromPoints2.Radius = 3.0

# Then select critical points of CellDimension 3 using 'Threshold' to select maxima
threshold3 = Threshold(Input=tTKIcospheresFromPoints2)
threshold3.Scalars = ['POINTS', 'CellDimension']
threshold3.ThresholdRange = [3.0, 3.0]

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1,1))
threshold1.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold1.ThresholdRange = [0.0, 0.0]

# create a new 'Threshold'
threshold2 = Threshold(Input=threshold1)
threshold2.Scalars = ['CELLS', 'SeparatrixType']
threshold2.ThresholdRange = [2.0, 2.0]

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 50

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKGeometrySmoother1)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Radius = 1.25

# create a new 'Threshold'
threshold8 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1,1))
threshold8.Scalars = ['CELLS', 'SeparatrixType']
threshold8.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold9 = Threshold(Input=threshold8)
threshold9.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold9.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold11 = Threshold(Input=threshold9)
threshold11.Scalars = ['CELLS', 'SeparatrixId']
threshold11.ThresholdRange = [75.0, 76.0]

# create a new 'Threshold'
threshold10 = Threshold(Input=threshold9)
threshold10.Scalars = ['CELLS', 'SeparatrixId']
threshold10.ThresholdRange = [73.0, 74.0]

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[threshold10, threshold11])

# create a new 'Clean to Grid'
cleantoGrid4 = CleantoGrid(Input=appendDatasets1)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother4 = TTKGeometrySmoother(Input=cleantoGrid4)
tTKGeometrySmoother4.IterationNumber = 10

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKGeometrySmoother4)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface3)
tube2.Scalars = ['POINTS', 'CellDimension']
tube2.Radius = 0.75

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1,2))
threshold4.Scalars = ['CELLS', 'SeparatrixType']
threshold4.ThresholdRange = [1.0, 1.0]

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(Input=threshold4)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=cleantoGrid2)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tetrahedralize1)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=extractSurface2)
tTKGeometrySmoother2.IterationNumber = 20

# select 2-separatrices using 'Threshold'
threshold5 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1,2))
threshold5.Scalars = ['CELLS', 'SeparatrixType']
threshold5.ThresholdRange = [2.0, 2.0]

# create a new 'Threshold'
threshold6 = Threshold(Input=threshold5)
threshold6.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold6.ThresholdRange = [4.0, 4.0]

# select a particular 2-separatrix using 'Threshold'
threshold7 = Threshold(Input=threshold6)
threshold7.Scalars = ['CELLS', 'SeparatrixId']
threshold7.ThresholdRange = [2.0, 2.0]

# create a new 'Clean to Grid'
cleantoGrid3 = CleantoGrid(Input=threshold7)

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=cleantoGrid3)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(Input=tetrahedralize2)
tTKGeometrySmoother3.IterationNumber = 20

# save the output
SaveData('CriticalPoints.vtp', tTKIcospheresFromPoints1)
SaveData('Maxima.vtu', threshold3)
SaveData('CovalentBonds.vtp', tube1)
SaveData('Selected2saddle1saddleConnectors.vtp', tube2)
SaveData('CovalentBondSeparatrixWalls.vtp', tTKGeometrySmoother2)
SaveData('SelectedType2SeparatrixWall.vtu', tTKGeometrySmoother3)
