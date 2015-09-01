#lokasi6
#Jika keywordnya ada di file corpus, maka
        #keyword.lang,keyword.lati
#selain itu jika tidak ada di file corpus, maka
        #cari keyword dari geocoder
        #print keyword.lang dan key.lat (adari geopy)
        #update corpus lama




import pandas as pd
import re
import csv
from geopy.geocoders import Nominatim
geolocator=Nominatim()
corpus_path='/home/ahmad/Documents/kerja2 (data)/tes.csv'

lokasi=geolocator.geocode('Jakarta')
print lokasi



def baca_data():
    data=pd.read_csv(corpus_path,header=None)
    return data[0]
 

def search_data():
    
    with open(corpus_path) as openfile:
        
        for line in openfile:
            for part in line.split('\n'):
                if key in part:
                    #print lokasi=geolocator.geocode(keyword)
                    print "key"
                else:
                    #print "Tidak Ada"
                    lokasi=geolocator.geocode(part)
                    print lokasi

def update_data():
     data_lama=open(corpus_path,'r')

     data_baru=open(corpus_path,'w')



def get_from_geocoder(keyword):
    
    list_of_words = keyword.split()
    location=[]
    for kata in lis_of_word:
        location.append()
    
    address_longlat = []      
    for address in location:
        g = geocoder.google(address)
        list_longlat = g.latlng
        list_longlat.insert(0,address)
        address_longlat.append(list_longlat)
        print address_longlat





y=baca_data()


