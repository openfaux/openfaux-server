#!/usr/bin/python
import urllib2, sys
from bs4 import BeautifulSoup
from difflib import context_diff
from optparse import OptionParser
from aes import *

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
	soup=BeautifulSoup(res.read())
	print soup.get_text()
	exampleKey = [84, 121, 169, 117, 172, 150, 208, 78, 219L, 179L, 157L, 156L, 233L, 96L, 125L, 99L, 118L, 49L, 206L, 145L, 56L, 98L, 75L, 176L, 160L, 108L, 173L, 200L, 223L, 146L, 195L, 8L]
	cleartextRequest = decryptAES(soup.get_text(), exampleKey)
	print cleartextRequest
	
moo = AESModeOfOperation()
def decryptAES(cipherText, key):
	# split cipher into char pairs and interpret them as base 16 (hex):
	cipherByteList = [int(cipherText[i:i+2], 16) for i in range(0, len(cipherText), 2)]
	print cipherByteList
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
		
	
