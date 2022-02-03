import requests

BASE = "http://127.0.0.1:2305/"

##### 4. Read Cases .....

nics = [972179086, 985367408, 972179086, 972179086, 914567390, 673498279]

for i in nics:
	nic = i

	url_read = f"read/{nic}"

	response_read = requests.get(BASE+url_read)
	print ("Read function response is ", response_read.json())