#!/usr/bin/env python3

import argparse
import multiprocessing
import os
import pathlib
import resource
import time

from paraview import simple

OUTPUT_DIR = "tests/output_screenshots"


def gen_screenshot(state, dest=OUTPUT_DIR, resFactor=1):
    for i, view in enumerate(simple.GetViews()):
        resX, resY = view.ViewSize
        resX *= resFactor
        resY *= resFactor

        simple.SaveScreenshot(f"{dest}/{state.stem}_{i}.png", view, ImageResolution=[resX, resY])
        print(f"{state}: view #{i} saved, with resolution {resX}x{resY}")
    simple.ResetSession()


def process_pvsm(state, dest, resFactor=1):
    simple.LoadState(str(state))
    gen_screenshot(state, dest, resFactor)


def process_py(state, dest, resFact=1):
    with open(state, "r") as st:
        # pylint: disable=W0122
        exec(st.read())
    gen_screenshot(state, dest, resFact)


def run_one(state_file, dest, resFact=1):
    if not state_file.exists():
        raise FileNotFoundError

    print(f"Processing {state_file.name}")
    start_time = time.time()


    {".pvsm": process_pvsm, ".py": process_py}[state_file.suffix](state_file, dest, resFact)
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
    timings = {}
    for gl in ["*.pvsm", "*.py"]:
        for state in sorted(p.glob(gl)):
            # keep instances isolated (fix segfaults)
            start = time.time()
            proc = multiprocessing.Process(
                target=run_one,
                args=(state, dest),
            )
            proc.start()
            proc.join()
            if proc.exitcode != 0:
                fails.append(state.name)

            timings[state.name] = round(time.time() - start, 3)

    print(f"Failing cases: {fails}")
    for k, v in timings.items():
        print(f"- {k} took {v} s")


def main():
    parser = argparse.ArgumentParser(
        description="Run either one or all state files, generate a screenshot per view"
    )
    parser.add_argument(
        "-r", "--res_factor", type=int, help="Resolution factor for output pics",
    )
    default=1
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
        run_one(args.input_state, args.dest_dir, args.res_factor)
    else:
        run_all(args.dest_dir)


if __name__ == "__main__":
    main()
