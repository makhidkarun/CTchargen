"""
chargen.py
Classic Traveller character generator
v0.01, March 30th, 2018
By Omer Golan-Joel, golan2072@gmail.com
This code is open-source
"""

#import modules

import random
import string
import os
import unittest
import platform
import stellagama

#career data

Navy={"enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Ensign", "Lieutenant",
"Lt Commander", "Commander", "Captain", "Admiral"], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "+1 SOC"], "service": ["Ship's Boat",
"Vacc Suit", "Forward Obs", "Gunnery", "Blade Combat", "Gun Combat"], "advanced": ["Vacc Suit",
"Mechanical", "Electronics", "Engineering", "Gunnery", "J-o-T"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"], "rank skill key": [5, 6], "rank skills": ["+1 SOC",
"+1 SOC"]}

#additional data

guns=["Body Pistol", "Autopistol", "Revolver", "Carbine", "Rifle", "Autorifle", "Shotgun", "SMG", "Laser Carbine", "Laser Rifle"]
melee=["Club", "dagger", "Blade", "Foil", "Cutlass", "Sword", "Broadsword", "Bayonet", "Spear", "Halberd", "Pike", "Cudgel"]
vehicles=["Aircraft (Helicopter)", "Aircraft (Propeller-driven)", "Aircraft (Jet-driven)" "Grav Vehicle", "Tracked Vehicle", "Wheeled Vehicle", "Watercraft (Small Watercraft)", "Watercraft (Large Watercraft)", "Watercraft (Hovercraft)", "Watercraft (Submerisible)"]

#character data format

# chardict={"UPP": [], "name": "", "sex": "", "age": 18, "career": "", "rank": 0, "terms": 0, "alive": "",
# "skills": {}, "possessions": {}, "cash": 0}

testchar={"UPP": [999999], "name": "", "sex": "", "age": 18, "career": "Navy", "rank": 0, "terms": 0, "alive": "",
"skills": {"Gunnery": 1, "Gun Combat": 1, "Pilot": 1}, "possessions": {}, "cash": 0}

#functions

def sex_gen():
	"""
	sex-generating function
	"""
	roll=stellagama.dice(1,6)
	if roll in [1, 2, 3]:
		return "male"
	elif roll in [4, 5, 6]:
		return "female"
	else:
		return "androgynous"
		
def name_gen(sex): #input character sex
	"""
	randomly chooses a character name from a list
	"""
	name=""
	if sex=="male":
		return stellagama.random_line("malenames.txt") #output random male name
	elif sex=="female":
		return stellagama.random_line("femalenames.txt") #output random female name
	else:	#in case of wrong input
		return "Tokay" #output placeholder

def add_skill(character, skill): #inputs the character dictionary and skill
	"""
	adds a skill or characteristic bonus to a character
	"""
	if skil=="+1 STR":
		character["UPP"][0]+=1
	elif skil=="+1 DEX":
		character["UPP"][1]+=1
	elif skil=="+1 END":
		character["UPP"][2]+=1
	elif skil=="+1 INT":
		character["UPP"][3]+=1
	elif skil=="+1 EDU":
		character["UPP"][4]+=1
	elif skil=="+1 SOC":
		character["UPP"][5]+=1
	elif skill in character["skills"]:
		character["skills"][skill] += 1
	elif skill not in character ["skills"]:
		character["skills"][skill] = 1
	return character #outputs the character dictionary

def skill_stringer(input_dict): #input a dictionary
	"""
	converts a dictionary to a string, Traveller skill format
	"""
	return ', '.join('-'.join((k, str(v))) for k,v in sorted(input_dict.items())) #output formatted skill list string

def possession_stringer(input_dict):
	"""
	converts a dictionary to a string, Traveller possessions format
	"""
	return ', '.join(' x'.join((k, str(v))) for k,v in sorted(input_dict.items())) #output formatted skill list string

def upp_stringer(input_list): #input a characteristics list
	"""
	converts a characteristics list to a UPP string
	"""
	output_list=[]
	for item in input_list:
		output_list.append(str(stellagama.pseudo_hex(item)))
	return ''.join (output_list) #output a string

def career_choice (character): #input character dictionary
	if character["UPP"][4]==max(character["UPP"]):
		character["career"]="Navy"
	elif character["UPP"][0]==max(character["UPP"]):
		character["career"]=stellagama.random_choice(["Scout", "Marines"])
	elif character["UPP"][2]==max(character["UPP"]):
		character["career"]="Army"
	elif character["UPP"][3]==max(character["UPP"]):
		character["career"]="Merchants"
	else:
		character["career"]="Other"
	return character

# def enlistment (chardict): #input character dictionary
	# career=chardict["career"]
	# enlisted = stellagama.dice(2, 6)
	# if chardict["UPP"][career["enlistment DM+1"]]>=career["enlistment DM+1 level"]:
		# enlisted+=1
	# if chardict["UPP"][career["enlistment DM+2"]]>=career["enlistment DM+2 level"]:
		# enlisted+=2
	# if enlisted >= enlisted_level:
		# return True
	# else:
		# return False
		
def chargen (chardict): #input character dictionary
	"""
	main character generation loop
	"""
	chardict = career_choice (chardict)
	career= Navy
	enlistment=stellagama.dice (2, 6)
	if enlistment >= career["enlistment"]:
		chardict["career"]=chardict["career"]
	else:
		chardict["career"]=stellagama.random_choice(["Navy", "Marines", "Army", "Scouts", "Merchants", "Other"])
	return chardict
	
#classes	

class character:
	def __init__ (self):
		character.chardict={"UPP": [stellagama.dice(2, 6), stellagama.dice(2, 6), stellagama.dice(2, 6),
		stellagama.dice(2, 6), stellagama.dice(2, 6), stellagama.dice(2, 6)], "name": "", "sex": sex_gen(),
		"age": 18, "career": "", "rank": 0, "terms": 0, "alive": "", "skills": {}, "possessions": {},
		"cash": 0}
		character.chardict["name"] = name_gen(character.chardict["sex"])
		character.chardict = chargen (character.chardict)

#test area
# career=navy
# if stellagama.dice (2, 6) >= career["survival"]:
	# print ("Survived!")
# else:
	# print ("Died in the line of duty!")
	
character1=character()
print (upp_stringer(character1.chardict["UPP"]))
print (character.chardict["sex"])
print (character.chardict["name"])
print (character.chardict["career"])
print (possession_stringer ({"Laser Rifle":1, "Laser Pistol":2, "Low Passage": 3}))

# print (enlistment(testchar))
