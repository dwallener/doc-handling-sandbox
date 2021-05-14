#! /usr/local/bin/python3

# Support Functions

import tkinter as tk
import time
import logging


################################################################################
# Logging function to console display incoming decrypted documents

def logging_incoming_doc(input_json):

    previous_level = logging.root.level
    logging.basicConfig(level=logging.INFO)

    logging.info('Document Push')
    logging.info(input_json['document']['section 1'])
    logging.info('')
    logging.info(input_json['document']['section 2'])
    logging.info('')
    logging.info(input_json['document']['section 3'])
    logging.info('')

    logging.basicConfig(level=previous_level)

    return "Done"


################################################################################
# Display json text in a self-destructing window

def display_text (input_json):

    window = tk.Tk()
    window.after(5000, lambda: window.destroy())

    # section 1
    greeting = tk.Label(text="Hello from Tkinter!")
    text_1 = input_json['document']['section 1']['text']
    greeting = tk.Label(text=text_1, wraplength=400, justify="left")
    greeting.pack()

    greeting = tk.Label(text="\n")
    greeting.pack()
    text_2 = input_json['document']['section 2']['text']
    greeting = tk.Label(text=text_2, wraplength=400, justify="left")
    greeting.pack()

    greeting = tk.Label(text="\n")
    greeting.pack()
    text_3 = input_json['document']['section 3']['text']
    greeting = tk.Label(text=text_3, wraplength=400, justify="left")
    greeting.pack()

    window.mainloop()

    return "Done"
