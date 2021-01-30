# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:52:32 2021

@author: SREERAM S
"""


import requests
from bs4 import BeautifulSoup


id = input(str("Enter Url:"))
print("URL: ",id)


request = requests.get(id)  #fetches the response

a = BeautifulSoup(request.text, "html.parser") #scrape the info from website
meta = a.find("meta", property = "og:description")

if meta is not None:
    a = meta.attrs['content']
    a = a.split()
    

profile = {}      #creating tuple for data
profile['Followers'] = a[0]
profile['Following'] = a[2]
profile['Posts'] = a[4]

print(profile)



