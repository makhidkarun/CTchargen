"""
chargen.py
Classic Traveller character generator
v0.15, April 6th, 2018
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
from collections import namedtuple

#career data

Navy={"name": "Navy", "enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Starman", "Ensign", "Lieutenant",
"Lt Commander", "Commander", "Captain", "Admiral"], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "+1 SOC"], "service": ["Ship's Boat",
"Vacc Suit", "Forward Obs", "Gunnery", "Blade Combat", "Gun Combat"], "advanced": ["Vacc Suit",
"Mechanical", "Electronics", "Engineering", "Gunnery", "J-o-T"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"], "rank skill key": [5, 6], "rank skills": ["+1 SOC",
"+1 SOC"]}

Marines={"name": "Marines", "enlistment": 9, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 0,
"enlistment DM+2 level": 8, "survival": 6, "survival DM+1": 2, "survival DM+1 level": 8,
"commission": 9, "commission DM+1": 4, "commission DM+1 level": 7, "promotion": 9,
"promotion DM+1": 5, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Trooper", "Lieutenant", "captain",
"Force Cmdr", "Lt Colonel", "Colonel", "Brigadier"], "muster": ["Low Passage", "+2 INT", "+1 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 30000, 40000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "Gambling", "Brawling", "Blade Cbt"], "service": ["ATV",
"Mechanical", "Electronic", "Tactics", "Blade Cbt", "Gun Combat"], "advanced": ["Vehicle",
"Mechanical", "Electronic", "Tactics", "Blade Cbt", "Gun Combat"], "advanced 2": ["Medical", "Tactics",
"Tactics", "Computer", "Leader", "Admin"], "rank skill key": [0, 1], "rank skills": ["Cutlass",
"Revolver"]}

Army={"name": "Army", "enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Starman", "Ensign", "Lieutenant",
"Lt Commander", "Commander", "Captain", "Admiral"], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "+1 SOC"], "service": ["Ship's Boat",
"Vacc Suit", "Forward Obs", "Gunnery", "Blade Combat", "Gun Combat"], "advanced": ["Vacc Suit",
"Mechanical", "Electronics", "Engineering", "Gunnery", "J-o-T"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"], "rank skill key": [5, 6], "rank skills": ["+1 SOC",
"+1 SOC"]}

Merchants={"name": "Merchants", "enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Starman","Ensign", "Lieutenant",
"Lt Commander", "Commander", "Captain", "Admiral"], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "+1 SOC"], "service": ["Ship's Boat",
"Vacc Suit", "Forward Obs", "Gunnery", "Blade Combat", "Gun Combat"], "advanced": ["Vacc Suit",
"Mechanical", "Electronics", "Engineering", "Gunnery", "J-o-T"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"], "rank skill key": [5, 6], "rank skills": ["+1 SOC",
"+1 SOC"]}

Scouts={"name": "Scouts", "enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["", "", "",
"", "", "", ""], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "+1 SOC"], "service": ["Ship's Boat",
"Vacc Suit", "Forward Obs", "Gunnery", "Blade Combat", "Gun Combat"], "advanced": ["Vacc Suit",
"Mechanical", "Electronics", "Engineering", "Gunnery", "J-o-T"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"], "rank skill key": [5, 6], "rank skills": ["+1 SOC",
"+1 SOC"]}

Other={"name": "Other", "enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["", "", "",
"", "", "", ""], "muster": ["Low Passage", "+1 INT", "+2 EDU",
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

def add_skill(skill_list, skill): #inputs the skill list, and skill
	"""
	adds a skill or characteristic bonus to a character
	"""
	if skill in skill_list:
		skill_list[skill] += 1
	elif skill not in skill_list:
		skill_list[skill] = 1
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

def career_choice (upp): #input upp list
	"""
	chooses a career based on UPP characteristics.
	"""	
	if upp[4]==max(upp):
		career=Navy
	elif upp[0]==max(upp):
		career=stellagama.random_choice([Scouts, Marines])
	elif upp[2]==max(upp):
		career=Army
	elif upp[3]==max(upp):
		career=Merchants
	else:
		career=Other
	return career #outputs the chatacter's career
	
#classes	

class character:
	"""character generation class"""
	def __init__ (self):
		"""generate basic stats"""
		self.upp=[stellagama.dice(2, 6), stellagama.dice(2, 6), stellagama.dice(2, 6), stellagama.dice(2, 6), stellagama.dice(2, 6), stellagama.dice(2, 6)]
		self.skills={}
		self.possessions={}
		self.rank=0
		self.terms=0
		self.title=""
		self.status = ""
		self.sex=sex_gen()
		self.name=name_gen(self.sex)
		self.surname=stellagama.random_line ("surnames.txt")
		self.career=career_choice(self.upp)
		self.age=18
		"""enlistment"""
		enlistment=stellagama.dice(2,6)
		if enlistment>=self.career["enlistment"]:
			self.career=self.career
		else:
			self.career=stellagama.random_choice([Navy, Marines, Army, Merchants, Scouts, Other])
		in_career=True
		while in_career == True:
			survival=stellagama.dice(2,6)
			if survival>=self.career["survival"]:
				in_career=True
				self.terms+=1
				self.age+=4
			else:
				self.status="DECEASED"
				in_career=False
				break
			"""skill generation"""			
			if self.career in [Scouts, Other]:
				for i in range (0,2):	
					skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"]) 	
					add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))
			else:
				if self.terms==1:
					for i in range (0,2): 
						skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"]) 	
						add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))				
				else:
					skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"]) 	
					add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))		
			"""commission and promotion"""			
			if self.career in [Scouts, Other]:
				self.rank=0			
			elif self.rank==0:
				commission=stellagama.dice(2,6)
				if commission>=self.career["commission"]:
					self.rank+=1
					skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"]) 
					add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))	
				else:
					self.rank=self.rank
			elif self.rank>0 and self.rank<6:
				promotion=stellagama.dice(2,6)
				if promotion>=self.career["promotion"]:
					self.rank+=1
					skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"]) 
					add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))
				else:
					self.rank=self.rank
			"""reenlistment"""
			reenlistment=stellagama.dice(2,6)
			if self.terms<7 and reenlistment>= self.career["reenlist"]:
				in_career=True
			elif self.terms>=7 and reenlistment==12:
				in_career=True
			else:
				in_career=False
		if self.upp[5]==11:
			self.title="Knight"
		elif self.upp[5]==12:
			self.title="Baron"
		elif self.upp[5]==13:
			self.title="Marquis"
		elif self.upp[5]==14:
			self.title="Count"
		elif self.upp[5]==15:
			self.title="Duke"
		else:
			if self.sex=="male":
				self.title="Mr."
			elif self.sex=="female":
				self.title=stellagama.random_choice(["Ms.", "Mrs."])	

#main program	
character1=character()
print ("")
print (character1.title, character1.name, character1.surname+",", "UPP", upp_stringer(character1.upp)+",", character1.age, "years old"+",", character1.career["name"], character1.career["ranks"][character1.rank], character1.terms, "Terms", character1.status)
print (skill_stringer(character1.skills))
print ("")
