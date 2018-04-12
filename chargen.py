"""
chargen.py
Classic Traveller character generator
v0.4, April 12th, 2018
By Omer Golan-Joel, golan2072@gmail.com
This code is open-source
"""

# import modules

import stellagama

# career data

Navy={"name": "Navy", "enlistment": 8, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 4,
"enlistment DM+2 level": 9, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Starman", "Ensign", "Lieutenant",
"Lt Commander", "Commander", "Captain", "Admiral"], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "+1 SOC"], "service": ["Ship's Boat",
"Vacc Suit", "Forward Obs", "Gunnery", "Blade Combat", "Gun Combat"], "advanced": ["Vacc Suit",
"Mechanical", "Electronics", "Engineering", "Gunnery", "J-o-T"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"], "rank skills": {5:"+1 Soc", 6: "+1 SOC"}}

Marines={"name": "Marines", "enlistment": 9, "enlistment DM+1": 3, "enlistment DM+1 level": 8,  "enlistment DM+2": 0,
"enlistment DM+2 level": 8, "survival": 6, "survival DM+1": 2, "survival DM+1 level": 8,
"commission": 9, "commission DM+1": 4, "commission DM+1 level": 7, "promotion": 9,
"promotion DM+1": 5, "promotion DM+1 level": 8, "reenlist": 6, "ranks": ["Trooper", "Lieutenant", "Captain",
"Force Cmdr", "Lt Colonel", "Colonel", "Brigadier"], "muster": ["Low Passage", "+2 INT", "+1 EDU",
"Blade", "TAS", "High Passage", "+2 SOC"], "cash": [1000, 5000, 5000, 10000, 20000, 30000, 40000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "Gambling", "Brawling", "Blade Cbt"], "service": ["ATV",
"Mechanical", "Electronic", "Tactics", "Blade Cbt", "Gun Combat"], "advanced": ["Vehicle",
"Mechanical", "Electronic", "Tactics", "Blade Cbt", "Gun Combat"], "advanced 2": ["Medical", "Tactics",
"Tactics", "Computer", "Leader", "Admin"], "rank skills":{0:"Cutlass", 1:"Revolver"}}

Army={"name": "Army", "enlistment": 5, "enlistment DM+1": 1, "enlistment DM+1 level": 6,  "enlistment DM+2": 2,
"enlistment DM+2 level": 5, "survival": 5, "survival DM+1": 4, "survival DM+1 level": 6,
"commission": 5, "commission DM+1": 1, "commission DM+1 level": 7, "promotion": 6,
"promotion DM+1": 4, "promotion DM+1 level": 7, "reenlist": 7, "ranks": ["Private", "Lieutenant", "Captain",
"Major", "Lt. Colonel", "Colonel", "General"], "muster": ["Low Passage", "+1 INT", "+2 EDU",
"Gun", "High Passage", "Mid Passage", "+1 SOC"], "cash": [2000, 5000, 10000, 10000, 10000, 20000, 30000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "Gambling", "+1 EDU", "Brawling"], "service": ["ATV",
"Air/Raft", "Gun Combat", "Forward Obs", "Blade Combat", "Gun Combat"], "advanced": ["Vehicle",
"Mechanical", "Electronics", "Tactics", "Blade Combat", "Gun Combat"], "advanced 2": ["Medical", "Tactics",
"Tactics", "Computer", "Leader", "Admin"], "rank skills": {0:"Rifle",
1: "SMG"}}

Merchants={"name": "Merchants", "enlistment": 7, "enlistment DM+1": 0, "enlistment DM+1 level": 7,  "enlistment DM+2": 3,
"enlistment DM+2 level": 6, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 7,
"commission": 4, "commission DM+1": 3, "commission DM+1 level": 7, "promotion": 10,
"promotion DM+1": 3, "promotion DM+1 level": 9, "reenlist": 4, "ranks": ["Spaceman","4th Officer", "3rd Officer",
"2nd Officer", "1st Officer", "Captain", ""], "muster": ["Low Passage", "+1 INT", "+1 EDU",
"Blade", "Low Passage", "High Passage", "Free Trader"], "cash": [1000, 5000, 10000, 10000, 10000, 50000, 100000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 STR", "Blade Combat", "Bribery"], "service": ["Vehicle",
"Vacc Suit", "J-o-T", "Steward", "Electronic", "Gun Combat"], "advanced": ["Streetwise",
"Mechanical", "Electronic", "Navigation", "Gunnery", "Medical"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "Admin"],  "rank skills": {1: "Pilot"}}

Scouts={"name": "Scouts", "enlistment": 7, "enlistment DM+1": 3, "enlistment DM+1 level": 6,  "enlistment DM+2": 0,
"enlistment DM+2 level": 8, "survival": 7, "survival DM+1": 2, "survival DM+1 level": 9,
"commission": 12, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 3, "ranks": ["", "", "",
"", "", "", ""], "muster": ["Low Passage", "+2 INT", "+2 EDU",
"Blade", "Gun", "Scout Ship", ""], "cash": [20000, 20000, 30000, 30000, 50000, 50000, 50000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "+1 INT", "+1 EDU", "Gun Combat"], "service": ["Air/Raft",
"Vacc Suit", "Mechanical", "Navigation", "Electronic", "J-o-T"], "advanced": ["Vehicle",
"Mechanical", "Electronics", "J-o-T", "Gunnery", "Medical"], "advanced 2": ["Medical", "Navigation",
"Engineering", "Computer", "Pilot", "J-o-T"], "rank skills": {0: "Pilot"}}

Other={"name": "Other", "enlistment": 3, "enlistment DM+1": 3, "enlistment DM+1 level": 14,  "enlistment DM+2": 4,
"enlistment DM+2 level": 14, "survival": 5, "survival DM+1": 3, "survival DM+1 level": 9,
"commission": 10, "commission DM+1": 5, "commission DM+1 level": 9, "promotion": 8,
"promotion DM+1": 4, "promotion DM+1 level": 8, "reenlist": 5, "ranks": ["", "", "",
"", "", "", ""], "muster": ["Low Passage", "+1 INT", "+1 EDU",
"Gun", "High Passage", "", ""], "cash": [1000, 5000, 10000, 10000, 10000, 50000, 100000],
"personal": ["+1 STR", "+1 DEX", "+1 END", "Blade Combat", "Brawling", "-1 SOC"], "service": ["Vehicle",
"Gambling", "Brawling", "Bribery", "Blade Combat", "Gun Combat"], "advanced": ["Streetwise",
"Mechanical", "Electronics", "Gambling", "Brawling", "Forgery"], "advanced 2": ["Medical", "Forgery",
"Electronic", "Computer", "Streetwise", "J-o-T"], "rank skills": {}}

# additional data

guns=["Body Pistol", "Autopistol", "Revolver", "Carbine", "Rifle", "Autorifle", "Shotgun", "SMG", "Laser Carbine", "Laser Rifle"]
melee=["Blade", "Foil", "Cutlass", "Sword", "Broadsword", "Bayonet", "Spear", "Halberd", "Pike", "Cudgel"]
vehicles=["Aircraft (Helicopter)", "Aircraft (Propeller-driven)", "Aircraft (Jet-driven)" "Grav Vehicle", "Tracked Vehicle", "Wheeled Vehicle", "Watercraft (Small Watercraft)", "Watercraft (Large Watercraft)", "Watercraft (Hovercraft)", "Watercraft (Submerisible)"]

# functions

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

def add_skill(skill_list, skill): #inputs the skill dictionary and skill
	"""
	adds a skill or characteristic bonus to a character
	"""
	if skill=="Gun Combat":
		if stellagama.dice(1,6)>=3:
			for item in guns:
				if item in skill_list:
					skill=item
				else:
					skill=stellagama.random_choice(guns)
		else:
			skill=stellagama.random_choice(guns)
	elif skill in ["Blade Combat", "Blade Cbt"]:
		if stellagama.dice(1,6)>=3:
			for item in melee:
				if item in skill_list:
					skill=item
				else:
					skill=stellagama.random_choice(melee)
		else:
			skill=stellagama.random_choice(melee)
	elif skill=="Vehicle":
		if stellagama.dice(1,6)>=3:
			for item in vehicles:
				if item in skill_list:
					skill=item
			else:
				skill=stellagama.random_choice(vehicles)
		else:
			skill=stellagama.random_choice(vehicles)
	if skill in skill_list:
		skill_list[skill] += 1
	elif skill not in skill_list:
		skill_list[skill] = 1
	return skill_list #outputs the skill dictionary

def add_possession(possessions, item): #inputs the possession dictionary and item
	"""

	adds a skill or characteristic bonus to a character
	"""
	if item=="Blade":
		item=stellagama.random_choice(melee)
	if item=="Gun":
		item=stellagama.random_choice(guns)
	if item in possessions:
		possessions[item] += 1
	elif item not in possessions:
		possessions[item] = 1
	return possessions #outputs the skill dictionary

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
		self.cash=0
		self.title=""
		self.status = ""
		self.sex=stellagama.random_choice(["male", "female"])
		self.name=name_gen(self.sex)
		self.surname=stellagama.random_line ("surnames.txt")
		self.career=career_choice(self.upp)
		self.age=18
		"""enlistment"""
		enlistment=stellagama.dice(2,6)
		if self.upp[self.career["enlistment DM+1"]]>=self.career["enlistment DM+1 level"]:
			enlistment+=1
		if self.upp[self.career["enlistment DM+2"]]>=self.career["enlistment DM+2 level"]:
			enlistment+=2
		if enlistment>=self.career["enlistment"]:
			self.career=self.career
		else:
			self.career=stellagama.random_choice([Navy, Marines, Army, Merchants, Scouts, Other])
		"""career generation loop"""
		in_career=True
		while in_career == True:
			if self.terms==0:
					if 0 in self.career["rank skills"]:
						add_skill(self.skills, self.career["rank skills"][0])
			survival=stellagama.dice(2,6)
			if self.upp[self.career["survival DM+1"]]>=self.career["survival DM+1 level"]:
				survival+=1
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
				if self.upp[self.career["commission DM+1"]]>=self.career["commission DM+1 level"]:
					commission+=1
				if commission>=self.career["commission"]:
					self.rank+=1
					skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"])
					add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))
					if self.rank in self.career["rank skills"]:
						add_skill(self.skills, self.career["rank skills"][self.rank])
				else:
					self.rank=self.rank
			if self.rank>0 and self.rank<6:
				promotion=stellagama.dice(2,6)
				if self.upp[self.career["promotion DM+1"]]>=self.career["promotion DM+1 level"]:
					promotion+=1
				if promotion>=self.career["promotion"]:
					self.rank+=1
					skill_table=stellagama.random_choice(["personal", "service", "advanced", "advanced 2"])
					add_skill(self.skills, stellagama.random_choice(self.career[skill_table]))
					if self.rank in self.career["rank skills"]:
						add_skill(self.skills, self.career["rank skills"][self.rank])
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
		"""mustering out"""
		if self.status=="DECEASED":
			self.possessions={}
		else:
			muster_throws=self.terms
			if self.rank in [1,2]:
				muster_throws+=1
			elif self.rank in [3,4]:
				muster_throws+=2
			elif self.rank in [5,6]:
				muster_throws+=3
			for i in range (0, muster_throws):
				muster_table=stellagama.random_choice(["muster", "cash"])
				muster_roll=stellagama.dice(1, 6)-1
				if muster_table=="muster" and self.rank>=5:
					muster_roll+=1
				if muster_table=="cash" and "Gambling" in self.skills:
					muster_roll+=1
				if muster_table=="muster":
					add_possession(self.possessions, self.career["muster"][muster_roll])
				elif muster_table=="cash":
					self.cash+=self.career["cash"][muster_roll]
		"""characteristic modifications"""
		for k in list(self.skills.keys()):
			if k == "+1 STR":
				self.upp[0]+=1
				del self.skills[k]
			elif k == "+1 DEX":
				self.upp[1]+=1
				del self.skills[k]
			elif k == "+1 END":
				self.upp[2]+=1
				del self.skills[k]
			elif k == "+1 INT":
				self.upp[3]+=1
				del self.skills[k]
			elif k == "+1 EDU":
				self.upp[4]+=1
				del self.skills[k]
			elif k == "+2 EDU":
				self.upp[4]+=2
				del self.skills[k]
			elif k == "+1 SOC":
				self.upp[5]+=1
				del self.skills[k]
			elif k == "+2 SOC":
				self.upp[5]+=2
				del self.skills[k]
			elif k == "-1 SOC":
				self.upp[5]-=1
		for k in list(self.possessions.keys()):
			if k == "+1 STR":
				self.upp[0]+=1
				del self.possessions[k]
			elif k == "+1 DEX":
				self.upp[1]+=1
				del self.possessions[k]
			elif k == "+1 END":
				self.upp[2]+=1
				del self.possessions[k]
			elif k == "+1 INT":
				self.upp[3]+=1
				del self.possessions[k]
			elif k == "+1 EDU":
				self.upp[4]+=1
				del self.possessions[k]
			elif k == "+2 EDU":
				self.upp[4]+=2
				del self.possessions[k]
			elif k == "+1 SOC":
				self.upp[5]+=1
				del self.possessions[k]
			elif k == "+2 SOC":
				self.upp[5]+=2
				del self.possessions[k]
		"""titles"""
		if self.upp[5]==11:
			if self.sex=="male":
				self.title="Knight"
			elif self.sex=="female":
				self.title="Dame"
		elif self.upp[5]==12:
			if self.sex=="male":
				self.title="Baron"
			elif self.sex=="female":
				self.title="Baroness"
		elif self.upp[5]==13:
			if self.sex=="male":
				self.title="Marquis"
			elif self.sex=="female":
				self.title="Marquesa"
		elif self.upp[5]==14:
			if self.sex=="male":
				self.title="Count"
			elif self.sex=="female":
				self.tatile="Contessa"
		elif self.upp[5]==15:
			if self.sex=="male":
				self.title="Duke"
			elif self.sex=="female":
				self.title="Duchess"
		elif self.rank>=5:
			self.title=self.career["ranks"][self.rank]
		else:
			if self.sex=="male":
				self.title="Mr."
			elif self.sex=="female":
				self.title=stellagama.random_choice(["Ms.", "Mrs."])
		if self.upp[4]>=12:
			self.title="Dr." #you get PhD at EDU 12+!
		if "Medical" in self.skills:
			if self.skills["Medical"]>=3:
				self.title="Dr."


#main program
character1=character()
print ("")
print (character1.title, character1.name, character1.surname+",", "UPP", upp_stringer(character1.upp)+",", character1.age, "years old")
print (character1.career["name"], character1.career["ranks"][character1.rank], character1.terms, "Terms", character1.status, "Cr"+str(character1.cash))
print (skill_stringer(character1.skills))
print (possession_stringer(character1.possessions))
print ("")
