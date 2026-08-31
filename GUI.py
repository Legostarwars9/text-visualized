import tkinter as tk

def startgui():
    window = tk.Tk()
    window.title("txt2img")
    window.geometry("500x250")
    label = tk.Label(window, text="Hello World")
    label.pack()
    window.mainloop()