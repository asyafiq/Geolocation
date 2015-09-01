# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:27:22 2015

@author: 1152
"""
import csv
import re

def extraction_location(sentences):
    with open("D:/tasya/python/code/Geo-Tag/corpus/triger-word.csv") as file:
        reader = csv.reader(file)
        reader.next()
        corpus = []
        for column in reader:
            corpus.append(column[0])
    #print corpus
    file_stopwords = csv.reader(open("D:/tasya/python/code/Geo-Tag/corpus/stopword_twitter.csv"))
    stopwords = []
    for column in file_stopwords:
        stopwords.append(column[0])
    #print stopwords
    """
    sentences = "gw habis dari jakarta barat nih"
    
    location = []
    for word in sentences.split():
        if word in corpus:
            location.append(''.join(re.findall(word+"\s[a-zA-Z0-9].*",sentences)))
            #break
    print location
    """
    list_of_words = sentences.split()
    location = []
    for word in list_of_words:
        if word in corpus:
            word_loc = sentences.split(word)[0]
            location.append(word_loc)
            sentences = ' '.join(sentences.split(word))
            sentences = sentences.replace(word_loc,"",sentences)
            #location = ''.join(re.findall(word+"\s[a-zA-Z0-9].*",sentences))
            #print location
            #location = ''.join(re.sub(word,"",location))
        #else:
         #   location = "Location not found"
            
    #print location
    #if location != "Location not found":
    
    for word1 in location.split():
        if word1 in stopwords:
            #print word1
            location = re.sub(word1,"",location)
            #print location
            
    if len(location) == 0:
        location = "Location not found"
    else:
        location = location
    return ' '.join(location.split())
    
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
    

if __name__=="__main__":
    print extraction_location("mau mepet banget")