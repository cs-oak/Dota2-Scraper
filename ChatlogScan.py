from urllib2 import Request, urlopen, URLError
from collections import Counter
from time import sleep
import random
import json

#read the chatlog and other variables

print 'Please enter 64-bit Steam Profile ID: ',
id64 = raw_input()
steamid64 = long(id64)
scanid = str(steamid64)
count = 0
status=0
content = list()
with open("C:\Project\samplechat.txt") as f:
	content = f.readlines()
with open("C:\Project\slangdb.txt") as g:
	english = g.readlines()

#end read
#begin scan

for x in content:
	y = str(x)
	if y.count(scanid) == 1:
		for q in english:
			z=str(q)
			count += y.count(z)+y.count(z.upper())

if count == 0:
		status = 0
elif count > 0 and count <= 5:
		status = 1
elif count > 5 and count <= 10:
		status = 2
elif count > 10 and count <= 20:
		status = 3
elif count > 20:
		status = 4

com_out={'id':scanid,'count':count}
dest = open('C:\Project\comout.json', 'w+')
jout = json.dumps(com_out)
print >> dest, jout
		
#end scans