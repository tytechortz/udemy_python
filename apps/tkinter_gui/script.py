from tkinter import *

window=Tk()

def km_to_miles():
    print("success")

b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

e1=Entry(window)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()
