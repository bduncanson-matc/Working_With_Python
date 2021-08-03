#! /usr/bin/env python3

def c_to_f(c):
    # f = known conversion formula
    f = (c * 9/5) + 32
    return f

def main():
    # take user input and save it to variable f
    c = float(input("Enter the temperature in Celsius: "))
    # using c_to_f to print Celcius
    outputF = c_to_f(c)
    print(f"{c} Celsius degrees is equal to {outputF} degrees in Celsius.")

main()