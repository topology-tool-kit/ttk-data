# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1419, 421]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [4.5, 3.9796665557660162, 1.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [56.40171081420424, 4.379638901312168, 24.515679322623463]
renderView1.CameraFocalPoint = [56.40171081420424, 4.379638901312168, 1.0]
renderView1.CameraParallelScale = 6.086305667218497
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.EnvironmentNorth = [1.0, 0.0, 0.0]
renderView1.EnvironmentEast = [0.0, 1.0, 0.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1419, 422]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [4.5, 3.9796665557660162, 1.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [56.40171081420424, 4.379638901312168, 24.515679322623463]
renderView2.CameraFocalPoint = [56.40171081420424, 4.379638901312168, 1.0]
renderView2.CameraParallelScale = 6.086305667218497
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.EnvironmentNorth = [1.0, 0.0, 0.0]
renderView2.EnvironmentEast = [0.0, 1.0, 0.0]
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView2)
layout1.AssignView(2, renderView1)
layout1.SetSize(1419, 844)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
viscousFingerscdb = TTKCinemaReader(registrationName='ViscousFingers.cdb', DatabasePath='ViscousFingers.cdb')

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(registrationName='TTKCinemaQuery1', InputTable=viscousFingerscdb)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE Sim='run01'
ORDER BY Time
LIMIT 100 OFFSET 20"""

# create a new 'TTK ForEach'
tTKForEach1 = TTKForEach(registrationName='TTKForEach1', Input=tTKCinemaQuery1)
tTKForEach1.InputArray = ['POINTS', '']

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=tTKForEach1)

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(registrationName='MergeBlocks1', Input=tTKCinemaProductReader1)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=mergeBlocks1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'ImageFile']
clip1.Value = 38.38161849975586

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [31.5, 31.5, 50.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=clip1)
threshold2.Scalars = ['POINTS', 'ImageFile']
threshold2.ThresholdRange = [28.0, 2000.0]

# create a new 'Connectivity'
connectivity2 = Connectivity(registrationName='Connectivity2', Input=threshold2)

# create a new 'TTK BlockAggregator'
tTKBlockAggregator6 = TTKBlockAggregator(registrationName='TTKBlockAggregator6', Input=connectivity2)
tTKBlockAggregator6.ForceReset = 1

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=clip1)
threshold3.Scalars = ['POINTS', 'ImageFile']
threshold3.ThresholdRange = [32.0, 2000.0]

# create a new 'Connectivity'
connectivity3 = Connectivity(registrationName='Connectivity3', Input=threshold3)

# create a new 'TTK BlockAggregator'
tTKBlockAggregator7 = TTKBlockAggregator(registrationName='TTKBlockAggregator7', Input=connectivity3)
tTKBlockAggregator7.ForceReset = 1

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=clip1)
threshold1.Scalars = ['POINTS', 'ImageFile']
threshold1.ThresholdRange = [20.0, 2000.0]

# create a new 'Connectivity'
connectivity1 = Connectivity(registrationName='Connectivity1', Input=threshold1)

# create a new 'TTK BlockAggregator'
tTKBlockAggregator5 = TTKBlockAggregator(registrationName='TTKBlockAggregator5', Input=connectivity1)
tTKBlockAggregator5.ForceReset = 1

# create a new 'TTK BlockAggregator'
tTKBlockAggregator1 = TTKBlockAggregator(registrationName='TTKBlockAggregator1', Input=[tTKBlockAggregator5, tTKBlockAggregator6, tTKBlockAggregator7])
tTKBlockAggregator1.ForceReset = 1
tTKBlockAggregator1.FlattenInput = 0

# create a new 'TTK ArrayEditor'
tTKArrayEditor1 = TTKArrayEditor(registrationName='TTKArrayEditor1', Target=tTKBlockAggregator1,
    Source=tTKCinemaProductReader1)
tTKArrayEditor1.EditorMode = 'Add Arrays from Source'
tTKArrayEditor1.TargetAttributeType = 'Field Data'
tTKArrayEditor1.SourceFieldDataArrays = ['_ttk_IterationInfo']
tTKArrayEditor1.TargetArray = ['POINTS', 'RegionId']

# create a new 'TTK TrackingFromOverlap'
tTKTrackingFromOverlap1 = TTKTrackingFromOverlap(registrationName='TTKTrackingFromOverlap1', Input=tTKArrayEditor1)
tTKTrackingFromOverlap1.Labels = 'RegionId'

# create a new 'TTK EndFor'
tTKEndFor1 = TTKEndFor(registrationName='TTKEndFor1', Data=tTKTrackingFromOverlap1,
    For=tTKForEach1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=tTKEndFor1)
calculator1.ResultArrayName = 'Size'
calculator1.Function = 'Size/6000'
calculator1.ResultArrayType = 'Float'

# create a new 'TTK PlanarGraphLayout'
tTKPlanarGraphLayout1 = TTKPlanarGraphLayout(registrationName='TTKPlanarGraphLayout1', Input=calculator1)
tTKPlanarGraphLayout1.SequenceArray = ['POINTS', 'SequenceIndex']
tTKPlanarGraphLayout1.UseSizes = 1
tTKPlanarGraphLayout1.SizeArray = ['POINTS', 'Size']
tTKPlanarGraphLayout1.UseBranches = 1
tTKPlanarGraphLayout1.BranchArray = ['POINTS', 'BranchId']
tTKPlanarGraphLayout1.UseLevels = 1
tTKPlanarGraphLayout1.LevelArray = ['POINTS', 'LevelIndex']

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=tTKPlanarGraphLayout1)
calculator2.CoordinateResults = 1
calculator2.Function = 'iHat*SequenceIndex+jHat*Layout_Y+kHat*LevelIndex'

# create a new 'TTK MeshGraph'
tTKMeshGraph1 = TTKMeshGraph(registrationName='TTKMeshGraph1', Input=calculator2)
tTKMeshGraph1.SizeArray = ['POINTS', 'Size']

# create a new 'Threshold'
threshold5 = Threshold(registrationName='Threshold5', Input=tTKMeshGraph1)
threshold5.Scalars = ['POINTS', 'LevelIndex']
threshold5.ThresholdRange = [2.0, 2.0]

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=threshold5)
calculator3.CoordinateResults = 1
calculator3.Function = 'coords+kHat*Size/100'

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=tTKMeshGraph1)
threshold4.Scalars = ['POINTS', 'LevelIndex']

# create a new 'Threshold'
threshold6 = Threshold(registrationName='Threshold6', Input=tTKMeshGraph1)
threshold6.Scalars = ['POINTS', 'LevelIndex']
threshold6.ThresholdRange = [1.0, 1.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from threshold4
threshold4Display = Show(threshold4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold4Display.Representation = 'Surface'
threshold4Display.ColorArrayName = [None, '']
threshold4Display.Opacity = 0.04
threshold4Display.NonlinearSubdivisionLevel = 3
threshold4Display.OSPRayScaleArray = 'BranchId'
threshold4Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold4Display.SelectOrientationVectors = 'BranchId'
threshold4Display.ScaleFactor = 7.800000000000001
threshold4Display.SelectScaleArray = 'BranchId'
threshold4Display.GlyphType = 'Arrow'
threshold4Display.GlyphTableIndexArray = 'BranchId'
threshold4Display.GaussianRadius = 0.39
threshold4Display.SetScaleArray = ['POINTS', 'BranchId']
threshold4Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold4Display.OpacityArray = ['POINTS', 'BranchId']
threshold4Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold4Display.DataAxesGrid = 'GridAxesRepresentation'
threshold4Display.PolarAxes = 'PolarAxesRepresentation'
threshold4Display.ScalarOpacityUnitDistance = 8.07970446854871
threshold4Display.OpacityArrayName = [None, '']

# show data from threshold6
threshold6Display = Show(threshold6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold6Display.Representation = 'Surface'
threshold6Display.ColorArrayName = ['POINTS', '']
threshold6Display.Opacity = 0.1
threshold6Display.NonlinearSubdivisionLevel = 3
threshold6Display.OSPRayScaleArray = 'BranchId'
threshold6Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display.SelectOrientationVectors = 'BranchId'
threshold6Display.ScaleFactor = 7.1000000000000005
threshold6Display.SelectScaleArray = 'BranchId'
threshold6Display.GlyphType = 'Arrow'
threshold6Display.GlyphTableIndexArray = 'BranchId'
threshold6Display.GaussianRadius = 0.355
threshold6Display.SetScaleArray = ['POINTS', 'BranchId']
threshold6Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display.OpacityArray = ['POINTS', 'BranchId']
threshold6Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display.PolarAxes = 'PolarAxesRepresentation'
threshold6Display.ScalarOpacityUnitDistance = 6.837095335468346
threshold6Display.OpacityArrayName = [None, '']

# show data from calculator3
calculator3Display = Show(calculator3, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'BranchId'
branchIdLUT = GetColorTransferFunction('BranchId')
branchIdLUT.AutomaticRescaleRangeMode = 'Never'
branchIdLUT.InterpretValuesAsCategories = 1
branchIdLUT.AnnotationsInitialized = 1
branchIdLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 60.0, 0.865003, 0.865003, 0.865003, 120.0, 0.705882, 0.0156863, 0.14902]
branchIdLUT.NanColor = [1.0, 1.0, 0.6]
branchIdLUT.ScalarRangeInitialized = 1.0
branchIdLUT.Annotations = ['0', '0', '1', '1', '10', '10', '100', '100', '101', '101', '102', '102', '103', '103', '104', '104', '105', '105', '106', '106', '107', '107', '11', '11', '12', '12', '13', '13', '14', '14', '15', '15', '16', '16', '19', '19', '2', '2', '21', '21', '22', '22', '23', '23', '24', '24', '25', '25', '26', '26', '27', '27', '29', '29', '3', '3', '30', '30', '31', '31', '32', '32', '33', '33', '36', '36', '4', '4', '40', '40', '41', '41', '42', '42', '43', '43', '44', '44', '45', '45', '46', '46', '47', '47', '48', '48', '49', '49', '5', '5', '50', '50', '51', '51', '52', '52', '53', '53', '54', '54', '55', '55', '56', '56', '57', '57', '58', '58', '59', '59', '6', '6', '60', '60', '61', '61', '62', '62', '63', '63', '64', '64', '65', '65', '66', '66', '67', '67', '68', '68', '69', '69', '7', '7', '70', '70', '71', '71', '72', '72', '73', '73', '74', '74', '75', '75', '76', '76', '77', '77', '78', '78', '79', '79', '80', '80', '81', '81', '82', '82', '83', '83', '84', '84', '85', '85', '86', '86', '87', '87', '88', '88', '89', '89', '9', '9', '90', '90', '91', '91', '92', '92', '93', '93', '94', '94', '95', '95', '96', '96', '97', '97', '98', '98', '99', '99', '17', '17', '18', '18', '20', '20', '35', '35', '37', '37', '38', '38', '39', '39', '8', '8']
branchIdLUT.IndexedColors = [0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883]
branchIdLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# get opacity transfer function/opacity map for 'BranchId'
branchIdPWF = GetOpacityTransferFunction('BranchId')
branchIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 120.0, 1.0, 0.5, 0.0]
branchIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['CELLS', 'BranchId']
calculator3Display.LookupTable = branchIdLUT
calculator3Display.NonlinearSubdivisionLevel = 3
calculator3Display.OSPRayScaleArray = 'BranchId'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'BranchId'
calculator3Display.ScaleFactor = 7.1000000000000005
calculator3Display.SelectScaleArray = 'BranchId'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'BranchId'
calculator3Display.GaussianRadius = 0.355
calculator3Display.SetScaleArray = ['POINTS', 'BranchId']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'BranchId']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityFunction = branchIdPWF
calculator3Display.ScalarOpacityUnitDistance = 7.41816737330701
calculator3Display.OpacityArrayName = [None, '']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tTKMeshGraph1
tTKMeshGraph1Display = Show(tTKMeshGraph1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'LevelIndex'
levelIndexLUT = GetColorTransferFunction('LevelIndex')
levelIndexLUT.InterpretValuesAsCategories = 1
levelIndexLUT.AnnotationsInitialized = 1
levelIndexLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
levelIndexLUT.ScalarRangeInitialized = 1.0
levelIndexLUT.Annotations = ['0', '0', '1', '1', '2', '2']
levelIndexLUT.ActiveAnnotatedValues = ['0', '1', '2', '0', '1', '2', '1']
levelIndexLUT.IndexedColors = [0.19215686274509805, 0.5098039215686274, 0.7411764705882353, 0.4196078431372549, 0.6823529411764706, 0.8392156862745098, 0.6196078431372549, 0.792156862745098, 0.8823529411764706]
levelIndexLUT.IndexedOpacities = [1.0, 1.0, 1.0]

# get opacity transfer function/opacity map for 'LevelIndex'
levelIndexPWF = GetOpacityTransferFunction('LevelIndex')
levelIndexPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
levelIndexPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKMeshGraph1Display.Representation = 'Surface'
tTKMeshGraph1Display.ColorArrayName = ['POINTS', 'LevelIndex']
tTKMeshGraph1Display.LookupTable = levelIndexLUT
tTKMeshGraph1Display.NonlinearSubdivisionLevel = 3
tTKMeshGraph1Display.OSPRayScaleArray = 'BranchId'
tTKMeshGraph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMeshGraph1Display.SelectOrientationVectors = 'BranchId'
tTKMeshGraph1Display.ScaleFactor = 7.800000000000001
tTKMeshGraph1Display.SelectScaleArray = 'BranchId'
tTKMeshGraph1Display.GlyphType = 'Arrow'
tTKMeshGraph1Display.GlyphTableIndexArray = 'BranchId'
tTKMeshGraph1Display.GaussianRadius = 0.39
tTKMeshGraph1Display.SetScaleArray = ['POINTS', 'BranchId']
tTKMeshGraph1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMeshGraph1Display.OpacityArray = ['POINTS', 'BranchId']
tTKMeshGraph1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMeshGraph1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMeshGraph1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMeshGraph1Display.ScalarOpacityFunction = levelIndexPWF
tTKMeshGraph1Display.ScalarOpacityUnitDistance = 5.059614262060725
tTKMeshGraph1Display.OpacityArrayName = [None, '']

# setup the color legend parameters for each legend in this view

# get color legend/bar for levelIndexLUT in view renderView2
levelIndexLUTColorBar = GetScalarBar(levelIndexLUT, renderView2)
levelIndexLUTColorBar.AutoOrient = 0
levelIndexLUTColorBar.Orientation = 'Horizontal'
levelIndexLUTColorBar.WindowLocation = 'LowerCenter'
levelIndexLUTColorBar.Title = 'LevelIndex'
levelIndexLUTColorBar.ComponentTitle = ''
levelIndexLUTColorBar.TitleFontSize = 24
levelIndexLUTColorBar.LabelFontSize = 24

# set color bar visibility
levelIndexLUTColorBar.Visibility = 1

# show color legend
tTKMeshGraph1Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------
