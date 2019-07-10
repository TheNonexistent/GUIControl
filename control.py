#!/usr/bin/python
import gi
import os
import functions
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def setlable():
   if functions.checkactive():
      status_lable.set_text("     Connected ")
      status_lable.modify_fg(Gtk.StateFlags.NORMAL,Gdk.color_parse( "#73D216" ))
      connectbtn.set_sensitive(False)
      disconnectbtn.set_sensitive(True)
   else:
      status_lable.set_text("Disconnected ")
      status_lable.modify_fg(Gtk.StateFlags.NORMAL,Gdk.color_parse( "#CC0000" ))
      disconnectbtn.set_sensitive(False)
      connectbtn.set_sensitive(True)

class Handler:
   def connectsig(self, button):
     functions.start()
     setlable()
   def dconnectsig(self, button):
     functions.stop()
     setlable()
   def confsig(self,button):
     functions.configure()
     status_lable = builder.get_object("statuslbl")
     setlable()

builder = Gtk.Builder()
builder.add_from_file("keriographical.glade")
builder.connect_signals(Handler())
status_lable = builder.get_object("statuslbl")
connectbtn = builder.get_object("connectbtn")
disconnectbtn = builder.get_object("dconnectbtn")
setlable()
window = builder.get_object("mainwindow")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
