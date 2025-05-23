#!/usr/bin/env python

from paraview.simple import *

twistedEllipsecsv = CSVReader(FileName=["twistedEllipse.csv"])
tTKDimensionReduction1 = TTKDimensionReduction(Input=twistedEllipsecsv)
tTKDimensionReduction1.InputColumns = ["x", "y", "z"]
tTKDimensionReduction1.Method = "Autoencoder"
tTKDimensionReduction1.Lossfunction = "Asymmetric Cascade Autoencoder"
tTKDimensionReduction1.Numberofepochs = 1000
tTKDimensionReduction1.Hiddenlayers = "32 32"
tTKDimensionReduction1.Enforcedeterminism = 1
tTKDimensionReduction1.Randomseed = 5
SaveData("twistedEllipse_topoAE++.csv", tTKDimensionReduction1)

k4csv = CSVReader(FileName=["K4.csv"])
tTKDimensionReduction2 = TTKDimensionReduction(Input=k4csv)
tTKDimensionReduction2.InputColumns = ["x", "y", "z"]
tTKDimensionReduction2.Method = "Autoencoder"
tTKDimensionReduction2.Lossfunction = "Asymmetric Cascade Autoencoder"
tTKDimensionReduction1.Numberofepochs = 1000
tTKDimensionReduction2.Hiddenlayers = "128 32"
tTKDimensionReduction2.Enforcedeterminism = 1
tTKDimensionReduction2.Randomseed = 100
SaveData("K4_topoAE++.csv", tTKDimensionReduction2)

coil20csv = CSVReader(FileName=["coil20.csv"])
thresholdTable = ThresholdTable(Input=coil20csv)
thresholdTable.Column = ["ROWS", "1025"]
thresholdTable.MinValue = 1.0
thresholdTable.MaxValue = 1.0
tTKDimensionReduction3 = TTKDimensionReduction(Input=thresholdTable)
tTKDimensionReduction3.InputColumns = sorted([str(x) for x in range(1, 1025)])
tTKDimensionReduction3.Method = "Autoencoder"
tTKDimensionReduction3.Lossfunction = "Asymmetric Cascade Autoencoder"
tTKDimensionReduction3.Numberofepochs = 1000
tTKDimensionReduction3.Hiddenlayers = "128 32"
tTKDimensionReduction3.Enforcedeterminism = 1
tTKDimensionReduction3.Randomseed = 0
SaveData("coil20-1_topoAE++.csv", tTKDimensionReduction3)
