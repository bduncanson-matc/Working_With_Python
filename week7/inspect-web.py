#!/usr/bin/env python3

# importing the modules
import requests
from bs4 import BeautifulSoup

# target url
url = input("Enter a URL or press Enter for https://notpurple.com: ")
if url == "":
    url = "https://notpurple.com"
# making requests instance
response = requests.get(url)

# using the BeaitifulSoup module
soup = BeautifulSoup(response.content, 'html.parser')

# displaying the title
print("Title of this URL is: ")
for title in soup.find_all('title'):
    urlTitle = title.get_text()

print(urlTitle)

links = []
for link in soup.find_all("a", href=True):
    links.append(link['href'])

print(f"The Links on the URL {url} are: ")
for link in links:
    print(link)
