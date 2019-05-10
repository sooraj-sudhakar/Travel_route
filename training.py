#!/usr/bin/env python3
# -*- coding: utf-8 -*-

path = "<project-folder-path>"

# Dependancies installation and library loading
import os
import time
import json
os.chdir(path)
start = time.time()
#os.system("pip install -r /home/sooraj/Desktop/Grapes/Travel_route/requirements.txt")
#os.system("pip install rasa_nlu")
#os.system("pip install rasa_nlu[spacy]")
#os.system("python -m spacy download en_core_web_md")import
#os.system("python -m spacy link en_core_web_md en")
#os.system("pip install nodejs")
#os.system("npm i -g rasa-nlu-trainer")

# Load the Packages
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Loading DataSet
print("\nLoading the training tagged json data..")
input_path=path+"/dataset/demo-rasa.json"
train_data = load_data(input_path)

# Config Backend using Sklearn and Spacy
trainer = Trainer(config.load("config_spacy.yml"))

# Training Data
print("\nStarting the training phase..")
trainer.train(train_data)

# Returns the directory the model is stored in (Creat a folder to store model in)
model_directory = trainer.persist(path+'/projects')

import spacy
nlp = spacy.load('en')

from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory)
print("\nThe trained models saved in the projects directory !")
end = time.time()
print("\nTotal time in sec taken for training ",end - start)

# Prediction of Intent
print("\nTesting a sample input : There was less restuarants on the way from Kottayam to Kozhikode,the road was broken and then traffic was less . ")
time.sleep(2)
print("\n")
out=interpreter.parse(u"There was less restuarants on the way from Kottayam to Kozhikode,the road was broken and then traffic was less . ")
print(out)

# Calculation of model accuracy
'''
    Accuracy = (Number of correct predictions)/total number of class
'''

with open(input_path,'r') as f:
    datastore=json.load(f)
print("\nTaking 150 samples from the test data to calculate accuracy..")

# Calculating the total number of entities for the 200 test data
entity_sum=[]
for i in range(0,150):
    count=len(datastore['rasa_nlu_data']['common_examples'][i]['entities'])
    entity_sum.append(count)

score=[]
entity_values=[]
rasa_values=[]
for i in range(0,150):
    in_data=datastore['rasa_nlu_data']['common_examples'][i]['text']
    in_classes=datastore['rasa_nlu_data']['common_examples'][i]['entities']
    for j in range(0,len(in_classes)):
        entity_values.append(in_classes[j]['value'])
    rasa_out=interpreter.parse(in_data)
    for k in range(0,len(rasa_out['entities'])):
        rasa_values.append(rasa_out['entities'][k]['value'])
        
entity_values=[x.strip() for x in entity_values]
rasa_values=[x.strip() for x in rasa_values]
entity_values.sort()
rasa_values.sort()
print("\nThe total number of unique entities are ",len(entity_values))
count=len(entity_values)

# Checking for matching entity values in the input and rasa predicted
matching=0
for i in range(0,len(rasa_values)):
    if(rasa_values[i] in entity_values):
        matching=matching+1
print("\nTotal number of matching entites with rasa predicted ",matching)
accuracy = (matching/count)*100
print("\nThe accuracy of the model is "+str(accuracy)+"%")

    

