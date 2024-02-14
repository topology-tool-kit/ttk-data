#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader2_Isabel = TTKCinemaReader(DatabasePath="./Isabel.cdb")

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader7 = TTKCinemaProductReader(Input=tTKCinemaReader2_Isabel)
tTKCinemaProductReader7.AddFieldDataRecursively = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKCinemaProductReader7)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "velocityMag"]
tTKPersistenceDiagram1.InputOffsetField = ["POINTS", "velocityMag"]
tTKPersistenceDiagram1.Backend = "FTM (IEEE TPSD 2019)"

# create a new 'TTK MergeTreeAutoencoder'
tTKMergeTreeAutoencoder1 = TTKMergeTreeAutoencoder(
    Input=tTKPersistenceDiagram1, OptionalInput=None, Info=None
)
tTKMergeTreeAutoencoder1.NormalizedWasserstein = 0
tTKMergeTreeAutoencoder1.ScaleLayerAfterLatent = 1
tTKMergeTreeAutoencoder1.InputOriginPrimeSizePercent = 12.0
tTKMergeTreeAutoencoder1.LatentSpaceNumberofAxes = 1
tTKMergeTreeAutoencoder1.LatentSpaceOriginPrimeSizePercent = 5.0
tTKMergeTreeAutoencoder1.BarycenterSizeLimitPercent = 0.0
tTKMergeTreeAutoencoder1.MinIteration = 500
tTKMergeTreeAutoencoder1.GradientStepSize = 0.15
tTKMergeTreeAutoencoder1.TrackingLossWeight = 1e-06
tTKMergeTreeAutoencoder1.ClusteringArrayName = ""
tTKMergeTreeAutoencoder1.InitOriginPrimeStructByCopy = 0
tTKMergeTreeAutoencoder1.PairTypeMixtureCoefficient = 0.0
tTKMergeTreeAutoencoder1.Epsilon1 = 100.0
tTKMergeTreeAutoencoder1.PersistenceThreshold = 5.0

# create a new 'TTK MergeTreeAutoencoderDecoding'
tTKMergeTreeAutoencoderDecoding1 = TTKMergeTreeAutoencoderDecoding(
    Origins=OutputPort(tTKMergeTreeAutoencoder1, 1),
    BasesVectors=OutputPort(tTKMergeTreeAutoencoder1, 2),
    Coefficients=OutputPort(tTKMergeTreeAutoencoder1, 3),
)

# save the output
SaveData("MT-WAE_processed_diagrams.vtm", OutputPort(tTKMergeTreeAutoencoder1, 0))
SaveData("MT-WAE_origins.vtm", OutputPort(tTKMergeTreeAutoencoder1, 1))
SaveData("MT-WAE_axes.vtm", OutputPort(tTKMergeTreeAutoencoder1, 2))
SaveData("MT-WAE_coef.vtm", OutputPort(tTKMergeTreeAutoencoder1, 3))
SaveData("MT-WAE_reconstructed_diagrams.vtm", tTKMergeTreeAutoencoderDecoding1)
