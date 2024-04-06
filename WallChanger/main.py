import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import json
import os
from time import sleep

class WallChanger(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI.glade')
		self.window = builder.get_object('window')
		self.switch = builder.get_object('switch')
		self.chooser = builder.get_object('chooser')
		self.startButton = builder.get_object('button')
		self.cd_entry = builder.get_object('cd_entry')
		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)
		self.conf = dict()
		with open("wallchanger.config") as config:
			self.conf = json.load(config)
		self.switch.set_state(self.conf['start_on_login'])

	def onSwitch(self, data, state):
		self.conf['start_on_login'] = bool(state)
		with open("wallchanger.config", 'w') as config:
			json.dump(self.conf, config)

	def setFolder(self, data):
		self.conf['folder'] = self.chooser.get_filename()
		with open("wallchanger.config", 'w') as config:
			json.dump(self.conf, config)


	def Start(self, data):
		subprocess.run('python3 wallchanger.py &', shell=True)

	def setCD(self, data, bt):
		self.conf['countdown'] = self.cd_entry.get_text()
		with open("wallchanger.config", 'w') as config:
			json.dump(self.conf, config)

win = WallChanger()
win.window.show()
Gtk.main()
