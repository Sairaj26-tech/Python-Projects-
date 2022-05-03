# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:53:22 2022

@author: SAIRAJ
"""
from tkinter import *
def convert_to_celsius():    
    fahrenheit = float(input_box.get())
    celsius = (fahrenheit - 32) * 5/9
    output_box.config(text=round(celsius, 2))
    
  
window = Tk()
window.title("C to F Converter")
window.geometry("1000x600")
window.config(bg="light green")

a = Label(window,text="Enter Fahrenheit",font=("Comic Sans MS",20))
a.place(x=150,y=100)

input_box = Entry(window,font=("Comic Sans MS",20))
input_box.place(x=400,y=100)

def convert_to_celsius():
    
    fahrenheit = float(input_box.get())
    celsius = (fahrenheit - 32) * 5/9
    output_box.config(text=round(celsius, 2))
    
  
window = Tk()
window.title("C to F Converter")
window.geometry("1000x600")
window.config(bg="light blue")

a = Label(window,text="Enter Fahrenheit",font=("Comic Sans MS",20))
a.place(x=150,y=100)



b=Label(window,text="Celsius is:",font=("Comic Sans MS",20))
b.place(x=150,y=300)

output_box = Label(window,text="",font=("Comic Sans MS",20),width=20)
output_box.place(x=400,y=300)

button =Button(window,text='Convert', command=convert_to_celsius,font=("Arial Bold",12))
button.place(x=450,y=200)

def NEXT():
    window.destroy()
    
    root = Tk()
    root.title("F to C Converter")
    root.geometry("1000x600")
    root.config(bg="light green")
    
    a = Label(root,text="Enter Celsius",font=("Comic Sans MS",20))
    a.place(x=150,y=100)
    
    input_box = Entry(root,font=("Comic Sans MS",20))
    input_box.place(x=400,y=100)
    
    b=Label(root,text="Fahrehneit is:",font=("Comic Sans MS",20))
    b.place(x=150,y=300)
    
    output_box = Label(root,text="",font=("Comic Sans MS",20),width=20)
    output_box.place(x=400,y=300)
    
    
    def convert_to_fahrehneit():
        
        celsius = float(input_box.get())
        fahrenheit = (celsius * 9/5) + 32
        output_box.config(text=round(fahrenheit, 2))
        
        
    button =Button(root,text='Convert', command=convert_to_fahrehneit,font=("Arial Bold",12))
    button.place(x=450,y=200)
    
    def NEXT():
        root.destroy()
    
    button =Button(text='Next', command=NEXT,font=("Arial Bold",12))
    button.place(x=500,y=450)
    
    root.mainloop()

button =Button(text='Next', command=NEXT,font=("Arial Bold",12))
button.place(x=500,y=450)



window.mainloop()