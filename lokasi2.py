import geocoder
import urllib
import csv
from geopy.geocoders import Nominatim
import pandas as pd
#buat file get_location(keyword,user_profile)
#df = pd.read_csv(''/home/ahmad/Documents/kerja2 (data)/sample-poi.csv', sep='|')

#geolocator = Nominatim()
#lokasi=geolocator.geocode(keyword)
#print (lokasi.latitude,lokasi.longitude)



file_lokasi = csv.reader(open('/home/ahmad/Documents/kerja2 (data)/sample-poi.csv'),delimiter='|')
line_no=0

def get_location(keyword, user_profile):
    if user_profile in file_lokasi:
            check_corpus()
            check_geocoder()
            update_corpus()
           
    else:
        #fungsi bikinan mba tasya
        
def check_corpus():
        with open('/home/ahmad/Documents/kerja2 (data)/sample-poi.csv') as csvfile:
        #data=pd.read_table('/home/ahmad/Documents/kerja2 (data)/sample-poi.csv',sep='|')    
        reader = csv.reader(csvfile)
        reader.next()
        check_keyword = []
        for column in reader:
            check_keyword.append(column[0].lower())
                for word in sentences.split():
            if word in check_keyword:
                location = word  
        else:
                print "Lokasi Tidak ditemukan"

        return location

def check_geocoder(#dasdasdasdasdasd"):
    geolocator = Nominatim()
    lokasi=geolocator.geocode(keyword)
    print (lokasi.latitude,lokasi.longitude)

    return
    
def update_corpus():
    line_no = 0
    new_csv = [] 
    with open('/home/ahmad/Documents/kerja2 (data)/sample-poi.csv','r') as csvfile:
        filereader = csv.reader(csvfile)

        for line in filereader:
            if line_no == 0:
                for key in update_data:
                    update_data[key][0] = line.index(key) 
                   
            else:
                for key in update_data:
                    line[update_data[key][0]] = update_data[key][1].pop(0) 
                 

            new_csv.append(line)

            line_no +=1

    with open('/home/ahmad/Documents/kerja2 (data)/sample-poi.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)

        for line in new_csv:
            filewriter.writerow(line)


    return




def word_in_text(word,text):
	word=word.lower()
	text=text.lower()
	match=re.search(word,text)
	if match:
		return True
	return False
	
	
	corpus_path=.....
	tweets=[]
	corpus_file=open(corpus_path,"r")
	for line in corpus_file:
		tweets.append(line)
		
		
	print "tweet"+str(len(tweets))	 
