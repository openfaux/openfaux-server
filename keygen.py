#-*- coding: utf-8 -*-
# (c) 2012 Anders Andersen
# See http://www.cs.uit.no/~aa/dist/tools/py/COPYING for details

from sys import argv
from Crypto.PublicKey import RSA

# argv[1]: RSA key file name (creates)
# argv[2]: password (optional)
if len(argv) > 1:
    passwd = None
    key = RSA.generate(4096)
    pub = key.publickey()
    fkey = open(argv[1], 'wb')
    fpub = open(argv[1] + '.pub', 'wb')
    if len(argv) > 2:
        passwd = argv[2]
    fkey.write(key.exportKey('PEM', passwd))
    fpub.write(pub.exportKey('PEM'))
    fkey.close()
    fpub.close()