from tkinter import *
from tkinter import messagebox

def submit2():
    messagebox.showinfo('message','successfully withdrawed')
   
def withdraw():
    root=Tk()
    root.title("details")
    root.geometry("1400x700")
    root.config(bg="grey")
    t=Label(root,text="enter the balance",bg="grey",font=("Arial.Bold",30))
    t.place(x=50,y=150)
    u=Entry(root,bg="grey",font=("Arial.Bold",30),fg="black")
    u.place(x=450,y=150)
    engine = pyttsx3.init()
    text="enter the balance"
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
    v=Label(root,text="enter the amount to be withdrawn",bg="grey",font=("Arial.Bold",30))
    v.place(x=50,y=350)
    y=Entry(root,bg="grey",font=("Arial.Bold",30),fg="black")
    y.place(x=550,y=350)
    engine = pyttsx3.init()
    text="enter the amount to be withdrawed"
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
    l=Button(root,command=submit2,text="submit2",font=("Arial.Bold",30))
    l.place(x=50,y=450)
    t=u.get()
    print(t)
    v=y.get()
    print(v)
    amount=t-v
    print(amount)
    
    
    
def submit1():
      messagebox.showinfo('message','successfully deposited')


def deposit():
    root=Tk()
    root.title("details")
    root.geometry("1400x700")
    root.config(bg="grey")
    engine = pyttsx3.init()
    text="enter the balance"
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
    r=Label(root,text="enter the balance",bg="grey",font=("Arial.Bold",30))
    r.place(x=50,y=150)
    s=Entry(root,bg="grey",font=("Arial.Bold",30),fg="black")
    s.place(x=450,y=150)
    engine = pyttsx3.init()
    text="enter the amount to be deposited"
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
    p=Label(root,text="enter the amount to be depo",bg="grey",font=("Arial.Bold",30))
    p.place(x=50,y=350)
    q=Entry(root,bg="grey",font=("Arial.Bold",30),fg="black")
    q.place(x=550,y=350)
    l=Button(root,command=submit1,text="submit1",font=("Arial.Bold",30))
    l.place(x=50,y=450)
    r=s.get()
    print(r)
    p=q.get()
    print(p)
    amount=r+p
    print(amount)
    root.mainloop()
   

    
   

    
    
    
def submit():
    root=Tk()
    root.title("details")
    root.geometry("1400x700")
    root.config(bg="grey")
    engine = pyttsx3.init()
    text="enter the option"
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
    j=Label(root,text="enter the option",bg="grey",font=("Arial.Bold",30))
    j.place(x=50,y=150)
    k=Button(root,command=deposit,text="deposit",font=("Arial.Bold",30))
    k.place(x=50,y=200)
    l=Button(root,command=withdraw,text="withdraw",font=("Arial.Bold",30))
    l.place(x=50,y=300)
    root.mainloop()
     
     
     
def English():
    root=Tk()
    root.title("details")
    root.geometry("1400x700")
    root.config(bg="grey")
    engine = pyttsx3.init()
    text="enter the Name and pincode"
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
    e=Label(root,text="Name",bg="grey",font=("Arial.Bold",30))
    e.place(x=50,y=100)
    f=Entry(root,bg="grey",font=("Arial.Bold",30),fg="black")
    f.place(x=200,y=100)
    g=Label(root,text="pincode",bg="grey",font=("Arial.Bold",30))
    g.place(x=50,y=300)
    h=Entry(root,bg="grey",font=("Arial.Bold",30),fg="black")
    h.place(x=200,y=300)
    i=Button(root,command=submit,text="submit",font=("Arial.Bold",30))
    i.place(x=50,y=400)
    root.mainloop()
   
    
    
   
    
from tkinter import *
from tkinter import messagebox
import pyttsx3
window=Tk()
window.title("ATM")
window.geometry("1400x700")
window.config(bg="grey")
x=Label(window,text="Bank Name",bg="grey",font=("Arial.Bold",35))
x.place(x=650,y=25)
engine = pyttsx3.init()
text="enter the language"
engine.setProperty('rate',120)
engine.setProperty('volume',0.9)
engine.say(text)
engine.runAndWait()
a=Label(window,text="Enter the Language",bg="grey",font=("Arial.Bold",30))
a.place(x=50,y=100)
b=Button(window,text="Kannada",font=("Arial.Bold",30))
b.place(x=50,y=200)
c=Button(window,command=English,text="English",font=("Arial.Bold",30))
c.place(x=50,y=300)
d=Button(window,text="Hindi",font=("Arial.Bold",30))
d.place(x=50,y=400)
window.mainloop()



