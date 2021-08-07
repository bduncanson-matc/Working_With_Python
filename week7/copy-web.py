#!/usr/bin/env python3

import requests

# get function retrieves a URL's html
response = requests.get("https://notpurple.com")

if response.ok:
    htmlFile = open("my_web_file.html", "w+")
    htmlFile.write(response.text)

