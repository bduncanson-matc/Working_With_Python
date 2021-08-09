#!/usr/bin/env python3

# imported modules
import argparse
import requests
from bs4 import BeautifulSoup

# basic variables
firstName = "Bryan"
lastName = "Duncanson"
# adding arguments using the argparse module
parser = argparse.ArgumentParser(description='final exam arg parse')
parser.add_argument('-ip', required= True, type=str, dest='ipVar', help="Enter a ip address")
parser.add_argument('-f', required= True, choices=[1,2,3,4,5], type=int, dest='funcVar', help="Enter a function number")
# creating a variable to access arguments
args = parser.parse_args()
# url string variable using arguments from the terminal
url = f"http://{args.ipVar}/q{args.funcVar}"

print(f"{firstName} {lastName}")
print(url)

# function to return text of the url in the -ip argument
def get_response():
    response = requests.get(url)
    return response.text
# call if the argugment -f == 1
if args.funcVar == 1:
    print(get_response())

def parse_string():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

parse_string()

