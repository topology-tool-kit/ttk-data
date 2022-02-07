#!/usr/bin/env python3

import argparse
import multiprocessing
import os
import pathlib
import resource
import time

from paraview import simple

OUTPUT_DIR = "tests/output_screenshots"


def gen_screenshot(state, dest=OUTPUT_DIR):
    for i, view in enumerate(simple.GetViews()):
        simple.SaveScreenshot(f"{dest}/{state.stem}_{i}.png", view)
        print(f"{state}: view #{i} saved")
    simple.ResetSession()


def process_pvsm(state, dest):
    simple.LoadState(str(state))
    gen_screenshot(state, dest)


def process_py(state, dest):
    with open(state, "r") as st:
        # pylint: disable=W0122
        exec(st.read())
    gen_screenshot(state, dest)


def run_one(state_file, dest):
    if not state_file.exists():
        raise FileNotFoundError

    print(f"Processing {state_file.name}")
    start_time = time.time()

    {".pvsm": process_pvsm, ".py": process_py}[state_file.suffix](state_file, dest)

    duration = round(time.time() - start_time, 3)
    mem = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
    # pretty-print memory usage
    if mem > 1000:
        mem = f"{round(mem / 1000, 2)} GB"
    else:
        mem = f"{mem} MB"
    print(f"Processed {state_file.name} (took {duration} s, {mem})")


def run_all(dest):
    p = pathlib.Path(os.path.realpath(__file__)).parents[1]
    os.chdir(p)

    fails = []

    # create destination directory
    try:
        os.mkdir(dest)
    except FileExistsError:
        pass

    p = p / "states"
    for gl in ["*.pvsm", "*.py"]:
        for state in sorted(p.glob(gl)):
            # keep instances isolated (fix segfaults)
            proc = multiprocessing.Process(
                target=run_one,
                args=(state, dest),
            )
            proc.start()
            proc.join()
            if proc.exitcode != 0:
                fails.append(state.name)

    print(f"Failing cases: {fails}")


def main():
    parser = argparse.ArgumentParser(
        description="Run either one or all state files, generate a screenshot per view"
    )
    parser.add_argument(
        "-i", "--input_state", type=pathlib.Path, help="State file to process"
    )
    parser.add_argument(
        "-d",
        "--dest_dir",
        help="Directory to store generated screenshots",
        default=OUTPUT_DIR,
    )
    args = parser.parse_args()

    if args.input_state:
        run_one(args.input_state, args.dest_dir)
    else:
        run_all(args.dest_dir)


if __name__ == "__main__":
    main()
