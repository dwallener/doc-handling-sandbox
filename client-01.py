#! /usr/local/bin/python3

import requests
import json
import logging
from support_functions import display_text
from support_functions import logging_incoming_doc


# set logging levels
logging.basicConfig(level=logging.INFO)

# create ID JSON
id = '{"client_id":"client_1", "enc_level":"level_1"}'
id_json = json.loads(id)

host_address = "http://127.0.0.1:5000"
response = requests.get(host_address)
logging.debug(response.content)

response = requests.post(host_address + "/get_key",json=id_json)
logging.info('Client Verification')
logging.info(response.content)

response = requests.post(host_address + "/get_document",json=id_json)
response_json = json.loads(response.content)
logging_incoming_doc(response_json)

#logging.info('Document Push')
#logging.info(response_json['document']['section 1'])
#logging.info('')
#logging.info(response_json['document']['section 2'])
#logging.info('')
#logging.info(response_json['document']['section 3'])
#logging.info('')

print("Jsonify...")
response_json = json.loads(response.content)
print("GUI stuff...")

display_text(response_json)
