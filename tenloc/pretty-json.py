#! /usr/bin/env python3
import json
import sys


def reformat_json(input_file):
    with open(input_file, 'r') as in_json:
        with open(input_file.split('.')[:-1] + '-pretty.json', 'w') as out_json:
            json.dump(json.load(in_json), out_json, indent=2)


if __name__ == '__main__':
    for file_name in sys.argv[1:]:
        if file_name.endswith('.json'):
            reformat_json(file_name)
        else:
            print(f'Skipping non-JSON file {file_name}')


