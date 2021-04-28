#! /usr/local/bin/python3

import requests
import json

# create ID JSON
id = '{"client_id":"client_1", "enc_level":"level_1"}'
id_json = json.loads(id)

host_address = "http://127.0.0.1:5000"
response = requests.get(host_address)
print(response)

response = requests.post(host_address + "/get_key",json=id_json)
print(response.content)

response = requests.post(host_address + "/get_document",json=id_json)
print(response.content)
