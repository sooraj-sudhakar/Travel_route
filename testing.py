#!/usr/bin/env python3
# -*- coding: utf-8 -*-

path = "<project-folder-path>"

# Dependancies installation and library loading
import os
import time
import json
import pandas as pd
os.chdir(path)
start = time.time()

input_path=path+"/dataset/demo-rasa.json"

#nltk.download('sentiwordnet')

# Load the Packages
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Returns the directory the model is stored in (Creat a folder to store model in)
folder=os.listdir(path+"/projects/default")[0]
model_directory = path+'/projects/default/'+folder

import spacy
nlp = spacy.load('en')

from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory)

print("\nPrediction for a single input..")
print("\nThe sample sentence is : There was less restuarants on the way from Kottayam to Kozhikode,the road was broken and then traffic was less.")

# Prediction of Intent
out=interpreter.parse(u"There was less restuarants on the way from Kottayam to Kozhikode,the road was broken and then traffic was less . ")
print("\n")
print(out)
print("\nExtracting the entities and difficulty score calculation for test dataset..")

# Loading DataSet
# since we are not having a seperate test dataset we will be using a portion of
# input data
with open(input_path,'r') as f:
    datastore=json.load(f)
data=datastore['rasa_nlu_data']['common_examples']
database=pd.DataFrame(columns=['Input_text','road_condition','traffic_condition','scenary_data','Difficulty_score'])
for i in range(0,len(data)):
    temp=data[i]['text']
    database.loc[i,"Input_text"]=temp
    out=interpreter.parse(temp)
    for j in range(0,len(out['entities'])):
        try:
            database.loc[i,out['entities'][j]['entity']]=out['entities'][j]['value']
        except:
            print("")
        
database=database[['Input_text', 'road_condition', 'traffic_condition', 'scenary_data',
                   'weather_codition', 'attractions','Difficulty_score']]

database=database.fillna(0)
# Difficulty score generation can be done by checking the word polarity using 
# nltk sentiwordnet. Postive words will have a positive sentiment value    

from nltk.corpus import sentiwordnet as swn

def score_gen(List):
    out_list=[]
    Pscore=[]
    Nscore=[]

    for i in range(0,len(List)):
        try:
            if(List[i]!=0):
                temp=List[i].split()
                for j in range(0,len(temp)):
                    a=swn.senti_synsets(temp[j])
                    tmp=list(a)
                    if(len(tmp)!=0):
                        a1=tmp[0]
                        pscore=a1.pos_score()
                        nscore=a1.neg_score()
                        Pscore.append(pscore)
                        Nscore.append(nscore)
                pscore=sum(Pscore)/len(Pscore)
                nscore=sum(Nscore)/len(Nscore)
                if(pscore != 0.0):
                    out_list.append(pscore)
                else:
                    out_list.append(nscore)
            else:
                out_list.append(0.0)
        except:
            print("")
    return out_list

road_score=score_gen(list(database['road_condition']))
road_score.append(0.0)
traffic_score=score_gen(list(database['traffic_condition']))
scenary_score=score_gen(list(database['attractions']))
weather_score=score_gen(list(database['weather_codition']))


# Getting the average of all the different scores. All the list have same length

total_score=[]
for k in range(0,len(road_score)):
    total_score.append((road_score[k]+traffic_score[k]+scenary_score[k]+weather_score[k])*5)

database['Difficulty_score']=total_score

# Saving the dataframe as csv
database.to_csv(path+"/Entity_Db.csv")