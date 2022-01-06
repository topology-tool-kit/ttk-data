#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
manifoldCheck1vtu = XMLUnstructuredGridReader(FileName=["manifoldCheck1.vtu"])

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=manifoldCheck1vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck2 = TTKManifoldCheck(Input=tetrahedralize2)

# create a new 'Extract Edges'
extractEdges2 = ExtractEdges(Input=tTKManifoldCheck2)

# create a new 'Threshold'
# this extracts non-manifold edges
threshold2 = Threshold(Input=extractEdges2)
threshold2.Scalars = ["POINTS", "EdgeLinkComponentNumber"]
threshold2.LowerThreshold = 2.0
threshold2.UpperThreshold = 2.0

# save the output
SaveData("manifoldCheck1_check.vtu", tTKManifoldCheck2)
SaveData("manifoldCheck1_non_manifold.vtu", threshold2)
