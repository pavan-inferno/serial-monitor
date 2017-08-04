#!/usr/bin/env python
"""
/*  Password Hasher - might increase the security of some passwords
 *  Copyright (C) 2009 Henry Kroll, www.thenerdshow.com
 * 
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 * 
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 * 
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
"""
import os, sys, md5, string
import gtk
GDK_Escape=0xff1b;
class fooclass:
	def focus_received(self,widget,data=None):
		self.focused=widget
		#print(widget.get_name())
	def file_open(self,widget,data=None):
		pass
	def file_save(self,widget,data=None):
		pass
	def file_save_as(self,widget,data=None):
		pass
	def file_new(self,widget,data=None):
		pass
	def edit_cut(self,widget,data=None):
		gtk.Editable.cut_clipboard(self.focused)
	def edit_copy(self,widget,data=None):
		gtk.Editable.copy_clipboard(self.focused)
	def edit_paste(self,widget,data=None):
		gtk.Editable.paste_clipboard(self.focused)
	def edit_delete(self,widget,data=None):
		gtk.Editable.delete_selection(self.focused)
	def link_click(self,widget,data=None):
		os.system("htmlview "+widget.get_uri())
	def gtk_main_quit(self,widget,data=None):
		gtk.main_quit()
	def on_window1_remove(self,widget,data=None):
		gtk.main_quit()
	def generate_hash(self,widget,data=None):
		hash = md5.new()
		hash.update(self.entry1.get_text ())
		value = hash.hexdigest()
		self.entry2.set_text(value)
	def check_hash(self,widget,data=None):
		hash = md5.new()
		hash.update(self.entry1.get_text())
		value = hash.hexdigest()
		vtest = self.entry2.get_text()
		if value==vtest:
			self.label1.set_text("valid")
		else:
			self.label1.set_text("fail")
	def key_pressed(self,widget,event,data=None):
		#~ print "%4x" % (event.keyval)
		if (event.keyval==GDK_Escape):
			gtk.main_quit()
	def help_about(self,widget,data=None):
		result = self.about.run()
		self.about.hide()
		
	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("hasher.xml") 

		self.window = builder.get_object("window1")
		self.entry1 = builder.get_object("entry1")
		self.entry2 = builder.get_object("entry2")
		self.label1 = builder.get_object("label1")
		self.about  = builder.get_object("aboutdialog1")
		
		builder.connect_signals(self)
		self.entry1.connect("focus-in-event", self.focus_received)
		self.entry2.connect("focus-in-event", self.focus_received)
		self.focused=self.entry1

if __name__ == "__main__":
	foo=fooclass()
	foo.window.show()
	gtk.main()
