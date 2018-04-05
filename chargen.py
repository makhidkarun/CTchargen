"""
chargen.py
Classic Traveller character generator
v0.02, April 5th, 2018
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

# print (enlistment(testchar))
