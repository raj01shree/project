from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
root = Tk()
# root.geometry()
# root.geometry("1530*790")
img=Image.open(r"C:\Users\rajsh\Desktop\semester pro\44.png")
img1=img.resize((1600,1000),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(img1)
lbl=Label(root,image=photoimg)
lbl.place(x=0,y=0)
   
mylabel = Label(root, text="INSECT RECOGNITION SYSTEM",font=("arial",40),fg="#00ffff",bg="green").pack()


def lmn():
   root.destroy()
   import ImageClassifier.py

def lmn1():
   root.destroy()
   import instruction.py

def lmn2():
   root.destroy()
   import about.py

mybutton1 = Button(root, text="HOME",padx = 30, pady = 40, fg="white", bg="black")
mybutton1.place(x=200,y=100)
mybutton2 = Button(root, text="SCAN",padx = 30, pady = 40, fg="white", bg="black", command=lmn)
mybutton2.place(x=200,y=250)
mybutton3 = Button(root, text="INSTRUCTION",padx = 30, pady = 40, fg="white", bg="black",command=lmn1)
mybutton3.place(x=200,y=400)
mybutton4 = Button(root, text="ABOUT US",padx = 30, pady = 40, fg="white", bg="black",command=lmn2)
mybutton4.place(x=200,y=550)
# mybutton4.grid(row=1,column=4)
button_quit = Button(root, text="exit program", command=root.quit)  
button_quit.place(x=200,y=700)

root.mainloop()