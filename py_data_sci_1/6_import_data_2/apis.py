#api is set of protocals and routines to interact with software applications
import requests

url = 'http://www.omdbapi.com/?apikey=ff21610b&t=hackers'
r = requests.get(url)

#built in json decoder
json_data = r.json()

for key, value in json_data.items():
	print(key + ': ', value)

#?t=hackers is a query string - return data for a movie with title(t) 'Hackers'


# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
