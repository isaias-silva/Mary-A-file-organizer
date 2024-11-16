import datetime
import os
from config import getConfig

today = str(datetime.date.today())
filename = "/report-by-mary" + today + ".txt"
config= getConfig()

def generate():
    if os.path.exists(config["path"] + filename):
        return
    with open(config["path"] + filename, "w") as report_file:
        report_file.write("Hello sir! Below is the report of the files that were moved now at " + today + "\n")


def append(info):
    with open(config["path"] + filename, "a") as report_file:
        report_file.write(info)
