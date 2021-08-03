#! /usr/bin/env python3

import f2c
import c2f

# Validation loop breaks could make break after so many tries
loop = 0
temp = float(input("Enter a temperature: "))# should add digits but need to finish atm life is hard.
while loop == 0:
    scale = input("Enter the measurement scale of (F or C): ")# could add more strings that signify the degree
    counter = 1
    break

#after a degree is chosen
while loop == 1:
    if scale.lower() == "f":
        tempC = f2c.f_to_c(temp)
        print(f"{temp} in Fahrenheit is equal to {tempC} in Celsius")
        reset = input("Would you like to convert another temperature?(Y/N): ")
        if reset.lower() == "y":
            counter = 0
        else:
            break
    else:
        tempF = c2f.c_to_f(temp)
        print(f"{temp} in Celsius is equal to {tempF} in Fahrenheit")
        reset = input("Would you like to convert another temperature?(Y/N): ")
        if reset.lower() == "y":
            counter = 0
        else:
            break  # need to fix the loop logic above but dont have the time :(


