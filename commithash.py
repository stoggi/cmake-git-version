#!/usr/bin/env python
import subprocess
import sys
import os

# Define our header template
header_template = """
#ifndef COMMITHASH_H
#define COMMITHASH_H

extern const char COMMIT_HASH[20];

#endif
"""


# Define our source template
source_template = """
#include "commithash.h"

const char COMMIT_HASH[20] = "{value}";
"""


def replace_file_if_different(filename, new_contents):
    existing_contents = ""

    if (os.path.isfile(filename)):
        with open(filename, "r") as input_file:
            existing_contents = input_file.read()

    if existing_contents != new_contents:
        with open(filename, "w") as output_file:
            output_file.write(new_contents)


# Define the subprocess to extract the current commit hash using git.
proc = subprocess.Popen(['git', 'describe', '--dirty=*'], stdout=subprocess.PIPE)

# Call the command, and extract the standard output.
out, err = proc.communicate()

# If the git command exited successfully, then output the commithash.h file.
if proc.returncode == 0:
    commit_hash = out.strip().decode('utf-8')

    if "*" in commit_hash:
        print("\x1b[41mWarning: working tree is dirty!\x1b[0m")

    replace_file_if_different("commithash.h", header_template)
    replace_file_if_different("commithash.c", source_template.format(value=commit_hash))

# Keep the return code of the git command. This will allow make to pick up the error.
sys.exit(proc.returncode)
