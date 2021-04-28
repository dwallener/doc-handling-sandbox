#! /usr/local/bin/python3

# client to push original documents to host

import argparse
import requests
import json

host_address = "http://127.0.0.1:5000/document_input"

parser = argparse.ArgumentParser(description="Process command line.")
parser.add_argument('Original',
                    metavar='orig_doc',
                    type=str,
                    help='path to original doc')
parser.add_argument('Encrypted',
                    metavar='enc_doc',
                    type=str,
                    help='path to encrypted doc')

args = parser.parse_args()
input_path = args.Original
output_path = args.Encrypted

print("Input path: ", input_path)
print("Output path: ", output_path)

with open(input_path, 'rb') as f:
    data = json.load(f)
    print(data)
    r = requests.post(host_address, json=data)
    print(r.content)
print("That was json test")
