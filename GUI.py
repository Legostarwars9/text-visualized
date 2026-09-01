from tkinter import *
from tkinter import ttk
import random as random
import write
import read
def convert():
    write.write(path)

output = "hi"
def startgui():
    root = Tk()
    root.geometry("720x405")
    frm = Frame(root)
    frm.grid()
    ttk.Label(frm, text="Text Visualizer").grid(column=2, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=4)
    ttk.Checkbutton(frm, text="Use a text file").grid(column=4, row=4)
    ttk.Menubutton(frm, text="File").grid(column=5, row=4)
    ttk.Entry(frm, textvariable=output).grid(column=6, row=4)
    ttk.Radiobutton(frm).grid(column=7, row=4)
    ttk.Scrollbar(frm).grid(column=11, row=4)
    ttk.Scale(frm).grid(column=13, row=4)
    root.mainloop()
