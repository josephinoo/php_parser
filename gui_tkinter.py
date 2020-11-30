import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import php_lexico
import php_yacc  as phpy
import os
import subprocess


root = tk.Tk()
root.geometry("1000x640")
textOut=tk.Text(root, height=10)
def getTextInput():
    """
    result=textExample.get(1.0, tk.END+"-1c")
    f = open("tmp", "w+")
    f.write(result)
    f.close()"""

    textOut.delete(1.0, "end")

    out= phpy.executeFunction("test1.txt")
    print(out)
    if(out==None):
        out="NO HAY ERRORES BEBE"
    textOut.insert(1.0, out)



textExample=tk.Text(root, height=25)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read",
                    command=getTextInput)

def openfile():
    return filedialog.askopenfilename()

buttonFile = tk.Button(root, text="Open", command=openfile)

buttonFile.pack()
btnRead.pack()

textOut.pack()
root.mainloop()