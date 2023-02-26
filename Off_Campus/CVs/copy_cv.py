import os
import glob
import sys
from style import cprint


def copy(directory, new_directory):
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    else:
        raise Exception("Directory already exists")

    all_files = glob.glob(os.path.join(directory, "*"))
    all_files_without_base = [os.path.basename(path) for path in all_files]
    all_files_without_base.sort()
    all_files.sort()
    for path in all_files:
        new_path = os.path.join(new_directory, os.path.basename(path))
        new_path = new_path.replace(directory, new_directory)
        os.system(f"cp -r {path} {new_path}")
        cprint(f"Copying {path} to {new_path}", "green")


if __name__ == "__main__":
    directory = sys.argv[1]
    new_directory = sys.argv[2]
    copy(directory, new_directory)
