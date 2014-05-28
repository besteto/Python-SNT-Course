import os
import fnmatch
import argparse

def filefinder():
    parser = argparse.ArgumentParser(description='wanna see list of files')

    parser.add_argument("--directory",  type = str, default = "/Users/iUruru/Develop/", help = "where you hope to find")
    parser.add_argument("--extensions", type = str, default = "*.md", action = "store", help = "extensions with comma, like *.py, *.txt")

    options = parser.parse_args()
    listExtensions = [word.strip(" ") for word in options.extensions.split(",")]

    for root, dirs, files in os.walk(options.directory):
        for nameFile in files:
            for every in listExtensions:
                if fnmatch.fnmatch(nameFile, every):
                    print (os.path.join(root, nameFile))

    print("path is " + str(options.directory))
    print("ext is " + str(listExtensions))

filefinder()