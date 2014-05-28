import os
import fnmatch
import argparse

def filefinder():
    parser = argparse.ArgumentParser(description='wanna see list of files')

    parser.add_argument("--directory",  type = str, default = "/Users/iUruru/Develop/", help = "where you hope to find")
    parser.add_argument("--extensions", type = str, default = "*.md", action = "store", help = "one kind of files, like *.py")

    options = parser.parse_args()

    for root, dirs, files in os.walk(options.directory):
        for nameFile in files:
            if fnmatch.fnmatch(nameFile, options.extensions):
                print (os.path.join(root, nameFile))

    print("path is " + str(options.directory))
    print("ext is " + str(options.extensions))

filefinder()