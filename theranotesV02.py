import tkinter as tk
from typing_extensions import IntVar
from tkinter import filedialog as fd
import os
from os import path
import json
import sys
import configparser
import cmcommon
from tkinter import simpledialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from cmcommon import jsonhandler, confighandler, menus
from tkinter.filedialog import asksaveasfile
from ttkthemes import ThemedTk, THEMES
from ttkwidgets import ScaleEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image


class Theranotes(ThemedTk):
    # class Theranotes(tk.Tk):
    def __init__(self, theme="black"):
        super().__init__()
        self.set_theme(theme)
        self.inipath = os.path.join(os.getcwd(), "data")
        self.inipath = os.path.join(self.inipath, "Theranotes.ini")
        self.datapath = None
        self.ini = {}
        self.defaultconf()
        self.lastsize = self.ini["lastsize"]
        print(self.lastsize)
        self.geometry(self.lastsize)
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.curwidget = None
        # TODO: add size recording on exit

        # ===============setup GUI Elements===============

        self.tabcntl = ttk.Notebook(self)
        self.tabcntl.grid(row=0, column=0, sticky="nsew")
        self.sesstab = ttk.Frame(self.tabcntl)
        self.sesstab.grid(row=0, column=0, sticky="nsew")
        self.sesstab.rowconfigure(0, weight=1)
        self.sesstab.columnconfigure(0, weight=1)
        self.traintab = ttk.Frame(self.tabcntl)
        self.traintab.grid(row=0, column=0, sticky="nsew")
        self.traintab.rowconfigure(0, weight=1)
        self.traintab.columnconfigure(0, weight=1)
        self.tabcntl.add(self.sesstab, text="Session")
        self.tabcntl.add(self.traintab, text="Train")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.title(self.ini["mainwintitle"])
        self.devmode = self.ini["devmode"]
        self.menus = menus(self)

        self.trainfiller = ttk.Label(self.traintab, text="training window")
        self.trainfiller.grid(row=0, column=0, sticky="nsew")

        self.sessionframe = tk.LabelFrame(self.sesstab, text="Session Window Frame")
        self.sessionframe.grid(row=0, column=0, sticky="nsew")
        self.sessionframe.rowconfigure(0, weight=1)
        self.sessionframe.columnconfigure(0, weight=1)

        self.sessfiller = ttk.Label(self.sessionframe, text="Session window")
        self.sessfiller.grid(row=0, column=0, sticky="nsew")

        self.trainingframe = tk.LabelFrame(self.traintab, text="Training Window Frame")
        self.trainingframe.grid(row=0, column=0, sticky="nsew")

        self.trainingfiller = ttk.Label(self.trainingframe, text="Training window")
        self.trainingfiller.grid(row=0, column=0, sticky="nsew")

        # ======================setup session canvas====================
        self.sessioncanvas = tk.Canvas(self.sessionframe, bg="white")
        self.sessioncanvas.grid(row=0, column=0, sticky="nsew")

        # ==================canvas 'buttons' ====================
        self.testbtn = ttk.Button(self.sessioncanvas, text="this is a test phrase to be filled in with NLP engine")
        print("rectangle id return during widget creation is: \n")
        newid = self.sessioncanvas.create_window(300, 200, window=self.testbtn)
        print(newid)

        self.sessioncanvas.bind_class("Button", "ButtonPress-1>", self.drag_start)
        # self.sessioncanvas.bind_class("Button", "ButtonPress-1>", self.getcloseid)

        # self.testbtn.bind("<ButtonPress-1>", self.drag_start)
        self.testbtn.bind("<ButtonRelease-1>", self.drag_stop)
        self.testbtn.bind("<B1-Motion>", self.drag)

        self.testbtn2 = ttk.Button(self.sessioncanvas, text="more sillly ipsum")
        self.myrect2 = self.sessioncanvas.create_window(100, 100, window=self.testbtn2)

        # self.sessioncanvas.bind_class("Button", "<ButtonPress-1>", self.drag_start)
        # self.sessioncanvas.bind_class("Button", "<ButtonRelease-1>", self.drag_stop)
        # self.sessioncanvas.bind_class("Button", "<B1-Motion>", self.drag)

        # self.testbtn2.bind("<ButtonPress-1>", self.drag_start)
        self.testbtn2.bind("<ButtonRelease-1>", self.drag_stop)
        self.testbtn2.bind("<B1-Motion>", self.drag)

    # =============startup functions================
    # TODO: clean up initialization functions and simplify to a single configuration file

    def getcloseid(self, event):
        self.curwidget = self.sessioncanvas.find_closest(event.x, event.y, halo=2)
        print(self.curwidget)

    def drag_start(self, event):
        """Begining drag of an object"""
        print("Drag start function begun")
        self.getcloseid(event)
        print("drag start function")
        print("Current returns: " + tk.CURRENT)
        # record the item and its location
        self._drag_data["item"] = tk.CURRENT  # self.sessioncanvas.find_closest(event.x, event.y)[0]
        print("item id: " + str(self.sessioncanvas.find_closest(event.x, event.y)[0]))
        id = self._drag_data["item"]
        print("current widget is: " + str(id))
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        print("drag end function")
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        step = 40
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        print(delta_x)
        print(delta_y)
        delta_x = int(step * round(float(delta_x) / step))
        delta_y = int(step * round(float(delta_y) / step))
        # move the object the appropriate amount
        self.sessioncanvas.move(self.curwidget, delta_x, delta_y)

    def readconfig(self):
        """
        The readconfig function reads the config file and sets the datapath variable to
        the path specified in the config file. The function also sets a global variable,
        self.ini, which is a dictionary containing all of the settings from the config
        file.
            Args:
                self: Access variables that belongs to the class
            Returns:
                The configuration settings from the ini file as a dictionary
        """
        readconf = confighandler(
            "load",
            self.inipath,
        )
        self.ini = readconf.getconfig()
        print("ini. settings: " + str(self.ini))
        self.datapath = os.path.join(os.getcwd(), self.ini["datadirectory"])
        print("Data path: " + str(self.datapath))

    def defaultconf(self):
        """
        The defaultconf function checks if the default.ini file exists in the same directory as this script. If it does,
        it reads that file and sets all of its values to variables in the main program. If it doesn't exist, a new one is created
        and all of its values are set to their defaults.
            Args:
                self: Access variables that belongs to the class
            Returns:
                True if the default
        """
        print(self.inipath)
        if os.path.exists(self.inipath):
            print("ini file found")
            self.readconfig()
            print("ini file contents: " + str(self.ini))
            return True
        else:
            print("Theranotes.ini not found")
            self.writedefconfig()
            return False

    def writedefconfig(self):
        """
        The writedefconfig function creates a default configuration file for the program.
        It is called when no config file exists in the directory, and it sets up all of the
        default values for each setting.
            Args:
                self: Access variables that belong to the class
            Returns:
                None
        """
        wconfig = configparser.ConfigParser()
        wconfig["DEFAULT"]["MainWinTitle"] = "Theranotes"
        wconfig["DEFAULT"]["MainTheme"] = "None"
        wconfig["DEFAULT"]["DevMode"] = "False"
        wconfig["DEFAULT"]["DataDirectory"] = "data"
        with open(self.inipath, "w") as configfile:
            wconfig.write(configfile)
        configfile.close()


if __name__ == "__main__":
    app = Theranotes()
    app.mainloop()
