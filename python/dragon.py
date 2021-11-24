#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
dragonvtu = XMLUnstructuredGridReader(FileName=['dragon.vtu'])

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=dragonvtu)

# create a new 'Calculator'
elevation = Calculator(Input=tTKGeometrySmoother1)
elevation.ResultArrayName = 'Elevation'
elevation.Function = 'coordsY'

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=elevation)
tTKPersistenceCurve1.ScalarField = ['POINTS', 'Elevation']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=elevation)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Elevation']

# create a new 'Threshold'
diagonal = Threshold(Input=tTKPersistenceDiagram1)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=diagonal)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CriticalType']

# create a new 'Threshold'
pairs = Threshold(Input=tTKPersistenceDiagram1)
pairs.Scalars = ['CELLS', 'PairIdentifier']
pairs.ThresholdRange = [0.0, 1000.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=pairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [5.0, 1000.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=elevation,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'Elevation']

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = ['POINTS', 'Elevation']

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(Input=tTKScalarFieldCriticalPoints1)
tTKIcospheresFromPoints2.Radius = 1.5

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKTopologicalSimplification1)

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface3)

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKContourTree1 = TTKMergeandContourTreeFTM(Input=tTKTopologicalSimplification1)
tTKContourTree1.ScalarField = ['POINTS', 'Elevation']
tTKContourTree1.ArcSampling = 30

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CriticalType']
tube2.Radius = 0.893286056518555

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=persistenceThreshold)
tTKIcospheresFromPoints1.Radius = 1.5

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=OutputPort(tTKContourTree1,1))
tTKGeometrySmoother2.IterationNumber = 40

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'RegularMask']
tube4.NumberofSides = 12
tube4.Radius = 0.75

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints4 = TTKIcospheresFromPoints(Input=tTKContourTree1)
tTKIcospheresFromPoints4.Radius = 2.0

# save the output
SaveData('PersistenceDiagram.vtu', tTKPersistenceDiagram1)
SaveData('PersistenceCurve.csv', OutputPort(tTKPersistenceCurve1, 3))
SaveData('CriticalPoints.vtp', tTKScalarFieldCriticalPoints1)
SaveData('ContourTreeNodes.vtp', tTKIcospheresFromPoints4)
SaveData('ContourTreeArcs.vtp', tube4)
