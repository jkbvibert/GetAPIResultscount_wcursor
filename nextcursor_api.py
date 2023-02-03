#CSE-57666
import requests
import json

headers = {'Content-Type': 'application/json','li-api-session-key': '<scrubbed>'}
#headers = {'Content-Type': 'application/json'}


data = {"users": {"fields": ["id","first_name","last_name","registration_data.registration_time","last_visit_time"],"constraints": [{"registration_data.status": "partially-registered"}],"limit": 500,"sorts": ["id asc"]}}

final_size = 0

r = requests.post(url = "https://techcommunity.microsoft.com/api/2.0/search", data = json.dumps(data, default=str), headers=headers)

#print(r.text)
r2_formatted = r.json()

while True:
	try:
		size = r2_formatted['data']['size']
		final_size = final_size + int(size)
		next_cursor = r2_formatted['data']['next_cursor']
	except:
		print(final_size)
		exit(0)
		
	data2 = {"users": {"fields": ["id","first_name","last_name","registration_data.registration_time","last_visit_time"],"constraints": [{"registration_data.status": "partially-registered"}],"limit": 500,"sorts": ["id asc"],"cursor": next_cursor}}
	r2 = requests.post(url = "https://techcommunity.microsoft.com/api/2.0/search", data = json.dumps(data2, default=str), headers=headers)
	r2_formatted = r2.json()
