#! /usr/bin/env python3
#from c2f.py import C_to_f
#from f2c.py import f_to_c

temp = input("Enter the temperature: ")
scale = input("Enter the measurement scale of (F or C): ")

#make sure a valid input is entered
if scale == "F":
    f = temp
    tempC = f_to_c(f)
    print(f"{temp} in F is equal to {tempC} in C")

elif scale == "C":
    tempF = c_to_f(temp)
    print(f"{temp} in F is equal to {tempF} in F")
else:
    scale = input("invalid input try again (F or C)")