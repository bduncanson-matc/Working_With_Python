#! /usr/bin/env python3

import subprocess

myProc = subprocess.run(['ps', '-axco', 'command'], stdout=subprocess.PIPE)
myProcList = myProc.stdout.decode().split('\n')


for item in myProcList:
    print(f"{item}")

count = 0
for item in myProcList[1:]:
    count += 1

print(count)

# seemed too easy....