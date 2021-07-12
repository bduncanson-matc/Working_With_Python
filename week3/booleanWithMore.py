#! /usr/bin/env python3
from tkinter import *


boolFile = open("./Playing/boolString")
boolList = boolFile.readlines()
boolListFormat = {}
for i in range(1,19):
    boolListFormat[i] = boolList[i].strip("\n")

ansFile = open("./Playing/BoolAnswerOutput")
ansList = ansFile.readlines()
ansStr = {}

boolDict = {}
for i in range(1,19):
    ansStr[i] = ansList[i].strip("\n")
    boolDict[f"{boolListFormat[i]}"] = ansStr[i]


varToConsole = input("Would you like to print to the Console (Y/N)")
if varToConsole.lower() == "y":
    for i in range (1,19):
        print(f" {boolListFormat[i]} = {boolDict[boolListFormat[i]]}")
else:
    varToWindow = input("Would you like to print to a Message box(Y/N)")
    if varToWindow.lower() == "y":
        win = Tk()
        lb = Listbox(win, height= 30, width=75)
        for i in range(1,19):
            lb.insert(i, f"{i}) {boolListFormat[i]} = {boolDict[boolListFormat[i]]}")
        lb.pack()
        win.mainloop()


