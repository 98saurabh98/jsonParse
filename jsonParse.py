# import the json module
import json
import urllib.request, urllib.parse, urllib.error
import ssl
import re

url = input('Enter URL here')              #samples: http://py4e-data.dr-chuck.net/comments_64377.json
                                           #         http://py4e-data.dr-chuck.net/comments_42.json
data = urllib.request.urlopen(url).read()  #reading data from internet

lst=list()
pydata = json.loads(data)                  #changing formatting of data to dictionary
#print('Usercount: ', len(pydata))
for l in pydata['comments']:
	lst.append(int(l['count']))            #accessing values of the key count
print(sum(lst))
#final sum of all integers