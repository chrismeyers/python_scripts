#!/usr/bin/env bash

# This script performs the required steps to change the PHP version used by
# apache:
#   1. Determine the available PHP versions and update the ~/.PHP_VERSION file.
#   2. Source the ~/.PHP_VERSION file to update the $PHP_VERSION environment
#      variable
#   3. Stop and start apache to reflect the $PHP_VERSION changes (calling 
#      restart alone doesn't work).

/usr/bin/env python3 /Users/chris/Documents/Development/python-dev/python_scripts/setPHPVersion.py $1

if [ $? -eq 0 ] && [ "$1" != "-h" ]; then
  echo "Sourcing $HOME/.PHP_VERSION..."
  source $HOME/.PHP_VERSION

  echo "Stopping apache..."
  sudo apachectl stop
  echo "Starting apache..."
  sudo apachectl start
fi
