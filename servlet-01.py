#! /usr/local/bin/python3

# This is the servlet for testing doc and key distribution

import ast
import json
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

from encrypt_func import encrypt_func
from encrypt_func import decrypt_block

y = {}

@app.route('/')
#def activecalls():
#    return app.send_static_file('activecalls/active_calls_map.html')
def hello_world():
    return 'Hello, World!'

# now lets start creating endpoints and blah blah blah
@app.route('/hello')
def hello():
    return 'Hello, World!'

# endpoint to submit a document, as JSON
@app.route('/document_input', methods=['GET','POST'])
def document_input():
    print("document recieved...")
    # save the POSTed json
    req = request.get_json()
    print(req)
    print("Encrypting...")
    y = encrypt_func(req)
    print(y)
    f = open("enc_document.txt", "w")
    f.write(str(y))
    f.close()
    return 'Thanks! Document encrypted!', 200

# endpoint to request key(s)
@app.route('/get_key', methods=['GET','POST'])
def get_key():
    req = request.get_json()
    print("Key Setup")
    print("Client ID: ", req["client_id"])
    print("Security Level: ", req["enc_level"])
    return 'Processed key request...'

# endpoint to request document_input
@app.route('/get_document', methods=['POST','GET'])
def get_document():
    req = request.get_json()
    print("Document request")
    print("Client ID: ", req["client_id"])
    print("Security Level: ", req["enc_level"])

    if req["client_id"] == "client_1":
        with open('enc_document.txt') as f:
            print("Processing client...", req["client_id"])
            data = f.read()
            data_dict = ast.literal_eval(data)
            print(data_dict)
            data_dict['document']['section 1']['text'] = str(decrypt_block(data_dict['document']['section 1']['text'], 1))
            print(data_dict)

    if req["client_id"] == "client_2" :
        with open('enc_document.txt') as f:
            print("Processing client...", req["client_id"])
            data = f.read()
            data_dict = ast.literal_eval(data)
            print(data_dict)
            data_dict['document']['section 1']['text'] = str(decrypt_block(data_dict['document']['section 1']['text'], 1))
            data_dict['document']['section 2']['text'] = str(decrypt_block(data_dict['document']['section 2']['text'], 2))
            print(data_dict)

    if req["client_id"] == "client_3":
        with open('enc_document.txt') as f:
            print("Processing client...", req["client_id"])
            data = f.read()
            data_dict = ast.literal_eval(data)
            print(data_dict)
            data_dict['document']['section 1']['text'] = str(decrypt_block(data_dict['document']['section 1']['text'], 1))
            data_dict['document']['section 2']['text'] = str(decrypt_block(data_dict['document']['section 2']['text'], 2))
            data_dict['document']['section 3']['text'] = str(decrypt_block(data_dict['document']['section 3']['text'], 3))
            print(data_dict)

    print(type(data_dict))
    data_json = json.dumps(data_dict, default=lambda x: None)
    print(type(data_json))

    #return 'Processed document request...'
    return data_json
