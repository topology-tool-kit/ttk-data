#!/usr/bin/env python

from paraview.simple import *

# read input VTI with 'XML Image Data Reader'
naturalImage = XMLImageDataReader(FileName=["naturalImage_original.vti"])

# compress & save to TTK Topological Compression format
SaveData(
    "naturalImage_persistence10_zfp50.ttk",
    proxy=naturalImage,
    ScalarField=["POINTS", "PNGImage"],
    Topologicallosspersistencepercentage=10,  # Topological loss
    ZFPRelativeErrorToleranceextra=50,  # ZFP Relative Error Tolerance
)

# read the compressed file with 'TTK TopologicalCompressionReader'
naturalImage_compressed = TTKTopologicalCompressionReader(
    FileName="naturalImage_persistence10_zfp50.ttk",
)

# write compressed data-set to VTI
SaveData(
    "uncompressed_naturalImage_persistence10_zfp50.vti",
    naturalImage_compressed,
)
