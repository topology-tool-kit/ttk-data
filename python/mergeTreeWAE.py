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
tTKMergeandContourTreeFTM1.UseAllCores = 0

# create a new 'TTK BlockAggregator'
tTKBlockAggregator1 = TTKBlockAggregator(
    Input=[
        tTKMergeandContourTreeFTM1,
        OutputPort(tTKMergeandContourTreeFTM1, 1),
    ]
)
tTKBlockAggregator1.FlattenInput = 0

# create a new 'TTK MergeTreeAutoencoder'
tTKMergeTreeAutoencoder1 = TTKMergeTreeAutoencoder(
    Input=tTKBlockAggregator1, OptionalInput=None, Info=tTKCinemaReader1
)
tTKMergeTreeAutoencoder1.ScaleLayerAfterLatent = 1
tTKMergeTreeAutoencoder1.InputOriginPrimeSizePercent = 7.0
tTKMergeTreeAutoencoder1.LatentSpaceOriginPrimeSizePercent = 1.0
tTKMergeTreeAutoencoder1.MinIteration = 300
tTKMergeTreeAutoencoder1.MaxIteration = 1000
tTKMergeTreeAutoencoder1.GradientStepSize = 0.0005
tTKMergeTreeAutoencoder1.TrackingLossWeight = 1e-06
tTKMergeTreeAutoencoder1.ClusteringLossWeight = 0.02
tTKMergeTreeAutoencoder1.ClusteringArrayName = "ClusterID"
tTKMergeTreeAutoencoder1.PairTypeMixtureCoefficient = 0.0
tTKMergeTreeAutoencoder1.DeleteMultiPersistencePairs = 1
tTKMergeTreeAutoencoder1.Epsilon1 = 0.5
tTKMergeTreeAutoencoder1.Epsilon2 = 35.0
tTKMergeTreeAutoencoder1.Epsilon3 = 34.0
tTKMergeTreeAutoencoder1.PersistenceThreshold = 2.0

# create a new 'TTK MergeTreeAutoencoderDecoding'
tTKMergeTreeAutoencoderDecoding1 = TTKMergeTreeAutoencoderDecoding(
    Origins=OutputPort(tTKMergeTreeAutoencoder1, 0),
    BasesVectors=OutputPort(tTKMergeTreeAutoencoder1, 1),
    Coefficients=OutputPort(tTKMergeTreeAutoencoder1, 2),
)

# save the output
SaveData("MT-WAE_processed_diagrams.vtm", OutputPort(tTKMergeTreeAutoencoder1, 0))
SaveData("MT-WAE_origins.vtm", OutputPort(tTKMergeTreeAutoencoder1, 1))
SaveData("MT-WAE_axes.vtm", OutputPort(tTKMergeTreeAutoencoder1, 2))
SaveData("MT-WAE_coef.vtm", OutputPort(tTKMergeTreeAutoencoder1, 3))
SaveData("MT-WAE_reconstructed_diagrams.vtm", tTKMergeTreeAutoencoderDecoding1)
