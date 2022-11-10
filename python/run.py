import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import time

OUTPUT_DIR = pathlib.Path(os.path.realpath(__file__)).parent / "output_datasets"


class TestCase:
    def __init__(self, file):
        self._file = file
        self._case_name = file.stem

    def name(self):
        return self._case_name

    def __enter__(self):
        """Modify Python scripts to overload the written file names"""

        pattern = r"SaveData\(\s*(\"|\')(.*)(\"|\'),"
        regex = re._compile(pattern, re.MULTILINE)

        def replace(term):
            outfile = term.group(2)
            return f'SaveData("{OUTPUT_DIR / self._case_name}_{outfile}",'

        with self._file.open() as src:
            altered = regex.sub(replace, src.read())

            # handle TTKCinemaWriter in cinemaIO.py
            if "cinemaIO" in self._case_name:
                cdb_name = "ViscousFingersSampled.cdb"
                altered = altered.replace(cdb_name, f"{OUTPUT_DIR / cdb_name}")
                altered = altered.replace(cdb_name, f"{self._case_name}_{cdb_name}")

        if os.name == "nt":
            # escape all backslashes
            altered = altered.replace("\\", "\\\\")

        with self._file.open("w") as dst:
            dst.write(altered)

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Clean modified file with git"""
        subprocess.check_call(["git", "checkout", str(self._file)])

    def run(self):
        """Run modified Python script"""
        print(f"Executing {self._case_name}...")
        start_time = time.time()
        try:
            subprocess.check_call([sys.executable, str(self._file)])
            duration = round(time.time() - start_time, 3)
            print(f" > {self._case_name} executed (took {duration}s)...\n")
            return True
        except subprocess.CalledProcessError:
            print(f" > Error running {self._case_name}")
            return False

    def get_digests(self):
        """Gather the digests of the generated datasets"""
        output_hashes = {}
        for dataset in OUTPUT_DIR.glob(f"{self._case_name}_*"):
            if dataset.is_file():
                output_hashes[str(dataset.stem)] = compute_digest(dataset)
            elif dataset.is_dir():
                for item in dataset.glob("**/*"):
                    if item.is_file():
                        output_hashes[str(item.stem)] = compute_digest(item)
        return output_hashes


def compute_digest(dataset):
    """Compute the SHA1 digest of the given dataset"""
    ds_hash = hashlib.sha1()
    with dataset.open("rb") as src:
        for chunk in iter(lambda: src.read(65536), b""):
            ds_hash.update(chunk)
    return ds_hash.hexdigest()


def main():
    # go to ttk-data's root folder
    p = OUTPUT_DIR.parents[1]
    os.chdir(p)

    # create output directory if it doesn't exist
    try:
        OUTPUT_DIR.mkdir()
    except FileExistsError:
        pass

    res = {}
    fails = []
    for script in sorted(p.glob("python/*.py")):
        if "run.py" in str(script):
            # skip current script
            continue

        with TestCase(script) as ts:
            # run test and register failures
            if not ts.run():
                fails.append(ts.name())
            res.update(ts.get_digests())

    with (OUTPUT_DIR.parent / "res.json").open("w") as dst:
        # sort res by key (filename)
        res = dict(sorted(res.items()))
        json.dump(res, dst, indent=4)
        dst.write("\n")

    print(f"Failing cases: {fails}")

    if len(fails) > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
