#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
dragonvtu = XMLUnstructuredGridReader(FileName=["dragon.vtu"])

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=dragonvtu)

# create a new 'Calculator'
elevation = Calculator(Input=tTKGeometrySmoother1)
elevation.ResultArrayName = "Elevation"
elevation.Function = "coordsY"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=elevation)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "Elevation"]
tTKPersistenceDiagram1.IgnoreBoundary = True

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=tTKPersistenceDiagram1)

# create a new 'Threshold'
pairs = Threshold(Input=tTKPersistenceDiagram1)
pairs.Scalars = ["CELLS", "PairIdentifier"]
pairs.ThresholdMethod = "Between"
pairs.LowerThreshold = 0.0
pairs.UpperThreshold = 999999999

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=pairs)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdMethod = "Between"
persistenceThreshold.LowerThreshold = 5.0
persistenceThreshold.UpperThreshold = 999999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=elevation, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "Elevation"]

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(
    Input=tTKTopologicalSimplification1
)
tTKScalarFieldCriticalPoints1.ScalarField = ["POINTS", "Elevation"]

# create a new 'TTK Merge and Contour Tree ()'
tTKContourTree1 = TTKContourTree(Input=tTKTopologicalSimplification1)
tTKContourTree1.ScalarField = ["POINTS", "Elevation"]
tTKContourTree1.ArcSampling = 30

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=OutputPort(tTKContourTree1, 1))
tTKGeometrySmoother2.IterationNumber = 40

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.NumberofSides = 12
tube4.Radius = 0.75

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints4 = TTKIcospheresFromPoints(Input=tTKContourTree1)
tTKIcospheresFromPoints4.Radius = 2.0

# save the output
SaveData("PersistenceDiagram.vtu", tTKPersistenceDiagram1)
SaveData("PersistenceCurve.csv", OutputPort(tTKPersistenceCurve1, 3))
SaveData("CriticalPoints.vtp", tTKScalarFieldCriticalPoints1)
SaveData("ContourTreeNodes.vtp", tTKIcospheresFromPoints4)
SaveData("ContourTreeArcs.vtp", tube4)
