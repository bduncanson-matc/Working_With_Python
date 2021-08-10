#!/usr/bin/env python3

# imported modules
import argparse
import requests
from bs4 import BeautifulSoup
import json

# basic variables
firstName = "Bryan"
lastName = "Duncanson"
fullName = f"{firstName} {lastName}"
# adding arguments using the argparse module
parser = argparse.ArgumentParser(description='final exam arg parse')
parser.add_argument('-ip', required= True, type=str, dest='ipVar', default='172.23.23.252', help="Enter a ip address")
parser.add_argument('-f', required= True, choices=[1, 2, 3, 4, 5], type=int, dest='funcVar', help="Enter a function number")
# creating a variable to access arguments
args = parser.parse_args()
# url string variable using arguments from the terminal
url = f"http://{args.ipVar}/q{args.funcVar}"

print(fullName)
print(url)

# function to return text of the url in the -ip argument
def get_response():
    response = requests.get(url)
    return response.text
# call if the argugment -f == 1
# if args.funcVar == 1:
#   print(get_response())

def parse_string():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for msg in soup.find('h3'):
        hStr = msg.string

    return hStr[2::3]

#if args.funcVar == 2:
 #   print(parse_string())



def parse_header(arg=url):
    response = requests.get(arg)
    headerDict = response.headers
    return headerDict['MATC-HEADER']

def parse_json(arg=url):
    response = requests.get(arg)
    jsonDict = json.loads(response.text)
    decodedDict = complex(jsonDict)
    return response

funcKey = args.funcVar - 1
funcList = [get_response, parse_string, parse_header]
print(funcList[funcKey]())
print(parse_json())
