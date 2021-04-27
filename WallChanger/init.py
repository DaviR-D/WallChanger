import os
import json

config = dict()

with open("wallchanger.config") as conf:
	config = json.load(conf)

if(config['start_on_login']):
	os.system("python3 wallchanger.py")
    
