#!/usr/bin/env python

from paraview.simple import *

a3blobscsv = CSVReader(FileName=["3blobs.csv"])
tTKDimensionReduction1 = TTKDimensionReduction(Input=a3blobscsv)
tTKDimensionReduction1.InputColumns = ["x", "y", "z"]
tTKDimensionReduction1.Method = "TopoMap (IEEE VIS 2020)"
SaveData("3blobs_topoMap.csv", tTKDimensionReduction1)

a3ringscsv = CSVReader(FileName=["3rings.csv"])
tTKDimensionReduction2 = TTKDimensionReduction(Input=a3ringscsv)
tTKDimensionReduction2.InputColumns = ["x", "y", "z"]
tTKDimensionReduction2.Method = "TopoMap (IEEE VIS 2020)"
SaveData("3rings_topoMap.csv", tTKDimensionReduction2)

a2cavitiescsv = CSVReader(FileName=["2cavities.csv"])
tTKDimensionReduction3 = TTKDimensionReduction(Input=a2cavitiescsv)
tTKDimensionReduction3.InputColumns = ["X", "Y", "Z"]
tTKDimensionReduction3.Method = "TopoMap (IEEE VIS 2020)"
SaveData("2cavities_topoMap.csv", tTKDimensionReduction3)
