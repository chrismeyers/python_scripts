#! /usr/bin/env python3

import os
import sys
import argparse
from python_scripts.Utils import myConfigParser
from python_scripts.Utils import fileUtils

def perform_backup():
	# Copies files to ../Dropbox/misc/dotfiles/...
	file_num = 1
	for file in backup_data:
		os.system("cp " + backup_data[file][0] + "/" + file + " " + backup_data[file][1])
		print(str(file_num).rjust(3) + "  Copied: " + file + " to " + backup_data[file][1])

		file_num += 1


def perform_restore():
	# Copies files from ../Dropbox/misc/dotfiles/... to original location.
	# Is the file exists, the current file is renamed to *.backup_ext.
	file_num = 1
	for file in backup_data:
		orig_file = backup_data[file][0] + "/" + file
		backup_file = backup_data[file][1] + "/" + file

		if os.path.exists(modify_path_for_existance_check(orig_file)):
			os.system("mv " + orig_file + " " + orig_file + backup_ext)

		os.system("cp " + backup_file + " " + orig_file)
		print(str(file_num).rjust(3) + "  Restored: " + file + " to " + backup_data[file][0])

		file_num += 1


def perform_cleanup():
	# Removes all *.backup_ext files generated from perform_restore().
	file_num = 1
	for file in backup_data:
		current_file = handle_files_with_spaces(backup_data[file][0] + "/" + file)

		if os.path.exists(modify_path_for_existance_check(current_file)):
			os.system("rm -f " + current_file)
			print(str(file_num).rjust(3) + "  Removed: " + current_file)

			file_num += 1


def handle_files_with_spaces(file_name):
	if file_name.endswith("'"):
		return file_name[:-1] + backup_ext + "'"
	else:
		return file_name + backup_ext


def modify_path_for_existance_check(file_name):
	return file_name.replace("'", "")


if __name__ == "__main__":
	file_utils = fileUtils.FileUtils()
	config_parser = myConfigParser.MyConfigParser()

	dir_location = "."
	dir_name = ".config"
	file_name = "backups.config"

	backup_ext = ".backupsav"

	arg_parser = argparse.ArgumentParser(description='Backup or restore configuration files.')
	arg_parser.add_argument('-b', '--backup', help='perform a backup based on files in ./.config/backups.config', action='store_true')
	arg_parser.add_argument('-r', '--restore', help='perform a restore based on files in ./.config/backups.config', action='store_true')
	arg_parser.add_argument('-c', '--cleanup', help='removes *' + backup_ext + ' files', action='store_true')
	args = arg_parser.parse_args()
	
	full_path = file_utils.sanitized_full_path(dir_location, dir_name, file_name)

	if not os.path.exists(full_path):
		config_parser.make_config_dir(dir_location, dir_name)
		config_parser.make_config_file(file_utils.sanitized_path(dir_location, dir_name), file_name)

	backup_data = config_parser.parse_custom(full_path)

	if args.backup:
		perform_backup()
	elif args.restore:
		perform_restore()
	elif args.cleanup:
		perform_cleanup()
	else:
		perform_backup()
