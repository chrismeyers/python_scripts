#! /usr/bin/env python3

import os
import sys
import json
import argparse
from python_scripts.Utils import fileUtils

class MyConfigParser:
    file_utils = fileUtils.FileUtils()

    def parse_custom(self, file_path):
        parsed = {}

        with open(file_path) as f:
              for line in f:
                  line = line.strip().replace("\n", "")
                  if (not line.startswith("#")) and (line != ""):
                      parts = line.split("|")
                      if len(parts) == 3:
                          parsed[parts[0].strip()] = [parts[1].strip(), parts[2].strip()]

        return parsed


    def parse_json(self, file_path):
        with open(file_path) as f:
            data = json.load(f)

        return data


    def make_config_dir(self, location, name):
        full_path = self.file_utils.sanitized_path(location, name)

        if self.file_utils.remove_if_exists(full_path):
            os.system("mkdir " + full_path)


    def make_config_file(self, location, name):
        full_path = self.file_utils.sanitized_path(location, name)
        
        if self.file_utils.remove_if_exists(full_path):
            os.system("touch " + full_path)
            os.system("chmod 755 " + full_path)


if __name__ == "__main__":
    config_parser = MyConfigParser()

    desc = ('Utility class that provides configuration file parsing.\n'
        '  + parse_custom(file_path)\n'
        '    - Parses a custom configuration file format.\n'
        '      -- valid format: [key] [value1] [value2]\n'
        '    - Returns a map of parsed elements.\n'
        '  + parse_json(file_path)\n'
        '    - Parsed a json configuration file format\n'
        '    - Returns a map of parsed elements.\n'
        '  + make_config_dir(location, name)\n'
        '    - Creates a config directory named "name" at location "location".\n'
        '  + make_config_file(location, name)\n'
        '    - Crreates a config file named "name" at location "location".')
    arg_parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.parse_args()

    config_parser.make_config_dir(".", ".config")
    
    print("\n" + 80 * "=" + "\n")

    custom_data = config_parser.parse_custom("./.config/config.custom")
    print(custom_data)
    for custom_key in custom_data:
        print(custom_key)
        for custom_value in custom_data[custom_key]:
            print("  " + custom_value)

    print("\n" + 80 * "=" + "\n")
    
    json_data = config_parser.parse_json("./.config/config.json")
    print(json_data)
    for json_key in json_data:
        print(json_key)
        for json_value in json_data[json_key]:
            print("  " + json_value)
