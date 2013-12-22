#!/usr/bin/python
import os
from twisted.python import log
from twisted.web import http, proxy
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32
exampleKey = AES.new('\xc6\xb3\xbc\xe9\x87+\x99\xd2\xb5\xed!\x00R!\xc7\xcc\xf7\x19`\x86qx*L\xcc\x92v!\xa5:\xfc\xbd')

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * '.'

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

__author__ = "Yashin Mehaboobe aka sp3ctr3"

def encryptAES(cleartext, key):
    mode, originalLength, cipherByteList = moo.encrypt(cleartext, moo.modeOfOperation["CFB"],
            key, moo.aes.keySize["SIZE_256"], key[:16])
    # print bits as 2 digit hex numbers in a string
    cipherText = ''.join([format(x, '02x') for x in cipherByteList])
    return cipherText

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
        encryptedBuffer = EncodeAES(exampleKey, buffer)
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
portstr = "tcp:8080:interface=localhost" # serve on localhost:8080

if __name__ == '__main__': 
    import sys
    from twisted.internet import endpoints, reactor

    def shutdown(reason, reactor, stopping=[]):
        """Stop the reactor."""
        if stopping: return
        stopping.append(True)
        if reason:
            log.msg(reason.value)
        reactor.callWhenRunning(reactor.stop)

    log.startLogging(sys.stdout)
    endpoint = endpoints.serverFromString(reactor, portstr)
    d = endpoint.listen(ProxyFactory())
    d.addErrback(shutdown, reactor)
    reactor.run()

