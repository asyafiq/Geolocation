import pandas as pd
import re
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim()
tweets =[]
corpus_path='/home/ahmad/Documents/kerja2 (data)/sample-poi.csv'
corpus_file=open(corpus_path,"r")
#df=pd.read_table(corpus_file)
for line in range(100):
     print (corpus_file.readline())
    #print tweets.append(line[])


def get_location(keyword,user_profile):

    if user_profile in corpus_file:

    elif:     
        lokasi=geolocator.geocode(keyword)
        print (lokasi.latitude,lokasi.longitude)




def update_corpus(keyword):    
    
    with open(corpus_path,'a') as csvinput:
        writer=csv.writer(csvinput)
        writer.writerow(keyword)


def get_geolocasi():
    lokasi=geolocator.geocode(keyword)
     print (lokasi.latitude,lokasi.longitude)
        



def word_in_text(word,text):
    word=word.lower()
    text=text.lower()
    match=re.search()
    


    
    


