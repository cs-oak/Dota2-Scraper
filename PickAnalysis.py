from urllib2 import Request, urlopen, URLError
from collections import Counter
from time import sleep
import random
import json

#hero counter

car=0
sup=0
mof=0
carry = ['Carry',1,4,6,8,10,11,12,15,18,19,23,28,32,35,41,42,44,46,47,48,49,53,54,56,58,59,61,62,63,67,69,70,72,73,77,80,81,82,89,93,94,95,104,106,109];
support = ['Support',3,5,7,16,20,25,26,27,29,30,31,33,36,37,40,45,50,52,57,64,66,79,83,84,85,86,87,90,91,92,101,102,103,110]
others = ['Mid/Offlane',2,9,13,14,17,21,22,24,34,37,38,39,43,51,55,60,65,68,71,74,75,76,78,88,96,97,98,99,100,105,107,108,111]
hero_counter = {'Anti-Mage':0,'Axe':0,'Bane':0,'Bloodseeker':0,'Crystal Maiden':0,'Drow Ranger':0,'Earthshaker':0,'Juggernaut':0,'Mirana':0,'Shadow Fiend':0,'Morphling':0,'Phantom Lancer':0,'Puck':0,'Pudge':0,'Razor':0,'Sand King':0,'Storm Spirit':0,'Sven':0,'Tiny':0,'Vengeful Spirit':0,'Windranger':0,'Zeus':0,'Kunkka':0,'Lina':0,'Lich':0,'Lion':0,'Shadow Shaman':0,'Slardar':0,'Tidehunter':0,'Witch Doctor':0,'Riki':0,'Enigma':0,'Tinker':0,'Sniper':0,'Necrophos':0,'Warlock':0,'Beastmaster':0,'Queen of Pain':0,'Venomancer':0,'Faceless Void':0,'Wraith King':0,'Death Prophet':0,'Phantom Assassin':0,'Pugna':0,'Templar Assassin':0,'Viper':0,'Luna':0,'Dragon Knight':0,'Dazzle':0,'Clockwerk':0,'Leshrac':0,'Nature\'s Prophet':0,'Lifestealer':0,'Dark Seer':0,'Clinkz':0,'Omniknight':0,'Enchantress':0,'Huskar':0,'Night Stalker':0,'Broodmother':0,'Bounty Hunter':0,'Weaver':0,'Jakiro':0,'Batrider':0,'Chen':0,'Spectre':0,'Doom':0,'Ancient Apparition':0,'Ursa':0,'Spirit Breaker':0,'Gyrocopter':0,'Alchemist':0,'Invoker':0,'Silencer':0,'Outworld Devourer':0,'Lycan':0,'Brewmaster':0,'Shadow Demon':0,'Lone Druid':0,'Chaos Knight':0,'Meepo':0,'Treant Protector':0,'Ogre Magi':0,'Undying':0,'Rubick':0,'Disruptor':0,'Nyx Assassin':0,'Naga Siren':0,'Keeper of the Light':0,'Io':0,'Visage':0,'Slark':0,'Medusa':0,'Troll Warlord':0,'Centaur Warrunner':0,'Magnus':0,'Timbersaw':0,'Bristleback':0,'Tusk':0,'Skywrath Mage':0,'Abaddon':0,'Elder Titan':0,'Legion Commander':0,'Ember Spirit':0,'Earth Spirit':0,'Terrorblade':0,'Phoenix':0,'Oracle':0,'Techies':0}
hero_gpm = {'Anti-Mage':0,'Axe':0,'Bane':0,'Bloodseeker':0,'Crystal Maiden':0,'Drow Ranger':0,'Earthshaker':0,'Juggernaut':0,'Mirana':0,'Shadow Fiend':0,'Morphling':0,'Phantom Lancer':0,'Puck':0,'Pudge':0,'Razor':0,'Sand King':0,'Storm Spirit':0,'Sven':0,'Tiny':0,'Vengeful Spirit':0,'Windranger':0,'Zeus':0,'Kunkka':0,'Lina':0,'Lich':0,'Lion':0,'Shadow Shaman':0,'Slardar':0,'Tidehunter':0,'Witch Doctor':0,'Riki':0,'Enigma':0,'Tinker':0,'Sniper':0,'Necrophos':0,'Warlock':0,'Beastmaster':0,'Queen of Pain':0,'Venomancer':0,'Faceless Void':0,'Wraith King':0,'Death Prophet':0,'Phantom Assassin':0,'Pugna':0,'Templar Assassin':0,'Viper':0,'Luna':0,'Dragon Knight':0,'Dazzle':0,'Clockwerk':0,'Leshrac':0,'Nature\'s Prophet':0,'Lifestealer':0,'Dark Seer':0,'Clinkz':0,'Omniknight':0,'Enchantress':0,'Huskar':0,'Night Stalker':0,'Broodmother':0,'Bounty Hunter':0,'Weaver':0,'Jakiro':0,'Batrider':0,'Chen':0,'Spectre':0,'Doom':0,'Ancient Apparition':0,'Ursa':0,'Spirit Breaker':0,'Gyrocopter':0,'Alchemist':0,'Invoker':0,'Silencer':0,'Outworld Devourer':0,'Lycan':0,'Brewmaster':0,'Shadow Demon':0,'Lone Druid':0,'Chaos Knight':0,'Meepo':0,'Treant Protector':0,'Ogre Magi':0,'Undying':0,'Rubick':0,'Disruptor':0,'Nyx Assassin':0,'Naga Siren':0,'Keeper of the Light':0,'Io':0,'Visage':0,'Slark':0,'Medusa':0,'Troll Warlord':0,'Centaur Warrunner':0,'Magnus':0,'Timbersaw':0,'Bristleback':0,'Tusk':0,'Skywrath Mage':0,'Abaddon':0,'Elder Titan':0,'Legion Commander':0,'Ember Spirit':0,'Earth Spirit':0,'Terrorblade':0,'Phoenix':0,'Oracle':0,'Techies':0}
hero_xpm = {'Anti-Mage':0,'Axe':0,'Bane':0,'Bloodseeker':0,'Crystal Maiden':0,'Drow Ranger':0,'Earthshaker':0,'Juggernaut':0,'Mirana':0,'Shadow Fiend':0,'Morphling':0,'Phantom Lancer':0,'Puck':0,'Pudge':0,'Razor':0,'Sand King':0,'Storm Spirit':0,'Sven':0,'Tiny':0,'Vengeful Spirit':0,'Windranger':0,'Zeus':0,'Kunkka':0,'Lina':0,'Lich':0,'Lion':0,'Shadow Shaman':0,'Slardar':0,'Tidehunter':0,'Witch Doctor':0,'Riki':0,'Enigma':0,'Tinker':0,'Sniper':0,'Necrophos':0,'Warlock':0,'Beastmaster':0,'Queen of Pain':0,'Venomancer':0,'Faceless Void':0,'Wraith King':0,'Death Prophet':0,'Phantom Assassin':0,'Pugna':0,'Templar Assassin':0,'Viper':0,'Luna':0,'Dragon Knight':0,'Dazzle':0,'Clockwerk':0,'Leshrac':0,'Nature\'s Prophet':0,'Lifestealer':0,'Dark Seer':0,'Clinkz':0,'Omniknight':0,'Enchantress':0,'Huskar':0,'Night Stalker':0,'Broodmother':0,'Bounty Hunter':0,'Weaver':0,'Jakiro':0,'Batrider':0,'Chen':0,'Spectre':0,'Doom':0,'Ancient Apparition':0,'Ursa':0,'Spirit Breaker':0,'Gyrocopter':0,'Alchemist':0,'Invoker':0,'Silencer':0,'Outworld Devourer':0,'Lycan':0,'Brewmaster':0,'Shadow Demon':0,'Lone Druid':0,'Chaos Knight':0,'Meepo':0,'Treant Protector':0,'Ogre Magi':0,'Undying':0,'Rubick':0,'Disruptor':0,'Nyx Assassin':0,'Naga Siren':0,'Keeper of the Light':0,'Io':0,'Visage':0,'Slark':0,'Medusa':0,'Troll Warlord':0,'Centaur Warrunner':0,'Magnus':0,'Timbersaw':0,'Bristleback':0,'Tusk':0,'Skywrath Mage':0,'Abaddon':0,'Elder Titan':0,'Legion Commander':0,'Ember Spirit':0,'Earth Spirit':0,'Terrorblade':0,'Phoenix':0,'Oracle':0,'Techies':0}
hero_meter = {'Anti-Mage':0,'Axe':0,'Bane':0,'Bloodseeker':0,'Crystal Maiden':0,'Drow Ranger':0,'Earthshaker':0,'Juggernaut':0,'Mirana':0,'Shadow Fiend':0,'Morphling':0,'Phantom Lancer':0,'Puck':0,'Pudge':0,'Razor':0,'Sand King':0,'Storm Spirit':0,'Sven':0,'Tiny':0,'Vengeful Spirit':0,'Windranger':0,'Zeus':0,'Kunkka':0,'Lina':0,'Lich':0,'Lion':0,'Shadow Shaman':0,'Slardar':0,'Tidehunter':0,'Witch Doctor':0,'Riki':0,'Enigma':0,'Tinker':0,'Sniper':0,'Necrophos':0,'Warlock':0,'Beastmaster':0,'Queen of Pain':0,'Venomancer':0,'Faceless Void':0,'Wraith King':0,'Death Prophet':0,'Phantom Assassin':0,'Pugna':0,'Templar Assassin':0,'Viper':0,'Luna':0,'Dragon Knight':0,'Dazzle':0,'Clockwerk':0,'Leshrac':0,'Nature\'s Prophet':0,'Lifestealer':0,'Dark Seer':0,'Clinkz':0,'Omniknight':0,'Enchantress':0,'Huskar':0,'Night Stalker':0,'Broodmother':0,'Bounty Hunter':0,'Weaver':0,'Jakiro':0,'Batrider':0,'Chen':0,'Spectre':0,'Doom':0,'Ancient Apparition':0,'Ursa':0,'Spirit Breaker':0,'Gyrocopter':0,'Alchemist':0,'Invoker':0,'Silencer':0,'Outworld Devourer':0,'Lycan':0,'Brewmaster':0,'Shadow Demon':0,'Lone Druid':0,'Chaos Knight':0,'Meepo':0,'Treant Protector':0,'Ogre Magi':0,'Undying':0,'Rubick':0,'Disruptor':0,'Nyx Assassin':0,'Naga Siren':0,'Keeper of the Light':0,'Io':0,'Visage':0,'Slark':0,'Medusa':0,'Troll Warlord':0,'Centaur Warrunner':0,'Magnus':0,'Timbersaw':0,'Bristleback':0,'Tusk':0,'Skywrath Mage':0,'Abaddon':0,'Elder Titan':0,'Legion Commander':0,'Ember Spirit':0,'Earth Spirit':0,'Terrorblade':0,'Phoenix':0,'Oracle':0,'Techies':0}


#end hero counter
#acquire last 100 match ID's from GetMatHis

match_list=list()
dest = open('pick_out.json', 'w+')
request = Request('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key=ENTER_YOUR_ID')
sleep(1)
try:
	response = urlopen(request)
	kittens = response.read()
	print >> dest, kittens
except URLError, e:
	print 'Got an error code:', e
dest.close()
json_data = open('c:\Project\pick_out.json')
data = json.load(json_data)
for i in data["result"]["matches"]:
	match_list.append(i["match_id"])
	
#end of ID acquisition
#iterate for each match ID

for z in xrange(len(match_list)):
	dest_1 = open('match.json', 'w+')
	request_1 = Request('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=ENTER_YOUR_ID&match_id='+str(match_list[z]))
	sleep(1)
	try:
		response_1 = urlopen(request_1)
		puppies = response_1.read()
		print >> dest_1, puppies
	except URLError, e:
		print 'Got an error code:', e
	dest_1.close()
	json_data_1 = open('c:\Project\match.json')
	data_1 = json.load(json_data_1)
	for k in data_1["result"]["players"]:
		json_data_2 = open('c:\Project\hero_names.json')
		hero_name = json.load(json_data_2)
		for u in hero_name["result"]["heroes"]:
			if k["hero_id"] == u["id"]:
				name=u["localized_name"]
				hero_counter[name]+=1
				hero_gpm[name]+=float((k["gold_per_min"]))
				hero_xpm[name]+=float(k["xp_per_min"])
				for w in carry:
					if k["hero_id"]==w:
						car+=1
				for w in support:
					if k["hero_id"]==w:
						sup+=1
				for w in others:
					if k["hero_id"]==w:
						mof+=1
				
for x in hero_counter:
	print x,':\tGames:',hero_counter[x],'\n'
	if hero_counter[x]==0:
		hero_counter[x]=1
	for y in hero_gpm:
		if y == x:
			hero_gpm[y]=hero_gpm[y]/hero_counter[x]
	for z in hero_xpm:
		if z == x:
			hero_xpm[z]=hero_xpm[z]/hero_counter[x]
print '\n\n\n'
print 'Carries Picked:\t',car
print 'Supports Picked:\t',sup
print 'Mid/Off Picked:\t',mof
print '\n\n\n'
				
#end of iterations
#begin analysis

holder=list()
for x in hero_counter:
	holder.append(hero_counter[x])
sorted_holder=sorted(holder)
len_hol=len(holder)
median=0.0
idx=(len_hol-1)//2
if(len_hol%2):
	median=sorted_holder[idx]
else:
	median=(sorted_holder[idx]+sorted_holder[idx+1])/2.0
for x in hero_counter:
	for y in hero_meter:
		if y == x:
			if hero_counter[x]<0.7*median:
				hero_meter[y]-=1
			elif hero_counter[x]>1.7*median:
				hero_meter[y]+=1
for x in hero_meter:
	for y in hero_gpm:
		if y == x:
			if hero_meter[x]==-1 and hero_gpm[y]<500:
				hero_meter[x]-=1
			elif hero_meter[x]==1 and hero_gpm[y]>800:
				hero_meter[x]+=1
			elif hero_meter[x]==-1 and hero_gpm[y]>499:
				hero_meter[x]+=1
			elif hero_meter[x]==1 and hero_gpm<801:
				hero_meter[x]-=1
	if hero_meter[x]==0:
		print x,':\tStatus: Normal'
	elif hero_meter[x]==1:
		print x,':\tStatus: Popular'
	elif hero_meter[x]==2:
		print x,':\tStatus: Needs Nerf'
	elif hero_meter[x]==-1:
		print x,':\tStatus: Not Popular'
	elif hero_meter[x]==-2:
		print x,':\tStatus: Needs Buff'