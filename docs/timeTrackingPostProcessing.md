# Time Tracking Post-Processing

![Time tracking screenshot placeholder](https://topology-tool-kit.github.io/img/gallery/timeTracking.jpeg)

## Pipeline description

This example loads a 2D time-varying scalar field, where time steps are
stored as a sequence of data arrays, and tracks its extrema over time with
[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html).
As in the [Time Tracking](https://topology-tool-kit.github.io/examples/timeTracking/)
and [Tracking From Critical Points](https://topology-tool-kit.github.io/examples/trackingFromCriticalPoints/)
examples, each extremum is followed from one time step to the next by solving
an optimal assignment problem between the persistence diagrams of consecutive
steps, controlled by the persistence threshold and the relative destruction
cost. Here, each tracked minimum captures an individual debris fragment
ejected by a hypervelocity impact, so that the raw output of the tracking is,
for every fragment, the sequence of its positions through the time-space
domain.

This example focuses on the post-processing stage of the filter (parameter
`Enablepostprocessing`), which turns these raw, frame-by-frame tracks into
clean, analyzable trajectories and enriches them with geometric attributes.
In particular, for each time step a merge-tree segmentation (parameter
`Computemergetreesegmentation`) isolates the region around every tracked
extremum and attaches to each trajectory the surface of its associated
feature, recovering a measure of its size in addition to its position.

The resulting trajectory mesh carries, for each fragment, its linearized
motion model (`ax`, `bx`, `ay`, `by`), its duration and its surface
statistics. A sequence of Threshold filters then isolates the fragments of
interest — by axial velocity (`ax`), duration (`Duration`), critical type
(minima) and spatial region of origin (`bx`, `by`) — and two derived plots
summarize the experiment: a crater profile, obtained by binning the impact
positions (`by`), and an ejection diagram, plotting the ejection angle
atan(`ay` / -`ax`) against the axial velocity -`ax`.

Beyond the two tracking parameters described in the other examples, the
post-processing is mainly tuned through merging and segmentation controls:
increase `Maxlinkpx` to allow longer reconnections between consecutive
trajectory segments (decrease it to keep only tight, unambiguous links), and
adjust `Maxsurfacesize` to bound the size of the segmented features (lower it
to discard oversized background regions). Enabling `Otsusimplification` is
recommended when the features sit on a noisy or slowly-varying background.

## ParaView

To reproduce the above screenshot, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter
the following command:

```
paraview states/timeTrackingPostProcessing.pvsm
```

## Python code

```python linenums="1"
--8<-- "python/timeTrackingPostProcessing.py"
```

To run the above Python script, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter
the following command:

```
pvpython python/timeTrackingPostProcessing.py
```

## Inputs

- [hvi.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/hvi.vti):
  2D time-varying scalar field capturing debris fragments ejected by a
  hypervelocity impact, with each time step stored as a separate data array.

## Outputs

- `debrisTrajectories.vtu`: space-time trajectories of the selected debris
  fragments.
- `crater_profile.csv`: debris mass (mg) binned by centered vertical impact position (mm).
- `ejection_angle.csv`: ejection angle (°) versus axial velocity (m/s) per fragment.

## C++/Python API

[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html)
