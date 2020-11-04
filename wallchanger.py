import os
import glob
import time
import subprocess

home = subprocess.check_output("echo $HOME", shell=True, universal_newlines=True)[:-1]
wallpaper_list = glob.glob(home + '/Pictures/wall/*') # Wallpaper folder
current_wallpaper = subprocess.check_output("gsettings get org.gnome.desktop.background picture-uri", shell=True, universal_newlines=True)[8:-2]
index = wallpaper_list.index(current_wallpaper)

while True:
	for wallpaper in wallpaper_list[index::]:
		change = 'gsettings set org.gnome.desktop.background picture-uri' + ' file://' + wallpaper
		os.system(change)
		time.sleep(50) # Time for changing the wallpaper
	index = 0
