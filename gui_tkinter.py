import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import php_lexico
import php_yacc
import os
import subprocess


root = tk.Tk()
root.geometry("1000x640")
textOut=tk.Text(root, height=10)
def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    f = open("tmp", "w+")
    f.write(result)
    f.close()
    #tokens=php_lexico.tokens
    #lex=php_lexico.get_lexer()
    #parser=php_yacc.get_yacc()
    textOut.delete(1.0, "end")
    #print(chr(27) + "[0;36m" + "INICIA ANALISIS SINTACTICO" + chr(27) + "[0m")
    #print(parser.parse(result))
    #print(chr(27) + "[0;36m" + "TERMINA ANALISIS SINTACTICO" + chr(27) + "[0m")
    proc = subprocess.Popen(["python", "php_yacc.py","tmp"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    textOut.insert(1.0, out)



textExample=tk.Text(root, height=25)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read",
                    command=getTextInput)

def openfile():
    return filedialog.askopenfilename()

buttonFile = tk.Button(root, text="Open", command=openfile)  # <------

buttonFile.pack()
btnRead.pack()

textOut.pack()
root.mainloop()