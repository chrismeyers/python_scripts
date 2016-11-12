#! /usr/bin/env python3

import os
import sys

class FileUtils:
    def remove_if_exists(self, full_path):
        if os.path.exists(full_path):
            print(full_path + " already exists. Overwite? [y/n]")

            try:
                answer = input().lower()
            except KeyboardInterrupt:
                sys.exit(1)

            if answer == "y" or answer == "yes":
                print("Overwriting " + full_path + " ...")
                if os.path.isdir(full_path):
                    os.system("rm -rf " + full_path)
                else:
                    os.system("rm -f " + full_path)
                return True
            else:
                print(full_path + " NOT changed...")
                return False
        else:
            return True


    def sanitized_path(self, location, name):
        sanitized_location = location
        sanitized_name = name

        if location.endswith("/"):
            sanitized_location = location[:-1]

        if name.startswith("/"):
            sanitized_name = name[1:]

        return sanitized_location + "/" + sanitized_name


    def sanitized_full_path(self, dir_location, dir_name, file_name):
        sanitized_dir_location = dir_location
        sanitized_dir_name = dir_name
        sanitized_file_name = file_name

        if dir_location.endswith("/"):
            sanitized_dir_location = dir_location[:-1]

        if dir_name.startswith("/"):
            sanitized_dir_name = dir_name[1:]
        if dir_name.endswith("/"):
            sanitized_dir_name = dir_name[:-1]

        if file_name.startswith("/"):
            sanitized_file_name = file_name[1:]

        return sanitized_dir_location + "/" + sanitized_dir_name + "/" + sanitized_file_name


if __name__ == "__main__":
    print("FileUtils main")
