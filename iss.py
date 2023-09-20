import requests
# Importing library to make HTTP Requests

response = requests.get('http://api.open-notify.org/iss-now.json') # HTTP GET method, fetches data and saves it in response var
iss_data = response.json() # Parsing json response and storing it in iss_data 
iss_position = iss_data['iss_position'] # Extracts position object from json data

# Extract latitude and longitude values from the iss pos object, and stores them in
# the lat and long variables respectively

lat = iss_position['latitude'] 
long = iss_position['longitude']

print(lat)
print(long)