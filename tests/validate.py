#!/usr/bin/env python3

import argparse
import os
import pathlib
import shutil
import sys

import vtk

import run

REF_DIR = "tests/reference_screenshots"
OUTPUT_DIR = run.OUTPUT_DIR


def compare_screenshots(png0, png1, threshold=0.0):
    # load the two input images
    img0 = vtk.vtkPNGReader()
    img0.SetFileName(png0)
    img0.Update()

    img1 = vtk.vtkPNGReader()
    img1.SetFileName(png1)
    img1.Update()

    # compare the two images
    imdiff = vtk.vtkImageDifference()
    imdiff.SetInputConnection(img0.GetOutputPort())
    imdiff.SetImageConnection(img1.GetOutputPort())
    imdiff.Update()

    err = round(imdiff.GetThresholdedError(), 3)

    if err > threshold:
        return (False, err)

    return (True, err)


def main(gen_ref=False, only_comp=False, keep_identical=False):
    # change working directory to ttk-data root folder
    p = pathlib.Path(os.path.realpath(__file__)).parents[1]
    os.chdir(p)

    if gen_ref:
        run.run_all(REF_DIR)
    else:
        passed = True
        if not only_comp:
            # clean output directory
            try:
                shutil.rmtree(OUTPUT_DIR)
            except FileNotFoundError:
                pass
            # run all states
            run.run_all(OUTPUT_DIR)

        # compare generated screenshots to reference
        p = p / REF_DIR
        for img in sorted(p.glob("*.png")):
            out_im = pathlib.Path(f"{OUTPUT_DIR}/{img.name}")
            if not out_im.exists():
                print(f"{out_im} does not exists, skipping...")
                continue
            ident, err = compare_screenshots(str(out_im), str(img))
            if not ident:
                print(f"Error for {img.name}: {err}")
                passed = False
            elif not keep_identical:
                # keep only the modified screenshots
                out_im.unlink()

        if passed:
            print("Validation passed!")
        else:
            sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ttk-data validation")
    parser.add_argument(
        "-r",
        "--generate_reference",
        action="store_true",
        help="Generate reference screenshots",
    )
    parser.add_argument(
        "-c",
        "--only_compare",
        action="store_true",
        help="Only compare already generated screenshots",
    )
    parser.add_argument(
        "-k",
        "--keep_identical",
        action="store_true",
        help="Keep generated screenshots that are identical to reference",
    )
    args = parser.parse_args()

    main(args.generate_reference, args.only_compare, args.keep_identical)
