import os
import fnmatch
import datetime

def filefinder(dir, ext):

    with open(str(datetime.datetime.now())+"files_list.txt", "w") as listFiles:
        listFiles.write("path is " + str(dir) + "\n")
        listFiles.write("ext is " + str(ext) + "\n")
        for root, dirs, files in os.walk(dir):
            for nameFile in files:
                for every in ext:
                    if fnmatch.fnmatch(nameFile, every):
                        listFiles.write(os.path.join(root, nameFile) + "\n")
