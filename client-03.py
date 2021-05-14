#! /usr/local/bin/python3

import requests
import json

# create ID JSON
id = '{"client_id":"client_3", "enc_level":"level_3"}'
id_json = json.loads(id)

host_address = "http://127.0.0.1:5000"
response = requests.get(host_address)
print(response)

response = requests.post(host_address + "/get_key",json=id_json)
print(response.content)

response = requests.post(host_address + "/get_document",json=id_json)
print(response.content)

# let's display in a window

import tkinter as tk
import time

print("Jsonify...")
response_json = json.loads(response.content)
print("GUI stuff...")

# window housekeeping
window = tk.Tk()
window.after(5000, lambda: window.destroy())

# section 1
greeting = tk.Label(text="Hello from Tkinter!")
text_1 = str(response_json['document']['section 1']['text'])
greeting = tk.Label(text=text_1, wraplength=400, justify="left")
greeting.pack()

greeting = tk.Label(text="\n")
greeting.pack()
text_2 = str(response_json['document']['section 2']['text'])
greeting = tk.Label(text=text_2, wraplength=400, justify="left")
greeting.pack()

greeting = tk.Label(text="\n")
greeting.pack()
text_3 = str(response_json['document']['section 3']['text'])
greeting = tk.Label(text=text_3, wraplength=400, justify="left")
greeting.pack()

window.mainloop()
