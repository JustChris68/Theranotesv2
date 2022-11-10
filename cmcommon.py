# my standard import module
import tkinter as tk
import os
from os import path
import json
import pprint
import configparser
from tkinter import messagebox, filedialog, ttk, Frame
import inspect
import sys


class styler:
    pass


class initconfig:
    def __init__(self, defaultconf):
        self.defaultconf = defaultconf
        self.parser = configparser.ConfigParser()


class tabmaker:
    def __init__(self, tabdic, tkstyle=None):
        self.tkstyle = tkstyle
        self.maketabs(tabdic)

    def maketabs(self, tabdic):
        self.tabs = ttk.Notebook()
        print(tabdic)
        self.session = tk.Frame(self)
        self.tabs.add(self.session, text="Session")
        self.trainer = tk.Frame(self)
        self.tabs.add(self.tabs, text="Training")

        # for tab in tabdic:
        #     print("creating tabs")
        #     exec("self.{0} = tk.Frame(self.tabs)".format(tab))
        #     print("adding tabs")
        #     self.tabs.add(self.tab, text=self.tabdic[tab])
        #     # exec("self.tabs.add(self.{0}, text='tabdic[{1}]'".format((str(tabdic[tab]), tab)))
        self.tabs.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        return self.tabs


""" 
included classes
    json handling
    configparser wrapper class - confighandler.. handles python configuration files
    lframemaker - class to generate labelframes from dictionary
    

 """


""" 
             for frame in LFrames:
            print(frame + "\n")
            if frame == "LabelFrames":
                print("LabelFrames: ")
                for entry in LFrames[frame]:
                    tempdic = LFrames[frame][entry]
                    for term in tempdic:
                        terms.append(tempdic[term])
                    exec("{0} = ttk.LabelFrame({1}, text = '{2}')".format(entry, terms[0], terms[1]))
                    exec("{0}.grid({1}, {2})".format(entry, terms[2], terms[3]))

 """


class menuMaker(tk.Menu):
    # TODO: add menus and commands
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.create_Topmenu()
        parent.config(menu=self.menu_bar)

    def create_Topmenu(self):
        self.menu_bar = tk.Menu(self.parent)
        self.create_Filemenu()
        self.create_Editmenu()
        self.create_Viewmenu()
        self.create_Aboutmenu()

    def create_Filemenu(self):
        self.filemenu = tk.Menu(self.menu_bar, tearoff=0)
        self.filemenu.add_command(label="New", command=lambda: self.fNew())
        self.filemenu.add_command(label="Open", command=lambda: self.fOpen())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save", command=lambda: self.fSave())
        self.filemenu.add_command(label="Exit", command=quit)
        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        # display the menu
        self.parent.config(menu=self.filemenu)

    def create_Editmenu(self):
        self.editmenu = tk.Menu(self.menu_bar, tearoff=0)
        self.editmenu.add_command(label="Copy", command=None)
        self.editmenu.add_command(label="Paste", command=None)
        self.menu_bar.add_cascade(label="Edit", menu=self.editmenu)
        pass

    def create_Viewmenu(self):
        pass

    def create_Aboutmenu(self):
        pass

    def fNew(self):
        pass

    def fOpen(self):
        pass

    def fSave(self):
        pass


""" class lframemaker:
    # create dictionary of variables for labelframes
    def __init__(self, framedic):
        self.framedic = framedic
        self.frames = {}

    def getframes(self):
        for frame in self.framedic:
            lblid = frame
            for value in self.framedic[frame]:
                framedata = self.framedic[frame][value]
            self.frames[lblid] = framedata
        return self.frames """


class jsonhandler:
    def __init__(self, filepath=None, data=None):
        self.filepath = filepath
        if not self.filepath == None:
            os.path.join(os.getcwd(), self.filepath)
        self.data = data
        # print(self.checktype())
        self.warningmessage = "Error"

    def checktype(self):
        """
        The checktype function checks to see if the data attribute of a module is a dictionary. If it is not, then
        the program will print out that the data type is incorrect and return False. Otherwise, it returns True.
            Args:
                self: Refer to the object itself
            Returns:
                True if the data attribute is a dictionary
        """
        if not isinstance(self.data, dict):
            print("data not a dictionary, cannot save as json")
            return False
        else:
            return True

    def savejson(self):
        """
        The savejson function saves the data dictionary to a JSON file.
        It takes one argument, self. It checks if the data is a dictionary and then writes it
        to the filepath specified in self.filepath
            Args:
                self: Access variables that belong to the class
            Returns:
                A string message
        """
        if not self.checktype():
            message = "Data not a dictionary, cannot save as JSON"
            self.warn(message)
        else:
            with open(self.filepath, "w") as fp:
                datadic = json.dumps(self.data, indent=4)
                json.dump(datadic, fp)
                fp.close
                message = "JSON File " + self.filepath + " saved succesfully"
                self.warn(message)

    def readjson(self, jsonpath=None):
        """
        The readjson function opens a JSON file and returns the data in it.
        It takes one argument, self.
            Args:
                self: Reference the object itself
            Returns:
                A dictionary of the json file
        """
        if not jsonpath == None:
            try:
                self.filepath = jsonpath
                with open(self.filepath) as json_file:
                    filedata = json.load(json_file)
                    json_file.close()
                return True, filedata
            except:
                self.warn("Unable to open JSON File!")
                return False, "unable to open json file"

    def warn(self, warning):
        """
        The warningmessage function is a function that displays warning messages to the user.
        It takes in one argument, which is the warning message that will be displayed to the user.
        The function returns nothing.
            Args:
                self: Access the attributes and methods of the class in python
                warning: Display the warning message
            Returns:
                The warning message
        """
        messagebox.showwarning(
            title="Notice",
            message=warning,
        )


class sentencetracker:
    def __init__(self):
        # super().__init()
        self.trackerData = None
        self.boxmaker = sentencebox()

    def createboxes(self, phrase):
        pass

    def updateboxes(self):
        pass


class sentencebox:
    def __init__(self, parent=None, widgetname=None, widgetID=None):
        super().__init__()
        self.parent = parent
        self.name = widgetname
        self.ID = widgetID

    def create_box(self, parent):
        self.name = tk.Button(self.parent, text="test")
        return self.name

    def update_box(self):
        pass

    def delete_box(self):
        pass

    def config_box(self):
        pass

    def gather_boxes(self):
        pass


class confighandler:
    def __init__(self, operation=None, configfile=None, setting=None):

        self.configfile = configfile
        if not configfile == None:
            self.configfile = os.path.join(os.getcwd(), configfile)
        if not operation == "None":
            print("operation value is not 'None', value is " + str(operation))
            if not self.configfile == None:
                print('Configfile parameter has value other then "none", value is ' + str(self.configfile))
                self.operation = operation.lower()
                self.operationvalid = False
                self.checkoperation()
                self.setting = setting
                self.settingsdic = {}
                if not configfile == None:
                    self.configfile = os.path.join(os.getcwd(), configfile)

    def getconfig(self):
        """
        The getconfig function reads the config file and returns a dictionary of
        the settings. If no config file exists, it creates one with default values.
            Args:
                self: Access variables that belongs to the class
            Returns:
                A dictionary of the default settings in the config file
        """
        config = configparser.ConfigParser()
        if os.path.exists(self.configfile):
            config.read(self.configfile)
            confdata = config.defaults()
            self.settingsdic = dict(confdata)
            return self.settingsdic
        else:
            self.warningmessage("Config File Not Found")

    def saveconfig(self):
        """
        The saveconfig function saves the current configuration settings to a config file.
        The function takes no arguments and returns nothing.
            Args:
                self: Access variables that belong to the class
            Returns:
                A dictionary of the current settings
        """
        datawrite = self.formatsettings()
        filepath = os.path.join(self.conflocation, self.configname)
        if not os.path.exists(filepath):
            filepath = filedialog.asksaveasfilename(title="Save Config File As..")
        config = configparser.ConfigParser()
        for key in datawrite:
            config["DEFAULT"][key] = datawrite[key]
        with open(filepath, "w") as configfile:
            config.write(configfile)
        configfile.close()

    def checkoperation(self):
        """
        The checkoperation function checks to see if the operation is valid.
        If it is not, a warning message pops up.
            Args:
                self: Access variables that belongs to the class
            Returns:
                True if the operation is valid and false if it is not
        """
        match self.operation.lower():
            case "load":
                self.operationvalid = True
            case "save":
                self.operationvalid = True
        if self.operationvalid == False:
            self.warningmessage("Invalid Config Operation (save or load")

    def warningmessage(self, warning):
        """
        The warningmessage function is a function that displays warning messages to the user.
        It takes in one argument, which is the warning message that will be displayed to the user.
        The function returns nothing.
            Args:
                self: Access the attributes and methods of the class in python
                warning: Display the warning message
            Returns:
                The warning message
        """
        messagebox.showwarning(
            title="Warning",
            message=warning,
        )
