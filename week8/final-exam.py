#!/usr/bin/env python3

# imported modules
import argparse
import sys
import requests
from bs4 import BeautifulSoup
import json
import socket

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



def parse_header(url_arg=url):
    response = requests.get(url_arg)
    headerDict = response.headers
    return headerDict['MATC-HEADER']

def parse_json(url_arg=url):
    response = requests.get(url_arg)
    jsonDict = json.loads(response.text)
    for dict in jsonDict['Music And Books']:
        if dict['title'] == '1984':
            return dict['author']

def socket_client(ip=args.ipVar):
    if ip == '172.23.23.252':
        changeUrl = input(f"your url is set argument is set to 172.23.23.252. Would you like to change it 172.23.23.253 (Y/N)\n")
        if changeUrl.lower() == 'y':
            ip = '172.23.23.253'
    RHOST = ip
    RPORT = range(5000,6001)
    SND_DATA = "secret"

    try:
        for port in RPORT:
            C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = C_SOCK.connect_ex((RHOST, port))
            if result == 0:
                C_SOCK.send(bytearray(SND_DATA, 'utf8'))
                RCV_DATA = C_SOCK.recv(1024)
                C_SOCK.close()
                return RCV_DATA.decode()
    except KeyboardInterrupt:
        sys.exit()
    except socket.error:
        sys.exit


funcKey = args.funcVar - 1
funcList = [get_response, parse_string, parse_header, parse_json, socket_client]
print(funcList[funcKey]())

