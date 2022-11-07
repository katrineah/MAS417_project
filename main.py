from weather import weather
from stlGen import stlGen

def main():

    location = input('Type in your location:')
    refTime = input('For which date do you want to see the weather? Write your date in the following form: yyyy-mm-dd')

    Weather = weather(location, refTime)

    coordinates = Weather.get_coordinates()

    stationId = Weather.get_stationId()

    weatherdata = Weather.get_weather()

    stl = stlGen()
    stl.generate_png(weatherdata)
main()