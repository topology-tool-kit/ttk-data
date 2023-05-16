#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
atvti = XMLImageDataReader(FileName=["at.vti"])
atvti.PointArrayStatus = ["density"]
atvti.TimeArray = "None"

# create a new 'Calculator'
calculator1 = Calculator(registrationName="Calculator1", Input=atvti)
calculator1.ResultArrayName = "negdensity"
calculator1.Function = "-density"

# create a new 'TTK PathCompression'
tTKPathCompression1 = TTKPathCompression(
    registrationName="TTKPathCompression1", Input=calculator1
)
tTKPathCompression1.ScalarField = ["POINTS", "negdensity"]
tTKPathCompression1.OffsetField = ["POINTS", "negdensity"]
tTKPathCompression1.AscendingSegmentation = 0
tTKPathCompression1.DescendingSegmentation = 0

# create a new 'TTK MarchingTetrahedra'
tTKMarchingTetrahedra1 = TTKMarchingTetrahedra(
    registrationName="TTKMarchingTetrahedra1", Input=tTKPathCompression1
)
tTKMarchingTetrahedra1.ScalarField = ["POINTS", "DescendingSegmentation"]

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(
    registrationName="CleantoGrid1", Input=tTKMarchingTetrahedra1
)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(
    registrationName="TTKGeometrySmoother1", Input=cleantoGrid1
)
tTKGeometrySmoother1.IterationNumber = 20
tTKGeometrySmoother1.InputMaskField = ["CELLS", "MSCIds"]

# create a new 'TTK MarchingTetrahedra'
tTKMarchingTetrahedra2 = TTKMarchingTetrahedra(
    registrationName="TTKMarchingTetrahedra2", Input=tTKPathCompression1
)
tTKMarchingTetrahedra2.ScalarField = ["POINTS", "AscendingSegmentation"]

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(
    registrationName="CleantoGrid2", Input=tTKMarchingTetrahedra2
)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(
    registrationName="TTKGeometrySmoother2", Input=cleantoGrid2
)
tTKGeometrySmoother2.IterationNumber = 20
tTKGeometrySmoother2.InputMaskField = ["CELLS", "MSCIds"]


SaveData("descendingSegmentationAt.vtu", tTKGeometrySmoother1)
SaveData("ascendingSegmentationAt.vtu", tTKGeometrySmoother2)

if __name__ == "__main__":
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory="extracts")
