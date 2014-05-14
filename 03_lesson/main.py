from list import *
import random

def constructName(numb):
    newName = []
    for every in range(numb):
        newName.append(random.choice(list(wordAdj.keys())) + " " + random.choice(list(wordNoun.keys())) + " " + random.choice(list(wordAddNoun.keys())))
    return newName

with open("ImplantNames.txt", "w") as fileWithNames:
    for every in constructName(100):
        fileWithNames.write(every + "\n")