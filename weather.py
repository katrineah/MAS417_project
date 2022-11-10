import requests

class weather:

    def __init__(self, location, refTime):
        self.location = location
        self.refTime = refTime


    # Get the coordinates of the location inputted:
    def get_coordinates(self):
        self.client_id = 'd60cd339-6d78-4373-92e4-9747491e0b0e'
        endpoint = f'https://frost.met.no/locations/v0.jsonld?names={self.location}'

        r = requests.get(endpoint, auth=(self.client_id,''))

        json = r.json()

        if r.status_code == 200:
            data1 = json['data']
        else:
            print('Error! Returned status code %s' % r.status_code)
            print('Message: %s' % json['error']['message'])
            print('Reason: %s' % json['error']['reason'])

        # If the data1-list does not exist, it is most likely because the location did not exist in the api
        # --> tell the user to try another location or re-spell:
        try:
            self.lon = data1[0]['geometry']['coordinates'][0]
            self.lat = data1[0]['geometry']['coordinates'][1]
        except NameError:
            print('The was something wrong with the location you typed in. Check for misspellings or try another location.')

    # Find the source id for the nearest weather station:
    def get_stationId(self):

        endpoint = f'https://frost.met.no/sources/v0.jsonld?geometry=nearest(POINT({self.lon} {self.lat}))'

        r=requests.get(endpoint,auth=(self.client_id,''))

        json2 = r.json()

        if r.status_code == 200:
            data2 = json2['data']
        else:
            print('Error! Returned status code %s' % r.status_code)
            print('Message: %s' % json2['error']['message'])
            print('Reason: %s' % json2['error']['reason'])

        self.stationId = data2[0]['id']


    # Now get the weather for this place:
    def get_weather(self):
        endpoint = 'https://frost.met.no/observations/v0.jsonld'

        # Define parameters to send in to the observations-API
        parameters = {
            'sources' : f'{self.stationId}',
            'elements': 'air_temperature, sum(precipitation_amount PT1H)',
            'referencetime': f'{self.refTime}',
        }
        r = requests.get(endpoint, parameters,auth=(self.client_id,''))
        json3 = r.json()
        if r.status_code == 200:
            data3 = json3['data']
            print('Data retrieved from frost.met.no!')
        else:
            print('Error! Returned status code %s' % r.status_code)
            print('Message: %s' % json3['error']['message'])
            print('Reason: %s' % json3['error']['reason'])

        try:
            temp = data3[0]['observations'][0]['value']
            unit0 = data3[0]['observations'][0]['unit']
            rain = data3[0]['observations'][1]['value']
            unit1 = data3[0]['observations'][1]['unit']

            self.weatherdata = f"Temp: {temp} {unit0}\nRain: {rain} {unit1}"
            return self.weatherdata
        except NameError:
            print('No data available for this date')
        except IndexError:
            print('Temperature data not available for this date')



