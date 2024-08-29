from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='RoyalBlue2')
root.geometry('400x600')
root.resizable(False,False)
choice=IntVar()
Font=('arial',20,'bold')
password_lable= Label(root, text="Password Generator", font=("Helvetica", 40, "normal"), anchor="ne",
    width="3").pack(anchor="center", fill="both", pady=8)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.pack(pady=8)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.pack(pady=8)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.pack(pady=8)

length_lable= Label(root, text="Password Length", font=("Helvetica", 30, "normal"),width="3").pack( fill="both", pady=8)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.pack(pady=8)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.pack(pady=8)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.pack()

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.pack(pady=5)

root.mainloop()