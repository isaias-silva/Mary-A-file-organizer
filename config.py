import json
import os
from importlib.metadata import files
from os.path import exists
from pathlib import Path


def getConfig():
    print("\nload config...\n")
    if not exists("data/config.json"):
        print("config file not found: config now!");
        return createConfig()
    with open(os.path.abspath('data/config.json'), 'r') as file:
        config = json.load(file)
        if not config:
            createConfig()
            return getConfig()
        return config


def createConfig():
    data = {"path": input("principal path:"), "default_paths": [
    ]}
    add = True
    while add:
        action = input("add a path filter [Y/N]").upper()
        if action != "Y" and action != "N":
            raise print("Invalid response")
        add = action == "Y"
        if not add:
            break
        path_config = {"name": input("new path:"),
                       "regex": input("filter(regular expression for file ex = *.pdf|*.doc):")}
        data["default_paths"].append(path_config)
    if not Path("data").exists():
        print("generating: path config")
        Path("data").mkdir()

    with open("data/config.json", "w") as newfile:

        json.dump(data, newfile, indent=4)
