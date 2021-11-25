# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
isabelvti = XMLImageDataReader(registrationName='isabel.vti', FileName=['isabel.vti'])
isabelvti.PointArrayStatus = ['velocityMag_02', 'velocityMag_03', 'velocityMag_04', 'velocityMag_05', 'velocityMag_30', 'velocityMag_31', 'velocityMag_32', 'velocityMag_33', 'velocityMag_45', 'velocityMag_46', 'velocityMag_47', 'velocityMag_48']
isabelvti.TimeArray = 'None'

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM12 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM12', Input=isabelvti)
tTKMergeandContourTreeFTM12.ScalarField = ['POINTS', 'velocityMag_48']
tTKMergeandContourTreeFTM12.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM12.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM12_1 = FindSource('TTKMergeandContourTreeFTM12')

# find source
tTKMergeandContourTreeFTM12_2 = FindSource('TTKMergeandContourTreeFTM12')

# create a new 'Group Datasets'
groupDatasets12 = GroupDatasets(registrationName='GroupDatasets12', Input=[tTKMergeandContourTreeFTM12, OutputPort(tTKMergeandContourTreeFTM12_1,1), OutputPort(tTKMergeandContourTreeFTM12_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM11 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM11', Input=isabelvti)
tTKMergeandContourTreeFTM11.ScalarField = ['POINTS', 'velocityMag_47']
tTKMergeandContourTreeFTM11.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM11.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM11_1 = FindSource('TTKMergeandContourTreeFTM11')

# find source
tTKMergeandContourTreeFTM11_2 = FindSource('TTKMergeandContourTreeFTM11')

# create a new 'Group Datasets'
groupDatasets11 = GroupDatasets(registrationName='GroupDatasets11', Input=[tTKMergeandContourTreeFTM11, OutputPort(tTKMergeandContourTreeFTM11_1,1), OutputPort(tTKMergeandContourTreeFTM11_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM9 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM9', Input=isabelvti)
tTKMergeandContourTreeFTM9.ScalarField = ['POINTS', 'velocityMag_45']
tTKMergeandContourTreeFTM9.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM9.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM9_1 = FindSource('TTKMergeandContourTreeFTM9')

# find source
tTKMergeandContourTreeFTM9_2 = FindSource('TTKMergeandContourTreeFTM9')

# create a new 'Group Datasets'
groupDatasets9 = GroupDatasets(registrationName='GroupDatasets9', Input=[tTKMergeandContourTreeFTM9, OutputPort(tTKMergeandContourTreeFTM9_1,1), OutputPort(tTKMergeandContourTreeFTM9_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM6 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM6', Input=isabelvti)
tTKMergeandContourTreeFTM6.ScalarField = ['POINTS', 'velocityMag_31']
tTKMergeandContourTreeFTM6.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM6.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM6_1 = FindSource('TTKMergeandContourTreeFTM6')

# find source
tTKMergeandContourTreeFTM6_2 = FindSource('TTKMergeandContourTreeFTM6')

# create a new 'Group Datasets'
groupDatasets6 = GroupDatasets(registrationName='GroupDatasets6', Input=[tTKMergeandContourTreeFTM6, OutputPort(tTKMergeandContourTreeFTM6_1,1), OutputPort(tTKMergeandContourTreeFTM6_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM4 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM4', Input=isabelvti)
tTKMergeandContourTreeFTM4.ScalarField = ['POINTS', 'velocityMag_05']
tTKMergeandContourTreeFTM4.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM4.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM4_1 = FindSource('TTKMergeandContourTreeFTM4')

# find source
tTKMergeandContourTreeFTM4_2 = FindSource('TTKMergeandContourTreeFTM4')

# create a new 'Group Datasets'
groupDatasets4 = GroupDatasets(registrationName='GroupDatasets4', Input=[tTKMergeandContourTreeFTM4, OutputPort(tTKMergeandContourTreeFTM4_1,1), OutputPort(tTKMergeandContourTreeFTM4_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM8 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM8', Input=isabelvti)
tTKMergeandContourTreeFTM8.ScalarField = ['POINTS', 'velocityMag_33']
tTKMergeandContourTreeFTM8.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM8.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM8_1 = FindSource('TTKMergeandContourTreeFTM8')

# find source
tTKMergeandContourTreeFTM8_2 = FindSource('TTKMergeandContourTreeFTM8')

# create a new 'Group Datasets'
groupDatasets8 = GroupDatasets(registrationName='GroupDatasets8', Input=[tTKMergeandContourTreeFTM8, OutputPort(tTKMergeandContourTreeFTM8_1,1), OutputPort(tTKMergeandContourTreeFTM8_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM5 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM5', Input=isabelvti)
tTKMergeandContourTreeFTM5.ScalarField = ['POINTS', 'velocityMag_30']
tTKMergeandContourTreeFTM5.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM5.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM5_1 = FindSource('TTKMergeandContourTreeFTM5')

# find source
tTKMergeandContourTreeFTM5_2 = FindSource('TTKMergeandContourTreeFTM5')

# create a new 'Group Datasets'
groupDatasets5 = GroupDatasets(registrationName='GroupDatasets5', Input=[tTKMergeandContourTreeFTM5, OutputPort(tTKMergeandContourTreeFTM5_1,1), OutputPort(tTKMergeandContourTreeFTM5_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM3 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM3', Input=isabelvti)
tTKMergeandContourTreeFTM3.ScalarField = ['POINTS', 'velocityMag_04']
tTKMergeandContourTreeFTM3.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM3.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM3_1 = FindSource('TTKMergeandContourTreeFTM3')

# find source
tTKMergeandContourTreeFTM3_2 = FindSource('TTKMergeandContourTreeFTM3')

# create a new 'Group Datasets'
groupDatasets3 = GroupDatasets(registrationName='GroupDatasets3', Input=[tTKMergeandContourTreeFTM3, OutputPort(tTKMergeandContourTreeFTM3_1,1), OutputPort(tTKMergeandContourTreeFTM3_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM7 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM7', Input=isabelvti)
tTKMergeandContourTreeFTM7.ScalarField = ['POINTS', 'velocityMag_32']
tTKMergeandContourTreeFTM7.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM7.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM7_1 = FindSource('TTKMergeandContourTreeFTM7')

# find source
tTKMergeandContourTreeFTM7_2 = FindSource('TTKMergeandContourTreeFTM7')

# create a new 'Group Datasets'
groupDatasets7 = GroupDatasets(registrationName='GroupDatasets7', Input=[tTKMergeandContourTreeFTM7, OutputPort(tTKMergeandContourTreeFTM7_1,1), OutputPort(tTKMergeandContourTreeFTM7_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM1', Input=isabelvti)
tTKMergeandContourTreeFTM1.ScalarField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM1.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM1.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM1_1 = FindSource('TTKMergeandContourTreeFTM1')

# find source
tTKMergeandContourTreeFTM1_2 = FindSource('TTKMergeandContourTreeFTM1')

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[tTKMergeandContourTreeFTM1, OutputPort(tTKMergeandContourTreeFTM1_1,1), OutputPort(tTKMergeandContourTreeFTM1_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM2 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM2', Input=isabelvti)
tTKMergeandContourTreeFTM2.ScalarField = ['POINTS', 'velocityMag_03']
tTKMergeandContourTreeFTM2.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM2.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM2_1 = FindSource('TTKMergeandContourTreeFTM2')

# find source
tTKMergeandContourTreeFTM2_2 = FindSource('TTKMergeandContourTreeFTM2')

# create a new 'Group Datasets'
groupDatasets2 = GroupDatasets(registrationName='GroupDatasets2', Input=[tTKMergeandContourTreeFTM2, OutputPort(tTKMergeandContourTreeFTM2_1,1), OutputPort(tTKMergeandContourTreeFTM2_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM10 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM10', Input=isabelvti)
tTKMergeandContourTreeFTM10.ScalarField = ['POINTS', 'velocityMag_46']
tTKMergeandContourTreeFTM10.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM10.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM10_1 = FindSource('TTKMergeandContourTreeFTM10')

# find source
tTKMergeandContourTreeFTM10_2 = FindSource('TTKMergeandContourTreeFTM10')

# create a new 'Group Datasets'
groupDatasets10 = GroupDatasets(registrationName='GroupDatasets10', Input=[tTKMergeandContourTreeFTM10, OutputPort(tTKMergeandContourTreeFTM10_1,1), OutputPort(tTKMergeandContourTreeFTM10_2,2)])

# create a new 'Group Datasets'
groupDatasets13 = GroupDatasets(registrationName='GroupDatasets13', Input=[groupDatasets1, groupDatasets2, groupDatasets3, groupDatasets4, groupDatasets5, groupDatasets6, groupDatasets7, groupDatasets8, groupDatasets9, groupDatasets10, groupDatasets11, groupDatasets12])

# create a new 'TTK MergeTreeTemporalReductionEncoding'
tTKMergeTreeTemporalReductionEncoding1 = TTKMergeTreeTemporalReductionEncoding(registrationName='TTKMergeTreeTemporalReductionEncoding1', Input=groupDatasets13)
tTKMergeTreeTemporalReductionEncoding1.RemovalPercentage = 75.0
tTKMergeTreeTemporalReductionEncoding1.TimeVariable = ['POINTS', 'SegmentationId']
tTKMergeTreeTemporalReductionEncoding1.Epsilon1 = 0.0
tTKMergeTreeTemporalReductionEncoding1.Epsilon2 = 100.0
tTKMergeTreeTemporalReductionEncoding1.Epsilon3 = 100.0
tTKMergeTreeTemporalReductionEncoding1.PersistenceThreshold = 3.0

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tTKMergeTreeTemporalReductionEncoding1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')