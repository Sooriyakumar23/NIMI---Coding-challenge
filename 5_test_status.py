import requests

BASE = "http://127.0.0.1:2305/"

##### 5. Status Cases .....

nics = [972179086, 985367408, 972179086, 972179086, 914567390, 673498279]
statuses = ['archive', 'unarchive', 'archive', 'archive', 'unarchive', 'archive']

for i in range(len(nics)):
	nic = nics[i]
	status = statuses[i]

	url_status = f"status/{nic}/{status}" 

	response_status = requests.get(BASE+url_status)
	print ("Status function response is ", response_status.json())