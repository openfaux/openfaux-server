#!/usr/bin/env python

# modified by David
# from  source: https://launchkey.com/docs/api/encryption

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode 
import time

public_key_loc = "test.pub"
private_key_loc = "test"

key = open(public_key_loc, "r").read()
pubrsakey = RSA.importKey(key)
pubrsakey = PKCS1_OAEP.new(pubrsakey)

key = open(private_key_loc, "r").read() 
rsakey = RSA.importKey(key) 
rsakey = PKCS1_OAEP.new(rsakey)

print "10000 chars/byte"
start_time = time.time()
for i in range(100):
    x = "a" * 100
    encrypted = pubrsakey.encrypt(x)
    rsakey.decrypt(encrypted) 
print time.time() - start_time, "seconds"
