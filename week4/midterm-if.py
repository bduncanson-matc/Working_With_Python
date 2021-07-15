#!/usr/bin/env python3
#Variables
firstName = "Bryan"
lastName = "Duncanson"
openMidtermTxt = open("Midterm-if.txt")
midTermLines = openMidtermTxt.readlines()
Total = 0

#list
keyWordsList = {
"gmeach18@ed.gov",
"248.253.63.149",
"Whiteland",
"80.222.19.190",
"Kayley",
"dcassyqw@microsoft.com"}


#script code Learn how to format different characters on each side
#if time permits comeback and do it the long way
#

print (f"Name: {firstName:<>6}>{lastName:<>10}>")

#enumerate works way better than iterating on len()
for num, line in enumerate(midTermLines):
       for i in keyWordsList:
           if i in line:
               Total += num

print(f"The total is:{Total:> 5}")




