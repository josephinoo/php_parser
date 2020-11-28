import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.geometry("1000x640")

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    print(result)

textExample=tk.Text(root, height=30)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read",
                    command=getTextInput)

def openfile():
    return filedialog.askopenfilename()

buttonFile = tk.Button(root, text="Open", command=openfile)  # <------

buttonFile.pack()
btnRead.pack()

root.mainloop()