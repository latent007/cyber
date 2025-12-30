import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
if response.status_code == 200:
	data = response.json()
	
	print("First Title:", data[0]['title'])
	print("First Body:", data[0]['body'])

else:
	print("[-] Error:", response.status_code)
