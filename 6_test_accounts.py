import requests

BASE = "http://127.0.0.1:2305/"

##### 6. Accounts Cases ..... 

statuses = ['archive', 'unarchive', 'nothing']

for i in statuses:
	status = i

	url_accounts = f"accounts/{status}" 

	response_accounts = requests.get(BASE+url_accounts)
	print ("Accounts function response is ", response_accounts.json())