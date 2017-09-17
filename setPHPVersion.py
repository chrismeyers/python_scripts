#!/usr/bin/env python3

'''
usage: setPHPVersion.py [-h]

Determines which PHP versions are installed via Homebrew and updates the
~/.PHP_VERSION file.

optional arguments:
  -h, --help  show this help message and exit
'''

import sys
import os
import argparse
import subprocess
import re

def get_homebrew_php_versions():
    print("Determining available PHP versions installed via Homebrew...")

    brew_list = subprocess.check_output(["brew", "list"]).decode(sys.stdout.encoding).strip().replace("\n", " ")
    matches = re.findall(r"php[\d][\d]", brew_list)

    # Put the matches in a set to remove duplicates, then put it back in a list.
    unique_versions = list(set(matches))

    version_numbers = []
    for version in unique_versions:
        # Get version number: 71 from php71
        version_numbers.append(version[-2:])
        
    version_numbers.sort()

    return version_numbers


def get_selected_php_version():
    print("The following PHP versions are installed:")

    num = 1
    for version in versions:
        print("\t{}. php{}".format(num, version))
        num += 1

    try:
        input_number = input("Please select a number: ")
    except KeyboardInterrupt:
        print("\nScript cancelled.  $PHP_VERSION was NOT changed.")
        sys.exit(1)

    if input_number.isdigit() and int(input_number) > 0 and int(input_number) <= len(versions):
        return int(input_number)
    else:
        print("Invalid number selected.  $PHP_VERSION was NOT changed.")
        sys.exit(1)


def update_php_version_file():
    with open(os.path.expanduser("~/.PHP_VERSION"), "w") as version_file:
        version_file.write('export PHP_VERSION="{}"'.format(str(versions[selected - 1])))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Determines which PHP versions are installed via Homebrew and updates the ~/.PHP_VERSION file.")
    args = arg_parser.parse_args()

    versions = get_homebrew_php_versions()
    selected = get_selected_php_version()
    update_php_version_file()
