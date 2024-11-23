import datetime
import os
from pathlib import Path

from config import getConfig

today = str(datetime.date.today())
filename = "report-by-mary-" + today + ".txt"
config = getConfig()


def generate():
    if os.path.exists(get_report_file_path()):
        return
    with open(get_report_file_path(), "w") as report_file:
        report_file.write("Hello sir! Below is the report of the files that were moved now at " + today + "\n")


def append(info):
    with open(get_report_file_path(), "a") as report_file:
        report_file.write(info)


def clear_past_reports():
    directory = Path(config["path"])

    for item in directory.iterdir():
        if item.is_file() and ("report-by-mary" in item.name) and item.name != filename:
            os.remove(config["path"] + "/" + item.name)

def get_report_file_path():
        return config["path"] +"/" +filename