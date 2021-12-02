#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK TopologicalCompressionReader'
naturalImage_zfp50ttk = TTKTopologicalCompressionReader(
    FileName="naturalImage_zfp50.ttk"
)

# create a new 'XML Image Data Reader'
naturalImage_originalvti = XMLImageDataReader(FileName=["naturalImage_original.vti"])
naturalImage_originalvti.PointArrayStatus = ["PNGImage"]
naturalImage_originalvti.TimeArray = "None"

# create a new 'TTK TopologicalCompressionReader'
naturalImage_persistence10ttk = TTKTopologicalCompressionReader(
    FileName="naturalImage_persistence10.ttk",
)

# create a new 'TTK TopologicalCompressionReader'
naturalImage_persistence10_zfp50ttk = TTKTopologicalCompressionReader(
    FileName="naturalImage_persistence10_zfp50.ttk",
)

# save outputs to VTI
SaveData("uncompressed_naturalImage_zfp50.vti", naturalImage_zfp50ttk)
SaveData("uncompressed_naturalImage_persistence10.vti", naturalImage_persistence10ttk)
SaveData(
    "uncompressed_naturalImage_persistence10_zfp50.vti",
    naturalImage_persistence10_zfp50ttk,
)
