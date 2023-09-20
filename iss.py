import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
iss_data = response.json()
iss_position = iss_data['iss_position']

lat = iss_position['latitude']
long = iss_position['longitude']

print(lat)
print(long)