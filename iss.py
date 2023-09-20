import requests
import openpyxl
from datetime import datetime
# Importing requests library to make HTTP Requests, openpyx1 library to create a new excel workbook,
# datetime module from standard python library for dates and times


response = requests.get('http://api.open-notify.org/iss-now.json') # HTTP GET method, fetches data and saves it in response var
iss_data = response.json() # Parsing json response and storing it in iss_data 
iss_position = iss_data['iss_position'] # Extracts position object from json data

# Extract latitude and longitude values from the iss pos object, and stores them in
# the lat and long variables respectively

lat = iss_position['latitude'] 
long = iss_position['longitude']

print(lat)
print(long)

# vv method used to format d & t as a string according to specified format (YEAR_MONTH_DAY_HOUR_MINUTE_SECOND)
datestring = datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S')
print(datestring)

def create_excel():
    # Creating a new Excel workbook
    iss_workbook = openpyxl.Workbook()

    # Creating a new worksheet
    worksheet = iss_workbook.active

    # Change the title of the worksheet
    worksheet.title = "{datestring}_coordinates"

    # Add data to the worksheet
    worksheet['A1'] = "lat"
    worksheet['B1'] = "lng"

    worksheet['A2'] = lat
    worksheet['B2'] = long

    # Save the workbood to a file
    iss_workbook.save('{}_iss_coordinates')

    # Close the workbook
    iss_workbook.close()
    

# 9/20/23
# installed openpyx1 library