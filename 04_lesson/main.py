import argparse
import filefinder
import datetime

parser = argparse.ArgumentParser(description='wanna see list of files')

parser.add_argument("--directory",  type = str, default = "/Users/iUruru/Develop/", help = "where you hope to find")
parser.add_argument("--extensions", type = str, default = "*.md", action = "store", help = "extensions with comma, like '*.py, *.txt'")

options = parser.parse_args()
listExtensions = [word.strip(" ") for word in options.extensions.split(",")]

with open(str(datetime.datetime.now())+"files_list.txt", "w") as listFiles:
    listFiles.write("path is " + str(options.directory) + "\n")
    listFiles.write("ext is " + str(options.extensions) + "\n")

    for every in filefinder.filefinder(options.directory, listExtensions):
        listFiles.write(every + "\n")
