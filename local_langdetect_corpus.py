# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:37:11 2015

@author: 1152
"""

def local_langdetect(sentence):
    with open("D:/tasya/Project/GeoTag-Pulse Lab/kamus bahasa daerah/kamus fix/kamus jawa tanpa terjemahan part1.txt") as file:
        jawa = file.read().split("\n")
    with open("D:/tasya/Project/GeoTag-Pulse Lab/kamus bahasa daerah/kamus fix/kamus minang tanpa terjemahan part1.txt") as file:
        minang = file.read().split("\n")
    with open("D:/tasya/Project/GeoTag-Pulse Lab/kamus bahasa daerah/kamus fix/kamus sunda tanpa terjemahan part1.txt") as file:
        sunda = file.read().split("\n")
    #print sunda
    list_word = sentence.split()
    
    score_jawa = 0
    score_minang = 0
    score_sunda = 0
    for word in list_word:
        if word in jawa:
            #print word+" jawa"
            #lang = "jawa"
            score_jawa +=1
            #break
        if word in minang:
            #print word +" minang"
            #lang = "minang"
            score_minang += 1
            #break
        if word in sunda:
            #print word+" sunda"
            #lang = "sunda"
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
        
    return lang,score_jawa,score_minang,score_sunda
        
if __name__ == '__main__':
    print local_langdetect("aku pengen mangan neng angkringan tugu")
    