# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'

# create a new 'XML Image Data Reader'
atvti = XMLImageDataReader(registrationName='at.vti', FileName=['at.vti'])
atvti.PointArrayStatus = ['density']
atvti.TimeArray = 'None'

# create a new 'TTK PathCompression'
tTKPathCompression1 = TTKPathCompression(registrationName='TTKPathCompression1', Input=atvti)
tTKPathCompression1.ScalarField = ['POINTS', 'density']
tTKPathCompression1.OffsetField = ['POINTS', 'density']
tTKPathCompression1.MorseSmaleComplexHash = 0


# create a new 'TTK MergeTree'
tTKMergeTree1 = TTKMergeTree(registrationName='TTKMergeTree1', Input=tTKPathCompression1)
tTKMergeTree1.ScalarField = ['POINTS', 'density']
tTKMergeTree1.InputOffsetField = ['POINTS', 'density']
tTKMergeTree1.TreeType = 'Split Tree'
tTKMergeTree1.Backend = 'ExTreeM (IEEE TVCG 2023)'

# create a new 'TTK MergeTree'
tTKMergeTree2 = TTKMergeTree(registrationName='TTKMergeTree2', Input=tTKPathCompression1)
tTKMergeTree2.ScalarField = ['POINTS', 'density']
tTKMergeTree2.InputOffsetField = ['POINTS', 'density']
tTKMergeTree2.TreeType = 'Join Tree'
tTKMergeTree2.Backend = 'ExTreeM (IEEE TVCG 2023)'


SaveData('splitTree.vtu', proxy=OutputPort(tTKMergeTree1, 1))
SaveData('joinTree.vtu', proxy=OutputPort(tTKMergeTree2, 1))