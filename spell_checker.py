# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:29:38 2021

@author: SREERAM S
"""

from textblob import TextBlob
import nltk
nltk.download('punkt')


ip = input("Enter Sentence \n")
print("Sentence Entered : ",ip)
wordlist = ip.split()
corrected = []

for word in wordlist:
    corrected.append(TextBlob(word))

print("Corrected Sentence Is: ")
for e in corrected:
    print(str(e.correct()), end=" ")   