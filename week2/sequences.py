#! /usr/bin/env python3

varString = "Here is a nice string to slice"
varList = ["Here","is","a","nice","list","to","slice"]

print(varString[3:])
print(varString[:3])
print(varString[3:12])
print(varString[::2])
print(varString[::-1])

print(varList[::-1])
print(varList[2::-1])
print(varList[2:4])
print(varList[::3])
print(varList[1:7])


for i in varString: print(i)

for i in varList: print(i)



