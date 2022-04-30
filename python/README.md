This directory contains one particular Python script,
[run.py](./run.py), whose job is to run all other scripts located in
the same directory. These scripts will generate VTK datasets or CSV
outputs, stored in the `output_datasets` sub-directory. For each of
these outputs, a [SHA-1](https://en.wikipedia.org/wiki/SHA-1) digest
is computed and stored in alphabetical order in JSON format in a file
named `res.json` that resides in the current folder.

This `res.json` file can be renamed and compared to a future run of
the `run.py` script to check if the script outputs have changed. This
is the role of the platform files in the `python/hashes`
directory. These files store the hashes for the TTK GitHub Actions CI
(Ubuntu, macOS, Windows); the CI should print their content at the end
of the `Run ttk-data Python scripts` job log of the `test_build`
workflow. This allow for the hashes to be updated by overwriting the
files with the CI results.
