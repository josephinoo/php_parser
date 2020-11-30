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
    
    result=textExample.get(1.0, tk.END+"-1c")
    f = open("tmp2", "w+")
    f.truncate(0)
    f.write(result)
    f.close()
    
    textOut.delete(1.0, "end")

    out=phpy.executeFunction("tmp2")
    f2 = open("tmp", "r+")
    f2.truncate(0)
    f2.close()
    if(out==""):
        out="NO HAY ERRORES"
    textOut.insert(1.0, out)



textExample=tk.Text(root, height=25)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read",
                    command=getTextInput)

def openfile():
    textOut.delete(1.0, "end")

    out = phpy.executeFunction(filedialog.askopenfilename())
    print(out)
    if (out == ""):
        out = "NO HAY ERRORES"
    textOut.insert(1.0, out)
    file=open("tmp","r+")
    file.truncate(0)
    file.close()


buttonFile = tk.Button(root, text="Open", command=openfile)

buttonFile.pack()
btnRead.pack()

textOut.pack()
root.mainloop()