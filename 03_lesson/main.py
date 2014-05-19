from classes import *

with open("ImplantNames.txt", "w") as fileWithNames:
    for i in range(1, 100):
        tempImplant = Implant().create_by_random()
        fileWithNames.write(tempImplant.get_name() + ": " + str(tempImplant.get_params()) + "\n")