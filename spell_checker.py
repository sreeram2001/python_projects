# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:29:38 2021

@author: SREERAM S
"""

from textblob import TextBlob





ip = input("Enter Sentence")
wordlist = ip.strip()
corrected = []
print(wordlist)
for word in wordlist:
    corrected.append(TextBlob(word))
for e in corrected:
    print(e.correct(), end=" ")

