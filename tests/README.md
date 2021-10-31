This directory contains two Python scripts, [run.py](./run.py) and
[validate.py](./validate.py), used for validating all ttk-data state
files with new TTK releases.

The first script, [run.py](./run.py), generates PNG screenshots for
every state files. Just call `python3 run.py` or `python3
tests/run.py` to generate a PNG per view of every state file. These
PNGs will be stored by default under `tests/output_screenshots`. To
generate screenshots for only one state file, use `python3
tests/run.py -i states/file` (from the root `ttk-data` directory,
which contains the pipeline inputs).

The second script, [validation.py](validation.py), compares generated
screenshots from `tests/output_screenshots` to a refererence stored in
`tests/reference_screenshots`. By default, it will also run the
[run.py](./run.py) script to generate the current screenshots to be
compared. Use `python3 validate.py -c` to skip the screenshots
generation and only compare previoulsy generated screenshots.

To generate a new reference, use `python3 validate.py -r`. Please note
that the reference is dependent on the following factors:
* to be independent of the display resolution, an offscreen ParaView
  renderer (OSMesa on Linux) is recommended.
* macOS'offscreen renderer has some inconsistencies with Linux'.
* Windows segfaults during offscreen rendering.
* the TTKDimensionReduction filter ouput depends on the version of the
  Scikit-learn Python package. Please use a recent Scikit-learn (use
  pip on Ubuntu, the system package on ArchLinux).
* the HarmonicSkeleton state file depends on the
  `Eigen::ConjugateGradient` iterative solver, which is
  non-deterministic. The image comparison threshold has been increased
  for this state file accordingly.
* some filters, such as FTMTree, may have a non-deterministic output
  when used in a highly parallel context. Reducing the parallelism by
  setting UseAllCores to `false` in the affected state files might be
  necessary to ensure a deterministic output.

As a consequence, to reproduce the current reference, the following is required:
* a Linux OS
* an OSMesa installation of ParaView (configured with
  `-DPARAVIEW_USE_QT=OFF -DVTK_USE_X=OFF -DVTK_OPENGL_HAS_OSMESA=ON`)
* a pip-installed Scikit-Learn
* see [the automatic test yml
  script](https://github.com/topology-tool-kit/ttk/blob/dev/.github/workflows/test.yml)
  for installation examples.
