#!/usr/bin/env python3

# a file explorer in Tkinter

from tkinter import *

from tkinter import filedialog, Button


def fileBrowser():
    filename = filedialog.askopenfilename(initialdir="./", title = "Select a .txt file", filetypes=(("Text files","*.txt*"),("all files", "*.*")))
    label_file_explorer.configure(text="File Opened: " + filename)


window = Tk()

window.geometry("500x500")

window.title("Pick a text file to send")

window.config(background="white")

label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "black")

button_explorer = Button(window, text='Open a file', command = fileBrowser)

button_exit = Button(window, text="Exit", command = exit)

button_explorer.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()



