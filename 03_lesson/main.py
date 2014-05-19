from list import *
import random


class Implant:
    implantName = 'Default Implant Name'
    implantParams = []

    def __init__(self):
        self.implantParams = []
        self.implantName = 'Default Implant Name'

    def get_name(self):
        return self.implantName

    def get_params(self):
        return self.implantParams

 #   def create_by_name(self):

 #   def create_by_params(self):

    def create_by_random(self):
        self.implantName = random.choice(list(wordAdj.keys())) + " " + random.choice(list(wordNoun.keys())) + " " + random.choice(list(wordAddNoun.keys()))
        return self

with open("ImplantNames.txt", "w") as fileWithNames:
    for i in range(1, 100):
        newImplant = Implant()
        fileWithNames.write(newImplant.create_by_random().get_name() + "\n")