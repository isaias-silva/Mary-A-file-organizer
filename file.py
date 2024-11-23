
from pathlib import Path
from config import getConfig
from colors import *
import report
import regex
import shutil
import random
import string
import os


config = getConfig()


def proccess():
    report.clear_past_reports()
    generatePaths()
    organizeFiles()



def organizeFiles():
    files = getFiles(Path(config["path"]))
    for file in files:
        fileMatch(file)


def fileMatch(file):
    report.generate()
    for path in config["default_paths"]:
        regExp = regex.converter(path["regex"])
        if regex.isMatch(regExp, file.name) and not ("report-by-mary" in file.name):
            path_new = config["path"] + "/" + path["name"]
            path_old = config["path"] + "/" + file.name
            moveFile(path_old, path_new, file.name)
            report.append(path_old+" moved from "+ path_new+"\n")


def moveFile(path_old, path_new, file_name):
    if Path(path_new + "/" + file_name).exists():

        new_file_name = generateRandomName(file_name)
        os.rename(path_old, path_new + "/" + new_file_name)

    else:
        shutil.move(path_old, path_new + "/" + file_name)

def generatePaths():

        for path in config["default_paths"]:
            path_global = config["path"] + "/" + path["name"]

        if not Path(path_global).exists():
            print("generating: %s" % path_global)
            Path(path_global).mkdir()


def getFiles(path: Path):
    print("get files in %s" % path.name)
    filelist = []
    for item in path.iterdir():
        if item.is_file():
            print(YELLOW +
                  "|___" + item.name +
                  RESET)
            filelist.append(item)
    return filelist


def generateRandomName(name: str):
    characters = string.ascii_letters + string.digits

    file_info = name.split(".")

    return "MARY-A-" + (''.join(random.choice(characters) for _ in range(6))) + "." + file_info[-1]
