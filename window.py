#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

"""GUI module generated by PAGE version 4.14.
# In conjunction with Tcl version 8.6
#    Jun 04, 2018 08:42:31 PM
"""

import base64
import sys

from GaQueens import GaQueens

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

# spinbox = StringVar(root, '4')
# spinbox2 = StringVar(root, '10')
# spinbox3 = StringVar(root, '-1')

with open("7735732.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

root = Tk()

player1 = PhotoImage(data=encoded_string)
player1 = player1.subsample(3)


def vp_start_gui():
    """Start point when module is the main routine."""
    global val, w, root, spinbox, spinbox2, spinbox3
    # root = Tk()
    spinbox = StringVar(root, '6')
    spinbox2 = StringVar(root, '10')
    spinbox3 = StringVar(root, '-1')
    top = Algoritmo_gen_tico_con_N_reinas(root)
    init(root, top)
    root.mainloop()


w = None


def create_Algoritmo_gen_tico_con_N_reinas(root, *args, **kwargs):
    """Start point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Algoritmo_gen_tico_con_N_reinas(w)
    init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Algoritmo_gen_tico_con_N_reinas():
    global w
    w.destroy()
    w = None


class Algoritmo_gen_tico_con_N_reinas:
    def __init__(self, top=None):
        """Class that configures and populates the toplevel window.

        Top is the toplevel containing window.
        """
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("901x585+163+100")
        top.title("Algoritmo genético con N reinas")
        img = Image("photo", file="qeen.png")
        top.call('wm', 'iconphoto', top._w, img)
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.02, rely=0.09, height=21, width=142)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor=W)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text="""Tamaño de población:""")

        self.Label2 = Label(top)
        self.Label2.place(relx=0.02, rely=0.14, height=21, width=184)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor=W)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text="""Generaciones (-1 para infinito):""")

        self.Label3 = Label(top)
        self.Label3.place(relx=0.02, rely=0.03, height=21, width=174)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor=W)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text="""Tamaño de tablero:""")

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(top)
        self.Scrolledtreeview1.place(
            relx=0.02, rely=0.27, relheight=0.68, relwidth=0.41)
        self.Scrolledtreeview1.configure(columns="Col1")
        self.Scrolledtreeview1.heading("#0", text="Solucion")
        self.Scrolledtreeview1.heading("#0", anchor="center")
        # self.Scrolledtreeview1.heading("#0", command=lambda:)
        self.Scrolledtreeview1.column("#0", width="175")
        self.Scrolledtreeview1.column("#0", minwidth="20")
        self.Scrolledtreeview1.column("#0", stretch="1")
        self.Scrolledtreeview1.column("#0", anchor="w")
        self.Scrolledtreeview1.heading("Col1", text="Aptitud")
        self.Scrolledtreeview1.heading("Col1", anchor="center")
        self.Scrolledtreeview1.column("Col1", width="46")
        self.Scrolledtreeview1.column("Col1", minwidth="20")
        self.Scrolledtreeview1.column("Col1", stretch="1")
        self.Scrolledtreeview1.column("Col1", anchor="w")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.17, rely=0.19, height=35, width=106)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Comenzar''')
        self.TButton1.configure(width=106)
        self.TButton1.configure(command=lambda: self.start())

        self.Spinbox1 = Spinbox(top, from_=4.0, to=100.0, textvariable=spinbox)
        self.Spinbox1.place(relx=0.28, rely=0.03,
                            relheight=0.03, relwidth=0.13)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(from_="4.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=spinbox)
        self.Spinbox1.configure(to="100.0")

        self.Spinbox2 = Spinbox(
            top, from_=10.0, to=100.0, textvariable=spinbox2)
        self.Spinbox2.place(relx=0.28, rely=0.09,
                            relheight=0.03, relwidth=0.13)
        self.Spinbox2.configure(activebackground="#f9f9f9")
        self.Spinbox2.configure(background="white")
        self.Spinbox2.configure(buttonbackground="#d9d9d9")
        self.Spinbox2.configure(disabledforeground="#a3a3a3")
        self.Spinbox2.configure(foreground="black")
        self.Spinbox2.configure(from_="10.0")
        self.Spinbox2.configure(highlightbackground="black")
        self.Spinbox2.configure(highlightcolor="black")
        self.Spinbox2.configure(insertbackground="black")
        self.Spinbox2.configure(selectbackground="#c4c4c4")
        self.Spinbox2.configure(selectforeground="black")
        self.Spinbox2.configure(textvariable=spinbox2)
        self.Spinbox2.configure(to="100.0")

        self.Spinbox3 = Spinbox(
            top, from_=-1.0, to=10000.0, textvariable=spinbox3)
        self.Spinbox3.place(relx=0.28, rely=0.14,
                            relheight=0.03, relwidth=0.13)
        self.Spinbox3.configure(activebackground="#f9f9f9")
        self.Spinbox3.configure(background="white")
        self.Spinbox3.configure(buttonbackground="#d9d9d9")
        self.Spinbox3.configure(disabledforeground="#a3a3a3")
        self.Spinbox3.configure(foreground="black")
        self.Spinbox3.configure(from_="-1.0")
        self.Spinbox3.configure(highlightbackground="black")
        self.Spinbox3.configure(highlightcolor="black")
        self.Spinbox3.configure(insertbackground="black")
        self.Spinbox3.configure(selectbackground="#c4c4c4")
        self.Spinbox3.configure(selectforeground="black")
        self.Spinbox3.configure(textvariable=spinbox3)
        self.Spinbox3.configure(to="100.0")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.44, rely=0.03, height=19, width=46)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font11)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text="""Tablero""")

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.44, rely=0.1, relheight=0.84, relwidth=0.54)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="0")
        self.Canvas1.configure(highlightthickness="0")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=int(spinbox.get()) * 20)
        self.Canvas1.bind("<Configure>", self.refresh)
        # self.Canvas1.bind("<Button-1>", self.refresh)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.53, rely=0.03, height=31, width=394)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(width=394)
        self.pieces = {}
        self.size = 20

    def refresh(self, event):
        """Redraw the board, possibly in response to window being resized."""
        color1 = "#b1cbdd"
        color2 = "#b8e0d2"
        xsize = int((event.width - 1) / int(spinbox.get()))
        ysize = int((event.height - 1) / int(spinbox.get()))
        self.size = min(xsize, ysize)
        self.Canvas1.delete("square")
        color = color1
        for row in range(int(spinbox.get())):
            color = color2 if color == color1 else color1
            for col in range(int(spinbox.get())):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.Canvas1.create_rectangle(
                    x1, y1, x2, y2, outline=color2, fill=color, tags="square")
                color = color2 if color == color1 else color1
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.Canvas1.tag_raise("piece")
        self.Canvas1.tag_lower("square")

    def refresh2(self):
        """Redraw the board qhen pres the button."""
        color1 = "#b1cbdd"
        color2 = "#b8e0d2"
        width, height = self.Canvas1.winfo_width(), self.Canvas1.winfo_height()
        xsize = int((width - 1) / int(spinbox.get()))
        ysize = int((height - 1) / int(spinbox.get()))
        self.size = min(xsize, ysize)
        self.Canvas1.delete("square")
        color = color1
        for row in range(int(spinbox.get())):
            color = color2 if color == color1 else color1
            for col in range(int(spinbox.get())):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.Canvas1.create_rectangle(
                    x1, y1, x2, y2, outline=color2, fill=color, tags="square")
                color = color2 if color == color1 else color1
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.Canvas1.tag_raise("piece")
        self.Canvas1.tag_lower("square")

    def addpiece(self, name, image, row=0, column=0):
        """Add a piece to the playing board."""
        self.Canvas1.create_image(
            0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        """Place a piece at the given row/column."""
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size / 2)
        y0 = (row * self.size) + int(self.size / 2)
        self.Canvas1.coords(name, x0, y0)

    def clear_tree(self):
        x = self.Scrolledtreeview1.get_children()
        if x != '()':
            for child in x:
                self.Scrolledtreeview1.delete(child)

    def get_queens(self, algoritmo):
        list = algoritmo.solution.list_coords()
        i = 0
        for tupla in list:
            id = "player{}".format(i)
            self.addpiece(id, player1, tupla[0], tupla[1])
            i += 1

    def set_tree(self, algoritmo):
        for g in range(algoritmo.generation_count + 1):
            population = algoritmo.generations[g]
            gen_str = "Generación {}".format(g)
            id_str = "gen{}".format(g)
            id = self.Scrolledtreeview1.insert("", g, id_str, text=gen_str)
            for item in population:
                self.Scrolledtreeview1.insert(id, "end",
                                              text=str(item.queens),
                                              values=(item.fitness))

    def start(self):
        sl = GaQueens(int(spinbox.get()), int(spinbox2.get()),
                      int(spinbox3.get()))
        self.Label4.configure(text=sl.status)
        self.get_queens(sl)
        self.clear_tree()
        self.set_tree(sl)
        self.refresh2()


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    """A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed."""
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
