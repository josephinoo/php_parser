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
textOut=tk.Text(root, height=10, state='disabled')
def getTextInput():
    
    result=textInput.get(1.0, tk.END+"-1c")
    f = open("tmp2", "w+")
    f.truncate(0)
    f.write(result)
    f.close()

    textOut.configure(state='normal')
    textOut.delete(1.0, "end")

    out=phpy.executeFunction("tmp2")
    f2 = open("tmp", "r+")
    f2.truncate(0)
    f2.close()
    if(out==""):
        out="NO HAY ERRORES"
    textOut.insert(1.0, out)
    textOut.configure(state='disabled')



textInput=tk.Text(root, height=25)
textInput.pack()
btnRead=tk.Button(root, height=1, width=10, text="Analizar",
                    command=getTextInput)

def openfile():

    textInput.delete(1.0, "end")
    f= open(filedialog.askopenfilename(),"r+")
    input = f.read()

    textInput.insert(1.0, input)


buttonFile = tk.Button(root, text="Abrir archivo", command=openfile)


btnRead.pack()
buttonFile.pack()


textOut.pack()
root.mainloop()