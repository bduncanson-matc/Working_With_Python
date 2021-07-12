#! /usr/bin/env python3
from tkinter import *
from tkinter import messagebox

boolFile = open("boolString")
boolList = boolFile.readlines()
ansFile = open("BoolAnswerOutput")
ansList = ansFile.readlines()

win = Tk()
def boolCallBack(varNum):
    strExp = boolList[varNum]
    strAns = ansList[varNum]
    return messagebox.showinfo(strExp, strAns)

lb = Listbox(win,height=30, width=75)
for i in range(1,19):
    boolList[i] = boolList[i].strip("\n")
    str =f" {i}) {boolList[i]}"
    lb.insert(i, str)
lb.pack()
win.mainloop()
varNum = int(input("Enter the number of expression you want evaluated: "))
popup = Tk()
popup.title("Expression returns :")
Button(popup, text=boolList[varNum], command=boolCallBack(varNum)).pack(pady=20)
popup.mainloop()