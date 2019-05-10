#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:05:23 2019

@author: sooraj
"""

path= "<project-folder-path>"

district_list=["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam",
               "Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta",
               "Thiruvananthapuram","Thrissur","Wayanad"]

##################
# Road conditions 
#################

# Eg- the road from trivandrum to thrissur is very smooth
# Roads were smooth while driving from trivandrum to thrissur

input_road=[]
road_conditions=["smooth","very smooth","broken","bumpy","easy going","bad"]

try:
    #for i in range(0,len(district_list)):
    for j in range(0,len(road_conditions)):
        #road_1="The road from "+district_list[i]+" to "+district_list[i+1]+" are "+road_conditions[j]
        road_1="The roads are "+road_conditions[j]
        input_road.append(road_1)
        #road_2="Roads were "+road_conditions[j]+" while driving from "+district_list[i]+" to "+district_list[i+1]
        road_2="Roads were "+road_conditions[j]
        input_road.append(road_2)
except:
    print("")
    
# writing the output to the text file
with open(path+'/road_data.txt','w') as f:
    for item in input_road:
        f.write("%s\n" % item)
    
#####################
# Traffic conditions 
####################

# Eg- the traffic from trivandrum to thrissur have heavy traffic 
# Traffic was smooth while driving from trivandrum to thrissur

input_road=[]
traffic_conditions=["heavy","very smooth","crawling"]

try:
    #for i in range(0,len(district_list)):
    for j in range(0,len(traffic_conditions)):
        #road_1="The traffic from "+district_list[i]+" to "+district_list[i+1]+" is "+traffic_conditions[j]
        road_1="The traffic from is "+traffic_conditions[j]
        input_road.append(road_1)
        #road_2="Traffic was "+traffic_conditions[j]+" while driving from "+district_list[i]+" to "+district_list[i+1]
        road_2="On route the traffic was "+traffic_conditions[j]
        input_road.append(road_2)
except:
    print("")
    
    
# writing the output to the text file
with open(path+'/traffic_data.txt','w') as f:
    for item in input_road:
        f.write("%s\n" % item)
        
#####################
# Scenary conditions 
####################

# Eg- There is lot of resturants on the journey from trivandrum to thrissur
# There is amusement parks

input_road=[]
scenary_conditions=["lot of","less","few"]
scenary_conditions1=["amusement parks","forest","no scenary"]

try:
    #for i in range(0,len(district_list)):
    for j in range(0,len(scenary_conditions)):
        #road_1="There is "+scenary_conditions[j]+" resturants from "+district_list[i]+" to "+district_list[i+1]
        road_1="There is "+scenary_conditions[j]+" resturants"
        input_road.append(road_1)
        #road_2="On the way from "+district_list[i]+" to "+district_list[i+1]+" there is "+scenary_conditions1[j]
        road_2="While travelling there is "+scenary_conditions1[j]
        input_road.append(road_2)
except:
    print("")
    

# writing the output to the text file
with open(path+'/scenary_data.txt','w') as f:
    for item in input_road:
        f.write("%s\n" % item)
        
#####################
# full conditions 
####################

# Eg- On the way from trivandrum to thrissur, the road was smooth and the traffic was less. There was amusement parks on the way
# There is amusement parks

input_road=[]
road_conditions=["smooth","very smooth","broken","bumpy","easy going","bad"]
traffic_conditions=["heavy","very smooth","crawling","less"]
scenary_conditions=["lot of","less","few"]
scenary_conditions1=["amusement parks","forest","no scenary"]

try:
    #for i in range(0,len(district_list)):
    for j in range(0,len(road_conditions)):
        for k in range(0,len(traffic_conditions)):
            for l in range(0,len(scenary_conditions)):
                #road_1="On the way from "+district_list[i]+" to "+district_list[i+1]+",the road was "+road_conditions[j]+" and then traffic was "+traffic_conditions[k]+" .There was "+scenary_conditions[l]+" restuarants on the way"
                road_1="On the way from the road was "+road_conditions[j]+" and then traffic was "+traffic_conditions[k]+" .There was "+scenary_conditions[l]+" restuarants on the way"
                input_road.append(road_1)
except:
    print("")
    

# writing the output to the text file
with open(path+'/full_conditions_data.txt','w') as f:
    for item in input_road:
        f.write("%s\n" % item)