#!/usr/bin/env python
#### import the simple module from the paraview
from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
changesvtu = XMLUnstructuredGridReader(registrationName='changes.vtu', FileName=['changes.vtu'])
changesvtu.PointArrayStatus = ['VectorField']
changesvtu.TimeArray = 'None'

# create a new 'Random Vectors'
randomVectors1 = RandomVectors(registrationName='RandomVectors1', Input=changesvtu)
randomVectors1.MaximumSpeed = 0.3

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=randomVectors1)
calculator1.ResultArrayName = 'VectorsWithNoise'
calculator1.Function = 'VectorField+BrownianVectors'

# create a new 'TTK VectorWeightCurve'
tTKVectorWeightCurve1 = TTKVectorWeightCurve(registrationName='TTKVectorWeightCurve1', Input=calculator1)
tTKVectorWeightCurve1.InputArray = ['POINTS', 'VectorsWithNoise']

# create a new 'TTK TopologicalSkeleton'
tTKTopologicalSkeleton1 = TTKTopologicalSkeleton(registrationName='TTKTopologicalSkeleton1', Input=calculator1)
tTKTopologicalSkeleton1.VectorField = ['POINTS', 'VectorsWithNoise']
tTKTopologicalSkeleton1.RunSimplification = 1
tTKTopologicalSkeleton1.SimplificationThreshold = 27.0

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=tTKTopologicalSkeleton1)
tTKIcospheresFromPoints1.Radius = 6.5

# save the output
SaveData("WeightCurve.csv", tTKVectorWeightCurve1)
SaveData("CriticalPoints.csv", OutputPort(tTKTopologicalSkeleton1, 0))
SaveData("Separatrices1.csv", OutputPort(tTKTopologicalSkeleton1, 1))
SaveData("Segmentation.vtu", OutputPort(tTKTopologicalSkeleton1, 3))
