from list import *import randomclass Implant:	def __init__(self):		self.implantParams = Stats()		self.implantName = 'Default Implant Name'	def get_name(self):		return self.implantName	def get_params(self):		return self.implantParams.get_params()	def create_by_random(self):		self.implantName = ""		self.implantParams = Stats()		for i in range(0, 3):			newWord = Words().get_random(listOfWordsDicts[i])			self.implantName = self.implantName + newWord.word + " "			self.implantParams.add_params(newWord.params)		return self	def create_by_name(self):		passclass Words:	def __init__(self):		self.word = ""		self.params = Stats()	def get_random(self, wordDict):		self.word = random.choice(list(wordDict.keys()))		self.params = Stats().set_params(wordDict[self.word][0], wordDict[self.word][1], wordDict[self.word][2], wordDict[self.word][3])		return selfclass Stats:	def __init__(self):		self.set_params(0,0,0,0)	def set_params(self, beauty, charisma, sexuality, smart):		self.beauty = beauty		self.charisma = charisma		self.sexuality = sexuality		self.smart = smart		return self	def add_params(self, instanceStats):		self.beauty += instanceStats.beauty		self.charisma += instanceStats.charisma		self.sexuality += instanceStats.sexuality		self.smart += instanceStats.smart		return self	def get_params(self):		return [self.beauty, self.charisma, self.sexuality, self.smart]