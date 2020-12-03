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
textOut=tk.Text(root, height=12, state='disabled')
def errores():
    
    result=textInput.get(1.0, tk.END+"-1c")
    f = open("tmp2", "w+")
    f.truncate(0)
    f.write(result)
    f.close()

    textOut.configure(state='normal')
    textOut.delete(1.0, "end")

    proc = subprocess.Popen(["python", "php_yacc.py", "tmp2"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    f2 = open("tmp", "r+")
    out=f2.read()
    f2.truncate(0)
    f2.close()
    if(out==""):
        out="NO HAY ERRORES"
    textOut.insert(1.0, out)
    textOut.configure(state='disabled')


def getLexico():
    result = textInput.get(1.0, tk.END + "-1c")
    f = open("tmp2", "w+")
    f.truncate(0)
    f.write(result)
    f.close()

    textOut.configure(state='normal')
    textOut.delete(1.0, "end")

    php_lexico.executeFunction("tmp2")

    f2 = open("tmp", "r+")
    print(f2)
    out = f2.read()
    f2.truncate(0)
    f2.close()
    textOut.insert(1.0, out)
    textOut.configure(state='disabled')

def reglasDetectadas():
    f2 = open("parser.out", "r")
    f2.write("")
    f2.close()
    textOut.configure(state='normal')
    textOut.delete(1.0, "end")
    result = textInput.get(1.0, tk.END + "-1c")
    f = open("tmp2", "w+")
    f.truncate(0)
    f.write(result)
    f.close()
    phpy.executeFunction("tmp2")
    f2 = open("parser.out", "r")
    textOut.insert(1.0, f2.read())
    textOut.configure(state='disabled')
    f2.close()

textInput=tk.Text(root, height=25)
textInput.pack()
btnRead=tk.Button(root, height=1, width=12, text="Reglas detectadas",
                    command=reglasDetectadas)

btnLexico=tk.Button(root, height=1, width=12, text="Mostrar tokens",
                    command=getLexico)

btnErrores=tk.Button(root, height=1, width=12, text="Buscar errores",
                    command=errores)
def openfile():

    textInput.delete(1.0, "end")
    f= open(filedialog.askopenfilename(),"r+")
    input = f.read()

    textInput.insert(1.0, input)


buttonFile = tk.Button(root, text="Abrir archivo", command=openfile)



btnErrores.pack()
btnLexico.pack()
btnRead.pack()
buttonFile.pack()


textOut.pack()
root.mainloop()