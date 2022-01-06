#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
manifoldCheck2vtu = XMLUnstructuredGridReader(FileName=["manifoldCheck2.vtu"])

# create a new 'Tetrahedralize'
tetrahedralize3 = Tetrahedralize(
    registrationName="Tetrahedralize3", Input=manifoldCheck2vtu
)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck3 = TTKManifoldCheck(
    registrationName="TTKManifoldCheck3", Input=tetrahedralize3
)

# create a new 'Threshold'
# this extracts tetrahedra that contain non-manifold faces
threshold3 = Threshold(registrationName="Threshold3", Input=tTKManifoldCheck3)
threshold3.Scalars = ["CELLS", "TriangleLinkComponentNumber"]
threshold3.LowerThreshold = 3.0
threshold3.UpperThreshold = 3.0

# create a new 'Generate Ids'
generateIds1 = GenerateIds(registrationName="GenerateIds1", Input=threshold3)
generateIds1.PointIdsArrayName = "VertexIdentifiers"
generateIds1.CellIdsArrayName = "CellIdentifiers"

# create a new 'Threshold'
# select two of the tetrahedra
threshold4 = Threshold(registrationName="Threshold4", Input=generateIds1)
threshold4.Scalars = ["CELLS", "CellIdentifiers"]
threshold4.UpperThreshold = 1.0

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(registrationName="ExtractSurface2", Input=threshold4)

# create a new 'Threshold'
# this extracts non-manifold faces
threshold5 = Threshold(registrationName="Threshold5", Input=extractSurface2)
threshold5.Scalars = ["POINTS", "TriangleLinkComponentNumber"]
threshold5.LowerThreshold = 3.0
threshold5.UpperThreshold = 3.0

# save the output
SaveData("manifoldCheck2_check.vtu", tTKManifoldCheck3)
SaveData("manifoldCheck2_non_manifold.vtu", threshold5)
