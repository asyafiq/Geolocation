import csv
from geopy import Nominatim
geolocator=Nominatim()
##corpus_path='/home/ahmad/Documents/kerja2 (data)/tes.csv'
#def getFileToGeocode():   
#    geoCSV = csv.reader(open(corpus_path,'r'))
#    geoHeadings = geoCSV.next()
#    geoData = [row for row in geoCSV]
	 
#    return (geoHeadings,geoData)
	 
#def addToMaster(masterData,accrow):   
#    masterData.append(accrow)
	 
	 
#def main():
#    g = geocoders.Google()
#    acc = getFileToGeocode()
#    masterHeadings = "Place" ,"Lat/Long"
#    masterData=[]
	     
 #   for accrow in acc[1]:
 #       print g.geocode(accrow[1])      
 #       addToMaster(masterData,g.geocode(accrow[1]))
	 
 #   masterCSV = csv.writer(open('master.csv','wb'),dialect='excel')
 #   masterCSV.writerow(masterHeadings)
 #   for row in masterData:
#	    masterCSV.writerow(row)
	 
#if __name__ == "__main__":
	    
 #   main()

keyword=input()
lokasi=geolocator.geocode(keyword)
print lokasi.latitude
