#! /usr/bin/env/python

from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(
    registrationName="TTKCinemaReader1", DatabasePath="Isabel.cdb"
)

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(
    registrationName="TTKCinemaProductReader1", Input=tTKCinemaReader1
)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram13 = TTKPersistenceDiagram(
    registrationName="TTKPersistenceDiagram13", Input=tTKCinemaProductReader1
)
tTKPersistenceDiagram13.ScalarField = ["POINTS", "velocityMag"]
tTKPersistenceDiagram13.InputOffsetField = ["POINTS", "velocityMag"]

# create a new 'TTK PersistenceDiagramClustering'
tTKPersistenceDiagramClustering1 = TTKPersistenceDiagramClustering(
    registrationName="TTKPersistenceDiagramClustering1", Input=tTKPersistenceDiagram13
)
tTKPersistenceDiagramClustering1.Numberofclusters = 3
tTKPersistenceDiagramClustering1.Maximalcomputationtimes = 10.0
tTKPersistenceDiagramClustering1.Displayingmethod = "Clusters as stars"
tTKPersistenceDiagramClustering1.Spacing = 1.1
tTKPersistenceDiagramClustering1.GeometricalLiftingalpha = 0.2

# save the output
SaveData(
    "PersistenceDiagramClustering_centroids.vtm",
    OutputPort(tTKPersistenceDiagramClustering1, 1),
)

SaveData(
    "PersistenceDiagramClustering_clustering.csv",
    proxy=tTKPersistenceDiagramClustering1,
    ChooseArraysToWrite=1,
    FieldDataArrays=["FILE", "TimeStep", "ClusterId"],
    FieldAssociation="Field Data",
    AddMetaData=0,
)
