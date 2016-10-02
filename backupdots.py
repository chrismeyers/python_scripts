#! /usr/bin/env python3

import os
import sys
from python_scripts.Utils import configParser
from python_scripts.Utils import fileUtils

def perform_backup():
	file_num = 1
	for file in backup_data:
		os.system("cp " + backup_data[file][0] + "/" + file + " " + backup_data[file][1])
		print(str(file_num).rjust(3) + "  Copied: " + file + " to " + backup_data[file][1])
		file_num += 1


if __name__ == "__main__":
	file_utils = fileUtils.FileUtils()
	config_parser = configParser.ConfigParser()

	dir_location = "."
	dir_name = ".config"
	file_name = "backups.config"
	
	full_path = file_utils.sanitized_full_path(dir_location, dir_name, file_name)

	if not os.path.exists(full_path):
		config_parser.make_config_dir(dir_location, dir_name)
		config_parser.make_config_file(file_utils.sanitized_path(dir_location, dir_name), file_name)

	backup_data = config_parser.parse_custom(full_path)

	perform_backup()
