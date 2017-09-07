#standard form of transmitting data through APIs is json format
#JSON allows for real-time server to browser communication

#loading JSON
import json
with open('data/us-states.json', 'r') as json_file:
	json_data = json.load(json_file)

#json data is a dict
print(type(json_data))

for key, value in json_data.items():
	print(key + ':', value)
