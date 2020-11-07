import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

class Comp(Gtk.Window):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('UI.glade')
		self.window = builder.get_object('window')
		self.switch = builder.get_object('switch')
		self.chooser = builder.get_object('chooser')
		self.startButton = builder.get_object('button')
		builder.connect_signals(self)

	def onSwitch(self, state, data):
		pass

	def onFolderSet():
		pass

	def Start():
		pass

win = Comp()
win.window.show()
Gtk.main()
