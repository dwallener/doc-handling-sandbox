#! /usr/local/bin/python3

# encrypt a document three times
# one part once
# one part twice
# one part thrice
# then decrypt in reverse order

# initialization test
print("Super Basic Test")
from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
print ("Message: ", message)
ciphertext = obj.encrypt(message)
print ("Encrypted: ", ciphertext)
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = obj2.decrypt(ciphertext)
print ("Plaintext: ", plaintext)

# test using simplest possible document model
print("Test reading of 3-tier document model")
import json
# read JSON
with open('test-01.json', 'r') as myfile:
    data = myfile.read()
jobj = json.loads(data)
# dump contents to confirm read
# doc format is "document -> section 1/2/3 -> text, level"
print(jobj['document'])
print(jobj['document']['section 1'])
print(jobj['document']['section 2'])
print(jobj['document']['section 3'])
print("Section 1 text: ", jobj['document']['section 1']['text'])
print("Section 2 text: ", jobj['document']['section 2']['text'])
print("Section 3 text: ", jobj['document']['section 3']['text'])

# set up test conditions
test_1_txt = jobj['document']['section 1']['text']
test_2_txt = jobj['document']['section 2']['text']
test_3_txt = jobj['document']['section 3']['text']


# now encrypt as planned..level 1, 1x...level 2, 2x...level 3, 3x
print("Test iterative encrypt/decrypt")

# this is level 1...one cycle through AES
print("LEVEL 1 DIAGNOSTIC TEST")
l1_obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = str(jobj['document']['section 1']['text'])
# pad to multiple of 16 bytes
extra = len(message) % 16
padsize = 16 - extra
if extra > 0:
    message = message + (' ' * padsize)

# now encrypt...
ciphertext = l1_obj.encrypt(message)
print ("Level 1 cipher text: ",ciphertext)

# ...and decrypt
l1_obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = l1_obj2.decrypt(ciphertext)
print ("Level 1 plaintext:", plaintext)

# check for pass/fail
if plaintext == test_1_txt:
    print("LEVEL 1 TEST PASS")
else:
    print("LEVEL 1 TEST FAIL")


# this is level 2...two cycles through AES
print("LEVEL 2 DIAGNOSTIC TEST")
l2_obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = str(jobj['document']['section 2']['text'])
# pad to multiple of 16 bytes
extra = len(message) % 16
padsize = 16 - extra
if extra > 0:
    message = message + (' ' * padsize)

# now encrypt once
ciphertext = l2_obj.encrypt(message)
print("Level 2 Encrypt 1: ", ciphertext)

# encrypt again
l2_obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = ciphertext
ciphertext = l2_obj2.encrypt(message)
print("Level 2 Encrypt 2: ", ciphertext)

# decrypt once
l2_obj3 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = l2_obj3.decrypt(ciphertext)
print("Level 2 Decrypt 2:", plaintext)

#decrypt again
ciphertext = plaintext
l2_obj4 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = l2_obj4.decrypt(ciphertext)
print ("Level 3 Decrypt 1:", plaintext)

# check for pass/fail
if plaintext == test_2_txt:
    print("LEVEL 2 TEST PASS")
else:
    print("LEVEL 2 TEST FAIL")


# this is level 3...three cycles through AES
print("LEVEL 3 DIAGNOSTIC TEST")
l3_obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = str(jobj['document']['section 2']['text'])
# pad to multiple of 16 bytes
extra = len(message) % 16
padsize = 16 - extra
if extra > 0:
    message = message + (' ' * padsize)

# now encrypt once
ciphertext = l3_obj.encrypt(message)
print("Level 3 Encrypt 1: ", ciphertext)

# encrypt again
l3_obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = ciphertext
ciphertext = l3_obj2.encrypt(message)
print("Level 3 Encrypt 2: ", ciphertext)

# and once more
l3_obj2a = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = ciphertext
ciphertext = l3_obj2a.encrypt(message)
print("Level 3 Encrypt 3: ", ciphertext)

# decrypt once
l3_obj3 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = l3_obj3.decrypt(ciphertext)
print("Level 3 Decrypt 3:", plaintext)

# decrypt again
ciphertext = plaintext
l3_obj4 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = l3_obj4.decrypt(ciphertext)
print ("Level 3 Decrypt 2:", plaintext)

# and once more
ciphertext = plaintext
l3_obj4a = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plaintext = l3_obj4a.decrypt(ciphertext)
print ("Level 3 Decrypt 1:", plaintext)

# check for pass/fail
if plaintext == test_3_txt:
    print("LEVEL 3 TEST PASS")
else:
    print("LEVEL 3 TEST FAIL")
