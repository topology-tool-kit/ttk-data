#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
dragonvtu = XMLUnstructuredGridReader(FileName=["dragon.vtu"])

# create a new 'Elevation'
elevation1 = Calculator(Input=dragonvtu)
elevation1.ResultArrayName = "Elevation"
elevation1.Function = "coordsY"

# create a new 'TTK TriangulationManager'
tTKTriangulationManager1 = TTKTriangulationManager(Input=elevation1)
tTKTriangulationManager1.DataArrays = ["Elevation"]

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(
    Input=tTKTriangulationManager1
)
tTKScalarFieldCriticalPoints1.ScalarField = ["POINTS", "Elevation"]

# save the output
SaveData("CompactTriangulation.vtu", tTKTriangulationManager1)
SaveData("CriticalPoints.vtp", tTKScalarFieldCriticalPoints1)
