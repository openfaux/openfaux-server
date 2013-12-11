import urllib2
from BeautifulSoup import BeautifulSoup
#Change proxy settings here
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
req = urllib2.Request('http://www.google.com')
#Add headers here by calling req.add_header
req.add_header('Referer', 'OpenFaux')
urllib2.install_opener(opener)
res=urllib2.urlopen(req)
soup=BeautifulSoup(res.read())
print soup.prettify()
