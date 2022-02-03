import requests

BASE = "http://127.0.0.1:2305/"

##### 2. Delete Cases .....

nics = [972179086, 972179087, 97217, "nothing"]

for i in nics:
	nic = i

	url_delete = f"delete/{nic}"

	response_delete = requests.get(BASE+url_delete)
	print ("Delete function response is ", response_delete.json())