"""
import math
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from collections import defaultdict
from scipy.stats.stats import pearsonr
"""
import pandas as pd

df_tennis = pd.read_csv('prj_data/tennis_matches.csv', sep=',', index_col=0) 
#index_col=False indica di non usare la prima colonna come id, ma come dati
df_male = pd.read_csv('prj_data/male_players.csv', sep=',', index_col=False)
df_female = pd.read_csv('prj_data/female_players.csv', sep=',', index_col=False) 
"""
print(df_tennis.head(), end="\n\n") 
print(df_male.head(), end="\n\n") #only name - surname
print(df_female.head(), end="\n\n") #only name - surname

print(df_tennis.dtypes, end="\n\n")
print(df_tennis.info(), end="\n\n")

#print(df_tennis.columns)

for column in df_tennis.columns:
    if df_tennis[column].dtypes == "object":
        print("Distinct Values in "+str(column)+": \t", df_tennis[column].unique(), "\n")


#dice quale attributo presenta missing values
print(df_tennis.isnull().any(), end="\n\n")

#print(df_tennis.describe(), end="\n\n")

print(df_tennis.isnull().sum(axis = 0))
"""
wrong_names = []
wrong_surnames = []
wrong_sur = []

#ci sono cifre nei nomi/cognomi?
for row in df_male['name']:
    for i,caracter in enumerate(str(row)):
        if str(caracter).isdigit():
            wrong_names.append(str(row))
            break

#ci sono cifre nei nomi/cognomi?
for i,row in enumerate(df_male['surname']):
    for j,caracter in enumerate(str(row)):
        if str(caracter).isdigit():
            wrong_sur.append(str(row))
            wrong_surnames.append(i)
            break


new = []
for wrong in wrong_surnames:
    words = str(df_male['surname'][wrong]).split(" ")
    #se è =1 togliamo solo il numero dalla parola.
    if len(words)==1:
        for caracter in words[0]:
            if caracter.isdigit():
                words[0] = words[0].replace(str(caracter),"")
        new.append(words)
    
    
    #se >1 togliamo la seconda parola se ci sono numeri
    correct_surname = []
    if len(words)>1:
        for word in words:
            for char in word:
                if char.isdigit():
                    word = word.replace(str(caracter),"")
            #check se tutte le parole hanno len>1: se no toglile
            if len(word)==1:
                word = word.replace(word,"")
            word = word.strip()
    correct_surname.append(words)
    

print(df_male[df_male['name']=='Jose'], end="\n\n") 

print(wrong_names)
print("Not correct")
print(wrong_sur)
print("correct")
print(correct_surname)

#merge su nome e cognome 


#