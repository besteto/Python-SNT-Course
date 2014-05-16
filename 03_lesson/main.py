from list import *
import random


def constructName(numb):
    new_name = []
    for every in range(numb):
        new_name.append(random.choice(list(wordAdj.keys())) + " " + random.choice(list(wordNoun.keys())) + " " +
                       random.choice(list(wordAddNoun.keys())))
    return new_name

with open("ImplantNames.txt", "w") as fileWithNames:
    for every in constructName(100):
        fileWithNames.write(every + "\n")