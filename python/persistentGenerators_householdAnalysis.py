#!/usr/bin/env python

from paraview.simple import *

# create a new 'CSV Reader'
household_part1_ID_dailycsv = CSVReader(FileName=['household_part1_ID_daily.csv'])
household_part1_ID_dailycsv.HaveHeaders = 0

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(Input=household_part1_ID_dailycsv,
    ModulePath='default')
tTKDimensionReduction1.InputColumns = ['Field 2', 'Field 3', 'Field 4', 'Field 5', 'Field 6', 'Field 7', 'Field 8']
tTKDimensionReduction1.Method = 'Principal Component Analysis'
tTKDimensionReduction1.Components = 3

# create a new 'TTK TableDistanceMatrix'
tTKTableDistanceMatrix1 = TTKTableDistanceMatrix(Input=tTKDimensionReduction1)
tTKTableDistanceMatrix1.InputColumns = ['Field 2', 'Field 3', 'Field 4', 'Field 5', 'Field 6', 'Field 7', 'Field 8']

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints1.XColumn = 'Component_0'
tableToPoints1.YColumn = 'Component_1'
tableToPoints1.ZColumn = 'Component_2'
tableToPoints1.KeepAllDataArrays = 1

# create a new 'K Means'
kMeans1 = KMeans(Input=tableToPoints1,
    ModelInput=None)
kMeans1.VariablesofInterest = ['Component_0', 'Component_1', 'Component_2']
kMeans1.k = 8

# create a new 'TTK RipsComplex'
tTKRipsComplex1 = TTKRipsComplex(Input=tTKTableDistanceMatrix1)
tTKRipsComplex1.SelectFieldswithaRegexp = 1
tTKRipsComplex1.Regexp = 'Dist.*'
tTKRipsComplex1.Diameterepsilon = 18.0

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=tTKRipsComplex1)
cellDatatoPointData1.CellDataArraytoprocess = ['Diameter']

# create a new 'Threshold'
threshold1 = Threshold(Input=cellDatatoPointData1)
threshold1.Scalars = ['POINTS', 'Diameter']
threshold1.LowerThreshold = 9.0
threshold1.UpperThreshold = 17.38239404772305

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=threshold1)
tTKPersistentGenerators1.ScalarField = ['POINTS', 'Diameter']
tTKPersistentGenerators1.InputOffsetField = ['POINTS', 'Component_0']
tTKPersistentGenerators1.PruneHandlesGenerators = 1

SaveData("PersistentGeneratorsHouseholdAnalysis_cycle.vtp", tTKPersistentGenerators1)
SaveData("PersistentGeneratorsHouseholdAnalysis_points.vtp", OutputPort(kMeans1,1))
SaveData("PersistentGeneratorsHouseholdAnalysis_ripsComplex.vtu", tTKRipsComplex1)

