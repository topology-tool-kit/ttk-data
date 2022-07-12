#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
skullvtu = XMLUnstructuredGridReader(FileName=["skull.vtu"])
skullvtu.PointArrayStatus = ["Morse field"]
skullvtu.TimeArray = "None"

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=skullvtu)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=extractSurface1)

# create a new 'TTK EigenField'
tTKEigenField1 = TTKEigenField(InputGeometry=tetrahedralize1)
tTKEigenField1.Numberofeigenfunctions = 50
tTKEigenField1.Computestatistics = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKEigenField1)
calculator1.Function = '"OutputEigenFunctions_22"'

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=calculator1)
tTKPersistentGenerators1.ScalarField = ["POINTS", "Result"]
tTKPersistentGenerators1.InputOffsetField = ["POINTS", "Result"]
tTKPersistentGenerators1.PruneHandlesGenerators = 1

SaveData("PersistentGeneratorsSkull.vtp", tTKPersistentGenerators1)
