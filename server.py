#!/usr/bin/env python

__author__ = "Yashin Mehaboobe aka sp3ctr3"

# We are spawning import around the code because we are worried about the allocation of resource?
# Python have a wonderfull gargabe collector! If the dont need something he can make it go away. :3
# If we cant trust on it, its better switch to C and make use of malloc and free! @_@
# 
# Put all the import on top reduces the cut-points on the code! Less time search the bug, more time testing solutions! :)

import sys
from twisted.internet import endpoints, reactor

import os
from twisted.python import log
from twisted.web import http, proxy
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32
exampleKey = AES.new('\xc6\xb3\xbc\xe9\x87+\x99\xd2\xb5\xed!\x00R!\xc7\xcc\xf7\x19`\x86qx*L\xcc\x92v!\xa5:\xfc\xbd')

# 1 - Global lambdas will be a mess soon as the code grow
#      To keep the same idea of a static function without lose organization try a class of static methods!

# 2 - I dont know how other linux distros work with python 2.x and 3.x, 
#     but on mine (arch linux) they rename "pyhton" binary to "python2" to make use of python 2.x librarys
#     and let the "python" being used by python 3.x.
#     I'm commenting this because the first-call is set to "python" like this application is running ou both versions
#     but we have print on the old style of 2.x!

class CryptographyRoutines  :
    
    @staticmethod
    def pad( s ):
    # one-liner to sufficiently pad the text to be encrypted
    #pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * '.'
        
        return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * '.'
    
    @staticmethod
    def EncodeAES( c , s ):
    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    #EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        
        return base64.b64encode(c.encrypt(pad(s)))

    @staticmethod
    def encryptAES(cleartext, key):
        
        mode, originalLength, cipherByteList = moo.encrypt(cleartext, moo.modeOfOperation["CFB"],
                key, moo.aes.keySize["SIZE_256"], key[:16])
        # print bits as 2 digit hex numbers in a string
        #cipherText = ''.join([format(x, '02x') for x in cipherByteList]) # This line 
        #return cipherText                                                # and this other one can be
        return ''.join([format(x, '02x') for x in cipherByteList])        # can become this :)



class ProxyClient(proxy.ProxyClient):
    
    """Modify response as well as header here.
    """
    def handleHeader(self, key, value):
        
        """
        Modify header here
        """
        log.msg("Header: %s: %s" % (key, value))
        proxy.ProxyClient.handleHeader(self, key, value)

    def handleResponsePart(self, buffer):
        
        """
        Modify buffer to modify response. For example replacing buffer with buffer[::-1] will lead to a reversed output.
        This might cause content encoding errors. Currently test only on text only websites
        """
        log.msg("Content: %s" % (buffer,))
        
        print "encrypting..."
        encryptedBuffer = CryptographyRoutines.EncodeAES(exampleKey, buffer)
        
        print "done encrypting..."
        # encryptedBuffer = buffer
        
        print encryptedBuffer
        proxy.ProxyClient.handleResponsePart(self, encryptedBuffer)


class ProxyClientFactory(proxy.ProxyClientFactory):
    
    protocol = ProxyClient

class ProxyRequest(proxy.ProxyRequest):
    
    protocols = dict(http=ProxyClientFactory)

class Proxy(proxy.Proxy):
    
    requestFactory = ProxyRequest

class ProxyFactory(http.HTTPFactory):
    
    protocol = Proxy

if __name__ == '__main__': 
    
    # for now its only used on this block!
    portstr = "tcp:8080:interface=localhost" # serve on localhost:8080

    def shutdown(reason, reactor, stopping=[]):
        """Stop the reactor."""
        
        # The indent based grammar on pytho help us to reduce the time we spent on recognizing the logic behind the code 
        # one-line block for conditional statements doesnt give us more execution speed. They only have the power to slow down the process of recognition of the code!
        # let the PVM worry about the unnecessary white spaces on the code!
        
        if stopping: 
            
            return
        
        stopping.append(True)
        
        if reason:
            
            log.msg(reason.value)
            
        reactor.callWhenRunning(reactor.stop)

    log.startLogging(sys.stdout)
    endpoint = endpoints.serverFromString(reactor, portstr)
    d = endpoint.listen(ProxyFactory())
    d.addErrback(shutdown, reactor)
    reactor.run()
