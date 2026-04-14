#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="./Isabel.cdb")

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)
tTKCinemaProductReader1.AddFieldDataRecursively = 1

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM26 = TTKMergeTree(Input=tTKCinemaProductReader1)
tTKMergeandContourTreeFTM26.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM26.TreeType = "Split Tree"

# create a new 'Group Datasets'
all_MT = GroupDatasets(
    Input=[
        tTKMergeandContourTreeFTM26,
        OutputPort(tTKMergeandContourTreeFTM26, 1),
        OutputPort(tTKMergeandContourTreeFTM26, 2),
    ]
)

# create a new 'TTK MergeTreeTemporalReduction'
tTKMergeTreeTemporalReduction1 = TTKMergeTreeTemporalReduction(Input=all_MT)
tTKMergeTreeTemporalReduction1.RemovalPercentage = 75.0
tTKMergeTreeTemporalReduction1.Epsilon1 = 0.0
tTKMergeTreeTemporalReduction1.Epsilon2 = 100.0
tTKMergeTreeTemporalReduction1.Epsilon3 = 100.0
tTKMergeTreeTemporalReduction1.PersistenceThreshold = 3.0

SaveData("ReductionCoefficients.csv", OutputPort(tTKMergeTreeTemporalReduction1, 1))
