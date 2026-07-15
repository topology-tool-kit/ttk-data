#!/usr/bin/env python
# state file generated using paraview version 5.10.1

#### import the simple module from the paraview
from paraview.simple import *

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML MultiBlock Data Reader'
outliervtm = XMLMultiBlockDataReader(FileName=["bdied_outlier/outlier.vtm"])

# create a new 'TTK MergeTree'
tTKMergeandContourTreeFTM1 = TTKMergeTree(Input=outliervtm)
tTKMergeandContourTreeFTM1.ScalarField = ["POINTS", "test"]
tTKMergeandContourTreeFTM1.TreeType = "Split Tree"
tTKMergeandContourTreeFTM1.UseAllCores = 0

# create a new 'TTK BlockAggregator'
tTKBlockAggregator1 = TTKBlockAggregator(
    Input=[
        tTKMergeandContourTreeFTM1,
        OutputPort(tTKMergeandContourTreeFTM1, 1),
        OutputPort(tTKMergeandContourTreeFTM1, 2),
    ]
)
tTKBlockAggregator1.FlattenInput = 0

# create a new 'TTK MergeTreeDistanceMatrix'
tTKMergeTreeDistanceMatrix1 = TTKMergeTreeDistanceMatrix(
    Input=tTKBlockAggregator1, OptionalInput=None
)
tTKMergeTreeDistanceMatrix1.Backend = "Branch Mapping Distance (EuroVis 2022)"
tTKMergeTreeDistanceMatrix1.DistanceSquareRoot = 0
tTKMergeTreeDistanceMatrix1.Epsilon1 = 0.0
tTKMergeTreeDistanceMatrix1.Epsilon2 = 100.0
tTKMergeTreeDistanceMatrix1.Epsilon3 = 100.0

# create a new 'TTK MergeTreeClustering'
tTKMergeTreeClustering1 = TTKMergeTreeClustering(
    Input=tTKBlockAggregator1, OptionalInputclustering=None
)
tTKMergeTreeClustering1.Backend = "Branch Mapping Distance (EuroVis 2022)"
tTKMergeTreeClustering1.Deterministic = 1
tTKMergeTreeClustering1.DimensionSpacing = 0.05
tTKMergeTreeClustering1.DimensionToshift = "Z"
tTKMergeTreeClustering1.Epsilon1 = 0.0
tTKMergeTreeClustering1.Epsilon2 = 100.0
tTKMergeTreeClustering1.Epsilon3 = 100.0
tTKMergeTreeClustering1.ImportantPairs = 49.0
tTKMergeTreeClustering1.ImportantPairsSpacing = 32.0
tTKMergeTreeClustering1.NonImportantPairsSpacing = 8.0

# save the output
SaveData("merge_tree_mapping.vtm", proxy=OutputPort(tTKMergeTreeClustering1, 2))
SaveData("distance_matrix.csv", tTKMergeTreeDistanceMatrix1)
