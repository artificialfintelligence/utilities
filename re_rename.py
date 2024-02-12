#!/usr/bin/env python

# pylint: disable=C0114

import os
import re
import sys


def rename_files(path, pattern, replacement):
    """Rename files that match a regular expression.

    Args:
        path (str): The path to the root directory to start renaming files.
        pattern (str): The pattern to match in the file.
        replacement (str): The replacement text for the matched pattern.
    """
    count = 0
    for root, _, files in os.walk(path):
        for f in files:
            if re.search(pattern, f):
                old_file = os.path.join(root, f)
                new_file = os.path.join(root, re.sub(pattern, replacement, f))
                os.rename(old_file, new_file)
                count += 1
    print(f"\nRenamed {count} files.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} path pattern replacement")
        sys.exit(1)
    print("\033[31;5m\n ! ! ! ! ! WARNING ! ! ! ! !\n\033[0m")
    print(
        f"You are potentially about to batch-rename a whole bunch of files under the following root directory or anywhere under its subdirectories, recursively.\n"
        f"This is a one-way operation. There is no undo. You will need to manually revert the changes if you make a mistake.\n"
        f"Note: Directories will not be renamed. Only files.\n\n"
        f"Root dir: {sys.argv[1]}"
    )
    while response := input("\nAre you sure you want to continue? (y/n): "):
        if response.lower() in {"y", "n"}:
            break
    if response.lower() == "y":
        rename_files(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("\nExiting without making any changes.")
