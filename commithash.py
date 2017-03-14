#!/usr/bin/env python
import subprocess
import sys
import os
import re
import argparse

valid_version = re.compile("^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(-(?P<commits>\d+)-g(?P<hash>[0-9a-fA-F]+)-?(?P<dirty>d)?)?$")


def write_file_if_different(filename, new_contents):
    existing_contents = ""

    if (os.path.isfile(filename)):
        with open(filename, "r") as input_file:
            existing_contents = input_file.read()

    if existing_contents != new_contents:
        with open(filename, "w") as output_file:
            output_file.write(new_contents)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('template', help='Template filename. Formatted with Python String Formatting')
    parser.add_argument('-o', '--output', help='Output filename. Default prints to stdout.')

    args = parser.parse_args()

    try:
        # Define the subprocess to extract the current commit hash using git.
        proc = subprocess.Popen(['git', 'describe', '--dirty=-d', '--long'], stdout=subprocess.PIPE)

        # Call the command, and extract the standard output.
        stdout, stderr = proc.communicate()

        # If the git command exited successfully, then output the commithash.h file.
        if proc.returncode == 0:
            git_describe = stdout.strip().decode('utf-8')
            match = valid_version.match(git_describe)

            if match:
                version = match.groupdict()
                version['dirty'] = bool(version['dirty'])

                if version['dirty']:
                    print("\x1b[41mWarning: working tree is dirty!\x1b[0m")

                template = open(args.template, "r").read()
                output = template.format(**version)

                if (args.output):
                    write_file_if_different(args.output, output)
                else:
                    print(output)
            else:
                sys.exit('Invalid git-describe output. Got {} expected 1.2.3-0-g1234567'.format(git_describe))

        # Keep the return code of the git command. This will allow make to pick up any errors.
        sys.exit(proc.returncode)

    except OSError as e:
        # Touch 5 buildworld doesn't currently have git, python script is run by build script outside the chroot world
        sys.exit('Git not available. Required to extract version information.')
