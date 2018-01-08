import json
import urllib.request, urllib.parse, urllib.error
import ssl
import re

url = input('Enter URL here')
data = urllib.request.urlopen(url).read()

lst=list()
pydata = json.loads(data)
#print('Usercount: ', len(pyda))
for l in pydata['comments']:
	lst.append(int(l['count']))
print(sum(lst))