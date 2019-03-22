#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, gi

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk, WebKit


class Browser:
  def __init__(self):
    self.builder = Gtk.Builder()
   
    self.builder.add_from_file("roksolana.glade")
    self.builder.connect_signals(self)

    self.toolbar1 = self.builder.get_object("toolbar1")
    self.back = self.builder.get_object("back")
    self.forward = self.builder.get_object("forward")
    self.refresh = self.builder.get_object("refresh")
    self.stop = self.builder.get_object("stop")
    self.url = self.builder.get_object("url")
    self.spinner = self.builder.get_object("spinner")
    self.progressbar = self. builder.get_object("progressbar")
    self.window = self.builder.get_object("window1")
    self.window.connect('destroy', lambda w: Gtk.main_quit())
    self.scrolledwindow = self.builder.get_object("scrolledwindow")
    self.window.show_all()

    self.webview = WebKit.WebView()
    self.scrolledwindow.add(self.webview)
    self.webview.open('http://google.com')
    self.webview.connect('title-changed', self.change_title)
    self.webview.connect('load-committed', self.change_url)
    self.webview.connect('load-committed', self.spinner_on)
    self.webview.connect('load_finished',self.spinner_off)
    #self.webview.connect('load-committed', self.progress_on)
    #self.webview.connect('load-progress-changed', self.progress_change)
    #self.webview.connect('document_load_finished',self.progress_off)
    self.webview.show()
