#! /usr/bin/env python3
# 1)
passwdFile = open("/etc/passwd")
passwdStr = passwdFile.read()
print(len(passwdStr))
print(type(passwdStr))
print("The .read() method is used when a file size does not cause problems")

# 2)
passwdFile = open("/etc/passwd")
passwdList = passwdFile.readlines()
print(len(passwdList))
print(type(passwdList))
print("The .readlines method is used when size of the file is a factor")

# 3)
count = 0
passwdFile = open("/etc/passwd")
for line in passwdList:
    count += len(line)
print("this method is used when you need to loop through and read a file one line at a time.")



