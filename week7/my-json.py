#!/usr/bin/env python3

import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Add IP address")
parser.add_argument('-ip', dest='ipaddress', default='172.217.8.206', help='Enter an IP address' )
args = parser.parse_args()

# Retrieve json data from WebAPI
json_raw = requests.get(f"http://ipinfo.io/172.217.8.206/json")

# Convert json byte stream into a dictionary
myDict = json.loads(json_raw.text)

for key in myDict:
    if args.ipaddress and myDict['ip']:
        myDict['ip'] = args.ipaddress
    print(f"{key} : {myDict[key]}")




