import requests

BASE = "http://127.0.0.1:2305/"

##### 1. Create Cases .....

nics = [972179086, 985367408, 972179086, 972179086, 914567390, 673498279, 747890040, 914567390, 657389028, 867989560]
names = ["Sooriya", "Nimi", "Yolo", "RCNN", "Yash", "Achini", "Kumar", "ANN", "CNN", "RNN"]
places = ["Jaffna", "Colombo", "Trinco", "USA", "London", "Kandy", "Gampaha", "Jaffna", "Colombo", "Jaffna"]
works = ["Developer", "Data Analyst", "ML Engineer", "Team Lead", "Software Archtect", "Devops Engineer", "PhD student", "undergraduate", "HR", "CEO"]
contacts = ["0701234567", "0772345678", "0761234789", "0779087654", "0753456789", "0701255567", "0772555678", "0779000654", "07790876994", "0761266660"]
amounts = [0, 500, 0, 0, 1000, 0, 50000, 120000000, 6500, 9900]


for i in range(len(nics)):
	nic = nics[i]
	name = names[i]
	place = places[i]
	work = works[i]
	contact = contacts[i]
	amount = amounts[i]

	url_create = f"create/{nic}/{name}/{place}/{work}/{contact}/{amount}"

	response_create = requests.get(BASE+url_create)
	print ("Create function response is ", response_create.json())