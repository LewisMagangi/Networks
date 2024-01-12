#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

# Define headers as a dictionary
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Create a Request object with the specified URL and headers
request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')
    
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf8_content)
    
    # Display response headers
    print("\nHeaders:")
    for header in response.getheaders():
        print(f"\t- {header[0]}: {header[1]}")
                                        
