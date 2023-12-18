#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath='./Isabel.cdb')

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)
tTKCinemaProductReader1.AddFieldDataRecursively = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKCinemaProductReader1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'velocityMag']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'velocityMag']
tTKPersistenceDiagram1.Backend = 'FTM (IEEE TPSD 2019)'

# create a new 'TTK MergeTreePrincipalGeodesics'
tTKMergeTreePrincipalGeodesics1 = TTKMergeTreePrincipalGeodesics(Input=tTKPersistenceDiagram1,
    OptionalInput=None)
tTKMergeTreePrincipalGeodesics1.NormalizedWasserstein = 0
tTKMergeTreePrincipalGeodesics1.BarycenterSizeLimitPercent = 20.0
tTKMergeTreePrincipalGeodesics1.Deterministic = 1
tTKMergeTreePrincipalGeodesics1.PairTypeMixtureCoefficient = 0.0
tTKMergeTreePrincipalGeodesics1.PersistenceThreshold = 2.0

# save the output
SaveData("PD-PGA_coef.csv", OutputPort(tTKMergeTreePrincipalGeodesics1, 1))
