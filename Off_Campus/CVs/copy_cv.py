#!/usr/bin/python3
import os
import glob
import sys
from style import cprint

DIRS = [
    "data_analyst",
    "finance",
    "ML_DL",
]


def search_dir(directory):
    for dir in DIRS:
        if directory in os.listdir(dir):
            return os.path.join(dir, directory), dir


def copy(directory, new_directory):
    directory_c = directory
    new_directory_c = new_directory
    directory, base_dir = search_dir(directory)
    new_directory = os.path.join(base_dir, new_directory)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    else:
        raise BaseException("Directory already exists")

    all_files = glob.glob(os.path.join(directory, "*"))
    all_files_without_base = [os.path.basename(path) for path in all_files]
    # all_files_without_base = [
    #     os.path.join(base_dir, path) for path in all_files_without_base
    # ]
    all_files_without_base.sort()
    all_files.sort()
    for path in all_files:
        new_path = os.path.join(new_directory, os.path.basename(path))
        # if new_directory in new_path:
        #     pass
        # else:
        new_path = new_path.replace(directory_c, new_directory_c)
        os.system(f"cp -r {path} {new_path}")
        cprint(f"Copying {path} to {new_path}", "green")


if __name__ == "__main__":
    directory = sys.argv[1]
    new_directory = sys.argv[2]
    cprint(f"Copying {directory} to {new_directory}", "red")
    copy(directory, new_directory)
