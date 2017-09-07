#Two ways to do this, urllib or requests

#URL LIB Package

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()


##EASIER WAY USE REQUESTS
import requests
url = "https://www.wikipedia.org/"
r = requests.get(url)
text = r.text

print(text)
