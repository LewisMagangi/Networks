#!/usr/bin/python3
import urllib.request

url = "https://www.google.com"
response = urllib.request.urlopen(url)
html_content = response.read()

print(html_content)
