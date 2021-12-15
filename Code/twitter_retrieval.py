# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:06:35 2021

@author: Mirror Craze
"""
import pandas as pd

fake = pd.read_csv("https://raw.githubusercontent.com/cuilimeng/CoAID/master/05-01-2020/ClaimFakeCOVID-19_tweets.csv")
real = pd.read_csv("https://raw.githubusercontent.com/cuilimeng/CoAID/master/05-01-2020/ClaimRealCOVID-19_tweets.csv")

fake["label"] = "fake"
real["label"] = "real"
df = pd.concat([fake, real])
df["text"] = "None"

import requests
from bs4 import BeautifulSoup

for i, row in df.iterrows():
  id = row.tweet_id
  url = "https://mobile.twitter.com/Richx183/status/" + str(id)
  print(url)
  body = requests.get(url)
  body = BeautifulSoup(body.content, 'html.parser')
  #print(body)
  for el in body.find_all(("div"), attrs={"data-id":str(id)}):
    #print(body)
    text = ""
    #print(el.div)
    if(el.div == None):
        continue
    for x in el.div.contents:
      x = str(x)
      #print(x)
      if "class=" not in x:
        text += x
      text = text.strip()
      print(text)
    #print("SIZE" + str(df.size))
    df.at[i, "text"] = text
    
df = df.drop(df[df.text == "None"].index) #drop unnsuccessful queries

df.head()