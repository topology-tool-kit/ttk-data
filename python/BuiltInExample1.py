#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
builtInExamplevti = XMLImageDataReader(FileName=['BuiltInExample1.vti'])
builtInExamplevti.PointArrayStatus = ['Vectors_']

# create a new 'Transform'
transform1 = Transform(Input=builtInExamplevti)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Rotate = [0.0, 0.0, -90.0]

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=transform1)
computeDerivatives1.Scalars = [None, '']
computeDerivatives1.Vectors = ['POINTS', 'Vectors_']
computeDerivatives1.OutputVectorType = 'Vorticity'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=computeDerivatives1)

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData1)
calculator1.ResultArrayName = 'myVorticity'
calculator1.Function = 'Vorticity_Z'

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
tTKScalarFieldNormalizer1.ScalarField = ['POINTS', 'myVorticity']

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=tTKScalarFieldNormalizer1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'myVorticity']
tTKPersistenceDiagram1.InputOffsetField = [None, '']

# create a new 'Threshold'
diagonal = Threshold(Input=tTKPersistenceDiagram1)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=diagonal)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CriticalType']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'Threshold'
persistencePairs = Threshold(Input=tTKPersistenceDiagram1)
persistencePairs.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs.ThresholdRange = [-0.1, 957.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=persistencePairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.02, 1.0]

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=persistenceThreshold)
tTKIcospheresFromPoints1.Radius = 0.025

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CriticalType']
tube2.Vectors = [None, '']
tube2.Radius = 0.015

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=tetrahedralize1)
tTKPersistenceCurve1.ScalarField = ['POINTS', 'myVorticity']
tTKPersistenceCurve1.InputOffsetField = ['POINTS', '']

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKIcospheresFromPoints1)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'myVorticity']
tTKTopologicalSimplification1.InputOffsetField = [None, '']
tTKTopologicalSimplification1.VertexIdentifierField = [None, '']

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=tTKTopologicalSimplification1)
warpByScalar1.Scalars = ['POINTS', 'myVorticity']
warpByScalar1.ScaleFactor = 300.0
warpByScalar1.UseNormal = 1

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=warpByScalar1)
tTKScalarFieldCriticalPoints1.ScalarField = ['POINTS', 'myVorticity']
tTKScalarFieldCriticalPoints1.InputOffsetField = ['POINTS', 'OutputOffsetScalarField']

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(Input=tTKScalarFieldCriticalPoints1)
tTKIcospheresFromPoints2.Radius = 5.0

# create a new 'Threshold'
minima = Threshold(Input=tTKIcospheresFromPoints2)
minima.Scalars = ['POINTS', 'CriticalType']
minima.ThresholdRange = [0.0, 0.1]

# create a new 'Threshold'
maxima = Threshold(Input=tTKIcospheresFromPoints2)
maxima.Scalars = ['POINTS', 'CriticalType']
maxima.ThresholdRange = [3.0, 3.0]

# save the output
SaveData('minima.vtu', minima)
SaveData('maxmima.vtu', maxima)
SaveData('warpedInput.vtu', warpByScalar1)
SaveData('PersistenceDiagram.vtu', tTKPersistenceDiagram1)
SaveData('PersistenceCurve.csv', OutputPort(tTKPersistenceCurve1, 3))
