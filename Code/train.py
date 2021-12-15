# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:35:18 2021

@author: Mirror Craze
"""

from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer(binary=False) # we cound ignore binary=False argument since it is default
csvList = ["train2"]

def sepSubject(df):
    for index, row in df.iterrows():
        if(type(row["subject"]) == float):
            continue
        #print(row["subject"])
        titleArr = row["subject"].split(",")
        #print(titleArr)
        newDF = row * len(titleArr)
        if len(titleArr) ==1:
            continue
        df = df.drop(index)
        for sub in titleArr:
            #print(sub)
            newRow = row
            newRow["subject"] = sub.strip()
            df = df.append(newRow)
    return df
def convertYVal(df):
    y = df["label"].to_frame().copy()
    mapping = {'true' : 0,'mostly-true':1,'half-true':2,'barely-true':3,'false':4,'pants-fire':5}
   
    
    vec = CountVectorizer(binary=False) # we cound ignore binary=False argument since it is default
    vec.fit(df["statement"].astype(str))
    st = lambda s : str(s)
    vocab_key = []
    for col in df:
        df[col] = df[col].astype('category')
    df = df.append(pd.DataFrame(vec.transform(df["statement"].astype(str)).toarray(), columns = vec.vocabulary_.keys()))
    df = df.dropna()
    y = y.replace({"label":mapping})
    print("append success")
    del df["justification"]
    del df["speaker"]
    del df["context"]
    del df["barelyTrueCount"]
    del df["falseCount"]
    del df["halfTrueCount"]
    del df["mostlyTrueCount"]
    del df["pantsCount"]
    del df["label"]
    #df = df.apply(LabelEncoder().fit_transform)
    
    x = df
    return x,y


#main
for csvName in csvList:
    #fileName = os.path.join('dataset',csvName)
    fileName = 'Dataset\\' + csvName + '.csv'
    print(fileName)
    #df = pd.read_csv(fileName,header = None,sep = "\t",names = ["ID","label","statement","subject","speaker","speakerJob","stateInfo","party","barelyTrueCount","falseCount","halfTrueCount","mostlyTrueCount","pantsCount","context","justification"])
    df = pd.read_csv(fileName)
    #for col in df:
    #    print ("{} : {}".format(col,df[col].nunique()))
        
    #    amount = df[col].value_counts()
    #    print(amount)
    
    #print(df.describe())
    #df = df.drop("ID",1)
    #df = df.drop("statement",1)
    #df = df.drop("justification",1)
    #df = df.drop("speaker",1)
    #df = df.drop("context",1)
    #pd.set_option('max_columns', 10)
    #df = sepSubject(df)
    print("Seperate success")
    df = df.dropna()
    df = df.iloc[: , 1:]
    x,y = convertYVal(df)
    print("Convert Success")
    
    print(x)
    print(y)
    for col in x:
        print(x[col].dtypes)
    clf = AdaBoostClassifier(n_estimators = 100,random_state=0)
    print("Fit successful")
    clf.fit(x,y)
    fileNameVal = 'Dataset\\' + 'test2.tsv'
    dfVal = pd.read_csv(fileNameVal,header = None,sep = "\t",names = ["ID","label","statement","subject","speaker","speakerJob","stateInfo","party","barelyTrueCount","falseCount","halfTrueCount","mostlyTrueCount","pantsCount","context","justification"])
    dfVal = sepSubject(dfVal)
    print("Seperate success")
    dfVal = dfVal.fillna(method = "bfill")
    del dfVal["ID"]
    dfValX, dfValY = convertYVal(dfVal)
    print("Convert Success")
    print(dfValX,dfValY)
    print(clf.score(dfValX,dfValY))
    #print(df.head())
    #df = sepSubject(df)
    
        
    #print(df.head())
    #df.to_csv(r"Dataset\\"+csvName+'.csv',index = True)
