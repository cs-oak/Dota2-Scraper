from urllib2 import Request, urlopen, URLError
from collections import Counter
from time import sleep
import random
import json

# declare lists of heroes based on roles

carry = ['Carry',1,4,6,8,10,11,12,15,18,19,23,28,32,35,41,42,44,46,47,48,49,53,54,56,58,59,61,62,63,67,69,70,72,73,77,80,81,82,89,93,94,95,104,106,109];
support = ['Support',3,5,7,16,20,25,26,27,29,30,31,33,36,37,40,45,50,52,57,64,66,79,83,84,85,86,87,90,91,92,101,102,103,110]
others = ['Mid/Offlane',2,9,13,14,17,21,22,24,34,37,38,39,43,51,55,60,65,68,71,74,75,76,78,88,96,97,98,99,100,105,107,108,111]

# end lists
# declare program functions

def return_matches(a,b):
	count = 0
	for i in (set(a) & set(b)):
		count+=1
	return count	
def max_played(c,s,o):
	max = c
	if s > max:
		max = s
		return 'Support'
	elif o > max:
		max = o
		return 'Mid/Offlane'
	else: return 'Carry'
def what_type(a,list):
	for i in xrange(len(list)):
		if a == list[i]:
			return list[0]
# end program functions
# begin favorite hero calculation

picked_heroes = list()
matches_list = list()
hero_name = ''
print 'Please enter 64-bit Steam Profile ID: ',
id64 = raw_input()
steamid64 = long(id64)
dest = open('output.json', 'w+')
request = Request('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key=ENTER_YOUR_ID&account_id='+id64)
sleep(1)
steamid32 = steamid64-76561197960265728
try:
	response = urlopen(request)
	kittens = response.read()
	print >> dest, kittens
except URLError, e:
    print 'No kittez. Got an error code:', e
dest.close()
json_data = open('output.json')
data = json.load(json_data)
for i in data["result"]["matches"]:
	for j in i["players"]:
		if j["account_id"] == (steamid32):
			picked_heroes.append(j["hero_id"])
	matches_list.append(i["match_id"])
picked =  Counter(picked_heroes).most_common()
carries_picked = (return_matches(picked,carry))
supports_picked = (return_matches(picked,support))
others_picked = (return_matches(others,carry))
favorite_role = max_played(carries_picked,supports_picked,others_picked)
most_played = max(i[1] for i in picked)
favorite_hero = [i[0] for i in picked if i[1] == most_played]
random.shuffle(favorite_hero)
print 'Collecting data for the last 100 games...'
print ' '
json_data_1 = open('C:\Project\hero_names.json')
hero_name = json.load(json_data_1)
for i in hero_name["result"]["heroes"]:
	if i["id"] == favorite_hero[0]:
		hero_name = i["localized_name"]
print 'Favorite Hero is: ',
print hero_name
print 'Favorite Role is: ',
print favorite_role

# end favorite hero calculation
# begin kda calculation

kda = 0.00
kda_fav = 0.00
match_count = 0.00
gpm = 0.00
xpm = 0.00
skill_points = 0.00
gold_points = 0.00
xp_points = 0.00
disconnects = 0
disconnect_abandons = 0
intentional_abandons = 0
afk_abandons = 0
load_failures = 0
wins = 0
for k in xrange(len(matches_list)):
	match_count+=1
	match_holder = open('temp_match.json', 'w+')
	required_match = str(matches_list[k])
	request_1 = Request('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=ENTER_YOUR_ID&match_id='+required_match)
	sleep(1)
	try:
		response_1 = urlopen(request_1)
		puppies = response_1.read()
		print >> match_holder, puppies
	except URLError, f:
		print 'No puppez. Got an error code:', f
		continue
	match_holder.close()
	json_data_2 = open('temp_match.json')
	match_data = json.load(json_data_2)
	current_role = ''
	for z in match_data["result"]["players"]:
		if z["account_id"] == (steamid32):
			k = float(z["kills"])
			d = float(z["deaths"])
			if d == 0:
				d = 1
			a = float(z["assists"])
			gpm += float(z["gold_per_min"])
			xpm += float(z["xp_per_min"])
			kda = (k+a)/d + kda
			
			#begin decisions
			
			if current_role == what_type(int(z["hero_id"]),carry):
				if kda < 1:
					skill_points -= 1.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 3.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points -= 2.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points -= 1.00
					else: continue
					if int(z["xp_per_min"]) < 200:
						xp_points -= 3.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points -= 2.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points -= 1.00
					else: continue
				elif kda < 3 and kda > 1:
					if int(z["gold_per_min"]) < 200:
						gold_points -= 3.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						continue
					else: gold_points += 1.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 3.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						continue
					else: xp_points += 1.00
				elif kda < 5 and kda > 3:
					skill_points += 1.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 3.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						continue
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 1.00
					else: gold_points += 2.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 3.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						continue
					else: xp_points += 1.00
				elif kda > 5:
					skill_points -= 3.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 2.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points += 1.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 2.00
					else: gold_points += 3.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 2.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 1.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 2.00
					else: xp_points += 3.00
					
			if current_role == what_type(int(z["hero_id"]),support):
				if kda < 1:
					if int(z["gold_per_min"]) < 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						continue
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 1.00
					else: gold_points += 2.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 1.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 2.00
					else: xp_points += 3.00
				elif kda < 3 and kda > 1:
					skill_points += 2.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						continue
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 3.00
					else: gold_points += 4.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 2.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 2.00
					else: xp_points += 3.00
				elif kda < 5 and kda > 3:
					skill_points += 3.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points += 2.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 3.00
					else: gold_points += 4.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 3.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 4.00
					else: xp_points += 5.00
				elif kda > 5:
					skill_points += 4.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points += 4.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 4.00
					else: gold_points += 5.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 3.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 4.00
					else: xp_points += 5.00
					
			if current_role == what_type(int(z["hero_id"]),others):
				if kda < 1:
					skill_points -= 5.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 4.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 1.00
					else: gold_points += 2.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 5.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points -= 1.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 1.00
					else: xp_points += 2.00
				elif kda < 3 and kda > 1:
					skill_points += 1.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 3.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points -= 1.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 2.00
					else: gold_points += 3.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 5.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 2.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 2.00
					else: xp_points += 3.00
				elif kda < 5 and kda > 3:
					skill_points += 2.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 3.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points += 2.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 3.00
					else: gold_points += 5.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 5.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 1.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 3.00
					else: xp_points += 4.00
				elif kda > 5:
					skill_points += 5.00
					if int(z["gold_per_min"]) < 200:
						gold_points -= 3.00
					elif int(z["gold_per_min"]) < 400 and int(z["gold_per_min"]) > 200:
						gold_points += 3.00
					elif int(z["gold_per_min"]) < 600 and int(z["gold_per_min"]) > 400:
						gold_points += 4.00
					else: gold_points += 5.00
					if int(z["xp_per_min"]) < 200:
						xp_points -= 5.00
					elif int(z["xp_per_min"]) < 400 and int(z["xp_per_min"]) > 200:
						xp_points += 3.00
					elif int(z["xp_per_min"]) < 600 and int(z["xp_per_min"]) > 400:
						xp_points += 4.00
					else: xp_points += 5.00
			
			# end decisions
			
			# start leaver status
			
			if int(z["leaver_status"]) == 1:
				disconnects += 1
			if int(z["leaver_status"]) == 2:
				disconnect_abandons += 1
			if int(z["leaver_status"]) == 3:
				intentional_abandons += 1
			if int(z["leaver_status"]) == 4:
				afk_abandons += 1
			if int(z["leaver_status"]) == 5 or int(z["leaver_status"]) == 6:
				load_failures += 1
			
			# end leaver status
			
			if z["hero_id"] == favorite_hero[0]:
				k_fav = float(z["kills"])
				d_fav = float(z["deaths"])
				if d_fav == 0:
					d_fav = 1
				a_fav = float(z["assists"])
				kda_fav += (k_fav+a_fav)/d_fav
average_kda = float(kda/match_count)
average_gpm = float(gpm/match_count)
average_xpm = float(xpm/match_count)
average_kda_fav = float(kda_fav/most_played)
kda_deviation = average_kda_fav - average_kda
skill_level = float(((skill_points+gold_points+xp_points)/3)/match_count)
skill_type = ''
success_rate = int((wins/match_count)*100)
print 'Average KDA is: ',
print average_kda
print 'Average KDA with favorite Hero is: ',
print average_kda_fav
print 'KDA deviation from mean is: ',
print kda_deviation
print 'Average GPM is: ',
print average_gpm
print 'Average XPM is: ',
print average_xpm
if skill_level < 0:
	skill_type = 'Below_Normal'
elif skill_level > 0 and skill_level < 5:
	skill_type = 'Normal'
elif skill_level > 5 and skill_level < 10:
	skill_type = 'High'
else: skill_type = 'Very High'
print 'Load Failures: ', load_failures
print 'Disconnects: ', disconnects
print 'Disconnects (Abandonment): ', disconnect_abandons
print 'Ragequits: ', intentional_abandons
print 'AFKs: ', afk_abandons

player_out = {'fh':hero_name,'fr':favorite_role,'kda':average_kda,'kdaf':average_kda_fav,'kdad':kda_deviation,'gpm':average_gpm,'xpm':average_xpm,'loadf':load_failures,'disc':disconnects,'abdn':disconnect_abandons,'afk':afk_abandons,'rgqt':intentional_abandons,'id':id64}

dest_2 = open('pickout.json', 'w+')
jout = json.dumps(player_out)
print >> dest_2, jout

# end KDA calculation