import tkinter as tk
from tkinter import Canvas
from tkinter import StringVar
from functools import partial
from tkinter import ttk
import os
from os import path
import json
from cmcommon import jsonhandler, sentencetracker, confighandler, menuMaker, tabmaker, styler


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configfile = "Theranotes.ini"
        self.errors = {}
        self.datadir = os.path.join(os.getcwd(), "data")
        self.confparse = confighandler("None", self.datadir, self.configfile)
        print("config data: " + str(self.confparse.getconfig()))
        self.datareader = jsonhandler(self.datadir)
        self.phrases = self.datareader.readjson(os.path.join(self.datadir, "keyphrass.json"))
        if self.phrases[0] == False:
            self.errors["Open Keyphrases"] = self.phrases[1]
        self.tracker = sentencetracker()
        self.menus = menuMaker(self)
        self.tabdic = {"Session": "Session Window", "Trainer": "Training Window"}
        self.tabs = tabmaker(self.tabdic)
        self.tabs.maketabs()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.styler = styler()
        print(self.phrases)
        print("Current Error List: " + str(self.errors))


if __name__ == "__main__":
    Theranotes = App()
    Theranotes.mainloop()
