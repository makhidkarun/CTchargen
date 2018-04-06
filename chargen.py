"""
chargen.py
Classic Traveller character generator
v0.03, April 6th, 2018
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

career = namedtuple("career", ["name", "enlistment", "survival",
"commission", "promotion", "reenlistment", "ranks_and_skills", "benefits", "cash", "personal", "service", "advanced", "advanced2"])

ranks = namedtuple("ranks", ["rank0", "rank1", "rank2", "rank3", "rank4", "rank5", "rank6"])

benefits = namedtuple ("benefits", ["benefit1", "benefit2", "benefit3", "benefit4", "benefit5", "benefit6", "benefit7"])

skills = namedtuple ("skills", ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6"])

#naval career

navy_ranks=ranks(
rank0=("Starman", None),
rank1=("Ensign", None),
rank2=("Lieutenant", None),
rank3=("Lt. Cmdr.", None),
rank4=("Commander", None),
rank5=("Captain", {"SOC": 1}),
rank6=("Admiral", {"SOC": 1}))

navy_personal = skills(
skill1={"STR": 1},
skill2={"DEX": 1},
skill3={"END": 1},
skill4={"INT": 1},
skill5={"EDU": 1},
skill6={"SOC": 1})

navy_service = skills(
skill1={"Ship's Boat": None},
skill2={"Vacc Suit": None},
skill3={"Fwd Obs": None},
skill4={"Gunnery": None},
skill5={"Melee Cbt": None},
skill6={"Gun Cbt": None})

navy_advanced = skills(
skill1={"Vacc Suit": None},
skill2={"Mechanical": None},
skill3={"Electronic": None},
skill4={"Engineering": None},
skill5={"Gunnery": None},
skill6={"J-o-T": None})

navy_advanced2 = skills(
skill1={"Medical": None},
skill2={"Navigation": None},
skill3={"Engineering": None},
skill4={"Computer": None},
skill5={"Pilot": None},
skill6={"Admin": None})

navy_cash=benefits(
benefit1=1000,
benefit2=5000,
benefit3=10000,
benefit4=10000,
benefit5=20000,
benefit6=50000,
benefit7=50000)

navy_benefits=benefits(
benefit1="Low Passage",
benefit2="INT",
benefit3="EDU",
benefit4="Blade",
benefit5="TAS",
benefit6="High Passage",
benefit7="SOC")

navy=career(
name="Navy",
enlistment={"INT": 8},
survival={"INT": 5},
commission={"SOC": 10},
promotion={"EDU": 8},
reenlistment=6,
ranks_and_skills=navy_ranks,
personal=navy_personal,
service=navy_service,
advanced=navy_advanced,
advanced2=navy_advanced2,
benefits=navy_benefits,
cash=navy_cash)

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

def add_skill(skill_list, upp, skill): #inputs the skill list, UPP, and skill
	"""
	adds a skill or characteristic bonus to a character
	"""
	if skill=="+1 STR":
		upp[0]+=1
	elif skill=="+1 DEX":
		upp[1]+=1
	elif skill=="+1 END":
		upp[2]+=1
	elif skill=="+1 INT":
		upp[3]+=1
	elif skill=="+1 EDU":
		upp[4]+=1
	elif skill=="+1 SOC":
		upp[5]+=1
	elif skill in skill_list:
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
		career="Navy"
	elif upp[0]==max(upp):
		career=stellagama.random_choice(["Scout", "Marines"])
	elif upp[2]==max(upp):
		career="Army"
	elif upp[3]==max(upp):
		career="Merchants"
	else:
		career="Other"
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
		self.sex=sex_gen()
		self.name=name_gen(self.sex)
		self.career=career_choice(self.upp)
		self.age=18
		"""enlistment"""

#main program	
character1=character()
print (upp_stringer(character1.upp))
print (character1.sex)
print (character1.name)
print (character1.career)
print (character1.age)

print (navy.name)
print (navy.promotion)
print (navy[7])
print (navy.cash.benefit1)
print (navy.benefits[1])
print (navy.ranks_and_skills.rank1)
print (navy.ranks_and_skills[0])
print (navy.service.skill3)
print (stellagama.random_choice(navy.service))
