import requests

BASE = "http://127.0.0.1:2305/"

##### 3. Update Cases .....

nics = [972179086, 985367408, 972179086, 972179086, 914567390]
fields = ["name", "place", "work", "amount", "nic"]
values = ["Sooriya", "Antartica", "DL Engineer", 999999, 973243546]

for i in range(len(nics)):
	nic = nics[i]
	field = fields[i]
	value = values[i]

	url_update= f"update/{nic}/{field}/{value}"

	response_update = requests.get(BASE+url_update)
	print ("Update function response is ", response_update.json())