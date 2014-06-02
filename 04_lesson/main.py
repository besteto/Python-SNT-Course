import argparse
import filefinder

parser = argparse.ArgumentParser(description='wanna see list of files')

parser.add_argument("--directory",  type = str, default = "/Users/iUruru/Develop/", help = "where you hope to find")
parser.add_argument("--extensions", type = str, default = "*.md", action = "store", help = "extensions with comma, like *.py, *.txt")

options = parser.parse_args()
listExtensions = [word.strip(" ") for word in options.extensions.split(",")]

filefinder.filefinder(options.directory, listExtensions)
