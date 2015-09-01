import pandas as pd
import re
import csv
from geopy.geocoders import Nominatim
geolocator=Nominatim()
corpus_path='/home/ahmad/Documents/kerja2 (data)/tes.csv'
#misal keywordnya = jakarta
keyword='jakarta' or 'Jakarta'
#lokasi_corpus=pd.read_csv(corpus_path)
#okasi_baru=lokasi_corpus['Keyword']
#lokasi=geolocator.geocode(lokasi_baru)

#print lokasi, (lokasi.latitude,lokasi.longitude) 

def get_location():
    lokasi3=open(corpus_path,'r')
    tweet=[]
    for data in lokasi3:
        tweet.append(data[1])
        print tweet
    #lokasi=geolocator.geocode([tweet])
    #print (lokasi.latitude,lokasi.longitude)
    
       


def update_corpus():
    with open(corpus_path,'a') as csvinput:
        writer=csv.writer(csvinput)
        writer.writerow()
    
def search_corpus():


    return



def split_data(corpus_path):
    corpus_file=open(corpus_path,"r") 
    data_split = corpus.read().split("\t")
    #corpus_file=pd.read_table(corpus_path)
    #corpus_file=corpus_file.values 
    data=corpus_file
    
    return data
    
    
    


