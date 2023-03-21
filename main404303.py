import pyfiglet
import time
import phonenumbers
from number2 import number
from phonenumbers import geocoder
Key = 'b0148a00603b416db43dbc80b4a35b95'

# Get input from user
user_input = ("DarkWatch")

# Display input in green ASCII art letters
ascii_banner = pyfiglet.figlet_format(user_input.upper())
print('\033[1;32;40m')
print(ascii_banner)
print('\033[0m')

# Generate animated ASCII art banner of input in green color
for i in range(4):
    print('\033[1;32;40m')
    print(ascii_banner)
    print('\033[0m')
    time.sleep(0.5)
    print("\033[2J\033[1;1H")
    time.sleep(0.5)
    
user_input = ("Dark WaTch")    
ascii_banner = pyfiglet.figlet_format(user_input)
print('\033[1;32;40m')
print(ascii_banner)
print('\033[0m')    
 
user_input1 = input('\033[1;32;40m'"Will You Use It Ethically?(y/n) ")
if user_input1.lower() == "y":
 print("wait... \n")
 time.sleep(3.5)
elif user_input1.lower() == "n":
 	print("Exit...")
 	exit()
 	
yourlocation = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(yourlocation, "en"))

from phonenumbers import carrier
services = phonenumbers.parse(number)
print(carrier.name_for_number(services, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(yourlocation)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

import folium
myMap = folium.Map(yourlocation[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup= yourlocation).add_to((myMap))

myMap.save("victum_locaton.html")
