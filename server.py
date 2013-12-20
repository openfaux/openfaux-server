#!/usr/bin/python
from twisted.python import log
from twisted.web import http, proxy
from aes import *

__author__ = "Yashin Mehaboobe aka sp3ctr3"

moo = AESModeOfOperation()
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
        exampleKey = [84, 121, 169, 117, 172, 150, 208, 78, 219L, 179L, 157L, 156L, 233L, 96L, 125L, 99L, 118L, 49L, 206L, 145L, 56L, 98L, 75L, 176L, 160L, 108L, 173L, 200L, 223L, 146L, 195L, 8L]
        encryptedBuffer = encryptAES(buffer, exampleKey)
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

