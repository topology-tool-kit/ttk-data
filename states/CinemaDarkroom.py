from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [783, 460]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.05099499225616455, 0.007758498191833496, -0.00749649852514267]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.8539705454414804, -0.024920842240718458, -0.8002740272761396]
renderView1.CameraFocalPoint = [0.08626552246541902, -0.009835400685793486, 0.02561075275148361]
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
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [1011.203164778182, 456.03516378044503, 4478.569583624059]
renderView2.CameraFocalPoint = [1011.203164778182, 456.03516378044503, -0.007495880126953125]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 540.7478513266177

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath='GroundWater.cdb')

# create a new 'TTK CinemaQuery'
tTKCinemaQuery2 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery2.SQLStatement = """SELECT * FROM InputTable0
WHERE Description="Stone"
"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader2 = TTKCinemaProductReader(Input=tTKCinemaQuery2)

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE Description="Streamlines"
"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaQuery1)

# create a new 'Elevation'
elevation1 = Elevation(Input=tTKCinemaProductReader1)
elevation1.LowPoint = [0.051649510860443115, -0.13051000237464905, -0.02352450042963028]
elevation1.HighPoint = [0.051649510860443115, 0.15952299535274506, -0.02352450042963028]

# create a new 'Elevation'
elevation2 = Elevation(Input=tTKCinemaProductReader2)
elevation2.LowPoint = [-0.3657500147819519, 0.007758498191833496, -0.00749649852514267]
elevation2.HighPoint = [0.467739999294281, 0.007758498191833496, -0.00749649852514267]

# create a new 'TTK IcosphereFromObject'
tTKIcosphereFromObject1 = TTKIcosphereFromObject(Object=elevation2)
tTKIcosphereFromObject1.Scale = 2.0

# create a new 'TTK Identifiers'
tTKIdentifiers1 = TTKIdentifiers(Input=tTKIcosphereFromObject1)

# create a new 'TTK Extract'
tTKExtract1 = TTKExtract(Input=tTKIdentifiers1)
tTKExtract1.ExtractionMode = 'Geometry'
tTKExtract1.Expression = '8'
tTKExtract1.InputArray = ['POINTS', 'ttkVertexScalarField']

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKExtract1)
calculator1.ResultArrayName = 'CamUp'
calculator1.Function = 'jHat'

# create a new 'TTK CinemaImaging'
tTKCinemaImaging2 = TTKCinemaImaging(Dataset=elevation1,
    SamplingGrid=calculator1)
tTKCinemaImaging2.Resolution = [2048, 1024]
tTKCinemaImaging2.ProjectionMode = 'Perspective'
tTKCinemaImaging2.CamAngle = 30.0
tTKCinemaImaging2.AutoCamNearFar = 0
tTKCinemaImaging2.CamNearFar = [0.1, 2.0]
tTKCinemaImaging2.AutoCamFocus = 0
tTKCinemaImaging2.CamFocus = [0.2, 0.0, 0.0]

# create a new 'TTK Extract'
tTKExtract3 = TTKExtract(Input=tTKCinemaImaging2)
tTKExtract3.Expression = '0'
tTKExtract3.OutputType = 'vtkImageData'
tTKExtract3.ImageBounds = [0.0, 2047.0, 0.0, 1023.0, 0.0, 0.0]
tTKExtract3.InputArray = ['POINTS', 'Depth']

# create a new 'ttkCinemaDarkroomColorMapping'
ttkCinemaDarkroomColorMapping2 = ttkCinemaDarkroomColorMapping(Input=tTKExtract3)
ttkCinemaDarkroomColorMapping2.ScalarArray = ['POINTS', 'Elevation']
ttkCinemaDarkroomColorMapping2.NANColor = [1.0, 1.0, 1.0]
ttkCinemaDarkroomColorMapping2.SolidColor = [0.0, 0.6666666666666666, 1.0]

# create a new 'TTK CinemaImaging'
tTKCinemaImaging1 = TTKCinemaImaging(Dataset=elevation2,
    SamplingGrid=calculator1)
tTKCinemaImaging1.Resolution = [2048, 1024]
tTKCinemaImaging1.ProjectionMode = 'Perspective'
tTKCinemaImaging1.CamAngle = 30.0
tTKCinemaImaging1.AutoCamNearFar = 0
tTKCinemaImaging1.CamNearFar = [0.1, 2.0]
tTKCinemaImaging1.AutoCamFocus = 0
tTKCinemaImaging1.CamFocus = [0.2, 0.0, 0.0]

# create a new 'TTK Extract'
tTKExtract2 = TTKExtract(Input=tTKCinemaImaging1)
tTKExtract2.Expression = '0'
tTKExtract2.OutputType = 'vtkImageData'
tTKExtract2.ImageBounds = [0.0, 2047.0, 0.0, 1023.0, 0.0, 0.0]
tTKExtract2.InputArray = ['POINTS', 'Depth']

# create a new 'ttkCinemaDarkroomColorMapping'
ttkCinemaDarkroomColorMapping1 = ttkCinemaDarkroomColorMapping(Input=tTKExtract2)
ttkCinemaDarkroomColorMapping1.ScalarArray = ['POINTS', 'Elevation']
ttkCinemaDarkroomColorMapping1.ColorMap = 'OrRd'
ttkCinemaDarkroomColorMapping1.NANColor = [1.0, 1.0, 1.0]

# create a new 'ttkCinemaDarkroomCompositing'
ttkCinemaDarkroomCompositing1 = ttkCinemaDarkroomCompositing(Input=[ttkCinemaDarkroomColorMapping2, ttkCinemaDarkroomColorMapping1])
ttkCinemaDarkroomCompositing1.DepthArray = ['POINTS', 'Depth']

# create a new 'ttkCinemaDarkroomSSAO'
ttkCinemaDarkroomSSAO1 = ttkCinemaDarkroomSSAO(Input=ttkCinemaDarkroomCompositing1)
ttkCinemaDarkroomSSAO1.Depth = ['POINTS', 'Depth']
ttkCinemaDarkroomSSAO1.Radius = 0.02

# create a new 'ttkCinemaDarkroomSSSAO'
ttkCinemaDarkroomSSSAO1 = ttkCinemaDarkroomSSSAO(Input=ttkCinemaDarkroomSSAO1)
ttkCinemaDarkroomSSSAO1.Depth = ['POINTS', 'Depth']
ttkCinemaDarkroomSSSAO1.Samples = 242
ttkCinemaDarkroomSSSAO1.Radius = 0.1

# create a new 'ttkCinemaDarkroomIBS'
ttkCinemaDarkroomIBS1 = ttkCinemaDarkroomIBS(Input=ttkCinemaDarkroomSSSAO1)
ttkCinemaDarkroomIBS1.Color = ['POINTS', 'Diffuse']
ttkCinemaDarkroomIBS1.Depth = ['POINTS', 'Depth']
ttkCinemaDarkroomIBS1.AO = ['POINTS', 'SSSAO']
ttkCinemaDarkroomIBS1.Strength = 2000.0
ttkCinemaDarkroomIBS1.Luminance = 0.78

# create a new 'ttkCinemaDarkroomSSDoF'
ttkCinemaDarkroomSSDoF1 = ttkCinemaDarkroomSSDoF(Input=ttkCinemaDarkroomIBS1)
ttkCinemaDarkroomSSDoF1.Color = ['POINTS', 'IBS']
ttkCinemaDarkroomSSDoF1.Depth = ['POINTS', 'Depth']
ttkCinemaDarkroomSSDoF1.Radius = 0.1
ttkCinemaDarkroomSSDoF1.Distance = 0.91
ttkCinemaDarkroomSSDoF1.MaxBlur = 0.32

# create a new 'ttkCinemaDarkroomFXAA'
ttkCinemaDarkroomFXAA1 = ttkCinemaDarkroomFXAA(Input=ttkCinemaDarkroomSSDoF1)
ttkCinemaDarkroomFXAA1.Color = ['POINTS', 'IBS']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from elevation2
elevation2Display = Show(elevation2, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Elevation'
elevationLUT = GetColorTransferFunction('Elevation')
elevationLUT.RGBPoints = [0.0, 1.0, 0.968627, 0.92549, 0.05882349999999992, 0.998155, 0.940946, 0.859054, 0.12156849999999997, 0.996186, 0.911419, 0.788189, 0.18431350000000002, 0.994218, 0.872587, 0.706159, 0.24705899999999992, 0.992249, 0.833218, 0.623483, 0.30980399999999997, 0.992157, 0.784468, 0.570827, 0.372549, 0.992157, 0.735256, 0.519646, 0.43529399999999996, 0.990265, 0.646321, 0.436309, 0.49803921500000004, 0.988297, 0.555771, 0.351665, 0.5607845, 0.963445, 0.476663, 0.316601, 0.6235295000000001, 0.937855, 0.397924, 0.283137, 0.6862745, 0.891119, 0.294195, 0.203537, 0.7490195, 0.843875, 0.189865, 0.12283, 0.8117645, 0.773379, 0.095225, 0.061499, 0.87451, 0.702514, 0.000738, 0.000477, 0.937255, 0.6004, 0.0, 0.0, 1.0, 0.498039, 0.0, 0.0]
elevationLUT.ColorSpace = 'Lab'
elevationLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
elevation2Display.Representation = 'Surface'
elevation2Display.ColorArrayName = ['POINTS', 'Elevation']
elevation2Display.LookupTable = elevationLUT
elevation2Display.OSPRayScaleArray = 'Elevation'
elevation2Display.OSPRayScaleFunction = 'PiecewiseFunction'
elevation2Display.SelectOrientationVectors = 'Elevation'
elevation2Display.ScaleFactor = 0.0833490014076233
elevation2Display.SelectScaleArray = 'Elevation'
elevation2Display.GlyphType = 'Arrow'
elevation2Display.GlyphTableIndexArray = 'Elevation'
elevation2Display.GaussianRadius = 0.004167450070381165
elevation2Display.SetScaleArray = ['POINTS', 'Elevation']
elevation2Display.ScaleTransferFunction = 'PiecewiseFunction'
elevation2Display.OpacityArray = ['POINTS', 'Elevation']
elevation2Display.OpacityTransferFunction = 'PiecewiseFunction'
elevation2Display.DataAxesGrid = 'GridAxesRepresentation'
elevation2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
elevation2Display.ScaleTransferFunction.Points = [0.045205097645521164, 0.0, 0.5, 0.0, 0.9571114182472229, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
elevation2Display.OpacityTransferFunction.Points = [0.045205097645521164, 0.0, 0.5, 0.0, 0.9571114182472229, 1.0, 0.5, 0.0]

# show data from elevation1
elevation1Display = Show(elevation1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
elevation1Display.Representation = 'Surface'
elevation1Display.AmbientColor = [0.0, 0.6666666666666666, 1.0]
elevation1Display.ColorArrayName = ['POINTS', '']
elevation1Display.DiffuseColor = [0.0, 0.6666666666666666, 1.0]
elevation1Display.OSPRayScaleArray = 'Elevation'
elevation1Display.OSPRayScaleFunction = 'PiecewiseFunction'
elevation1Display.SelectOrientationVectors = 'Elevation'
elevation1Display.ScaleFactor = 0.08308770060539246
elevation1Display.SelectScaleArray = 'Elevation'
elevation1Display.GlyphType = 'Arrow'
elevation1Display.GlyphTableIndexArray = 'Elevation'
elevation1Display.GaussianRadius = 0.004154385030269623
elevation1Display.SetScaleArray = ['POINTS', 'Elevation']
elevation1Display.ScaleTransferFunction = 'PiecewiseFunction'
elevation1Display.OpacityArray = ['POINTS', 'Elevation']
elevation1Display.OpacityTransferFunction = 'PiecewiseFunction'
elevation1Display.DataAxesGrid = 'GridAxesRepresentation'
elevation1Display.PolarAxes = 'PolarAxesRepresentation'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from ttkCinemaDarkroomFXAA1
ttkCinemaDarkroomFXAA1Display = Show(ttkCinemaDarkroomFXAA1, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'FXAA'
fXAALUT = GetColorTransferFunction('FXAA')
fXAALUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 220.83647796503186, 0.865003, 0.865003, 0.865003, 441.6729559300637, 0.705882, 0.0156863, 0.14902]
fXAALUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
ttkCinemaDarkroomFXAA1Display.Representation = 'Surface'
ttkCinemaDarkroomFXAA1Display.ColorArrayName = ['POINTS', 'FXAA']
ttkCinemaDarkroomFXAA1Display.LookupTable = fXAALUT
ttkCinemaDarkroomFXAA1Display.MapScalars = 0
ttkCinemaDarkroomFXAA1Display.Ambient = 1.0
ttkCinemaDarkroomFXAA1Display.Diffuse = 0.0
ttkCinemaDarkroomFXAA1Display.OSPRayScaleArray = 'Depth'
ttkCinemaDarkroomFXAA1Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkCinemaDarkroomFXAA1Display.SelectOrientationVectors = 'Depth'
ttkCinemaDarkroomFXAA1Display.ScaleFactor = 102.30000000000001
ttkCinemaDarkroomFXAA1Display.SelectScaleArray = 'Depth'
ttkCinemaDarkroomFXAA1Display.GlyphType = 'Arrow'
ttkCinemaDarkroomFXAA1Display.GlyphTableIndexArray = 'Depth'
ttkCinemaDarkroomFXAA1Display.GaussianRadius = 5.115
ttkCinemaDarkroomFXAA1Display.SetScaleArray = ['POINTS', 'Depth']
ttkCinemaDarkroomFXAA1Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkCinemaDarkroomFXAA1Display.OpacityArray = ['POINTS', 'Depth']
ttkCinemaDarkroomFXAA1Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkCinemaDarkroomFXAA1Display.DataAxesGrid = 'GridAxesRepresentation'
ttkCinemaDarkroomFXAA1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkCinemaDarkroomFXAA1Display.ScaleTransferFunction.Points = [0.89214026927948, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkCinemaDarkroomFXAA1Display.OpacityTransferFunction.Points = [0.89214026927948, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'FXAA'
fXAAPWF = GetOpacityTransferFunction('FXAA')

# get opacity transfer function/opacity map for 'Elevation'
elevationPWF = GetOpacityTransferFunction('Elevation')
elevationPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveView(renderView2)
SetActiveSource(ttkCinemaDarkroomFXAA1)
# ----------------------------------------------------------------