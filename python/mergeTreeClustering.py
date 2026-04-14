#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="./Isabel.cdb")

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)
tTKCinemaProductReader1.AddFieldDataRecursively = 1

# create a new 'TTK Merge and Contour Tree'
tTKMergeandContourTreeFTM26 = TTKMergeTree(Input=tTKCinemaProductReader1)
tTKMergeandContourTreeFTM26.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM26.TreeType = "Join Tree"

# create a new 'Group Datasets'
mt_JT_all = GroupDatasets(
    Input=[
        tTKMergeandContourTreeFTM26,
        OutputPort(tTKMergeandContourTreeFTM26, 1),
        OutputPort(tTKMergeandContourTreeFTM26, 2),
    ]
)

# create a new 'TTK Merge and Contour Tree'
tTKMergeandContourTreeFTM25 = TTKMergeTree(Input=tTKCinemaProductReader1)
tTKMergeandContourTreeFTM25.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM25.TreeType = "Split Tree"

# create a new 'Group Datasets'
mT_all = GroupDatasets(
    Input=[
        tTKMergeandContourTreeFTM25,
        OutputPort(tTKMergeandContourTreeFTM25, 1),
        OutputPort(tTKMergeandContourTreeFTM25, 2),
    ]
)

# create a new 'TTK MergeTreeClustering'
tTKMergeTreeClustering1 = TTKMergeTreeClustering(
    Input=mT_all, OptionalInputclustering=mt_JT_all
)
tTKMergeTreeClustering1.ComputeBarycenter = 1
tTKMergeTreeClustering1.NumberOfClusters = 3
tTKMergeTreeClustering1.Deterministic = 1
tTKMergeTreeClustering1.DimensionSpacing = 0.1
tTKMergeTreeClustering1.PersistenceThreshold = 2.0
tTKMergeTreeClustering1.ImportantPairs = 34.0
tTKMergeTreeClustering1.MaximumNumberofImportantPairs = 3
tTKMergeTreeClustering1.MinimumNumberofImportantPairs = 2
tTKMergeTreeClustering1.ImportantPairsSpacing = 15.0
tTKMergeTreeClustering1.NonImportantPairsProximity = 0.15

# create a new 'Extract Block'
nodes = ExtractBlock(Input=OutputPort(tTKMergeTreeClustering1, 1))
nodes.Selectors = ["/Root/Block0"]

# create a new 'Extract Block'
nodes_1 = ExtractBlock(Input=tTKMergeTreeClustering1)
nodes_1.Selectors = ["/Root/Block0"]

# create a new 'Extract Block'
arcs = ExtractBlock(Input=OutputPort(tTKMergeTreeClustering1, 1))
arcs.Selectors = ["/Root/Block1"]

# create a new 'Extract Block'
arcs_1 = ExtractBlock(Input=tTKMergeTreeClustering1)
arcs_1.Selectors = ["/Root/Block1"]

# create a new 'TTK BlockAggregator'
tTKBlockAggregator1 = TTKBlockAggregator(
    registrationName="TTKBlockAggregator1", Input=[nodes_1, nodes]
)

# create a new 'TTK FlattenMultiBlock'
tTKFlattenMultiBlock1 = TTKFlattenMultiBlock(
    registrationName="TTKFlattenMultiBlock1", Input=tTKBlockAggregator1
)

# create a new 'TTK BlockAggregator'
tTKBlockAggregator2 = TTKBlockAggregator(
    registrationName="TTKBlockAggregator2", Input=[arcs_1, arcs]
)

# create a new 'TTK FlattenMultiBlock'
tTKFlattenMultiBlock3 = TTKFlattenMultiBlock(
    registrationName="TTKFlattenMultiBlock3", Input=tTKBlockAggregator2
)

# create a new 'TTK BlockAggregator'
tTKBlockAggregator3 = TTKBlockAggregator(
    registrationName="TTKBlockAggregator3",
    Input=[tTKFlattenMultiBlock1, tTKFlattenMultiBlock3],
)
tTKBlockAggregator3.FlattenInput = 0

# create a new 'TTK MergeTreeDistanceMatrix'
tTKMergeTreeDistanceMatrix2 = TTKMergeTreeDistanceMatrix(Input=tTKBlockAggregator3)
tTKMergeTreeDistanceMatrix2.PersistenceThreshold = 2.0

# create a new 'TTK DimensionReduction'
tTKDimensionReduction2 = TTKDimensionReduction(
    Input=tTKMergeTreeDistanceMatrix2, ModulePath="default"
)
tTKDimensionReduction2.SelectFieldswithaRegexp = 1
tTKDimensionReduction2.Regexp = "Tree[0-9]+"
tTKDimensionReduction2.InputIsaDistanceMatrix = 1
tTKDimensionReduction2.UseAllCores = 0  # MDS is unstable in parallel mode

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction2)
tableToPoints1.XColumn = "Component_0"
tableToPoints1.YColumn = "Component_1"
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'Mask Points' (to threshold on points)
maskPoints1 = MaskPoints(Input=tableToPoints1)
maskPoints1.OnRatio = 0
maskPoints1.GenerateVertices = 1
maskPoints1.SingleVertexPerCell = 1

# create a new 'Threshold'
threshold33 = Threshold(Input=maskPoints1)
threshold33.Scalars = ["POINTS", "treeID"]
threshold33.ThresholdMethod = "Between"
threshold33.LowerThreshold = 0.0
threshold33.UpperThreshold = 11.0

# create a new 'Threshold'
threshold34 = Threshold(Input=maskPoints1)
threshold34.Scalars = ["POINTS", "treeID"]
threshold34.ThresholdMethod = "Between"
threshold34.LowerThreshold = 12.0
threshold34.UpperThreshold = 14.0

# save the output
SaveData("MDS_trees.csv", threshold33)
SaveData("MDS_centroids.csv", threshold34)
