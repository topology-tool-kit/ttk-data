#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="./Isabel.cdb")

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE TimeStep == 2 or TimeStep == 32"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaQuery1)

# create a new 'TTK Merge and Contour Tree'
tTKMergeandContourTreeFTM4 = TTKMergeTree(Input=tTKCinemaProductReader1)
tTKMergeandContourTreeFTM4.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM4.TreeType = "Split Tree"

# create a new 'TTK BlockAggregator'
tTKBlockAggregator1 = TTKBlockAggregator(
    Input=[
        tTKMergeandContourTreeFTM4,
        OutputPort(tTKMergeandContourTreeFTM4, 1),
        OutputPort(tTKMergeandContourTreeFTM4, 2),
    ]
)
tTKBlockAggregator1.FlattenInput = 0

# create a new 'TTK MergeTreeClustering'
tTKMergeTreeClustering3 = TTKMergeTreeClustering(
    Input=tTKBlockAggregator1, OptionalInputclustering=None
)
tTKMergeTreeClustering3.Deterministic = 1
tTKMergeTreeClustering3.DimensionSpacing = 0.1
tTKMergeTreeClustering3.DimensionToshift = "Y"
tTKMergeTreeClustering3.Epsilon1 = 20.0
tTKMergeTreeClustering3.Epsilon2 = 100.0
tTKMergeTreeClustering3.Epsilon3 = 100.0
tTKMergeTreeClustering3.PersistenceThreshold = 2.0
tTKMergeTreeClustering3.ImportantPairs = 20.0
tTKMergeTreeClustering3.ImportantPairsSpacing = 20.0
tTKMergeTreeClustering3.NonImportantPairsProximity = 0.2

# create a new 'TTK CinemaQuery'
tTKCinemaQuery2 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery2.SQLStatement = """SELECT * FROM InputTable0
WHERE TimeStep == 32 or TimeStep == 45"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader2 = TTKCinemaProductReader(Input=tTKCinemaQuery2)
tTKCinemaProductReader2.AddFieldDataRecursively = 1

# create a new 'TTK Merge and Contour Tree'
tTKMergeandContourTreeFTM5 = TTKMergeTree(Input=tTKCinemaProductReader2)
tTKMergeandContourTreeFTM5.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM5.TreeType = "Split Tree"

# create a new 'TTK BlockAggregator'
tTKBlockAggregator2 = TTKBlockAggregator(
    Input=[
        tTKMergeandContourTreeFTM5,
        OutputPort(tTKMergeandContourTreeFTM5, 1),
        OutputPort(tTKMergeandContourTreeFTM5, 2),
    ]
)
tTKBlockAggregator2.FlattenInput = 0

# create a new 'TTK MergeTreeClustering'
tTKMergeTreeClustering4 = TTKMergeTreeClustering(
    Input=tTKBlockAggregator2, OptionalInputclustering=None
)
tTKMergeTreeClustering4.Deterministic = 1
tTKMergeTreeClustering4.DimensionSpacing = 0.1
tTKMergeTreeClustering4.DimensionToshift = "Y"
tTKMergeTreeClustering4.PersistenceThreshold = 2.0
tTKMergeTreeClustering4.ImportantPairs = 23.0
tTKMergeTreeClustering4.ImportantPairsSpacing = 20.0
tTKMergeTreeClustering4.NonImportantPairsProximity = 0.2

# save the output
SaveData("matching_T2_T32.vtm", OutputPort(tTKMergeTreeClustering3, 2))
SaveData("matching_T32_T45.vtm", OutputPort(tTKMergeTreeClustering4, 2))
