# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:57:31 2020

@author: vinay
"""

import pyttsx3
from PIL import Image, ImageDraw
import PIL
from tkinter import *
import random
from PIL import ImageTk, Image
import tkinter.messagebox

top = tkinter.Tk()
voice = pyttsx3.init()
top.geometry('400x400')


def texttospeech(a):
    voice.say(a)
    voice.runAndWait()


def attach():
    texttospeech('your are running main window')
    b = Button(top, text='draw', command=draw, width=12, height=2)
    b.place(x=100, y=100)
    b1 = Button(top, text='path', command=path, width=12, height=2)
    b1.place(x=100, y=200)
    b2 = Button(top, text='camera', command=camera, width=12, height=2)
    b2.place(x=100, y=300)


def draw():
    top.withdraw()
    texttospeech('you are running drawing window')

    def des():
        top.update()
        top.deiconify()
        root.destroy()

    white = (255, 255, 255)

    def save():
        filename = "image.png"
        image1.save('c:\\Users\\vinay\\OneDrive\\Pictures\\Screenshots\\' + str(random.randint(1, 100000)) + filename)
        image1.paste(image)

    def paint(event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        cv.create_oval(x1, y1, x2, y2, fill="black", width=5)
        draw1.line([x1, y1, x2, y2], fill="black", width=5)

    root = Tk()
    root.geometry('300x300')
    cv = Canvas(root, width=150, height=150, bg='white')
    image = PIL.Image.new("RGB", (150, 150), white)
    image1 = PIL.Image.new("RGB", (150, 150), white)
    draw1 = ImageDraw.Draw(image1)

    cv.pack(expand=YES, fill=BOTH)
    cv.bind("<B1-Motion>", paint)

    def clear():
        cv.delete('all')

    button1 = Button(root,text='clear', command=clear)
    button2 = Button(root,text="back", command=des)
    button3 = Button(root,text="save", command=save)
    button3.pack(side=RIGHT)
    button1.pack(side=RIGHT)
    button2.pack(side=BOTTOM)
    root.mainloop()


def path():
    top.withdraw()
    texttospeech('you are running image path window')

    def des():
        top.update()
        top.deiconify()
        top2.destroy()

    def clear():
        e1.delete(0, END)
        if sbmitbtn['state'] == DISABLED:
            sbmitbtn['state'] = NORMAL
            sbmitbtn1['state'] = DISABLED

    def get1():
        try:
            # Open the image
            my = Image.open(e1.get().replace('"', ''))
            ii = my.resize((220, 220))

            # Convert the image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(ii)

            # Keep a reference to the PhotoImage object to prevent garbage collection
            get1.photo=photo

            # Create a Tkinter label to display the image
            my_label = Label(top2, image=photo, width=220, height=220)
            my_label.place(x=160, y=60)
            sbmitbtn["state"] = DISABLED
            if sbmitbtn1['state'] == DISABLED:
                sbmitbtn1['state'] = NORMAL
        except Exception as e:
            print(f"Error loading image: {e}")

    top2 = Tk()
    top2.geometry("400x300")
    Label(top2, text="EHTER THE PATH:").place(x=0, y=25)
    Label(top2, text="IMAGE-->").place(x=105, y=60)
    e1 = Entry(top2, width=22)
    e1.place(x=100, y=25)
    sbmitbtn = Button(top2, text="Submit", activebackground="pink", bg='yellow', activeforeground="blue", command=get1,
                      width=12,
                      height=8)
    sbmitbtn.configure(state=NORMAL)
    sbmitbtn.place(x=30, y=110)
    sbmitbtn1 = Button(top2, text="clear path", activebackground="pink", bg='yellow', activeforeground="blue",
                       command=clear)
    sbmitbtn1.configure(state=NORMAL)
    sbmitbtn1.place(x=260, y=25)
    butt0n = Button(top2, text="<=BACK", activebackground="pink", bg='yellow', activeforeground="blue",
                    command=des)
    butt0n.place(x=0, y=0)
    top2.mainloop()


def camera():
    top3 = Tk()
    top3.geometry('400x400')
    top.withdraw()
    texttospeech('you are running camera window')

    def des():
        top.update()
        top.deiconify()
        top3.destroy()

    button = Button(top3, text='draw1')
    button.place(x=100, y=100)
    button1 = Button(top3, text='back', command=des)
    button1.place(x=100, y=200)


attach()

top.mainloop()
