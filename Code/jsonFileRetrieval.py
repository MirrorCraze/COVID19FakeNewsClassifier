# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 21:30:29 2021

@author: Mirror Craze
"""

import urllib
import pandas as pd

beginURL = "http://www.politifact.com//api/v/2/statement/"
endURL = "?format=json"

csvList = ["train","test","valid"]

for csvName in csvList:
    fileName = csvName + ".tsv"
    print(fileName)
    df = pd.read_csv(fileName,header = None,sep = "\t",names = ["ID","label","statement","subject","speaker","speakerJob","stateInfo","party","barelyTrueCount","falseCount","halfTrueCount","mostlyTrueCount","pantsCount","context"])
    for id in df["ID"]:
        urllib.request.urlretrieve(beginURL + id + endURL)
    
    