#! /usr/bin/env python3
import json
import sys


def pretty_json(input_filename):
    out_filename = '.'.join(input_filename.split('.')[:-1]) + '-pretty.json'
    with open(input_filename, 'r') as in_json:
        with open(out_filename, 'w') as out_json:
            json.dump(json.load(in_json), out_json, indent=2)
            print(f'Wrote JSON to: {out_filename}')


if __name__ == '__main__':
    for file_name in sys.argv[1:]:
        if file_name.endswith('.json'):
            try:
                pretty_json(file_name)
            except json.decoder.JSONDecodeError as err:
                print(f'Could not decode {file_name}... {err}')
        else:
            print(f'Skipping non-JSON file {file_name}')


