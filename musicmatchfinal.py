# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 21:31:30 2021

@author: kwonj

v"""

import pandas as pd
import numpy

def standardize(columnName, df):
    dfScaled = df.copy()
    column = columnName
    dfScaled[column] = (dfScaled[column] - dfScaled[column].min()) / (dfScaled[column].max() - dfScaled[column].min())    
      
    return dfScaled
    
        
print("Welcome to the song suggester! Here, you will be able to enter a song and magically be shown any number of similar songs you like! Enjoy!")
print("\nThe default attributes automatically used for your recommendations are:\n")
filename = "tracks1.csv"
dataFile = pd.read_csv(filename, usecols = range(2,10))
for name in dataFile.columns:
    print(name, end = "    ")
print("\n")
    
print("\nWhat is the name of your song?")
df = pd.read_csv(filename)
user_input = input()
value = df[df['name'] == user_input]

dfScaled = standardize('loudness', df)
dfFinal = standardize('tempo', dfScaled)
dataFileScaled = standardize('loudness', dataFile)
dataFileFinal = standardize('tempo', dataFileScaled)

print(value[['name','artists']])
print("\n")
print("Please input the leftmost number of the song you want to use.")
index = int(input())
song = dfFinal.iloc[index]
print(song)

print("\nHow many recommendations would you like?")
k = int(input())

songstats = dataFileFinal.iloc[index]
songarray = songstats.to_numpy()
rows = dataFileFinal.shape[0]
allrows = []
for i in range(rows):
    row = dataFileFinal.iloc[i].to_numpy()
    allrows.append(row)

distances = []
for row in allrows:
    dims = []
    for i in range(len(row)):
        dim = (float(row[i]) - float(songarray[i]))**2 
        dims.append(dim)
    distance = (sum(dims))**0.5
    distances.append(distance)
distances.pop(index)

songrecs = []
while len(songrecs) < k:
    songrec = dfFinal.iloc[distances.index(min(distances))]
    songrecs.append([songrec[0], songrec[1]])
    distances.pop(distances.index(min(distances)))
              

print("The recommendations are:")
for songrec in songrecs:
    print(songrec[0], "by", songrec[1])