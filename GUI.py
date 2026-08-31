from tkinter import *
from tkinter import ttk
import random as random
import write
import read
def convert():
    write.write(path)
def startgui(x, y):
    root = Tk()
    root.geometry("720x405")
    frm = Frame(root)
    frm.grid()
    ttk.Label(frm, text="Text Visualizer").grid(column=2, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
