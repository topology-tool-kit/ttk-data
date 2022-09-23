#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath='khi.cdb')

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery1.SQLStatement = """
    SELECT * FROM InputTable0
        WHERE Resolution='512' 
            AND (Time='0' OR Time='2') 
            AND (NOT (Solver='hll'))"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaQuery1)

# create a new 'TTK TriangulationManager'
tTKTriangulationManager1 = TTKTriangulationManager(Input=tTKCinemaProductReader1)
tTKTriangulationManager1.PeriodicityinAllDimensions = 1

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=tTKTriangulationManager1)
tTKScalarFieldNormalizer1.ScalarField = ['POINTS', 'Enstrophy']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKScalarFieldNormalizer1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Enstrophy']

# create a new 'TTK PersistenceDiagramClustering'
tTKPersistenceDiagramClustering1 = TTKPersistenceDiagramClustering(Input=tTKPersistenceDiagram1)
tTKPersistenceDiagramClustering1.Criticalpairsusedfortheclustering = 'saddle-max pairs'
tTKPersistenceDiagramClustering1.Numberofclusters = 2

# create a new 'TTK PersistenceDiagramDistanceMatrix'
tTKPersistenceDiagramDistanceMatrix1 = TTKPersistenceDiagramDistanceMatrix(Input=tTKPersistenceDiagramClustering1)
tTKPersistenceDiagramDistanceMatrix1.Criticalpairsused = 'saddle-max pairs'

# create a new 'TTK LDistanceMatrix'
tTKLDistanceMatrix1 = TTKLDistanceMatrix(Input=tTKCinemaProductReader1)
tTKLDistanceMatrix1.ScalarField = ['POINTS', 'Enstrophy']

# create a new 'TTK DimensionReduction'
tTKDimensionReduction2 = TTKDimensionReduction(Input=tTKLDistanceMatrix1)
tTKDimensionReduction2.Regexp = "Dataset.*"
tTKDimensionReduction2.SelectFieldswithaRegexp = 1
tTKDimensionReduction2.InputIsaDistanceMatrix = 1

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(Input=tTKDimensionReduction2)
tableToPoints2.XColumn = 'Component_0'
tableToPoints2.YColumn = 'Component_1'
tableToPoints2.a2DPoints = 1
tableToPoints2.KeepAllDataArrays = 1

# create a new 'K Means'
kMeans1 = KMeans(Input=tableToPoints2)
kMeans1.VariablesofInterest = ['Component_0', 'Component_1']
kMeans1.k = 2

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(Input=tTKPersistenceDiagramDistanceMatrix1)
tTKDimensionReduction1.Regexp = "Diagram.*"
tTKDimensionReduction1.SelectFieldswithaRegexp = 1
tTKDimensionReduction1.InputIsaDistanceMatrix = 1

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints1.XColumn = 'Component_0'
tableToPoints1.YColumn = 'Component_1'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

SaveData("W2clusteringAndW2dimensionReduction.csv", tableToPoints1)

SaveData("L2dimensionReductionAndClustering.csv", OutputPort(kMeans1, 1))
