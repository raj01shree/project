from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk


root =Tk()



img=Image.open(r"C:\Users\rajsh\Desktop\semester pro\abt.png")
img1=img.resize((1600,1000),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(img1)
lbl=Label(root,image=photoimg)
lbl.place(x=0,y=0)

def back():
   root.destroy()
   import tseting.py

mybutton1 = Button(root, text="HOME",padx = 20, pady = 30, fg="white", bg="black",command=back)
mybutton1.place(x=700,y=700)

tk.mainloop()
