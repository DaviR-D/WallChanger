import os
import glob
import time
import json
import subprocess

config = dict()

with open("wallchanger.config") as conf:
	config = json.load(conf)

wallpaper_list = glob.glob(config['folder'] + '/*') # Wallpaper folder
current_wallpaper = subprocess.check_output("gsettings get org.gnome.desktop.background picture-uri", shell=True, universal_newlines=True)[8:-2]
index = wallpaper_list.index(current_wallpaper)
countdown = config['countdown']

while True:
	for wallpaper in wallpaper_list[index::]:
		change = 'gsettings set org.gnome.desktop.background picture-uri' + ' file://' + wallpaper
		os.system(change)
		time.sleep(50) # Time for changing the wallpaper
	index = 0
