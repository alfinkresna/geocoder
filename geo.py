#Copyright 2022 alfinkresna
from geopy.geocoders import Nominatim as Geo
from geopy import distance as ds
import os

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
        except:
            print("\n{!} Lokasi Tidak Ada")
               
    def dist():
        try:
            os.system("clear")
            print("\t\tJarak\n")
            print("Lokasi 1")
            lat = input("\nInput Latitude : ")
            long = input("\nInput Longitude : ")
            print("\nLokasi 2")
            lat2 = input("\nInput Latitude : ")
            long2 = input("\nInput Longitude : ")
            dist1 = (lat, long)
            dist2 = (lat2, long2)
            ds1 = ds.great_circle(dist1, dist2).miles
            ds2 = ds.great_circle(dist1, dist2).km
            print("\nJarak (Mil) : {} {}".format(ds1,"mil"))
            print("\nJarak (Kilometer) : {} {}".format(ds2, "km"))
        except :
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
            print("\n{!} Koordinat Salah")
        
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
