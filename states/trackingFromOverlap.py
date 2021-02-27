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
ttkCinemaReader1 = TTKCinemaReader(registrationName='TTKCinemaReader1', DatabasePath='ViscousFingers.cdb')

# create a new 'TTK CinemaQuery'
ttkCinemaQuery1 = TTKCinemaQuery(registrationName='TTKCinemaQuery1', InputTable=ttkCinemaReader1)
ttkCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE Sim='run01'
ORDER BY Time"""

# create a new 'TTK ForEach'
ttkForEach1 = TTKForEach(registrationName='TTKForEach1', Input=ttkCinemaQuery1)

# create a new 'TTK CinemaProductReader'
ttkCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=ttkForEach1)

# create a new 'TTK Extract'
ttkExtract1 = TTKExtract(registrationName='TTKExtract1', Input=ttkCinemaProductReader1)
ttkExtract1.Expression = '0'
ttkExtract1.OutputType = 'vtkImageData'
ttkExtract1.ImageExtent = [0, 63, 0, 63, 0, 63]

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=ttkExtract1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Value = 38.38161849975586

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [31.5, 31.5, 50.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=clip1)
threshold1.Scalars = ['POINTS','NONE']
threshold1.Scalars = ['POINTS', 'ImageFile']
threshold1.ThresholdRange = [30.0, 2000.0]

# create a new 'Connectivity'
connectivity1 = Connectivity(registrationName='Connectivity1', Input=threshold1)

# create a new 'TTK TrackingFromOverlap'
ttkTrackingFromOverlap1 = TTKTrackingFromOverlap(registrationName='TTKTrackingFromOverlap1', Input=connectivity1)
ttkTrackingFromOverlap1.Labels = 'NONE'
ttkTrackingFromOverlap1.Labels = 'RegionId'

# create a new 'TTK EndFor'
ttkEndFor1 = TTKEndFor(registrationName='TTKEndFor1', Data=ttkTrackingFromOverlap1,
    For=ttkForEach1)

# create a new 'TTK ArrayEditor'
ttkArrayEditor1 = TTKArrayEditor(registrationName='TTKArrayEditor1', Target=ttkEndFor1,
    Source=None)
ttkArrayEditor1.TargetArray = ['POINTS','NONE']
ttkArrayEditor1.TargetArray = ['POINTS', 'BranchId']

# create a new 'Calculator'
calculate_SizeCategory = Calculator(registrationName='Calculate_SizeCategory', Input=ttkEndFor1)
calculate_SizeCategory.ResultArrayName = 'SizeCategory'
calculate_SizeCategory.Function = 'floor((Size/12000)*3+1)'

# create a new 'TTK PlanarGraphLayout'
ttkPlanarGraphLayout1 = TTKPlanarGraphLayout(registrationName='TTKPlanarGraphLayout1', Input=calculate_SizeCategory)
ttkPlanarGraphLayout1.UseSequences = 1
ttkPlanarGraphLayout1.SequenceArray = ['POINTS','NONE']
ttkPlanarGraphLayout1.SequenceArray = ['POINTS', 'SequenceIndex']
ttkPlanarGraphLayout1.UseSizes = 1
ttkPlanarGraphLayout1.SizeArray = ['POINTS','NONE']
ttkPlanarGraphLayout1.SizeArray = ['POINTS', 'SizeCategory']
ttkPlanarGraphLayout1.UseBranches = 1
ttkPlanarGraphLayout1.BranchArray = ['POINTS','NONE']
ttkPlanarGraphLayout1.BranchArray = ['POINTS', 'BranchId']

# create a new 'Calculator'
calculate_Position = Calculator(registrationName='Calculate_Position', Input=ttkPlanarGraphLayout1)
calculate_Position.CoordinateResults = 1
calculate_Position.Function = 'iHat*SequenceIndex+jHat*Layout_Y*0.4'

# create a new 'TTK MeshGraph'
ttkMeshGraph1 = TTKMeshGraph(registrationName='TTKMeshGraph1', Input=calculate_Position)
ttkMeshGraph1.SizeArray = ['POINTS','NONE']
ttkMeshGraph1.SizeArray = ['POINTS', 'SizeCategory']
ttkMeshGraph1.SizeScale = 0.3

# create a new 'Calculator'
calculator_CorrectEdgeOverlap = Calculator(registrationName='Calculator_CorrectEdgeOverlap', Input=ttkMeshGraph1)
calculator_CorrectEdgeOverlap.CoordinateResults = 1
calculator_CorrectEdgeOverlap.Function = 'iHat*coordsX+jHat*coordsY+kHat*(coordsZ+Size/100000)'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from ttkExtract1
ttkExtract1Display = Show(ttkExtract1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
ttkExtract1Display.Representation = 'Outline'
ttkExtract1Display.ColorArrayName = ['POINTS', '']
ttkExtract1Display.OSPRayScaleArray = 'ImageFile'
ttkExtract1Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkExtract1Display.SelectOrientationVectors = 'ImageFile'
ttkExtract1Display.ScaleFactor = 6.300000000000001
ttkExtract1Display.SelectScaleArray = 'ImageFile'
ttkExtract1Display.GlyphType = 'Arrow'
ttkExtract1Display.GlyphTableIndexArray = 'ImageFile'
ttkExtract1Display.GaussianRadius = 0.315
ttkExtract1Display.SetScaleArray = ['POINTS', 'ImageFile']
ttkExtract1Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkExtract1Display.OpacityArray = ['POINTS', 'ImageFile']
ttkExtract1Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkExtract1Display.DataAxesGrid = 'GridAxesRepresentation'
ttkExtract1Display.PolarAxes = 'PolarAxesRepresentation'
ttkExtract1Display.ScalarOpacityUnitDistance = 1.7320508075688774
ttkExtract1Display.OpacityArrayName = [None, '']
ttkExtract1Display.IsosurfaceValues = [38.38161849975586]
ttkExtract1Display.SliceFunction = 'Plane'
ttkExtract1Display.Slice = 31

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkExtract1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 76.76323699951172, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkExtract1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 76.76323699951172, 1.0, 0.5, 0.0]

# show data from ttkEndFor1
ttkEndFor1Display = Show(ttkEndFor1, renderView1, 'UnstructuredGridRepresentation')

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
ttkEndFor1Display.Representation = 'Surface'
ttkEndFor1Display.ColorArrayName = ['CELLS', 'BranchId']
ttkEndFor1Display.LookupTable = branchIdLUT
ttkEndFor1Display.LineWidth = 4.0
ttkEndFor1Display.OSPRayScaleArray = 'BranchId'
ttkEndFor1Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkEndFor1Display.SelectOrientationVectors = 'BranchId'
ttkEndFor1Display.ScaleFactor = 4.69800934791565
ttkEndFor1Display.SelectScaleArray = 'BranchId'
ttkEndFor1Display.GlyphType = 'Arrow'
ttkEndFor1Display.GlyphTableIndexArray = 'BranchId'
ttkEndFor1Display.GaussianRadius = 0.23490046739578246
ttkEndFor1Display.SetScaleArray = ['POINTS', 'BranchId']
ttkEndFor1Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkEndFor1Display.OpacityArray = ['POINTS', 'BranchId']
ttkEndFor1Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkEndFor1Display.DataAxesGrid = 'GridAxesRepresentation'
ttkEndFor1Display.PolarAxes = 'PolarAxesRepresentation'
ttkEndFor1Display.ScalarOpacityFunction = branchIdPWF
ttkEndFor1Display.ScalarOpacityUnitDistance = 20.386356096541355
ttkEndFor1Display.OpacityArrayName = [None, '']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkEndFor1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 18.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkEndFor1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 18.0, 1.0, 0.5, 0.0]

# show data from ttkArrayEditor1
ttkArrayEditor1Display = Show(ttkArrayEditor1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
ttkArrayEditor1Display.Representation = 'Points'
ttkArrayEditor1Display.ColorArrayName = [None, '']
ttkArrayEditor1Display.PointSize = 10.0
ttkArrayEditor1Display.RenderPointsAsSpheres = 1
ttkArrayEditor1Display.OSPRayScaleArray = 'BranchId'
ttkArrayEditor1Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkArrayEditor1Display.SelectOrientationVectors = 'BranchId'
ttkArrayEditor1Display.ScaleFactor = 5.462362766265869
ttkArrayEditor1Display.SelectScaleArray = 'BranchId'
ttkArrayEditor1Display.GlyphType = 'Arrow'
ttkArrayEditor1Display.GlyphTableIndexArray = 'BranchId'
ttkArrayEditor1Display.GaussianRadius = 0.27311813831329346
ttkArrayEditor1Display.SetScaleArray = ['POINTS', 'BranchId']
ttkArrayEditor1Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkArrayEditor1Display.OpacityArray = ['POINTS', 'BranchId']
ttkArrayEditor1Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkArrayEditor1Display.DataAxesGrid = 'GridAxesRepresentation'
ttkArrayEditor1Display.PolarAxes = 'PolarAxesRepresentation'
ttkArrayEditor1Display.ScalarOpacityUnitDistance = 11.589457544592316
ttkArrayEditor1Display.OpacityArrayName = [None, '']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkArrayEditor1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkArrayEditor1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from ttkCinemaQuery1
ttkCinemaQuery1Display = Show(ttkCinemaQuery1, spreadSheetView1, 'SpreadSheetRepresentation')

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------
