__Author__: "Alfin"
__Copyright__: "© 2022 alfinkresna"

import os
from geopy.geocoders import Nominatim as Geo
from geopy import distance as ds


geocoder = Geo(user_agent="Geo.app")

class Src:
    
    def lok():
        os.system("clear")
        try:
            print("\t\tLokasi\n")
            lokasi = input("\nInput Lokasi : ")
            location = geocoder.geocode(lokasi)
            print("\nLokasi : {}".format(location))
            print("\nLatitude : %s \n\nLongitude : %s" % (location.latitude, location.longitude))
            print("\nGoogle Maps : https://www.google.com/maps/search/?api=1&query={},{}".format(location.latitude,location.longitude))
        except AttributeError:
            print("\n{!} Lokasi Tidak Ada")
   
                 
    def dist():
        os.system("clear")
        try:
            print("\t\tJarak\n")
            print("Lokasi 1")
            lat, long = input("\nInput Latitude : "), input("\nInput Longitude : ")
            print("\nLokasi 2")
            lat2, long2 = input("\nInput Latitude : "), input("\nInput Longitude : ")
            dist1, dist2 = (lat, long), (lat2, long2)
            ds1 = ds.great_circle(dist1, dist2).miles
            ds2 = ds.great_circle(dist1, dist2).km
            print("\nJarak (Mil) : {} {}".format(ds1,"mil"))
            print("\nJarak (Kilometer) : {} {}".format(ds2, "km"))
        except ValueError:
            os.system("clear")
            print("\n{!} Input Salah")

                
    def rev():
        os.system("clear")
        try:
            print("\t\tReverse Geocoding\n")
            print("Contoh Input : -7.2459717, 112.7378266\n")
            x = str(input("Input Latitude Longitude : "))
            loc = geocoder.reverse(x)
            print("\n%s" % loc)
        except ValueError:
            os.system("clear")
            print("\n{!} Koordinat Salah")


if __name__ == "__main__":         
     print("\t\tGeocoder\n")     
     i = input("{1} Lokasi \n\n{2} Jarak \n\n{3} Reverse Geocoding\n\nPilih Menu : ")    
     if i == "1":
         Src.lok()
     elif i == "2":
         Src.dist()
     elif i == "3":
         Src.rev()
     else:
         print("\nPilihan Salah !")
