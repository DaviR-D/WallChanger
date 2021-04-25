from gi.repository import Gio
import glob
import time
import json

config = dict()

with open("wallchanger.config") as conf:
	config = json.load(conf)

wallpaper_list = glob.glob(config['folder'] + '/*') # Wallpaper folder

settings = Gio.Settings.new("org.gnome.desktop.background")

current_wallpaper = settings['picture-uri'][7:]

try:
	index = wallpaper_list.index(current_wallpaper)
except ValueError as e:
	index = 0


countdown = config['countdown']

while True:
	for wallpaper in wallpaper_list[index::]:
		settings['picture-url'] = 'file://' + wallpaper
		time.sleep(50) # Time for changing the wallpaper
	index = 0
