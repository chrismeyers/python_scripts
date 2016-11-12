#! /usr/bin/env python3

import os
import sys
import time

def wait_until_writable():
	print("Waiting for " + file_name + " to become writable ", end="", flush=True)
	while not is_writable():
		print(". ", end="", flush=True)
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			sys.exit(2)

	print(file_name + " is now writable!")


def is_writable():
	return os.access(file_name, os.W_OK)


def display_usage():
	print("Supply a read-only file.")


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		file_name = sys.argv[1]
		if not is_writable():
			wait_until_writable()
		else:
			display_usage()
	else:
		display_usage()
