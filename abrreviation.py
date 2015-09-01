# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:02:33 2015

@author: 1152
"""
import csv
import re

def abbreviation(sentences):
    corpus = csv.reader(open("D:/tasya/python/code/Geo-Tag/corpus/abbreviation.csv"))
    dictionary={}
    for row in corpus:
        dictionary[row[0]]=row[1]
   
    for word in sentences.split():
        if word in dictionary.keys():
            sentences = re.sub(word,dictionary[word],sentences)
    return sentences
    
if __name__=='__main__':
    kalimat = "gw lagi d jln nih"
    print abbreviation(kalimat)