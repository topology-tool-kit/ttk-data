#### import the simple module from the paraview
from paraview.simple import *

# create a new 'XML Image Data Reader'
builtInExamplevti = XMLImageDataReader(FileName=["BuiltInExample2.vti"])

#### Topological analysis of 'log(Rho)'

# extract the critical points using 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=builtInExamplevti)
tTKScalarFieldCriticalPoints1.ScalarField = ["POINTS", "log(Rho)"]

# covert these points to spheres using 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints3 = TTKIcospheresFromPoints(Input=tTKScalarFieldCriticalPoints1)
tTKIcospheresFromPoints3.Radius = 3.0

#### Topological analysis of 'log(s)'

# compute the 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=builtInExamplevti)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "log(s)"]

# compute the 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=tTKPersistenceDiagram1)

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = 0.0
threshold1.UpperThreshold = 999999999

# remove low persistence critical points using 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdMethod = "Between"
persistenceThreshold.LowerThreshold = 0.5
persistenceThreshold.UpperThreshold = 999999999

# simplify the field using 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=builtInExamplevti, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "log(s)"]

# create a new 'TTK Merge and Contour Tree' to compute the join tree
tTKJoinTree1 = TTKMergeTree(Input=tTKTopologicalSimplification1)
tTKJoinTree1.ScalarField = ["POINTS", "log(s)"]
tTKJoinTree1.TreeType = "Join Tree"
tTKJoinTree1.ArcSampling = 30

# covert the critical points to spheres using 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints4 = TTKIcospheresFromPoints(Input=tTKJoinTree1)
tTKIcospheresFromPoints4.Radius = 2.0

# extract the join tree arcs and save them as tubes
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=OutputPort(tTKJoinTree1, 1))
tTKGeometrySmoother2.IterationNumber = 300

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube5 = Tube(Input=extractSurface4)
tube5.Radius = 0.25

# Extract the segmentation region corresponding to the interaction site
threshold6 = Threshold(Input=OutputPort(tTKJoinTree1, 2))
threshold6.Scalars = ["POINTS", "RegionType"]

# create a new 'Threshold'
threshold7 = Threshold(Input=threshold6)
threshold7.Scalars = ["POINTS", "SegmentationId"]
threshold7.ThresholdMethod = "Between"
threshold7.LowerThreshold = 13.0
threshold7.UpperThreshold = 13.0

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=threshold7)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=extractSurface5)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(Input=tetrahedralize1)
tTKGeometrySmoother3.IterationNumber = 10

# save the output
SaveData("logRhoCriticalPoints.vtp", tTKIcospheresFromPoints3)
SaveData("logSPersistenceCurve.csv", OutputPort(tTKPersistenceCurve1, 0))
SaveData("logSPersistenceDiagram.vtu", tTKPersistenceDiagram1)
SaveData("logSJoinTreeCriticalPoints.vtp", tTKIcospheresFromPoints4)
SaveData("logSJoinTreeArcs.vtp", tube5)
SaveData("NonCovalentInteractionSite.vtu", tTKGeometrySmoother3)
