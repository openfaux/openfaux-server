#!/bin/env python

# Packing meta data
# ---------------------------------------------------------------------------------------------

__name__    = "openfaux proxy server"
__desc__    = "Thee openfaux proxy server"
__ldesc__   = "This is the main proxy server of openfaux system! it's hosted on dagobah planet!" 
__version__ = "0.0.1" 
__license__ = "AGPL3"
__url__     = "http://openfaux.org"
__author__  = "Yashin Mehaboobe (@sp3ctr3)"
__email__   = "unknow"

# ---------------------------------------------------------------------------------------------

# I dont see with good eye the import different point on the code!
# For more control it is better all of them on the top.
#
# If the excuse to use import around the code is about perfomance so i think
# it is time to switch for C and make use of alloc function :D

import sys
from twisted.internet import endpoints, reactor

from twisted.python import log
from twisted.web import http, proxy

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
        proxy.ProxyClient.handleResponsePart(self, buffer)

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
    
    
    def shutdown(reason, reactor, stopping=[]):
        
        """Stop the reactor."""
        
        if stopping: 
            
            return # a one line  statements only slows down our process of visual recognition of the code
            
        stopping.append(True)
        
        if reason:
            
            log.msg(reason.value)
            
        reactor.callWhenRunning(reactor.stop)

    log.startLogging(sys.stdout)
    
    endpoint = endpoints.serverFromString(reactor, portstr)

    d = endpoint.listen(ProxyFactory())

    d.addErrback(shutdown, reactor)

    reactor.run()

