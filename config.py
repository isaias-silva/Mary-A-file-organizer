import json
import os
def getConfig():
    
    print("\nload config...\n")
    with open(os.path.abspath('data/config.json'), 'r') as file:
        
        return json.load(file)