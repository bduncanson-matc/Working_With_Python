#! /usr/bin/env python3

def f_to_c(f):
    # c = known conversion formula
    c = (5/9) * (f-32)
    return c

def main():
    # take user input and save it to variable f
    f = float(input("Enter the temperature in Fahrenheit: "))
    # using f in f_to_c function prints Celcius
    outputC = f_to_c(f)
    print(f"{f} Fahrenheit degrees is equal to {outputC} degrees in Celcius.")

if __name__ == "__main__":
    main()
