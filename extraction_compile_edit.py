# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:30:00 2015

@author: 1152
"""
import csv
import re
from ngram import NGram
import geocoder

def abbreviation(sentences):
    corpus = csv.reader(open("D:/tasya/python/code/Geo-Tag/corpus/abbreviation.csv"))
    dictionary={}
    for row in corpus:
        dictionary[row[0]]=row[1]
   
    for word in sentences.split():
        if word in dictionary.keys():
            sentences = re.sub(word,dictionary[word],sentences)
    return sentences
    
def alay_normalizer(kalimat):
    #kamusalay
    kamusnya = csv.reader(open("d:/kamusalay.csv"))
    kamus={}
    for row in kamusnya:
        kamus[row[0]]=row[1]
    

    # preprocessing
    
    # huruf mejadi lower case semua
    ubah=kalimat.lower()
    
    # menghilangkan link
    ubah=re.sub("http://\w.\w+.\w+|https://\w.\w+.\w+"," ", ubah)
    
    # perulangan a>2 =a
    ubah=re.sub(r'([a-z])\1\1+', r'\1', ubah)
    
    # menghilangkan puntuation tertentu
    ubah=re.sub("\?|!|\""," ", ubah)
    # rules alay
    # replace ea to ya 
    ubah=re.sub("\sea|^ea"," ya",ubah)
    
    # replace th to c
    tuples=re.findall("\w+th\w+|\w+th",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("th","c",tuple)
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
                
    # replace 2 to z
    tuples=re.findall("^2[^\d]\w+|\s2[^\d]\w+|[^\d]2[^\d]|\s2[^\d]\w+|\w+[^\d]2\s|\w+[^\d]2\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("2","z",tuple)
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
                    
    # replace 3 to e
    tuples=re.findall("^3[^\d]\w+|\s3[^\d]\w+|[^\d]3[^\d]|\s3[^\d]\w+|\w+[^\d]3\s|\w+[^\d]3\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("3","e",tuple)
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
    
    #replace 5 to s
    tuples=re.findall("\w+[^\d]5[^\d]",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("5","s",tuple)
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
    
    # replace 6 to g
    tuples=re.findall("^6[^\d]\w+|\s6[^\d]\w+|[^\d]6[^\d]|\s6[^\d]\w+|\w+[^\d]6\s|\w+[^\d]6\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("6","g",tuple)
        
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
                    
    # replace 7 to j
    tuples=re.findall("^7[^\d]\w+|\s7[^\d]\w+|[^\d]7[^\d]|\s7[^\d]\w+|\w+[^\d]7\s|\w+[^\d]7\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("7","j",tuple)
        
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
    
    # replace 8 to b
    tuples=re.findall("^8[^\d]\w+|\s8[^\d]\w+|[^\d]8[^\d]|\s8[^\d]\w+|\w+[^\d]8\s|\w+[^\d]8\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("8","b",tuple) 
       
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
    
    # replace 9 to g
    tuples=re.findall("^9[^\d]\w+|\s9[^\d]\w+|[^\d]9[^\d]|\s9[^\d]\w+|\w+[^\d]9\s|\w+[^\d]9\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("9","g",tuple)
        
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
                    
    # replace 0 to o
    tuples=re.findall("^0[^\d]\w+|\s0[^\d]\w+|[^\d]0[^\d]|\s0[^\d]\w+|\w+[^\d]0\s|\w+[^\d]0\w+[^\d]\w\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("0","o", tuple) 
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
                    
    #token2f=re.findall("[^\d]\w+4[^\d]+",token1) #nonumber #noawal #2step
    #token2=re.sub("4","empat",token2f[0]) #nonumber #noawal #2step #masukkamus aja
    
    # replace zt to s
    tuples=re.findall("\w+zt\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("zt","s",tuple)
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
    
    # replace z to s
    tuples=re.findall("\w+z\s",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("z","s",tuple)
    
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
       
    # replace ua to w                 
    tuples=re.findall("\wua\w+",ubah)
    ganti={}
    for tuple in tuples:
        ganti[tuple]=re.sub("ua","w",tuple)
        
    for i in ganti.keys():
             ubah=re.sub(i,ganti[i],ubah)
    
    ubah=re.sub("ie","i",ubah)
    
    ubah=re.sub("q|x","k",ubah)
    
    ubah=re.sub("b\s|b$","p ",ubah)
    #Kalo kitab
    ubah=re.sub("dh\s|dh$","t ",ubah)
    
    ubah=re.sub("oe","u",ubah)
    
    ubah=re.sub("nk\s|nk$","ng ",ubah)
    
    ubah=re.sub("aw\s|aw$","au ",ubah) 
    
    ubah=re.sub("\su\s"," kamu ",ubah)
    
    ubah=re.sub("\saj\s|\sja\s"," saja ",ubah)
    
    # cek kamus
    ubah1=ubah
    for word in ubah1.split():
        if word in kamus.keys():
            ubah = re.sub(word,kamus[word],ubah)
            #ubah = re.sub(kamus.keys(),kamus.values(), ubah)
    return ubah

def extraction_location(sentences):
    with open("D:/tasya/python/code/Geo-Tag/corpus/triger-word.csv") as file:
        reader = csv.reader(file)
        reader.next()
        corpus = []
        for column in reader:
            corpus.append(column[0])

    file_stopwords = csv.reader(open("D:/tasya/python/code/Geo-Tag/corpus/stopword_twitter.csv"))
    stopwords = []
    for column in file_stopwords:
        stopwords.append(column[0])

    file_stopwords_formal = csv.reader(open("D:/tasya/python/code/Geo-Tag/corpus/stopwords.csv"))
    for column in file_stopwords_formal:
        stopwords.append(column[0])
        
        
    list_of_words = sentences.split()
    location = []
    for word in list_of_words:
        if word in corpus:
            location.append(sentences.split(word)[0])
            location.append(sentences.split(word)[1])
            sentences = sentences.split(word)[1]
            
    for i, word in enumerate(location):
        if len(word.split()) <=2:
            word = word.replace(' ','')
            location.pop(i)
            location.insert(i,word)
            
    for i in range(len(location)):        
        if (2*i)+1 < len(location)-1:
            location.pop((2*i)+1)
            location.insert((2*i)+1,"")
    
    #stopwords
    for i, word0 in enumerate(location):        
        for word1 in word0.split():
            if word1 in stopwords:
                word0 = re.sub(word1,"",word0)
                location.pop(i)
                location.insert(i,word0)
                
    location_out = []
    for word in location:
        if len(word.split()) > 0:
            location_out.append(' '.join(word.split()))
       
    if len(location_out) == 0:
        location = "Location not found"
    else:
        location = location_out
    return location
    
def extraction_location_corpus(sentences):
    with open("D:/tasya/python/code/Geo-Tag/corpus/lokasilibrary.csv") as file:
        reader = csv.reader(file)
        reader.next()
        corpus_location = []
        for column in reader:
            corpus_location.append(column[0].lower())
            
    for word in sentences.split():
        if word in corpus_location:
            location = word
            #print location
        else:
            location = "Location not found"
    return location
    
def local_langdetect(sentence):
    with open("D:/tasya/Project/GeoTag-Pulse Lab/kamus bahasa daerah/kamus fix/kamus jawa tanpa terjemahan part1.txt") as file:
        jawa = file.read().split("\n")
    with open("D:/tasya/Project/GeoTag-Pulse Lab/kamus bahasa daerah/kamus fix/kamus minang tanpa terjemahan part1.txt") as file:
        minang = file.read().split("\n")
    with open("D:/tasya/Project/GeoTag-Pulse Lab/kamus bahasa daerah/kamus fix/kamus sunda tanpa terjemahan part1.txt") as file:
        sunda = file.read().split("\n")

    list_word = sentence.split()
    
    score_jawa = 0
    score_minang = 0
    score_sunda = 0
    for word in list_word:
        if word in jawa:
            score_jawa +=1
        if word in minang:
            score_minang += 1
        if word in sunda:
            score_sunda +=1
    
    if score_jawa > score_minang and score_jawa>score_sunda:
        lang = "jawa"
    elif score_minang > score_jawa and score_minang>score_sunda:
        lang = "minang"
    elif score_sunda > score_minang and score_sunda>score_jawa:
        lang = "sunda"
    elif score_jawa == score_sunda:
        lang = "sunda atau jawa"
    elif score_jawa ==score_minang:
        lang = "jawa atau minang"
    elif score_sunda == score_minang:
        lang = "sunda atau minang"
    else:
        lang = "Bahasa tidak terdeteksi"
        
    return lang
    
def ngram_sentences(sentences,nc):
    words=re.sub("\'","",sentences)
    words=re.sub("[^a-zA-Z]"," ",words)
    words=words.split()
    nw=len(words)
    ngr=nw-nc+1
    ng=[]
    if(nc>1):
        for i in range(ngr):
            ng.append(" ".join(words[i:(i+nc)]))
        return ng
    elif(nc==1):
        return words

if __name__ =='__main__':

    """
    Ekstraksi Lokasi based on tweet
    """
    sentences = "mau pergi skrg ke seminar di jkt coz udah mepEt bangedh"
    
    sentences = alay_normalizer(sentences)
    sentences = abbreviation(sentences)
    
    if extraction_location_corpus(sentences) != "Location not found":
        location = extraction_location_corpus(sentences)
    elif extraction_location(sentences) !="Location not found":
        location = extraction_location(sentences)
    else:
        location = local_langdetect(sentences)
    
    print location
    
    
    
    """
    get long lat from geocoder
    """
    address_longlat = []      
    for address in location:
        g = geocoder.google(address)
        list_longlat = g.latlnga
        list_longlat.insert(0,address)
        address_longlat.append(list_longlat)
    print address_longlat

    """
    get long lat from data POI using Ngram
    """

    with open("D:/tasya/python/code/Geo-Tag/corpus/sample-poi1.csv") as file:
        reader = csv.reader(file)
        #reader.next()
        corpus = []
        for row in reader:
            corpus.append(row[0])
            
    corpus_name = []
    for word in corpus:
        corpus_name.append(word.split(';')[0])
    address = []    
    G = NGram(corpus_name)
    G_latlng = NGram(corpus)
    for word in location:       
        out = G.search(word)
        out1 = G_latlng.append(out[0][0])
        address.append(out1[0][0])
