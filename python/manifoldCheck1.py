#!/usr/bin/env python
from paraview.simple import *

# paraview 5.9 VS 5.10 compatibility ===========================================
def ThresholdBetween(threshold, lower, upper):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [lower, upper]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Between"
        threshold.LowerThreshold = lower
        threshold.UpperThreshold = upper
# end of comphatibility ========================================================

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
ThresholdBetween(threshold2, 2.0, 2.0)

# save the output
SaveData("manifoldCheck1_check.vtu", tTKManifoldCheck2)
SaveData("manifoldCheck1_non_manifold.vtu", threshold2)
