import os
import fnmatch

def filefinder(dir, ext):
    filesList = []
    for root, dirs, files in os.walk(dir):
        for nameFile in files:
            for every in ext:
                if fnmatch.fnmatch(nameFile, every):
                    filesList.append(os.path.join(root, nameFile))
    return filesList