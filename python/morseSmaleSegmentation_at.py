#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
atvti = XMLImageDataReader(FileName=["at.vti"])

# create a new 'Calculator'
calculator1 = Calculator(registrationName="Calculator1", Input=atvti)
calculator1.ResultArrayName = "negdensity"
calculator1.Function = "-density"

# create a new 'TTK PathCompression'
tTKPathCompression1 = TTKPathCompression(
    registrationName="TTKPathCompression1", Input=calculator1
)
tTKPathCompression1.ScalarField = ["POINTS", "negdensity"]

# create a new 'TTK MarchingTetrahedra'
tTKMarchingTetrahedra1 = TTKMarchingTetrahedra(
    registrationName="TTKMarchingTetrahedra1", Input=tTKPathCompression1
)
tTKMarchingTetrahedra1.ScalarField = ["POINTS", "negdensity_DescendingManifold"]

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(
    registrationName="CleantoGrid1", Input=tTKMarchingTetrahedra1
)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(
    registrationName="TTKGeometrySmoother1", Input=cleantoGrid1
)
tTKGeometrySmoother1.IterationNumber = 20

# create a new 'TTK MarchingTetrahedra'
tTKMarchingTetrahedra2 = TTKMarchingTetrahedra(
    registrationName="TTKMarchingTetrahedra2", Input=tTKPathCompression1
)
tTKMarchingTetrahedra2.ScalarField = ["POINTS", "negdensity_AscendingManifold"]

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(
    registrationName="CleantoGrid2", Input=tTKMarchingTetrahedra2
)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(
    registrationName="TTKGeometrySmoother2", Input=cleantoGrid2
)
tTKGeometrySmoother2.IterationNumber = 20

SaveData("descendingSeparatorAt.vtu", tTKGeometrySmoother1)
SaveData("ascendingSeparatorAt.vtu", tTKGeometrySmoother2)
