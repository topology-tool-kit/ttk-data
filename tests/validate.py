import argparse
import os
import pathlib
import shutil

import run
import compare_screenshots

REF_DIR = "tests/reference_screenshots"
OUTPUT_DIR = run.OUTPUT_DIR
THRESHOLD = 1


def main(gen_ref=False, only_comp=False):
    # change working directory to ttk-data root folder
    p = pathlib.Path(os.path.realpath(__file__)).parents[1]
    os.chdir(p)

    if gen_ref:
        run.run_all(REF_DIR)
    else:
        if not only_comp:
            # clean output directory
            try:
                shutil.rmtree(OUTPUT_DIR)
            except FileNotFoundError:
                pass
            # run all states
            run.run_all(OUTPUT_DIR)
        p = p / REF_DIR
        for img in sorted(p.glob("*.png")):
            threshold = THRESHOLD
            if img.name == "harmonicSkeleton_1.png":
                # Reeb Graph depends on non stable Harmonic Field output
                threshold = 50
            ident, err = compare_screenshots.main(
                f"{OUTPUT_DIR}/{img.name}", str(img), threshold
            )
            if not ident:
                print(f"Error for {img.name}: {err}")


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
    args = parser.parse_args()

    main(args.generate_reference, args.only_compare)
