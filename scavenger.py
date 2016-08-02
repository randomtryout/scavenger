#!/usr/bin/python

from Tkinter import *
import tkMessageBox

def GetValue():
    enter = ent.get()
    if enter == 'Yes':
        button['bg'] = 'yellow'
        ent.delete(0, 'end')
        tkMessageBox.showinfo("Greaat Student!", "The world is better now!")
    else:
        ent.delete(0, 'end')
        tkMessageBox.showinfo("Mmm", "I thInk I don't like you!")

root = Tk()

lab = Label(root, text = 'Is this workshop interesting? Write Yes or No')
ent = Entry(root, bg = 'white')
button = Button(root, text = 'Enter Reply', command = GetValue)

ent.focus()

lab.pack(anchor = W)
ent.pack(anchor = W)
button.pack(ancho = E)

root.mainloop()
