
import requests
import pandas as pd

import requests


location = input('Type in your location:')
client_id = 'd60cd339-6d78-4373-92e4-9747491e0b0e'
endpoint = f'https://frost.met.no/locations/v0.jsonld?names={location}'


# Issue an HTTP GET request
r = requests.get(endpoint, auth=(client_id,''))
# Extract JSON data
json = r.json()

# Check if the request worked, print out any errors
if r.status_code == 200:
    data1 = json['data']
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json['error']['message'])
    print('Reason: %s' % json['error']['reason'])

lon = data1[0]['geometry']['coordinates'][0]
lat = data1[0]['geometry']['coordinates'][1]
print(lon,' ',lat)

# Now we get the source id for the nearest weather station:
endpoint = f'https://frost.met.no/sources/v0.jsonld?geometry=nearest(POINT({lon} {lat}))'

r=requests.get(endpoint,auth=(client_id,''))

json2 = r.json()

if r.status_code == 200:
    data2 = json2['data']
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json2['error']['message'])
    print('Reason: %s' % json2['error']['reason'])

stationId = data2[0]['id']


# Now get the weather for this place:
endpoint = 'https://frost.met.no/observations/v0.jsonld'
refTime = input('For which date do you want to see the weather?')

# Define parameters to send in to the observations-API
parameters = {
    'sources' : f'{stationId}',
    'elements': 'air_temperature, sum(precipitation_amount PT1H)',
    'referencetime': f'{refTime}',
}
r = requests.get(endpoint, parameters,auth=(client_id,''))
json3 = r.json()
if r.status_code == 200:
    data3 = json3['data']
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json3['error']['message'])
    print('Reason: %s' % json3['error']['reason'])

try:
    print(data3[0]['observations'][0]['value'], data3[0]['observations'][0]['unit'])
    print(data3[0]['observations'][1]['value'], data3[0]['observations'][1]['unit'])
except NameError:
    print('No data available for this date')
except IndexError:
    print('Temperature data not available for this date')


