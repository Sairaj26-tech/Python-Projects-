# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:15:24 2022

@author: SAIRAJ
"""
from tkinter import *
from tkinter import ttk,font
root=Tk()
root.config(bg="white")
root.geometry("800x400")
result_binary=StringVar()
result_octal=StringVar()
result_hexadecimal=StringVar()
def Convert():
    
     x1=int(Entry.get(x))
     binary=(bin(x1))
     result_binary.set(binary)
     octal=(oct(x1))
     result_octal.set(octal)
     hexadecimal=(hex(x1))
     result_hexadecimal.set(hexadecimal)
     
x1Lab= Label(root,text="Enter the Integer value for conversions",bg="orange",fg="white",font=("Calibri","20"))
binaryLab=Label(root,text="Binary",bg="blue",fg="black",font=("Calibri","18"))
binaryAns=Label(root,textvariable=result_binary,bg="yellow",fg="black",font=("Calibri","18"))
octalLab=Label(root,text="Octal",bg="pink",fg="black",font=("Calibri","18"))
octalAns=Label(root,textvariable=result_octal,bg="blue",fg="black",font=("Calibri","18"))
hexadecimalLab=Label(root,text="Hexadecimal",bg="yellow",font=("Calibri","18"))
hexadecimalAns=Label(root,textvariable=result_hexadecimal,bg="pink",fg="black",font=("Calibri","18"))
convert=Button(root,text="Convert",command=Convert)
x=Entry(root)
x1Lab.grid(row=160,column=0)
binaryLab.grid(row=3,column=0)
octalLab.grid(row=4,column=0)
hexadecimalLab.grid(row=5,column=0)
x.grid(row=1,column=2)
binaryAns.grid(row=3,column=2)
octalAns.grid(row=4,column=2)
hexadecimalAns.grid(row=5,column=2)
convert.grid(row=7)
root.wm_title("Type Conversions")
root.mainloop()