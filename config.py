import json
def getConfig():
    
    print("\nload config...\n")
    with open('./data/config.json', 'r') as file:
        
        return json.load(file)