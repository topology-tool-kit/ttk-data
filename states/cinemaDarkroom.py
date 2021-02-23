# state file generated using paraview version 5.8.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [783, 460]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.05099499225616455, 0.007758498191833496, -0.00749649852514267]
renderView1.CameraPosition = [0.7318841029738407, -0.022788215488852105, -0.6465637446021283]
renderView1.CameraFocalPoint = [0.0974171418365998, -0.010320908418666189, 0.035985660379378295]
renderView1.CameraViewUp = [-0.01977908845568779, 0.9991329306701646, -0.036635699942954535]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.6342075582553577

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [783, 459]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [1011.3609848022461, 502.6661043167114, -0.007495880126953125]
renderView2.CameraPosition = [1011.203164778182, 456.03516378044503, 4478.569583624059]
renderView2.CameraFocalPoint = [1011.203164778182, 456.03516378044503, -0.007495880126953125]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 540.7478513266177

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK Darkroom Camera'
ttkDarkroomCamera1 = TTKDarkroomCamera()
ttkDarkroomCamera1.Position = renderView1.CameraPosition
ttkDarkroomCamera1.Up = renderView1.CameraViewUp
ttkDarkroomCamera1.FocalPoint = renderView1.CameraFocalPoint

# create a new 'TTK CinemaReader'
ttkCinemaReader1 = TTKCinemaReader(DatabasePath='GroundWater.cdb')

# create a new 'TTK CinemaQuery'
ttkCinemaQuery1 = TTKCinemaQuery(InputTable=ttkCinemaReader1)
ttkCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
ORDER BY Description
"""

# create a new 'TTK CinemaProductReader'
ttkCinemaProductReader1 = TTKCinemaProductReader(Input=ttkCinemaQuery1)

# create a new 'Elevation'
elevation1 = Elevation(Input=ttkCinemaProductReader1)
elevation1.LowPoint = [-0.3657500147819519, 0.007758498191833496, -0.00749649852514267]
elevation1.HighPoint = [0.467739999294281, 0.007758498191833496, -0.00749649852514267]

# create a new 'TTK Extract'
ttkExtract4 = TTKExtract(Input=elevation1)
ttkExtract4.Expression = '0'

# create a new 'TTK CinemaImaging'
ttkCinemaImaging1 = TTKCinemaImaging(Dataset=elevation1,
    SamplingGrid=ttkDarkroomCamera1)
ttkCinemaImaging1.Resolution = [2048, 1024]
ttkCinemaImaging1.ProjectionMode = 'Perspective'
ttkCinemaImaging1.Angle = 55.0

# create a new 'TTK Extract'
ttkExtract2 = TTKExtract(Input=ttkCinemaImaging1)
ttkExtract2.Expression = '0'
ttkExtract2.OutputType = 'vtkMultiBlockDataSet'

# create a new 'TTK Darkroom ColorMapping'
ttkDarkroomColorMapping2 = TTKDarkroomColorMapping(Input=ttkExtract2)
ttkDarkroomColorMapping2.Scalars = ['POINTS', 'Elevation']
ttkDarkroomColorMapping2.ColorMap = 'OrRd'

# create a new 'TTK Extract'
ttkExtract1 = TTKExtract(Input=ttkCinemaImaging1)
ttkExtract1.Expression = '1'
ttkExtract1.OutputType = 'vtkMultiBlockDataSet'

# create a new 'TTK Darkroom ColorMapping'
ttkDarkroomColorMapping1 = TTKDarkroomColorMapping(Input=ttkExtract1)
ttkDarkroomColorMapping1.Scalars = ['POINTS', 'Elevation']
ttkDarkroomColorMapping1.SingleColor = [0.0, 0.6666666666666666, 1.0]

# create a new 'TTK Darkroom Compositing'
ttkDarkroomCompositing1 = TTKDarkroomCompositing(Input=[ttkDarkroomColorMapping1, ttkDarkroomColorMapping2])
ttkDarkroomCompositing1.Depth = ['POINTS', 'Depth']

# create a new 'TTK Darkroom SSAO'
ttkDarkroomSSAO1 = TTKDarkroomSSAO(Input=ttkDarkroomCompositing1)
ttkDarkroomSSAO1.Depth = ['POINTS', 'Depth']

# create a new 'TTK Extract'
ttkExtract5 = TTKExtract(Input=elevation1)
ttkExtract5.Expression = '1'

# create a new 'TTK Darkroom SSSAO'
ttkDarkroomSSSAO1 = TTKDarkroomSSSAO(Input=ttkDarkroomSSAO1)
ttkDarkroomSSSAO1.Depth = ['POINTS', 'Depth']
ttkDarkroomSSSAO1.Samples = 128
ttkDarkroomSSSAO1.Radius = 0.1

# create a new 'TTK Darkroom IBS'
ttkDarkroomIBS1 = TTKDarkroomIBS(Input=ttkDarkroomSSSAO1)
ttkDarkroomIBS1.Color = ['POINTS', 'Diffuse']
ttkDarkroomIBS1.Depth = ['POINTS', 'Depth']
ttkDarkroomIBS1.AO = ['POINTS', 'SSSAO']
ttkDarkroomIBS1.Strength = 600.0
ttkDarkroomIBS1.Luminance = 0.1
ttkDarkroomIBS1.Ambient = 0.5

# create a new 'TTK Darkroom SSDoF'
ttkDarkroomSSDoF1 = TTKDarkroomSSDoF(Input=ttkDarkroomIBS1)
ttkDarkroomSSDoF1.Color = ['POINTS', 'IBS']
ttkDarkroomSSDoF1.Depth = ['POINTS', 'Depth']
ttkDarkroomSSDoF1.Radius = 0.05
ttkDarkroomSSDoF1.Aperture = 0.25
ttkDarkroomSSDoF1.FocalDepth = 0.5
ttkDarkroomSSDoF1.MaxBlur = 0.08

# create a new 'TTK Darkroom FXAA'
ttkDarkroomFXAA1 = TTKDarkroomFXAA(Input=ttkDarkroomSSDoF1)
ttkDarkroomFXAA1.Color = ['POINTS', 'SSDoF']

# create a new 'TTK Extract'
ttkExtract3 = TTKExtract(Input=ttkDarkroomFXAA1)
ttkExtract3.Expression = '0'
ttkExtract3.OutputType = 'vtkImageData'
ttkExtract3.ImageExtent = [0, 2047, 0, 1023, 0, 0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from ttkDarkroomCamera1
ttkDarkroomCamera1Display = Show(ttkDarkroomCamera1, renderView1, 'UnstructuredGridRepresentation')
ttkDarkroomCamera1Display.Representation = 'Surface'
ttkDarkroomCamera1Display.PointSize = 10.0

# show data from ttkExtract4
ttkExtract4Display = Show(ttkExtract4, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Elevation'
elevationLUT = GetColorTransferFunction('Elevation')
elevationLUT.RGBPoints = [0.0, 1.0, 0.968627, 0.92549, 0.05882349999999992, 0.998155, 0.940946, 0.859054, 0.12156849999999997, 0.996186, 0.911419, 0.788189, 0.18431350000000002, 0.994218, 0.872587, 0.706159, 0.24705899999999992, 0.992249, 0.833218, 0.623483, 0.30980399999999997, 0.992157, 0.784468, 0.570827, 0.372549, 0.992157, 0.735256, 0.519646, 0.43529399999999996, 0.990265, 0.646321, 0.436309, 0.49803921500000004, 0.988297, 0.555771, 0.351665, 0.5607845, 0.963445, 0.476663, 0.316601, 0.6235295000000001, 0.937855, 0.397924, 0.283137, 0.6862745, 0.891119, 0.294195, 0.203537, 0.7490195, 0.843875, 0.189865, 0.12283, 0.8117645, 0.773379, 0.095225, 0.061499, 0.87451, 0.702514, 0.000738, 0.000477, 0.937255, 0.6004, 0.0, 0.0, 1.0, 0.498039, 0.0, 0.0]
elevationLUT.ColorSpace = 'Lab'
elevationLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
ttkExtract4Display.Representation = 'Surface'
ttkExtract4Display.ColorArrayName = ['POINTS', 'Elevation']
ttkExtract4Display.LookupTable = elevationLUT
ttkExtract4Display.Specular = 1.0
ttkExtract4Display.SpecularPower = 35.0
ttkExtract4Display.OSPRayScaleArray = 'Elevation'
ttkExtract4Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkExtract4Display.SelectOrientationVectors = 'Elevation'
ttkExtract4Display.ScaleFactor = 0.0833490014076233
ttkExtract4Display.SelectScaleArray = 'Elevation'
ttkExtract4Display.GlyphType = 'Arrow'
ttkExtract4Display.GlyphTableIndexArray = 'Elevation'
ttkExtract4Display.GaussianRadius = 0.004167450070381165
ttkExtract4Display.SetScaleArray = ['POINTS', 'Elevation']
ttkExtract4Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkExtract4Display.OpacityArray = ['POINTS', 'Elevation']
ttkExtract4Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkExtract4Display.DataAxesGrid = 'GridAxesRepresentation'
ttkExtract4Display.PolarAxes = 'PolarAxesRepresentation'

# show data from ttkExtract5
ttkExtract5Display = Show(ttkExtract5, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
ttkExtract5Display.Representation = 'Surface'
ttkExtract5Display.AmbientColor = [0.0, 0.6666666666666666, 1.0]
ttkExtract5Display.ColorArrayName = ['POINTS', '']
ttkExtract5Display.DiffuseColor = [0.0, 0.6666666666666666, 1.0]
ttkExtract5Display.OSPRayScaleArray = 'Elevation'
ttkExtract5Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkExtract5Display.SelectOrientationVectors = 'Elevation'
ttkExtract5Display.ScaleFactor = 0.08308770060539246
ttkExtract5Display.SelectScaleArray = 'Elevation'
ttkExtract5Display.GlyphType = 'Arrow'
ttkExtract5Display.GlyphTableIndexArray = 'Elevation'
ttkExtract5Display.GaussianRadius = 0.004154385030269623
ttkExtract5Display.SetScaleArray = ['POINTS', 'Elevation']
ttkExtract5Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkExtract5Display.OpacityArray = ['POINTS', 'Elevation']
ttkExtract5Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkExtract5Display.DataAxesGrid = 'GridAxesRepresentation'
ttkExtract5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkExtract5Display.ScaleTransferFunction.Points = [0.0023527848534286022, 0.0, 0.5, 0.0, 0.9992177486419678, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkExtract5Display.OpacityTransferFunction.Points = [0.0023527848534286022, 0.0, 0.5, 0.0, 0.9992177486419678, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from ttkExtract3
ttkExtract3Display = Show(ttkExtract3, renderView2, 'UniformGridRepresentation')

# get color transfer function/color map for 'FXAA'
fXAALUT = GetColorTransferFunction('FXAA')
fXAALUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 255.0, 0.865003, 0.865003, 0.865003, 510.0, 0.705882, 0.0156863, 0.14902]
fXAALUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'FXAA'
fXAAPWF = GetOpacityTransferFunction('FXAA')
fXAAPWF.Points = [0.0, 0.0, 0.5, 0.0, 510.0, 1.0, 0.5, 0.0]
fXAAPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
ttkExtract3Display.Representation = 'Slice'
ttkExtract3Display.ColorArrayName = ['POINTS', 'FXAA']
ttkExtract3Display.LookupTable = fXAALUT
ttkExtract3Display.MapScalars = 0
ttkExtract3Display.OSPRayScaleArray = 'FXAA'
ttkExtract3Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkExtract3Display.SelectOrientationVectors = 'Depth'
ttkExtract3Display.ScaleFactor = 204.70000000000002
ttkExtract3Display.SelectScaleArray = 'FXAA'
ttkExtract3Display.GlyphType = 'Arrow'
ttkExtract3Display.GlyphTableIndexArray = 'FXAA'
ttkExtract3Display.GaussianRadius = 10.235
ttkExtract3Display.SetScaleArray = ['POINTS', 'FXAA']
ttkExtract3Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkExtract3Display.OpacityArray = ['POINTS', 'FXAA']
ttkExtract3Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkExtract3Display.DataAxesGrid = 'GridAxesRepresentation'
ttkExtract3Display.PolarAxes = 'PolarAxesRepresentation'
ttkExtract3Display.ScalarOpacityUnitDistance = 17.886797802949964
ttkExtract3Display.ScalarOpacityFunction = fXAAPWF
ttkExtract3Display.IsosurfaceValues = [127.5]
ttkExtract3Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkExtract3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkExtract3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
ttkExtract3Display.SliceFunction.Origin = [1023.5, 511.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Elevation'
elevationPWF = GetOpacityTransferFunction('Elevation')
elevationPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveView(renderView2)
SetActiveSource(ttkExtract3)
# ----------------------------------------------------------------
