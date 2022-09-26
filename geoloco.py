from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises") 
a = input("Enter the zipcode : ")
zipcode = a 
location = geolocator.geocode(zipcode) 
print("Zipcode:",zipcode)
print("Details of the Zipcode:")
print(location)  
