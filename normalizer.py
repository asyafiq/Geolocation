# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:16:43 2015

@author: 1157

karena alay sangat membingungkan

Pre-Processing
"""

import re
import csv

def alay_normalizer(kalimat):
    #kamusalay
    kamusnya = csv.reader(open("d:/geo/doc/kamusalay.csv"))
    kamus={}
    for row in kamusnya:
        kamus[row[0]]=row[1]
    
    print kamus
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
    
    #ubah=re.sub("b\s|b$","p ",ubah)
    
    ubah=re.sub("dh\s|dh$","t ",ubah)
    
    ubah=re.sub("oe","u",ubah)
    
    ubah=re.sub("nk\s|nk$","ng ",ubah)
    
    ubah=re.sub("aw\s|aw$","au ",ubah) 
    
    ubah=re.sub("\su\s|\su"," kamu ",ubah)
    
    ubah=re.sub("\saj\s|\sja"," saja ",ubah)
    
    # cek kamus
    ubah1=ubah
    for word in ubah1.split():
        if word in kamus.keys():
            ubah = re.sub(word,kamus[word],ubah)
            #ubah = re.sub(kamus.keys(),kamus.values(), ubah)
    return ubah
    
if __name__=='__main___':
    # input
    filenya = open("d:/geo/doc/tweetcoba.csv","r")
    kalimat = filenya.read()
    filenya.close()
    print kalimat
    
    with open("d:/geo/doc/tweetcoba.csv") as file:
        tweet = []
        reader = csv.reader(file)
        for column in reader:
            tweet.append(column[0])

    file=open("D:/outputnyaaa.txt","w")
    for word in tweet:
        word_new = alay_normalizer(word)
        file.write(word_new+"\n")
    #output
    file.close()