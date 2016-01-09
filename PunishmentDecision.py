from urllib2 import Request, urlopen, URLError
from collections import Counter
from time import sleep
import random
import json
import os

#calculate metrics from present and previous data

gamBan=0
comBan=0
comPunCt=0
srsPunCt=0
gamPunCt=0
count=0
locvar = {}
json_data = open('C:\Project\pickout.json')
match_data = json.load(json_data)
for i in match_data:
	locvar[i] = match_data[i]
json_data_1 = open('C:\Project\comout.json')
com_data = json.load(json_data_1)
if locvar['id'] == com_data["id"]:
	id64 = locvar['id']
	count = com_data["count"]
check = os.path.exists('C:\Project\history_'+id64+'.json')
if check == True:
	json_data = open('C:\Project\history_'+id64+'.json')
	data = json.load(json_data)
	prevComPun = data["comPunish"]
	prevGamPun = data["gamPunish"]
	prevSrsPun = data["srsPunish"]
	prevComBan = data["comBans"]
	prevGamBan = data["gamBans"]
else:
	prevComPun = 1
	prevGamPun = 1
	prevSrsPun = 1
	prevComBan = 1
	prevGamBan = 1
if count != 0:
	comPun = count*prevComPun+0.2*(locvar['loadf']+locvar['abdn']+locvar['afk']+locvar['disc'])+0.5*locvar['rgqt']
	comPunCt = prevComPun+1
else:
	comPunCt = 1
gamPun = prevGamPun*(0.1*(locvar['loadf']+locvar['disc'])+0.8*(locvar['abdn']+locvar['afk'])*locvar['rgqt'])
srsPun = prevSrsPun*(comPun+gamPun)
if locvar['abdn'] != 0 or locvar['afk'] != 0 or locvar['rgqt'] != 0:
	gamPunCt = prevGamPun+1
else:
	gamPunCt = 1
if gamPunCt >= 3 and comPunCt >= 3:
	srsPunCt = prevSrsPun+1
if comPun > 50:
	comBan = prevComBan+1
if gamPun > 20:
	gamBan = prevGamBan+1
feedback = {'comPunish':comPunCt,'gamPunish':gamPunCt,'srsPunish':srsPunCt,'comBans':comBan,'gamBans':gamBan}
dest = open('C:\Project\history_'+id64+'.json','w+')
jout = json.dumps(feedback)
print >> dest, jout

#end calculations
#begin report generation

print 'REPORT:'
print 'ID: ',id64

if gamPunCt >= 10 and gamPunCt <= 20:
	if locvar['kda'] > 3.0 and locvar['kdaf'] < 2.5 and locvar['gpm'] > 350 and locvar['xpm'] > 300:
		print 'Occassional disconnects, possibly unintentional'
	else:
		print 'Occassional disconnects, possibly intentional'
elif gamPunCt > 20:
	print 'Frequent disconnects, intentional. Needs review and report checking'
if gamPunCt > 3 and comPunCt < 3:
	print 'Player has past history of abandonment'
	
if comPun < 15 and comPun >=0:
	print 'Mild communication abuse'
elif comPun < 30 and comPun >= 15:
	print 'Moderate communication abuse'
elif comPun > 30 and comPun < 50:
	print 'High communication abuse'
else:
	print 'Extreme communication abuse. Requires muting'
if gamPunCt < 3 and comPunCt > 3:
	print 'Player has several previous instances of communication abuse'
if gamPunCt > 3 and comPunCt > 3:
	print 'Player has past history of abandonment and previous instances of communication abuse. Needs immediate review'
	
if locvar['kdad'] > 3.0 and locvar['kda'] < 3.0:
	print 'Skill/Hero exploitation possible'

print 'There are ',locvar['abdn']+locvar['rgqt']+locvar['disc']+locvar['afk'],' instances which may have been intentional disconnects'
print 'There are ',count,' instances for communication abuse detected'

#end report generation