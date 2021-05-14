#! /usr/local/bin/python3

# encrypt a document three times
# one part once
# one part twice
# one part thrice
# then decrypt in reverse order
import json
from Crypto.Cipher import AES

# set up AES encryption
enc_obj = AES.new('This is a key123', AES.MODE_ECB, 'This is an IV456')

def pad_message (message):
    print("Checking message length...")
    extra = len(message) % 16
    padsize = 16 - extra
    if extra > 0:
        message = message + (' ' * padsize)
    return message

# basic block encrypt
def encrypt_block (message):
    print("Padding...")
    padded_message = pad_message(message)
    ciphertext = enc_obj.encrypt(padded_message)
    return ciphertext

def decrypt_block (message, iterations):
    print("Decrypting level ", iterations)
    for x in range(iterations):
        print(x)
        plaintext = enc_obj.decrypt(message)
        message = plaintext
    return plaintext

def assemble_doc(jobj, cipher_1, cipher_2, cipher_3):
    y = jobj
    y['document']['section 1']['text'] = cipher_1
    y['document']['section 2']['text'] = cipher_2
    y['document']['section 3']['text'] = cipher_3
    return y


# control what gets encrypted, how
def encrypt_func (jobj):

    message_1 = str(jobj['document']['section 1']['text'])
    message_2 = str(jobj['document']['section 2']['text'])
    message_3 = str(jobj['document']['section 3']['text'])

    # level 1, once...level 2, twice...level 3, thrice
    print("Level 1...")
    cipher_1 = encrypt_block(message_1)
    print("Level 2...")
    cipher_2 = encrypt_block(message_2)
    cipher_2 = encrypt_block(cipher_2)
    print("Level 3...")
    cipher_3 = encrypt_block(message_3)
    cipher_3 = encrypt_block(cipher_3)
    cipher_3 = encrypt_block(cipher_3)

    # recombine doc
    y = assemble_doc(jobj, cipher_1, cipher_2, cipher_3)
    print(y)
    return y

    # level 2
