#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [735, 551]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.0398357716009758, -0.01795783025812699, -0.46122550265265816]
renderView1.CameraFocalPoint = [0.16902173604025894, -0.004361312755364503, 0.018754563656392977]
renderView1.CameraViewUp = [0.0210861737723549, 0.9997282828918428, 0.009936481357587061]
renderView1.CameraFocalDisk = 1.0
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [736, 551]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [1023.5, 511.5, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [956.8623929885804, 526.5127215086243, 4420.833889881707]
renderView2.CameraFocalPoint = [956.8623929885804, 526.5127215086243, 0.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 645.8688162225527
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView2)
layout1.AssignView(2, renderView1)

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
cinemaReader = TTKCinemaReader(DatabasePath='GroundWater.cdb')

# create a new 'TTK CinemaQuery'
cinemaQuery = TTKCinemaQuery(InputTable=cinemaReader)
cinemaQuery.SQLStatement = """SELECT * FROM InputTable0
ORDER BY Description
"""
# create a new 'TTK CinemaProductReader'
cinemaProductReader = TTKCinemaProductReader(Input=cinemaQuery)

# create a new 'Elevation'
elevation = Elevation(Input=cinemaProductReader)
elevation.LowPoint = [-0.3657500147819519, 0.007758498191833496, -0.00749649852514267]
elevation.HighPoint = [0.467739999294281, 0.007758498191833496, -0.00749649852514267]

# create a new 'TTK Darkroom Camera'
darkroomCamera1 = TTKDarkroomCamera()
darkroomCamera1.Position = [1.0340093061551408, -0.01662681994245655, -0.47183399527637365]
darkroomCamera1.Up = [0.0210861737723549, 0.9997282828918428, 0.009936481357587061]
darkroomCamera1.FocalPoint = [0.1631952705944235, -0.0030303024396940645, 0.008146071032677569]

# create a new 'TTK CinemaImaging'
cinemaImaging = TTKCinemaImaging(Dataset=elevation,
    SamplingGrid=darkroomCamera1)
cinemaImaging.Resolution = [2048, 1024]
cinemaImaging.ProjectionMode = 'Perspective'
cinemaImaging.Angle = 50.0

# create a new 'TTK Extract'
extract1 = TTKExtract(Input=cinemaImaging)
extract1.Expression = '1'
extract1.OutputType = 'vtkMultiBlockDataSet'
extract1.ImageBounds = [0.0, 2047.0, 0.0, 1023.0, 0.0, 0.0]
extract1.InputArray = ['POINTS', 'Depth']

# create a new 'TTK Darkroom ColorMapping'
darkroomColorMapping1 = TTKDarkroomColorMapping(Input=extract1)
darkroomColorMapping1.SingleColor = [0.0, 0.6666666666666666, 1.0]
darkroomColorMapping1.Scalars = ['POINTS', 'Elevation']
darkroomColorMapping1.ColorMap = 'Single'

# create a new 'TTK Extract'
extract2 = TTKExtract(Input=cinemaImaging)
extract2.Expression = '0'
extract2.OutputType = 'vtkMultiBlockDataSet'
extract2.ImageBounds = [0.0, 255.0, 0.0, 255.0, 0.0, 0.0]
extract2.InputArray = ['POINTS', 'Depth']

# create a new 'TTK Darkroom ColorMapping'
darkroomColorMapping2 = TTKDarkroomColorMapping(Input=extract2)
darkroomColorMapping2.Scalars = ['POINTS', 'Elevation']
darkroomColorMapping2.ColorMap = 'OrRd'

# create a new 'TTK Darkroom Compositing'
darkroomCompositing1 = TTKDarkroomCompositing(Input=[darkroomColorMapping1, darkroomColorMapping2])
darkroomCompositing1.Depth = ['POINTS', 'Depth']

# create a new 'TTK Darkroom SSAO'
darkroomSSAO1 = TTKDarkroomSSAO(Input=darkroomCompositing1)
darkroomSSAO1.Depth = ['POINTS', 'Depth']

# create a new 'TTK Darkroom SSSAO'
darkroomSSSAO1 = TTKDarkroomSSSAO(Input=darkroomSSAO1)
darkroomSSSAO1.Depth = ['POINTS', 'Depth']
darkroomSSSAO1.Samples = 128
darkroomSSSAO1.Radius = 0.1

# create a new 'TTK Darkroom IBS'
darkroomIBS1 = TTKDarkroomIBS(Input=darkroomSSSAO1)
darkroomIBS1.Color = ['POINTS', 'Diffuse']
darkroomIBS1.Depth = ['POINTS', 'Depth']
darkroomIBS1.AO = ['POINTS', 'SSSAO']
darkroomIBS1.Strength = 500.0
darkroomIBS1.Luminance = 0.1
darkroomIBS1.Ambient = 0.5

# create a new 'TTK Darkroom SSDoF'
darkroomSSDoF1 = TTKDarkroomSSDoF(Input=darkroomIBS1)
darkroomSSDoF1.Color = ['POINTS', 'IBS']
darkroomSSDoF1.Depth = ['POINTS', 'Depth']
darkroomSSDoF1.Aperture = 0.2
darkroomSSDoF1.FocalDepth = 0.36
darkroomSSDoF1.MaxBlur = 0.08

# create a new 'TTK Darkroom FXAA'
darkroomFXAA1 = TTKDarkroomFXAA(Input=darkroomSSDoF1)
darkroomFXAA1.Color = ['POINTS', 'SSDoF']

# create a new 'TTK Extract'
extract3 = TTKExtract(Input=darkroomFXAA1)
extract3.Expression = '0'
extract3.OutputType = 'vtkImageData'
extract3.ImageBounds = [0.0, 2047.0, 0.0, 1023.0, 0.0, 0.0]
extract3.InputArray = ['POINTS', 'FXAA']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from elevation
elevationDisplay = Show(elevation, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
elevationDisplay.Representation = 'Surface'
elevationDisplay.ColorArrayName = ['POINTS', '']
elevationDisplay.OSPRayScaleArray = 'Elevation'
elevationDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
elevationDisplay.SelectOrientationVectors = 'Elevation'
elevationDisplay.ScaleFactor = 0.0833490014076233
elevationDisplay.SelectScaleArray = 'Elevation'
elevationDisplay.GlyphType = 'Arrow'
elevationDisplay.GlyphTableIndexArray = 'Elevation'
elevationDisplay.GaussianRadius = 0.004167450070381165
elevationDisplay.SetScaleArray = ['POINTS', 'Elevation']
elevationDisplay.ScaleTransferFunction = 'PiecewiseFunction'
elevationDisplay.OpacityArray = ['POINTS', 'Elevation']
elevationDisplay.OpacityTransferFunction = 'PiecewiseFunction'
elevationDisplay.DataAxesGrid = 'GridAxesRepresentation'
elevationDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from darkroomCamera1
darkroomCamera1Display = Show(darkroomCamera1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
darkroomCamera1Display.Representation = 'Surface'
darkroomCamera1Display.ColorArrayName = [None, '']
darkroomCamera1Display.OSPRayScaleArray = 'CamFocalPoint'
darkroomCamera1Display.OSPRayScaleFunction = 'PiecewiseFunction'
darkroomCamera1Display.SelectOrientationVectors = 'CamFocalPoint'
darkroomCamera1Display.ScaleFactor = 0.1
darkroomCamera1Display.SelectScaleArray = 'CamFocalPoint'
darkroomCamera1Display.GlyphType = 'Arrow'
darkroomCamera1Display.GlyphTableIndexArray = 'CamFocalPoint'
darkroomCamera1Display.GaussianRadius = 0.005
darkroomCamera1Display.SetScaleArray = ['POINTS', 'CamFocalPoint']
darkroomCamera1Display.ScaleTransferFunction = 'PiecewiseFunction'
darkroomCamera1Display.OpacityArray = ['POINTS', 'CamFocalPoint']
darkroomCamera1Display.OpacityTransferFunction = 'PiecewiseFunction'
darkroomCamera1Display.DataAxesGrid = 'GridAxesRepresentation'
darkroomCamera1Display.PolarAxes = 'PolarAxesRepresentation'
darkroomCamera1Display.ScalarOpacityUnitDistance = 0.0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
darkroomCamera1Display.ScaleTransferFunction.Points = [0.0531746282763316, 0.0, 0.5, 0.0, 0.05318225920200348, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
darkroomCamera1Display.OpacityTransferFunction.Points = [0.0531746282763316, 0.0, 0.5, 0.0, 0.05318225920200348, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from extract3
extract3Display = Show(extract3, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
extract3Display.ColorArrayName = ['POINTS', 'FXAA']
extract3Display.Representation = 'Slice'
extract3Display.MapScalars = 0

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(extract3)
SetActiveView(renderView2)
# ----------------------------------------------------------------