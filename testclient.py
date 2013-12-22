#!/usr/bin/python
import urllib2, sys
from bs4 import BeautifulSoup
from difflib import context_diff
from optparse import OptionParser
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32
exampleKey = AES.new('\xc6\xb3\xbc\xe9\x87+\x99\xd2\xb5\xed!\x00R!\xc7\xcc\xf7\x19`\x86qx*L\xcc\x92v!\xa5:\xfc\xbd')
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip('.')

def testBasicRequest(url = None):
	#Change proxy settings here
	proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
	opener = urllib2.build_opener(proxy)
	
	#allows custom urls
	if url is None:
		req = urllib2.Request('http://www.google.com')
	else:
		req = urllib2.Request(url)
		
	#Add headers here by calling req.add_header
	req.add_header('Referrer', 'OpenFaux')
	urllib2.install_opener(opener)
	res=urllib2.urlopen(req)
	# print res.read()
	# soup=BeautifulSoup(res.read())
	# print soup.get_text()
	# print res.read()
	cleartextRequest = DecodeAES(exampleKey, res.read())
	print cleartextRequest
	
def decryptAES(cipherText, key):
	# split cipher into char pairs and interpret them as base 16 (hex):
	cipherByteList = [int(cipherText[i:i+2], 16) for i in range(0, len(cipherText), 2)]
	# print cipherByteList
	return moo.decrypt(cipherByteList, None, moo.modeOfOperation["CFB"], key,
			moo.aes.keySize["SIZE_256"], key[:16])


def evalOpenfauxProxy(url = None):
	#Change proxy settings here
	proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
	opener = urllib2.build_opener(proxy)
	
	#allows custom urls
	if url is None:
		req = urllib2.Request('http://www.google.com')
	else:
		req = urllib2.Request(url)
		
	res_no_proxy = urllib2.urlopen(req)
	res = opener.open(req)

	#print the diff of the responses
	#This could be more elaborate
	s1 = res_no_proxy.readlines()
	s2 = res.readlines()
	for line in context_diff(s1, s2, fromfile='NoProxy', tofile='Proxy'):
		sys.stdout.write(line)
		
# Option parsing could be cleaned up a bit
def main(argv):
	usage = "usage: %prog [options] arg"
	parser = OptionParser(usage)
	# Add cmdline options here
	parser.add_option("-b", "--basicrequest", action="store_true", dest="basicrequest")
	parser.add_option("-e", "--eval", action="store_true", dest="evaluate")
	parser.add_option("-u", "--url", action="store", dest="url")
	
	(options, args) = parser.parse_args()
	if options.basicrequest:
		testBasicRequest(options.url)
	if options.evaluate:
		evalOpenfauxProxy(options.url)
		
main(sys.argv)
		
	
