#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
dragonvtu = XMLUnstructuredGridReader(registrationName='dragon.vtu', FileName=['dragon.vtu'])

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=dragonvtu)
tTKGeometrySmoother1.InputMaskField = [None, '']

# create a new 'Calculator'
elevation = Calculator(registrationName='Elevation', Input=tTKGeometrySmoother1)
elevation.ResultArrayName = 'Elevation'
elevation.Function = 'coordsY'

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(registrationName='TTKPersistenceCurve1', Input=elevation)
tTKPersistenceCurve1.ScalarField = ['POINTS', 'Elevation']
tTKPersistenceCurve1.InputOffsetField = ['POINTS', '']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=elevation)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Elevation']
tTKPersistenceDiagram1.InputOffsetField = [None, '']

# create a new 'Threshold'
diagonal = Threshold(registrationName='Diagonal', Input=tTKPersistenceDiagram1)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=diagonal)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CriticalType']
tube1.Vectors = [None, '']

# create a new 'Threshold'
pairs = Threshold(registrationName='Pairs', Input=tTKPersistenceDiagram1)
pairs.Scalars = ['CELLS', 'PairIdentifier']
pairs.ThresholdRange = [0.0, 1000.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(registrationName='PersistenceThreshold', Input=pairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [5.0, 1000.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(registrationName='TTKTopologicalSimplification1', Domain=elevation,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'Elevation']
tTKTopologicalSimplification1.InputOffsetField = [None, '']
tTKTopologicalSimplification1.VertexIdentifierField = [None, '']

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(registrationName='TTKScalarFieldCriticalPoints1', Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = ['POINTS', 'Elevation']
tTKScalarFieldCriticalPoints1.InputOffsetField = ['POINTS', 'OutputOffsetScalarField']
tTKScalarFieldCriticalPoints1.Withvertexidentifiers = 0
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints2', Input=tTKScalarFieldCriticalPoints1)
tTKIcospheresFromPoints2.Radius = 1.5

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(registrationName='CleantoGrid1', Input=tTKTopologicalSimplification1)

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(registrationName='ExtractSurface3', Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=extractSurface3)

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKContourTree1 = TTKMergeandContourTreeFTM(registrationName='TTKContourTree1', Input=tTKTopologicalSimplification1)
tTKContourTree1.ScalarField = ['POINTS', 'Elevation']
tTKContourTree1.InputOffsetField = ['POINTS', 'OutputOffsetScalarField']
tTKContourTree1.ArcSampling = 30

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(registrationName='ExtractSurface2', Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(registrationName='Tube2', Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CriticalType']
tube2.Vectors = [None, '']
tube2.Radius = 0.893286056518555

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=persistenceThreshold)
tTKIcospheresFromPoints1.Radius = 1.5

# find source
tTKContourTree1_1 = FindSource('TTKContourTree1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother2', Input=OutputPort(tTKContourTree1_1,1))
tTKGeometrySmoother2.IterationNumber = 40
tTKGeometrySmoother2.InputMaskField = [None, '']

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(registrationName='ExtractSurface4', Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube4 = Tube(registrationName='Tube4', Input=extractSurface4)
tube4.Scalars = ['POINTS', 'RegularMask']
tube4.Vectors = [None, '']
tube4.NumberofSides = 12
tube4.Radius = 0.75

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints4 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints4', Input=tTKContourTree1)
tTKIcospheresFromPoints4.Radius = 2.0

# save the output
SaveData('PersistenceDiagram.vtu', tTKPersistenceDiagram1)
SaveData('PersistenceCurve.csv', OutputPort(tTKPersistenceCurve1, 3))
SaveData('CriticalPoints.vtp', tTKScalarFieldCriticalPoints1)
SaveData('ContourTreeNodes.vtp', tTKIcospheresFromPoints4)
SaveData('ContourTreeArcs.vtp', tube4)
