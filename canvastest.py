import tkinter as tk
from tkinter import Canvas
from tkinter import StringVar
from functools import partial
from tkinter import ttk
from tkinter import colorchooser


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


class CanvasEvents(tk.Tk):
    def __init__(self):
        super().__init__()

        testdic = {}
        testdic[1] = "Affect: calm and rational"
        testdic[2] = "Affect: agressive"
        testdic[3] = "Affect: tense"
        testdic[4] = "Affect: upset/near tears"
        testdic[5] = "Affect: angry"

        newbox = sentencebox(self, "newname", 1)
        self.tracker = sentencetracker()

        sentboxsizes = {}

        print(testdic)
        startx = 50
        starty = 50
        incx = 100
        incy = 100

        self.title("Event")
        self.count = 0
        self.geometry("1000x1000")
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.canvas = Canvas(self)
        self.canvas.pack(expand=1, fill=tk.BOTH)
        self.canvas.bind_all("<Button-1>", self.object_click_event)
        self.label = StringVar(self, "testtext")
        self.sessiondic = {}
        testwidget = newbox.create_box(self.canvas)
        testbtn = self.canvas.create_window(50, 50, window=testwidget, anchor="w")

        for key in testdic:
            passedtags = key
            exec(
                "self.sentbtn{} = self.sentenceWidget(self.canvas, startx, starty, testdic[key], key)".format(
                    passedtags
                )
            )
            self.canvas.tag_bind(key, "<Button-4>", self.objectscroll)
            self.canvas.tag_bind(key, "<Button-5>", self.objectscroll)
            incx = incx + 30
            starty = starty + 40
            incy = incy + 40

        self.canvas.pack()
        print(vars())
        print(self.canvas.winfo_children())

    def testwidget(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", activefill="blue")
        self.canvas.create_text(x1, y1, text="Some test words")

    def sentenceWidget(self, parent, xpos, ypos, senttext, itemtags):
        print(itemtags)
        exec("checkvar{item} = 0".format(item=itemtags))
        exec("global editsent{}".format(itemtags))
        exec("editsent{} = 0".format(itemtags))
        sItem = tk.Frame(parent, relief="raised", bg="#74b4c3", padx=5, pady=3)
        sItem.lift
        print(sItem.winfo_height())
        handle = tk.Button(
            sItem,
            text="⌘",
            font=("Helvetica bold", 13),
            padx=1,
            pady=1,
            bg="#74b4c3",
        )
        handle.lower
        handle.bind("<Button-1>", self.dragstart)
        handle.bind("<ButtonRelease-1>", self.drag_stop)
        handle.bind("<B1-Motion>", self.drag)
        handle.grid(row=0, column=0)
        sentencetext = tk.Label(sItem, text=senttext, padx=3, pady=3, bg="#74b4c3")
        sentencetext.grid(row=0, column=1)
        sentencetext.lower
        exec(
            "editcheck{} = tk.Checkbutton(sItem, text='Edit', padx=2, pady=2, bg = '#74b4c3', variable='editsent{}')".format(
                itemtags, itemtags
            )
        )
        exec("editcheck{}.grid(row=0, column=2)".format(itemtags))
        widgetID = parent.create_window(xpos, ypos, window=sItem, anchor="w", tags=itemtags)
        parent.lift
        return widgetID

    def objectscroll(self, event, **args):
        global count
        if event.num == 5 or event.delta == -120:
            self.count -= 1
        if event.num == 4 or event.delta == 120:
            self.count += 1
        self.label.set(self.count)
        print(self.label.get())

    def object_click_event(self, event):
        widget = event.widget
        if isinstance(widget, tk.Label):
            widget.configure(text=widget.cget("text") + "---clicked")
        if isinstance(widget, tk.Button):
            pass
        if isinstance(widget, tk.Checkbutton):
            pass
            # print("mark entry for editing")

    def dragstart(self, event):
        widget = event.widget
        print(widget)
        if isinstance(widget, tk.Button):
            self._drag_data["x"] = event.x
            self._drag_data["y"] = event.y

    def drag_stop(self, event):
        widget = event.widget
        if isinstance(widget, tk.Button):
            self._drag_data["item"] = None
            self._drag_data["x"] = 0
            self._drag_data["y"] = 0

    def drag(self, event):
        widget = event.widget
        if isinstance(widget, tk.Button):
            key = str(widget.master)
            key = key[-1]
            if not key.isnumeric():
                key = "1"
            step = 40
            """Handle dragging of an object"""
            # compute how much the mouse has moved
            delta_x = event.x - self._drag_data["x"]
            delta_y = event.y - self._drag_data["y"]
            # print(delta_x)
            # print(delta_y)
            delta_x = int(step * round(float(delta_x) / step))
            delta_y = int(step * round(float(delta_y) / step))
            exec("self.canvas.move({}, delta_x, delta_y)".format(key))


class CustomWidget(tk.Frame):
    def __init__(self, parent, label, default=""):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text=label, anchor="w")
        self.entry = tk.Entry(self)
        self.entry.insert(0, default)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="bottom", fill="x", padx=4)

    def get(self):
        return self.entry.get()


if __name__ == "__main__":
    piechart = CanvasEvents()
    piechart.mainloop()
