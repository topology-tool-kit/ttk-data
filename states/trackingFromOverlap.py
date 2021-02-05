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
renderView1.ViewSize = [705, 422]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [30.754851818084717, 28.828651666641235, 28.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-67.08672888944989, -17.58915059577257, 58.41779900266543]
renderView1.CameraFocalPoint = [30.754851818084685, 28.828651666641235, 28.00000000000001]
renderView1.CameraViewUp = [0.2766548275634554, 0.04586422275771819, 0.9598742518979585]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 42.62464783834721
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.EnvironmentNorth = [1.0, 0.0, 0.0]
renderView1.EnvironmentEast = [0.0, 1.0, 0.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1419, 421]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [62.5, 5.302777573466301, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [63.33864364990629, 5.722099398419445, 138.55747653154634]
renderView2.CameraFocalPoint = [63.33864364990629, 5.722099398419445, 0.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 11.426519729973023
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.EnvironmentNorth = [1.0, 0.0, 0.0]
renderView2.EnvironmentEast = [0.0, 1.0, 0.0]
renderView2.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1
renderView2.AxesGrid.XTitle = 'Time'
renderView2.AxesGrid.YTitle = ''
renderView2.AxesGrid.ZTitle = ''
renderView2.AxesGrid.FacesToRender = 36
renderView2.AxesGrid.ShowGrid = 1
renderView2.AxesGrid.ShowTicks = 0
renderView2.AxesGrid.YAxisUseCustomLabels = 1
renderView2.AxesGrid.DataBoundsScaleFactor = 1.1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024
spreadSheetView1.HiddenColumnLabels = []
spreadSheetView1.FieldAssociation = 'Row Data'

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.SplitHorizontal(1, 0.500000)
layout1.AssignView(3, renderView1)
layout1.AssignView(4, spreadSheetView1)
layout1.AssignView(2, renderView2)
layout1.SetSize(1419, 844)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(registrationName='TTKCinemaReader1', DatabasePath='ViscousFingers.cdb')

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(registrationName='TTKCinemaQuery1', InputTable=tTKCinemaReader1)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE Sim='run01'
ORDER BY Time"""

# create a new 'TTK ForEach'
tTKForEach1 = TTKForEach(registrationName='TTKForEach1', Input=tTKCinemaQuery1)
tTKForEach1.InputArray = [None, '']

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=tTKForEach1)

# create a new 'TTK Extract'
tTKExtract1 = TTKExtract(registrationName='TTKExtract1', Input=tTKCinemaProductReader1)
tTKExtract1.Expression = '0'
tTKExtract1.OutputType = 'vtkImageData'
tTKExtract1.ImageBounds = [0.0, 63.0, 0.0, 63.0, 0.0, 63.0]
tTKExtract1.InputArray = ['POINTS', 'ImageFile']

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=tTKExtract1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'ImageFile']
clip1.Value = 38.38161849975586

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [31.5, 31.5, 50.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=clip1)
threshold1.Scalars = ['POINTS', 'ImageFile']
threshold1.ThresholdRange = [30.0, 2000.0]

# create a new 'Connectivity'
connectivity1 = Connectivity(registrationName='Connectivity1', Input=threshold1)

# create a new 'TTK TrackingFromOverlap'
tTKTrackingFromOverlap1 = TTKTrackingFromOverlap(registrationName='TTKTrackingFromOverlap1', Input=connectivity1)
tTKTrackingFromOverlap1.Labels = 'RegionId'

# create a new 'TTK EndFor'
tTKEndFor1 = TTKEndFor(registrationName='TTKEndFor1', Data=tTKTrackingFromOverlap1,
    For=tTKForEach1)

# create a new 'TTK ArrayEditor'
tTKArrayEditor1 = TTKArrayEditor(registrationName='TTKArrayEditor1', Target=tTKEndFor1,
    Source=None)
tTKArrayEditor1.TargetArray = ['POINTS', 'BranchId']

# create a new 'Calculator'
calculate_SizeCategory = Calculator(registrationName='Calculate_SizeCategory', Input=tTKEndFor1)
calculate_SizeCategory.ResultArrayName = 'SizeCategory'
calculate_SizeCategory.Function = 'floor((Size/12000)*3+1)'

# create a new 'TTK PlanarGraphLayout'
tTKPlanarGraphLayout1 = TTKPlanarGraphLayout(registrationName='TTKPlanarGraphLayout1', Input=calculate_SizeCategory)
tTKPlanarGraphLayout1.SequenceArray = ['POINTS', 'SequenceIndex']
tTKPlanarGraphLayout1.UseSizes = 1
tTKPlanarGraphLayout1.SizeArray = ['POINTS', 'SizeCategory']
tTKPlanarGraphLayout1.UseBranches = 1
tTKPlanarGraphLayout1.BranchArray = ['POINTS', 'BranchId']
tTKPlanarGraphLayout1.LevelArray = ['POINTS', 'SizeCategory']

# create a new 'Calculator'
calculate_Position = Calculator(registrationName='Calculate_Position', Input=tTKPlanarGraphLayout1)
calculate_Position.CoordinateResults = 1
calculate_Position.Function = 'iHat*SequenceIndex+jHat*Layout_Y*0.4'

# create a new 'TTK MeshGraph'
tTKMeshGraph1 = TTKMeshGraph(registrationName='TTKMeshGraph1', Input=calculate_Position)
tTKMeshGraph1.SizeArray = ['POINTS', 'SizeCategory']
tTKMeshGraph1.SizeScale = 0.3

# create a new 'Calculator'
calculator_CorrectEdgeOverlap = Calculator(registrationName='Calculator_CorrectEdgeOverlap', Input=tTKMeshGraph1)
calculator_CorrectEdgeOverlap.CoordinateResults = 1
calculator_CorrectEdgeOverlap.Function = 'iHat*coordsX+jHat*coordsY+kHat*(coordsZ+Size/100000)'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKExtract1
tTKExtract1Display = Show(tTKExtract1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKExtract1Display.Representation = 'Outline'
tTKExtract1Display.ColorArrayName = ['POINTS', '']
tTKExtract1Display.OSPRayScaleArray = 'ImageFile'
tTKExtract1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKExtract1Display.SelectOrientationVectors = 'ImageFile'
tTKExtract1Display.ScaleFactor = 6.300000000000001
tTKExtract1Display.SelectScaleArray = 'ImageFile'
tTKExtract1Display.GlyphType = 'Arrow'
tTKExtract1Display.GlyphTableIndexArray = 'ImageFile'
tTKExtract1Display.GaussianRadius = 0.315
tTKExtract1Display.SetScaleArray = ['POINTS', 'ImageFile']
tTKExtract1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKExtract1Display.OpacityArray = ['POINTS', 'ImageFile']
tTKExtract1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKExtract1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKExtract1Display.PolarAxes = 'PolarAxesRepresentation'
tTKExtract1Display.ScalarOpacityUnitDistance = 1.7320508075688774
tTKExtract1Display.OpacityArrayName = [None, '']
tTKExtract1Display.IsosurfaceValues = [38.38161849975586]
tTKExtract1Display.SliceFunction = 'Plane'
tTKExtract1Display.Slice = 31

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKExtract1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 76.76323699951172, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKExtract1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 76.76323699951172, 1.0, 0.5, 0.0]

# show data from tTKEndFor1
tTKEndFor1Display = Show(tTKEndFor1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'BranchId'
branchIdLUT = GetColorTransferFunction('BranchId')
branchIdLUT.InterpretValuesAsCategories = 1
branchIdLUT.AnnotationsInitialized = 1
branchIdLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 9.0, 0.865003, 0.865003, 0.865003, 18.0, 0.705882, 0.0156863, 0.14902]
branchIdLUT.NanColor = [1.0, 1.0, 0.6]
branchIdLUT.ScalarRangeInitialized = 1.0
branchIdLUT.Annotations = ['0', '0', '1', '1', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11', '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18', '18', '19', '19', '20', '20', '23', '23', '25', '25', '26', '26', '31', '31', '32', '32', '33', '33', '35', '35', '36', '36', '37', '37', '38', '38', '39', '39', '40', '40', '41', '41', '42', '42', '44', '44', '45', '45', '46', '46', '47', '47', '48', '48', '49', '49', '50', '50', '51', '51', '52', '52', '53', '53', '54', '54', '55', '55', '56', '56', '57', '57', '58', '58', '59', '59', '60', '60', '61', '61', '62', '62', '63', '63', '64', '64', '65', '65', '66', '66', '67', '67', '68', '68', '69', '69', '70', '70', '71', '71', '72', '72', '73', '73', '74', '74', '75', '75', '76', '76', '77', '77', '78', '78', '79', '79', '80', '80', '81', '81', '82', '82', '83', '83', '84', '84', '85', '85', '86', '86', '87', '87', '88', '88', '89', '89', '90', '90', '91', '91', '92', '92', '93', '93', '94', '94', '95', '95', '96', '96', '97', '97', '98', '98', '99', '99', '100', '100']
branchIdLUT.ActiveAnnotatedValues = ['0', '1', '3', '4', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '0', '1', '3', '4', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '0', '1', '3', '4', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
branchIdLUT.IndexedColors = [0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765, 0.6980392156862745, 0.8745098039215686, 0.5411764705882353, 0.2, 0.6274509803921569, 0.17254901960784313, 0.984313725490196, 0.6039215686274509, 0.6, 0.8901960784313725, 0.10196078431372549, 0.10980392156862745, 0.9921568627450981, 0.7490196078431373, 0.43529411764705883, 1.0, 0.4980392156862745, 0.0, 0.792156862745098, 0.6980392156862745, 0.8392156862745098, 0.41568627450980394, 0.23921568627450981, 0.6039215686274509, 1.0, 1.0, 0.6, 0.6509803921568628, 0.807843137254902, 0.8901960784313725, 0.12156862745098039, 0.47058823529411764, 0.7058823529411765]
branchIdLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# get opacity transfer function/opacity map for 'BranchId'
branchIdPWF = GetOpacityTransferFunction('BranchId')
branchIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 18.0, 1.0, 0.5, 0.0]
branchIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKEndFor1Display.Representation = 'Surface'
tTKEndFor1Display.ColorArrayName = ['CELLS', 'BranchId']
tTKEndFor1Display.LookupTable = branchIdLUT
tTKEndFor1Display.LineWidth = 4.0
tTKEndFor1Display.OSPRayScaleArray = 'BranchId'
tTKEndFor1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKEndFor1Display.SelectOrientationVectors = 'BranchId'
tTKEndFor1Display.ScaleFactor = 4.69800934791565
tTKEndFor1Display.SelectScaleArray = 'BranchId'
tTKEndFor1Display.GlyphType = 'Arrow'
tTKEndFor1Display.GlyphTableIndexArray = 'BranchId'
tTKEndFor1Display.GaussianRadius = 0.23490046739578246
tTKEndFor1Display.SetScaleArray = ['POINTS', 'BranchId']
tTKEndFor1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKEndFor1Display.OpacityArray = ['POINTS', 'BranchId']
tTKEndFor1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKEndFor1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKEndFor1Display.PolarAxes = 'PolarAxesRepresentation'
tTKEndFor1Display.ScalarOpacityFunction = branchIdPWF
tTKEndFor1Display.ScalarOpacityUnitDistance = 20.386356096541355
tTKEndFor1Display.OpacityArrayName = [None, '']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKEndFor1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 18.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKEndFor1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 18.0, 1.0, 0.5, 0.0]

# show data from tTKArrayEditor1
tTKArrayEditor1Display = Show(tTKArrayEditor1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKArrayEditor1Display.Representation = 'Points'
tTKArrayEditor1Display.ColorArrayName = [None, '']
tTKArrayEditor1Display.PointSize = 10.0
tTKArrayEditor1Display.RenderPointsAsSpheres = 1
tTKArrayEditor1Display.OSPRayScaleArray = 'BranchId'
tTKArrayEditor1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKArrayEditor1Display.SelectOrientationVectors = 'BranchId'
tTKArrayEditor1Display.ScaleFactor = 5.462362766265869
tTKArrayEditor1Display.SelectScaleArray = 'BranchId'
tTKArrayEditor1Display.GlyphType = 'Arrow'
tTKArrayEditor1Display.GlyphTableIndexArray = 'BranchId'
tTKArrayEditor1Display.GaussianRadius = 0.27311813831329346
tTKArrayEditor1Display.SetScaleArray = ['POINTS', 'BranchId']
tTKArrayEditor1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKArrayEditor1Display.OpacityArray = ['POINTS', 'BranchId']
tTKArrayEditor1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKArrayEditor1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKArrayEditor1Display.PolarAxes = 'PolarAxesRepresentation'
tTKArrayEditor1Display.ScalarOpacityUnitDistance = 11.589457544592316
tTKArrayEditor1Display.OpacityArrayName = [None, '']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKArrayEditor1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKArrayEditor1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from calculator_CorrectEdgeOverlap
calculator_CorrectEdgeOverlapDisplay = Show(calculator_CorrectEdgeOverlap, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator_CorrectEdgeOverlapDisplay.Representation = 'Surface'
calculator_CorrectEdgeOverlapDisplay.ColorArrayName = ['CELLS', 'BranchId']
calculator_CorrectEdgeOverlapDisplay.LookupTable = branchIdLUT
calculator_CorrectEdgeOverlapDisplay.OSPRayScaleArray = 'BranchId'
calculator_CorrectEdgeOverlapDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calculator_CorrectEdgeOverlapDisplay.SelectOrientationVectors = 'Result'
calculator_CorrectEdgeOverlapDisplay.ScaleFactor = 7.1000000000000005
calculator_CorrectEdgeOverlapDisplay.SelectScaleArray = 'BranchId'
calculator_CorrectEdgeOverlapDisplay.GlyphType = 'Arrow'
calculator_CorrectEdgeOverlapDisplay.GlyphTableIndexArray = 'BranchId'
calculator_CorrectEdgeOverlapDisplay.GaussianRadius = 0.355
calculator_CorrectEdgeOverlapDisplay.SetScaleArray = ['POINTS', 'BranchId']
calculator_CorrectEdgeOverlapDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calculator_CorrectEdgeOverlapDisplay.OpacityArray = ['POINTS', 'BranchId']
calculator_CorrectEdgeOverlapDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calculator_CorrectEdgeOverlapDisplay.DataAxesGrid = 'GridAxesRepresentation'
calculator_CorrectEdgeOverlapDisplay.PolarAxes = 'PolarAxesRepresentation'
calculator_CorrectEdgeOverlapDisplay.ScalarOpacityFunction = branchIdPWF
calculator_CorrectEdgeOverlapDisplay.ScalarOpacityUnitDistance = 7.739005741181658
calculator_CorrectEdgeOverlapDisplay.OpacityArrayName = [None, '']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator_CorrectEdgeOverlapDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator_CorrectEdgeOverlapDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'spreadSheetView1'
# ----------------------------------------------------------------

# show data from tTKCinemaQuery1
tTKCinemaQuery1Display = Show(tTKCinemaQuery1, spreadSheetView1, 'SpreadSheetRepresentation')

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------
