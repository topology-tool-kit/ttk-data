#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="periodicPicture.cdb")

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKCinemaProductReader1)
calculator1.Function = "PNGImage_X"

# create a new 'TTK DataSetToTable'
tTKDataSetToTable1 = TTKDataSetToTable(Input=calculator1)
tTKDataSetToTable1.DataAssociation = "Point"

# create a new 'Transpose Table'
transposeTable1 = TransposeTable(Input=tTKDataSetToTable1)
transposeTable1.VariablesofInterest = ["Result"]

# create a new 'TTK MergeBlockTables'
tTKMergeBlockTables1 = TTKMergeBlockTables(Input=transposeTable1)

# create a new 'TTK TableDistanceMatrix'
tTKTableDistanceMatrix1 = TTKTableDistanceMatrix(Input=tTKMergeBlockTables1)
tTKTableDistanceMatrix1.SelectFieldswithaRegexp = 1
tTKTableDistanceMatrix1.Regexp = "[01].*"

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(
    Input=tTKTableDistanceMatrix1, ModulePath="default"
)
tTKDimensionReduction1.SelectFieldswithaRegexp = 1
tTKDimensionReduction1.Regexp = "Dist.*"
tTKDimensionReduction1.Components = 3
tTKDimensionReduction1.InputIsaDistanceMatrix = 1
tTKDimensionReduction1.UseAllCores = 0

# create a new 'TTK RipsComplex'
tTKRipsComplex1 = TTKRipsComplex(Input=tTKDimensionReduction1)
tTKRipsComplex1.SelectFieldswithaRegexp = 1
tTKRipsComplex1.Regexp = "Dist.*"
tTKRipsComplex1.Diameterepsilon = 1500.0

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=tTKRipsComplex1)
cellDatatoPointData1.CellDataArraytoprocess = ["Diameter"]

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=cellDatatoPointData1)
tTKPersistentGenerators1.ScalarField = ["POINTS", "Diameter"]

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints1.XColumn = "Component_0"
tableToPoints1.YColumn = "Component_1"
tableToPoints1.ZColumn = "Component_2"
tableToPoints1.KeepAllDataArrays = 1

SaveData("PersistentGeneratorsPeriodicPicture_cycle.vtp", tTKPersistentGenerators1)
SaveData("PersistentGeneratorsPeriodicPicture_points.vtp", tableToPoints1)
SaveData("PersistentGeneratorsPeriodicPicture_ripsComplex.vtu", tTKRipsComplex1)
