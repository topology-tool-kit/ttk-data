#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="./Earthquake.cdb")

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)
tTKCinemaProductReader1.AddFieldDataRecursively = 1

# create a new 'TTK Merge and Contour Tree'
tTKMergeandContourTreeFTM1 = TTKMergeTree(Input=tTKCinemaProductReader1)
tTKMergeandContourTreeFTM1.ScalarField = ["POINTS", "VectorMag"]
tTKMergeandContourTreeFTM1.TreeType = "Split Tree"

# create a new 'TTK BlockAggregator'
tTKBlockAggregator1 = TTKBlockAggregator(
    Input=[
        tTKMergeandContourTreeFTM1,
        OutputPort(tTKMergeandContourTreeFTM1, 1),
        OutputPort(tTKMergeandContourTreeFTM1, 2),
    ]
)
tTKBlockAggregator1.FlattenInput = 0

# create a new 'TTK MergeTreePrincipalGeodesics'
tTKMergeTreePrincipalGeodesics1 = TTKMergeTreePrincipalGeodesics(
    Input=tTKBlockAggregator1, OptionalInput=None
)
tTKMergeTreePrincipalGeodesics1.BarycenterSizeLimitPercent = 17.0
tTKMergeTreePrincipalGeodesics1.Deterministic = 1
tTKMergeTreePrincipalGeodesics1.Epsilon1 = 1.5
tTKMergeTreePrincipalGeodesics1.Epsilon2 = 35.0
tTKMergeTreePrincipalGeodesics1.Epsilon3 = 34.0
tTKMergeTreePrincipalGeodesics1.PersistenceThreshold = 1.0
tTKMergeTreePrincipalGeodesics1.DeleteMultiPersistencePairs = 1

# create a new 'TTK MergeTreePrincipalGeodesicsDecoding'
tTKMergeTreePrincipalGeodesicsDecoding1 = TTKMergeTreePrincipalGeodesicsDecoding(
    Barycenter=tTKMergeTreePrincipalGeodesics1,
    Coefficients=OutputPort(tTKMergeTreePrincipalGeodesics1, 1),
    GeodesicsVectors=OutputPort(tTKMergeTreePrincipalGeodesics1, 2),
    CorrelationMatrixoptional=None,
    InputTreesoptional=None,
)

# save the output
SaveData("MT-PGA_coef.csv", OutputPort(tTKMergeTreePrincipalGeodesics1, 1))
SaveData("MT-PGA_geodesics.csv", OutputPort(tTKMergeTreePrincipalGeodesics1, 2))
SaveData("MT-PGA_reconstructed_trees.vtm", tTKMergeTreePrincipalGeodesicsDecoding1)
