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
tTKMergeandContourTreeFTM16 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM16', Input=isabelvti)
tTKMergeandContourTreeFTM16.ScalarField = ['POINTS', 'velocityMag_05']
tTKMergeandContourTreeFTM16.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM16.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM16_1 = FindSource('TTKMergeandContourTreeFTM16')

# find source
tTKMergeandContourTreeFTM16_2 = FindSource('TTKMergeandContourTreeFTM16')

# create a new 'Group Datasets'
groupDatasets5 = GroupDatasets(registrationName='GroupDatasets5', Input=[tTKMergeandContourTreeFTM16, OutputPort(tTKMergeandContourTreeFTM16_1,1), OutputPort(tTKMergeandContourTreeFTM16_2,2)])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram6 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram6', Input=isabelvti)
tTKPersistenceDiagram6.ScalarField = ['POINTS', 'velocityMag_48']
tTKPersistenceDiagram6.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram6.EmbedinDomain = 1

# create a new 'Threshold'
threshold29 = Threshold(registrationName='Threshold29', Input=tTKPersistenceDiagram6)
threshold29.Scalars = ['CELLS', 'PairType']
threshold29.ThresholdRange = [0.0, 1.0]
threshold29.Invert = 1

# create a new 'Cell Data to Point Data'
cellDatatoPointData6 = CellDatatoPointData(registrationName='CellDatatoPointData6', Input=threshold29)
cellDatatoPointData6.CellDataArraytoprocess = ['PairIdentifier', 'PairType', 'Persistence']

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM15 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM15', Input=isabelvti)
tTKMergeandContourTreeFTM15.ScalarField = ['POINTS', 'velocityMag_04']
tTKMergeandContourTreeFTM15.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM15.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM15_1 = FindSource('TTKMergeandContourTreeFTM15')

# find source
tTKMergeandContourTreeFTM15_2 = FindSource('TTKMergeandContourTreeFTM15')

# create a new 'Group Datasets'
groupDatasets4 = GroupDatasets(registrationName='GroupDatasets4', Input=[tTKMergeandContourTreeFTM15, OutputPort(tTKMergeandContourTreeFTM15_1,1), OutputPort(tTKMergeandContourTreeFTM15_2,2)])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram5', Input=isabelvti)
tTKPersistenceDiagram5.ScalarField = ['POINTS', 'velocityMag_45']
tTKPersistenceDiagram5.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram5.EmbedinDomain = 1

# create a new 'Threshold'
threshold23 = Threshold(registrationName='Threshold23', Input=tTKPersistenceDiagram5)
threshold23.Scalars = ['CELLS', 'PairType']
threshold23.ThresholdRange = [0.0, 1.0]
threshold23.Invert = 1

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM14 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM14', Input=isabelvti)
tTKMergeandContourTreeFTM14.ScalarField = ['POINTS', 'velocityMag_03']
tTKMergeandContourTreeFTM14.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM14.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM14_1 = FindSource('TTKMergeandContourTreeFTM14')

# find source
tTKMergeandContourTreeFTM14_2 = FindSource('TTKMergeandContourTreeFTM14')

# create a new 'Group Datasets'
groupDatasets3 = GroupDatasets(registrationName='GroupDatasets3', Input=[tTKMergeandContourTreeFTM14, OutputPort(tTKMergeandContourTreeFTM14_1,1), OutputPort(tTKMergeandContourTreeFTM14_2,2)])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram2', Input=isabelvti)
tTKPersistenceDiagram2.ScalarField = ['POINTS', 'velocityMag_03']
tTKPersistenceDiagram2.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram2.EmbedinDomain = 1

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM13 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM13', Input=isabelvti)
tTKMergeandContourTreeFTM13.ScalarField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM13.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM13.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM13_1 = FindSource('TTKMergeandContourTreeFTM13')

# find source
tTKMergeandContourTreeFTM13_2 = FindSource('TTKMergeandContourTreeFTM13')

# create a new 'Group Datasets'
groupDatasets2 = GroupDatasets(registrationName='GroupDatasets2', Input=[tTKMergeandContourTreeFTM13, OutputPort(tTKMergeandContourTreeFTM13_1,1), OutputPort(tTKMergeandContourTreeFTM13_2,2)])

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
mT_48 = GroupDatasets(registrationName='MT_48', Input=[tTKMergeandContourTreeFTM12, OutputPort(tTKMergeandContourTreeFTM12_1,1), OutputPort(tTKMergeandContourTreeFTM12_2,2)])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=isabelvti)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram1.EmbedinDomain = 1

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairType']
threshold1.ThresholdRange = [0.0, 1.0]
threshold1.Invert = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram4', Input=isabelvti)
tTKPersistenceDiagram4.ScalarField = ['POINTS', 'velocityMag_33']
tTKPersistenceDiagram4.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram4.EmbedinDomain = 1

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=isabelvti)
calculator1.Function = ''

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
mT_45 = GroupDatasets(registrationName='MT_45', Input=[tTKMergeandContourTreeFTM9, OutputPort(tTKMergeandContourTreeFTM9_1,1), OutputPort(tTKMergeandContourTreeFTM9_2,2)])

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
mT_47 = GroupDatasets(registrationName='MT_47', Input=[tTKMergeandContourTreeFTM11, OutputPort(tTKMergeandContourTreeFTM11_1,1), OutputPort(tTKMergeandContourTreeFTM11_2,2)])

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
mT_33 = GroupDatasets(registrationName='MT_33', Input=[tTKMergeandContourTreeFTM8, OutputPort(tTKMergeandContourTreeFTM8_1,1), OutputPort(tTKMergeandContourTreeFTM8_2,2)])

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
mT_02 = GroupDatasets(registrationName='MT_02', Input=[tTKMergeandContourTreeFTM1, OutputPort(tTKMergeandContourTreeFTM1_1,1), OutputPort(tTKMergeandContourTreeFTM1_2,2)])

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
mT_32 = GroupDatasets(registrationName='MT_32', Input=[tTKMergeandContourTreeFTM7, OutputPort(tTKMergeandContourTreeFTM7_1,1), OutputPort(tTKMergeandContourTreeFTM7_2,2)])

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
mT_31 = GroupDatasets(registrationName='MT_31', Input=[tTKMergeandContourTreeFTM6, OutputPort(tTKMergeandContourTreeFTM6_1,1), OutputPort(tTKMergeandContourTreeFTM6_2,2)])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram3', Input=isabelvti)
tTKPersistenceDiagram3.ScalarField = ['POINTS', 'velocityMag_30']
tTKPersistenceDiagram3.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKPersistenceDiagram3.EmbedinDomain = 1

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
mT_30 = GroupDatasets(registrationName='MT_30', Input=[tTKMergeandContourTreeFTM5, OutputPort(tTKMergeandContourTreeFTM5_1,1), OutputPort(tTKMergeandContourTreeFTM5_2,2)])

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
mT_05 = GroupDatasets(registrationName='MT_05', Input=[tTKMergeandContourTreeFTM4, OutputPort(tTKMergeandContourTreeFTM4_1,1), OutputPort(tTKMergeandContourTreeFTM4_2,2)])

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
mT_04 = GroupDatasets(registrationName='MT_04', Input=[tTKMergeandContourTreeFTM3, OutputPort(tTKMergeandContourTreeFTM3_1,1), OutputPort(tTKMergeandContourTreeFTM3_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM24 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM24', Input=isabelvti)
tTKMergeandContourTreeFTM24.ScalarField = ['POINTS', 'velocityMag_48']
tTKMergeandContourTreeFTM24.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM24.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM24_1 = FindSource('TTKMergeandContourTreeFTM24')

# find source
tTKMergeandContourTreeFTM24_2 = FindSource('TTKMergeandContourTreeFTM24')

# create a new 'Group Datasets'
groupDatasets13 = GroupDatasets(registrationName='GroupDatasets13', Input=[tTKMergeandContourTreeFTM24, OutputPort(tTKMergeandContourTreeFTM24_1,1), OutputPort(tTKMergeandContourTreeFTM24_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM23 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM23', Input=isabelvti)
tTKMergeandContourTreeFTM23.ScalarField = ['POINTS', 'velocityMag_47']
tTKMergeandContourTreeFTM23.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM23.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM23_1 = FindSource('TTKMergeandContourTreeFTM23')

# find source
tTKMergeandContourTreeFTM23_2 = FindSource('TTKMergeandContourTreeFTM23')

# create a new 'Group Datasets'
groupDatasets12 = GroupDatasets(registrationName='GroupDatasets12', Input=[tTKMergeandContourTreeFTM23, OutputPort(tTKMergeandContourTreeFTM23_1,1), OutputPort(tTKMergeandContourTreeFTM23_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM22 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM22', Input=isabelvti)
tTKMergeandContourTreeFTM22.ScalarField = ['POINTS', 'velocityMag_46']
tTKMergeandContourTreeFTM22.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM22.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM22_1 = FindSource('TTKMergeandContourTreeFTM22')

# find source
tTKMergeandContourTreeFTM22_2 = FindSource('TTKMergeandContourTreeFTM22')

# create a new 'Group Datasets'
groupDatasets11 = GroupDatasets(registrationName='GroupDatasets11', Input=[tTKMergeandContourTreeFTM22, OutputPort(tTKMergeandContourTreeFTM22_1,1), OutputPort(tTKMergeandContourTreeFTM22_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM21 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM21', Input=isabelvti)
tTKMergeandContourTreeFTM21.ScalarField = ['POINTS', 'velocityMag_45']
tTKMergeandContourTreeFTM21.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM21.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM21_1 = FindSource('TTKMergeandContourTreeFTM21')

# find source
tTKMergeandContourTreeFTM21_2 = FindSource('TTKMergeandContourTreeFTM21')

# create a new 'Group Datasets'
groupDatasets10 = GroupDatasets(registrationName='GroupDatasets10', Input=[tTKMergeandContourTreeFTM21, OutputPort(tTKMergeandContourTreeFTM21_1,1), OutputPort(tTKMergeandContourTreeFTM21_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM20 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM20', Input=isabelvti)
tTKMergeandContourTreeFTM20.ScalarField = ['POINTS', 'velocityMag_33']
tTKMergeandContourTreeFTM20.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM20.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM20_1 = FindSource('TTKMergeandContourTreeFTM20')

# find source
tTKMergeandContourTreeFTM20_2 = FindSource('TTKMergeandContourTreeFTM20')

# create a new 'Group Datasets'
groupDatasets9 = GroupDatasets(registrationName='GroupDatasets9', Input=[tTKMergeandContourTreeFTM20, OutputPort(tTKMergeandContourTreeFTM20_1,1), OutputPort(tTKMergeandContourTreeFTM20_2,2)])

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=isabelvti)
contour1.ContourBy = ['POINTS', 'velocityMag_02']
contour1.Isosurfaces = [1e-05]
contour1.PointMergeMethod = 'Uniform Binning'

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
mT_03 = GroupDatasets(registrationName='MT_03', Input=[tTKMergeandContourTreeFTM2, OutputPort(tTKMergeandContourTreeFTM2_1,1), OutputPort(tTKMergeandContourTreeFTM2_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM19 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM19', Input=isabelvti)
tTKMergeandContourTreeFTM19.ScalarField = ['POINTS', 'velocityMag_32']
tTKMergeandContourTreeFTM19.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM19.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM19_1 = FindSource('TTKMergeandContourTreeFTM19')

# find source
tTKMergeandContourTreeFTM19_2 = FindSource('TTKMergeandContourTreeFTM19')

# create a new 'Group Datasets'
groupDatasets8 = GroupDatasets(registrationName='GroupDatasets8', Input=[tTKMergeandContourTreeFTM19, OutputPort(tTKMergeandContourTreeFTM19_1,1), OutputPort(tTKMergeandContourTreeFTM19_2,2)])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM18 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM18', Input=isabelvti)
tTKMergeandContourTreeFTM18.ScalarField = ['POINTS', 'velocityMag_31']
tTKMergeandContourTreeFTM18.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM18.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM18_1 = FindSource('TTKMergeandContourTreeFTM18')

# find source
tTKMergeandContourTreeFTM18_2 = FindSource('TTKMergeandContourTreeFTM18')

# create a new 'Group Datasets'
groupDatasets7 = GroupDatasets(registrationName='GroupDatasets7', Input=[tTKMergeandContourTreeFTM18, OutputPort(tTKMergeandContourTreeFTM18_1,1), OutputPort(tTKMergeandContourTreeFTM18_2,2)])

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
mT_46 = GroupDatasets(registrationName='MT_46', Input=[tTKMergeandContourTreeFTM10, OutputPort(tTKMergeandContourTreeFTM10_1,1), OutputPort(tTKMergeandContourTreeFTM10_2,2)])

# create a new 'Group Datasets'
mT_all = GroupDatasets(registrationName='MT_all', Input=[mT_02, mT_03, mT_04, mT_05, mT_30, mT_31, mT_32, mT_33, mT_45, mT_46, mT_47, mT_48])

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM17 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM17', Input=isabelvti)
tTKMergeandContourTreeFTM17.ScalarField = ['POINTS', 'velocityMag_30']
tTKMergeandContourTreeFTM17.InputOffsetField = ['POINTS', 'velocityMag_02']
tTKMergeandContourTreeFTM17.TreeType = 'Join Tree'

# find source
tTKMergeandContourTreeFTM17_1 = FindSource('TTKMergeandContourTreeFTM17')

# find source
tTKMergeandContourTreeFTM17_2 = FindSource('TTKMergeandContourTreeFTM17')

# create a new 'Group Datasets'
groupDatasets6 = GroupDatasets(registrationName='GroupDatasets6', Input=[tTKMergeandContourTreeFTM17, OutputPort(tTKMergeandContourTreeFTM17_1,1), OutputPort(tTKMergeandContourTreeFTM17_2,2)])

# create a new 'Cell Data to Point Data'
cellDatatoPointData5 = CellDatatoPointData(registrationName='CellDatatoPointData5', Input=threshold23)
cellDatatoPointData5.CellDataArraytoprocess = ['PairIdentifier', 'PairType', 'Persistence']

# create a new 'Calculator'
calculator10 = Calculator(registrationName='Calculator10', Input=cellDatatoPointData5)
calculator10.CoordinateResults = 1
calculator10.Function = 'iHat*coordsX + jHat*coordsY + kHat*coordsZ'

# create a new 'Cell Data to Point Data'
cellDatatoPointData4 = CellDatatoPointData(registrationName='CellDatatoPointData4', Input=tTKPersistenceDiagram4)
cellDatatoPointData4.CellDataArraytoprocess = ['PairIdentifier', 'PairType', 'Persistence']

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=cellDatatoPointData4)
calculator8.CoordinateResults = 1
calculator8.Function = 'iHat*coordsX + jHat*coordsY + kHat*coordsZ'

# create a new 'Calculator'
calculator9 = Calculator(registrationName='Calculator9', Input=calculator8)
calculator9.Function = 'sqrt(Persistence)'

# create a new 'Glyph'
glyph9 = Glyph(registrationName='Glyph9', Input=calculator9,
    GlyphType='Sphere')
glyph9.OrientationArray = ['POINTS', 'No orientation array']
glyph9.ScaleArray = ['POINTS', 'Result']
glyph9.ScaleFactor = 12.0
glyph9.GlyphTransform = 'Transform2'
glyph9.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph9.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold19 = Threshold(registrationName='Threshold19', Input=glyph9)
threshold19.Scalars = ['POINTS', 'Persistence']
threshold19.ThresholdRange = [17.0, 74.30557414654186]

# create a new 'Threshold'
threshold20 = Threshold(registrationName='Threshold20', Input=threshold19)
threshold20.Scalars = ['POINTS', 'CriticalType']
threshold20.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph10 = Glyph(registrationName='Glyph10', Input=calculator9,
    GlyphType='Sphere')
glyph10.OrientationArray = ['POINTS', 'No orientation array']
glyph10.ScaleArray = ['POINTS', 'Result']
glyph10.ScaleFactor = 6.0
glyph10.GlyphTransform = 'Transform2'
glyph10.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph10.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold21 = Threshold(registrationName='Threshold21', Input=glyph10)
threshold21.Scalars = ['POINTS', 'Persistence']
threshold21.ThresholdRange = [0.0, 17.0]

# create a new 'Threshold'
threshold22 = Threshold(registrationName='Threshold22', Input=threshold21)
threshold22.Scalars = ['POINTS', 'CriticalType']
threshold22.ThresholdRange = [3.0, 3.0]

# create a new 'Calculator'
calculator11 = Calculator(registrationName='Calculator11', Input=calculator10)
calculator11.Function = 'sqrt(Persistence)'

# create a new 'Threshold'
threshold24 = Threshold(registrationName='Threshold24', Input=calculator11)
threshold24.Scalars = ['POINTS', 'Persistence']
threshold24.ThresholdRange = [60.0, 62.60187441514181]

# create a new 'Glyph'
glyph12 = Glyph(registrationName='Glyph12', Input=threshold24,
    GlyphType='Sphere')
glyph12.OrientationArray = ['POINTS', 'No orientation array']
glyph12.ScaleArray = ['POINTS', 'Result']
glyph12.ScaleFactor = 12.0
glyph12.GlyphTransform = 'Transform2'
glyph12.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph12.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold25 = Threshold(registrationName='Threshold25', Input=glyph12)
threshold25.Scalars = ['POINTS', 'CriticalType']
threshold25.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph13 = Glyph(registrationName='Glyph13', Input=calculator11,
    GlyphType='Sphere')
glyph13.OrientationArray = ['POINTS', 'No orientation array']
glyph13.ScaleArray = ['POINTS', 'Result']
glyph13.ScaleFactor = 6.0
glyph13.GlyphTransform = 'Transform2'
glyph13.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph13.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold28 = Threshold(registrationName='Threshold28', Input=glyph13)
threshold28.Scalars = ['POINTS', 'CriticalType']
threshold28.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph11 = Glyph(registrationName='Glyph11', Input=calculator11,
    GlyphType='Sphere')
glyph11.OrientationArray = ['POINTS', 'No orientation array']
glyph11.ScaleArray = ['POINTS', 'Result']
glyph11.ScaleFactor = 12.0
glyph11.GlyphTransform = 'Transform2'
glyph11.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph11.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold26 = Threshold(registrationName='Threshold26', Input=glyph11)
threshold26.Scalars = ['POINTS', 'Persistence']
threshold26.ThresholdRange = [20.0, 22.545888895088975]

# create a new 'Threshold'
threshold27 = Threshold(registrationName='Threshold27', Input=threshold26)
threshold27.Scalars = ['POINTS', 'CriticalType']
threshold27.ThresholdRange = [3.0, 3.0]

# create a new 'Threshold'
threshold8 = Threshold(registrationName='Threshold8', Input=tTKPersistenceDiagram2)
threshold8.Scalars = ['CELLS', 'PairType']
threshold8.ThresholdRange = [0.0, 1.0]
threshold8.Invert = 1

# create a new 'Cell Data to Point Data'
cellDatatoPointData2 = CellDatatoPointData(registrationName='CellDatatoPointData2', Input=threshold8)
cellDatatoPointData2.CellDataArraytoprocess = ['PairIdentifier', 'PairType', 'Persistence']

# create a new 'Cell Data to Point Data'
cellDatatoPointData3 = CellDatatoPointData(registrationName='CellDatatoPointData3', Input=tTKPersistenceDiagram3)
cellDatatoPointData3.CellDataArraytoprocess = ['PairIdentifier', 'PairType', 'Persistence']

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=cellDatatoPointData3)
calculator6.CoordinateResults = 1
calculator6.Function = 'iHat*coordsX + jHat*coordsY + kHat*coordsZ'

# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=calculator6)
calculator7.Function = 'sqrt(Persistence)'

# create a new 'Glyph'
glyph8 = Glyph(registrationName='Glyph8', Input=calculator7,
    GlyphType='Sphere')
glyph8.OrientationArray = ['POINTS', 'No orientation array']
glyph8.ScaleArray = ['POINTS', 'Result']
glyph8.ScaleFactor = 6.0
glyph8.GlyphTransform = 'Transform2'
glyph8.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph8.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold17 = Threshold(registrationName='Threshold17', Input=glyph8)
threshold17.Scalars = ['POINTS', 'Persistence']
threshold17.ThresholdRange = [0.0, 13.0]

# create a new 'Threshold'
threshold18 = Threshold(registrationName='Threshold18', Input=threshold17)
threshold18.Scalars = ['POINTS', 'CriticalType']
threshold18.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph7 = Glyph(registrationName='Glyph7', Input=calculator7,
    GlyphType='Sphere')
glyph7.OrientationArray = ['POINTS', 'No orientation array']
glyph7.ScaleArray = ['POINTS', 'Result']
glyph7.ScaleFactor = 12.0
glyph7.GlyphTransform = 'Transform2'
glyph7.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph7.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold15 = Threshold(registrationName='Threshold15', Input=glyph7)
threshold15.Scalars = ['POINTS', 'Persistence']
threshold15.ThresholdRange = [13.0, 78.65940926169091]

# create a new 'Threshold'
threshold16 = Threshold(registrationName='Threshold16', Input=threshold15)
threshold16.Scalars = ['POINTS', 'CriticalType']
threshold16.ThresholdRange = [3.0, 3.0]

# create a new 'Calculator'
calculator12 = Calculator(registrationName='Calculator12', Input=cellDatatoPointData6)
calculator12.CoordinateResults = 1
calculator12.Function = 'iHat*coordsX + jHat*coordsY + kHat*coordsZ'

# create a new 'Calculator'
calculator13 = Calculator(registrationName='Calculator13', Input=calculator12)
calculator13.Function = 'sqrt(Persistence)'

# create a new 'Glyph'
glyph15 = Glyph(registrationName='Glyph15', Input=calculator13,
    GlyphType='Sphere')
glyph15.OrientationArray = ['POINTS', 'No orientation array']
glyph15.ScaleArray = ['POINTS', 'Result']
glyph15.ScaleFactor = 6.0
glyph15.GlyphTransform = 'Transform2'
glyph15.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph15.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold32 = Threshold(registrationName='Threshold32', Input=glyph15)
threshold32.Scalars = ['POINTS', 'CriticalType']
threshold32.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph14 = Glyph(registrationName='Glyph14', Input=calculator13,
    GlyphType='Sphere')
glyph14.OrientationArray = ['POINTS', 'No orientation array']
glyph14.ScaleArray = ['POINTS', 'Result']
glyph14.ScaleFactor = 12.0
glyph14.GlyphTransform = 'Transform2'
glyph14.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph14.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold30 = Threshold(registrationName='Threshold30', Input=glyph14)
threshold30.Scalars = ['POINTS', 'Persistence']
threshold30.ThresholdRange = [20.0, 56.14129124616043]

# create a new 'Threshold'
threshold31 = Threshold(registrationName='Threshold31', Input=threshold30)
threshold31.Scalars = ['POINTS', 'CriticalType']
threshold31.ThresholdRange = [3.0, 3.0]

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=threshold1)
cellDatatoPointData1.CellDataArraytoprocess = ['PairIdentifier', 'PairType', 'Persistence']

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=cellDatatoPointData1)
calculator2.CoordinateResults = 1
calculator2.Function = 'iHat*coordsX + jHat*coordsY + kHat*coordsZ'

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.Function = 'sqrt(Persistence)'

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=calculator3,
    GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'Result']
glyph1.ScaleFactor = 12.0
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph1.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=glyph1)
threshold3.Scalars = ['POINTS', 'Persistence']
threshold3.ThresholdRange = [12.0, 13.66095652516955]

# create a new 'Threshold'
threshold5 = Threshold(registrationName='Threshold5', Input=threshold3)
threshold5.Scalars = ['POINTS', 'CriticalType']
threshold5.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph3 = Glyph(registrationName='Glyph3', Input=calculator3,
    GlyphType='Sphere')
glyph3.OrientationArray = ['POINTS', 'No orientation array']
glyph3.ScaleArray = ['POINTS', 'Result']
glyph3.ScaleFactor = 6.0
glyph3.GlyphTransform = 'Transform2'
glyph3.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph3.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold6 = Threshold(registrationName='Threshold6', Input=glyph3)
threshold6.Scalars = ['POINTS', 'Persistence']
threshold6.ThresholdRange = [0.0, 12.0]

# create a new 'Threshold'
threshold7 = Threshold(registrationName='Threshold7', Input=threshold6)
threshold7.Scalars = ['POINTS', 'CriticalType']
threshold7.ThresholdRange = [3.0, 3.0]

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=calculator3)
threshold2.Scalars = ['POINTS', 'Persistence']
threshold2.ThresholdRange = [60.0, 68.2454776917825]

# create a new 'Glyph'
glyph2 = Glyph(registrationName='Glyph2', Input=threshold2,
    GlyphType='Sphere')
glyph2.OrientationArray = ['POINTS', 'No orientation array']
glyph2.ScaleArray = ['POINTS', 'Result']
glyph2.ScaleFactor = 12.0
glyph2.GlyphTransform = 'Transform2'
glyph2.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph2.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=glyph2)
threshold4.Scalars = ['POINTS', 'CriticalType']
threshold4.ThresholdRange = [3.0, 3.0]

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=cellDatatoPointData2)
calculator4.CoordinateResults = 1
calculator4.Function = 'iHat*coordsX + jHat*coordsY + kHat*coordsZ'

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.Function = 'sqrt(Persistence)'

# create a new 'Glyph'
glyph5 = Glyph(registrationName='Glyph5', Input=calculator5,
    GlyphType='Sphere')
glyph5.OrientationArray = ['POINTS', 'No orientation array']
glyph5.ScaleArray = ['POINTS', 'Result']
glyph5.ScaleFactor = 12.0
glyph5.GlyphTransform = 'Transform2'
glyph5.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph5.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold11 = Threshold(registrationName='Threshold11', Input=glyph5)
threshold11.Scalars = ['POINTS', 'Persistence']
threshold11.ThresholdRange = [12.0, 13.60996706488422]

# create a new 'Threshold'
threshold12 = Threshold(registrationName='Threshold12', Input=threshold11)
threshold12.Scalars = ['POINTS', 'CriticalType']
threshold12.ThresholdRange = [3.0, 3.0]

# create a new 'Threshold'
threshold9 = Threshold(registrationName='Threshold9', Input=calculator5)
threshold9.Scalars = ['POINTS', 'Persistence']
threshold9.ThresholdRange = [70.0, 75.978892536971]

# create a new 'Glyph'
glyph4 = Glyph(registrationName='Glyph4', Input=threshold9,
    GlyphType='Sphere')
glyph4.OrientationArray = ['POINTS', 'No orientation array']
glyph4.ScaleArray = ['POINTS', 'Result']
glyph4.ScaleFactor = 12.0
glyph4.GlyphTransform = 'Transform2'
glyph4.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph4.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold10 = Threshold(registrationName='Threshold10', Input=glyph4)
threshold10.Scalars = ['POINTS', 'CriticalType']
threshold10.ThresholdRange = [3.0, 3.0]

# create a new 'Glyph'
glyph6 = Glyph(registrationName='Glyph6', Input=calculator5,
    GlyphType='Sphere')
glyph6.OrientationArray = ['POINTS', 'No orientation array']
glyph6.ScaleArray = ['POINTS', 'Result']
glyph6.ScaleFactor = 6.0
glyph6.GlyphTransform = 'Transform2'
glyph6.GlyphMode = 'All Points'

# init the 'Sphere' selected for 'GlyphType'
glyph6.GlyphType.ThetaResolution = 64

# create a new 'Threshold'
threshold13 = Threshold(registrationName='Threshold13', Input=glyph6)
threshold13.Scalars = ['POINTS', 'Persistence']
threshold13.ThresholdRange = [0.0002723664241370827, 12.0]

# create a new 'Threshold'
threshold14 = Threshold(registrationName='Threshold14', Input=threshold13)
threshold14.Scalars = ['POINTS', 'CriticalType']
threshold14.ThresholdRange = [3.0, 3.0]

# create a new 'Group Datasets'
mt_JT_all = GroupDatasets(registrationName='mt_JT_all', Input=[groupDatasets2, groupDatasets3, groupDatasets4, groupDatasets5, groupDatasets6, groupDatasets7, groupDatasets8, groupDatasets9, groupDatasets10, groupDatasets11, groupDatasets12, groupDatasets13])

# create a new 'TTK MergeTreeClustering'
tTKMergeTreeClustering1 = TTKMergeTreeClustering(registrationName='TTKMergeTreeClustering1', Input=mT_all,
    OptionalInputclustering=mt_JT_all)
tTKMergeTreeClustering1.ComputeBarycenter = 1
tTKMergeTreeClustering1.NumberOfClusters = 3
tTKMergeTreeClustering1.Deterministic = 1
tTKMergeTreeClustering1.DimensionSpacing = 0.1
tTKMergeTreeClustering1.PersistenceThreshold = 2.0
tTKMergeTreeClustering1.ImportantPairs = 34.0
tTKMergeTreeClustering1.MaximumNumberofImportantPairs = 3
tTKMergeTreeClustering1.MinimumNumberofImportantPairs = 2
tTKMergeTreeClustering1.ImportantPairsSpacing = 15.0
tTKMergeTreeClustering1.NonImportantPairsProximity = 0.15

# find source
tTKMergeTreeClustering1_1 = FindSource('TTKMergeTreeClustering1')

# create a new 'Extract Block'
arcs = ExtractBlock(registrationName='Arcs', Input=OutputPort(tTKMergeTreeClustering1_1,1))
arcs.BlockIndices = [9, 6, 3]

# create a new 'Threshold'
threshold55 = Threshold(registrationName='Threshold55', Input=arcs)
threshold55.Scalars = ['CELLS', 'isImportantPair']
threshold55.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold56 = Threshold(registrationName='Threshold56', Input=threshold55)
threshold56.Scalars = ['CELLS', 'isDummyArc']

# create a new 'Extract Surface'
extractSurface9 = ExtractSurface(registrationName='ExtractSurface9', Input=threshold56)

# create a new 'Tube'
tube9 = Tube(registrationName='Tube9', Input=extractSurface9)
tube9.Scalars = ['POINTS', '']
tube9.Vectors = ['POINTS', '1']
tube9.Radius = 2.0

# create a new 'Threshold'
threshold36 = Threshold(registrationName='Threshold36', Input=threshold55)
threshold36.Scalars = ['CELLS', 'isDummyArc']
threshold36.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(registrationName='ExtractSurface2', Input=threshold36)

# create a new 'Tube'
tube2 = Tube(registrationName='Tube2', Input=extractSurface2)
tube2.Scalars = ['POINTS', '']
tube2.Vectors = ['POINTS', '1']

# create a new 'Threshold'
threshold59 = Threshold(registrationName='Threshold59', Input=arcs)
threshold59.Scalars = ['CELLS', 'isImportantPair']

# create a new 'Threshold'
threshold60 = Threshold(registrationName='Threshold60', Input=threshold59)
threshold60.Scalars = ['CELLS', 'isDummyArc']

# create a new 'Extract Surface'
extractSurface11 = ExtractSurface(registrationName='ExtractSurface11', Input=threshold60)

# create a new 'Tube'
tube11 = Tube(registrationName='Tube11', Input=extractSurface11)
tube11.Scalars = ['POINTS', '']
tube11.Vectors = ['POINTS', '1']
tube11.Radius = -2e+297

# create a new 'Threshold'
threshold61 = Threshold(registrationName='Threshold61', Input=threshold59)
threshold61.Scalars = ['CELLS', 'isDummyArc']
threshold61.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface12 = ExtractSurface(registrationName='ExtractSurface12', Input=threshold61)

# create a new 'Tube'
tube12 = Tube(registrationName='Tube12', Input=extractSurface12)
tube12.Scalars = ['POINTS', '']
tube12.Vectors = ['POINTS', '1']
tube12.Radius = 0.5

# create a new 'Group Datasets'
groupDatasets14 = GroupDatasets(registrationName='GroupDatasets14', Input=[tTKMergeTreeClustering1, OutputPort(tTKMergeTreeClustering1_1,1)])

# create a new 'TTK FlattenMultiBlock'
tTKFlattenMultiBlock2 = TTKFlattenMultiBlock(registrationName='TTKFlattenMultiBlock2', Input=groupDatasets14)

# create a new 'TTK MergeTreeDistanceMatrix'
tTKMergeTreeDistanceMatrix2 = TTKMergeTreeDistanceMatrix(registrationName='TTKMergeTreeDistanceMatrix2', Input=tTKFlattenMultiBlock2)
tTKMergeTreeDistanceMatrix2.PersistenceThreshold = 2.0

# create a new 'TTK DimensionReduction'
tTKDimensionReduction2 = TTKDimensionReduction(registrationName='TTKDimensionReduction2', Input=tTKMergeTreeDistanceMatrix2,
    ModulePath='default')
tTKDimensionReduction2.InputColumns = ['Tree00', 'Tree01', 'Tree02', 'Tree03', 'Tree04', 'Tree05', 'Tree06', 'Tree07', 'Tree08', 'Tree09', 'Tree10', 'Tree11', 'Tree12', 'Tree13', 'Tree14']
tTKDimensionReduction2.InputIsaDistanceMatrix = 1
tTKDimensionReduction2.UseAllCores = 0

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=tTKDimensionReduction2)
tableToPoints1.XColumn = 'Component_0'
tableToPoints1.YColumn = 'Component_1'
tableToPoints1.ZColumn = 'Component_0'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=tableToPoints1)
tTKIcospheresFromPoints1.Radius = 0.4

# create a new 'Threshold'
threshold33 = Threshold(registrationName='Threshold33', Input=tTKIcospheresFromPoints1)
threshold33.Scalars = ['POINTS', 'treeID']
threshold33.ThresholdRange = [0.0, 11.0]

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints2', Input=tableToPoints1)
tTKIcospheresFromPoints2.Radius = 0.8

# create a new 'Threshold'
threshold34 = Threshold(registrationName='Threshold34', Input=tTKIcospheresFromPoints2)
threshold34.Scalars = ['POINTS', 'treeID']
threshold34.ThresholdRange = [12.0, 14.0]

# create a new 'Extract Block'
nodes = ExtractBlock(registrationName='Nodes', Input=tTKMergeTreeClustering1)
nodes.BlockIndices = [14, 29, 8, 11, 26, 5, 20, 32, 23, 35, 2, 17]

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints6 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints6', Input=nodes)
tTKIcospheresFromPoints6.Radius = 2.0

# create a new 'Threshold'
threshold49 = Threshold(registrationName='Threshold49', Input=tTKIcospheresFromPoints6)
threshold49.Scalars = ['POINTS', 'isDummyNode']

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints5 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints5', Input=nodes)
tTKIcospheresFromPoints5.Radius = 5.0

# create a new 'Threshold'
threshold44 = Threshold(registrationName='Threshold44', Input=tTKIcospheresFromPoints5)
threshold44.Scalars = ['POINTS', 'isImportantPair']
threshold44.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold45 = Threshold(registrationName='Threshold45', Input=threshold44)
threshold45.Scalars = ['POINTS', 'isDummyNode']

# create a new 'Extract Block'
arcs_1 = ExtractBlock(registrationName='Arcs', Input=tTKMergeTreeClustering1)
arcs_1.BlockIndices = [15, 33, 12, 27, 24, 9, 6, 21, 18, 36, 3, 30]

# create a new 'Threshold'
threshold50 = Threshold(registrationName='Threshold50', Input=arcs_1)
threshold50.Scalars = ['CELLS', 'isImportantPair']

# create a new 'Threshold'
threshold52 = Threshold(registrationName='Threshold52', Input=threshold50)
threshold52.Scalars = ['CELLS', 'isDummyArc']
threshold52.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface8 = ExtractSurface(registrationName='ExtractSurface8', Input=threshold52)

# create a new 'Tube'
tube8 = Tube(registrationName='Tube8', Input=extractSurface8)
tube8.Scalars = ['POINTS', '']
tube8.Vectors = ['POINTS', '1']
tube8.Radius = 0.5

# create a new 'Threshold'
threshold51 = Threshold(registrationName='Threshold51', Input=threshold50)
threshold51.Scalars = ['CELLS', 'isDummyArc']

# create a new 'Extract Surface'
extractSurface7 = ExtractSurface(registrationName='ExtractSurface7', Input=threshold51)

# create a new 'Tube'
tube7 = Tube(registrationName='Tube7', Input=extractSurface7)
tube7.Scalars = ['POINTS', '']
tube7.Vectors = ['POINTS', '1']
tube7.Radius = -2e+297

# create a new 'Threshold'
threshold46 = Threshold(registrationName='Threshold46', Input=arcs_1)
threshold46.Scalars = ['CELLS', 'isImportantPair']
threshold46.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold35 = Threshold(registrationName='Threshold35', Input=threshold46)
threshold35.Scalars = ['CELLS', 'isDummyArc']
threshold35.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=threshold35)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=extractSurface1)
tube1.Scalars = ['POINTS', '']
tube1.Vectors = ['POINTS', '1']

# create a new 'Threshold'
threshold47 = Threshold(registrationName='Threshold47', Input=threshold46)
threshold47.Scalars = ['CELLS', 'isDummyArc']

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(registrationName='ExtractSurface5', Input=threshold47)

# create a new 'Tube'
tube5 = Tube(registrationName='Tube5', Input=extractSurface5)
tube5.Scalars = ['POINTS', '']
tube5.Vectors = ['POINTS', '1']
tube5.Radius = 2.0

# create a new 'Extract Block'
nodes_1 = ExtractBlock(registrationName='Nodes', Input=OutputPort(tTKMergeTreeClustering1_1,1))
nodes_1.BlockIndices = [8, 5, 2]

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints7 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints7', Input=nodes_1)
tTKIcospheresFromPoints7.Radius = 5.0

# create a new 'Threshold'
threshold53 = Threshold(registrationName='Threshold53', Input=tTKIcospheresFromPoints7)
threshold53.Scalars = ['POINTS', 'isImportantPair']
threshold53.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold54 = Threshold(registrationName='Threshold54', Input=threshold53)
threshold54.Scalars = ['POINTS', 'isDummyNode']

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints8 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints8', Input=nodes_1)
tTKIcospheresFromPoints8.Radius = 2.0

# create a new 'Threshold'
threshold58 = Threshold(registrationName='Threshold58', Input=tTKIcospheresFromPoints8)
threshold58.Scalars = ['POINTS', 'isDummyNode']

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')