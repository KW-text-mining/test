import requests
import json
import time
import csv
import sys
import csv
 
f = open('data.csv','r')
rdr = csv.reader(f)
datalist=[]
for line in rdr:
    datalist=line

f = open('modelData.csv','w', newline='')
wr = csv.writer(f)

cnt=0
for i in datalist[:10]:
    print(i,int(i))
    cnt+=1
    url="https://api.thingiverse.com/things/"+str(int(i))+"?access_token=009771366fb227909df098e04303677c"
    print(url)
    response = requests.get("https://api.thingiverse.com/things/"+i+"?access_token=009771366fb227909df098e04303677c")
    data=response.json()
    
    try:
        #print(data['creator'])
        params={}
        params["id"]=data["id"]

        params["name"]=data["name"]

        

        
        
        wr.writerow([params['id'], params['name']])

        print(i,"success",cnt)
        
    except Exception as e:
        print(i,"fail",e)
        
f.close()







# '''
# 3D Printing:3d-printer-accessories
# 3D Printing:3d-printer-extruders
# 3D Printing:3d-printer-parts
# 3D Printing:3d-printers
# 3D Printing:3d-printing-tests
# Art:coins-and-badges
# Art:interactive-art
# Art:math-art
# Art:scans-and-replicas
# Art:sculptures
# Art:signs-and-logos
# Fashion:accessories
# Fashion:bracelets
# Fashion:costume
# Fashion:earrings
# Fashion:glasses
# Fashion:jewelry
# Fashion:keychains
# Fashion:rings
# Gadgets:audio
# Gadgets:camera
# Gadgets:computer
# Gadgets:mobile-phone
# Gadgets:tablet
# Gadgets:video-games
# Hobby:automotive
# Hobby:diy
# Hobby:electronics
# Hobby:music
# Hobby:rc-vehicles
# Hobby:robotics
# Hobby:sport-and-outdoors
# Household:bathroom
# Household:containers
# Household:decor
# Household:household
# Household:supplies
# Household:kitchen-and-dining
# Household:office-organization
# Household:outdoors-and-garden
# Household:pets
# Learning:biology
# Learning:engineering
# Learning:math
# Learning:physics-and-astronomy
# Models:animals
# Models:building-and-structures
# Models:creatures
# Models:food-and-drinks
# Models:model-furniture
# Models:model-robots
# Models:people
# Models:props
# Models:vehicles
# Tools:hand-tools
# Tools:machine-tools
# Tools:tool-holders-and-boxes
# Toys & Games:chess
# Toys & Games:construction-toys
# Toys & Games:dice
# Toys & Games:games
# Toys & Games:mechanical-toys
# Toys & Games:playsets
# Toys & Games:puzzles
# Toys & Games:toy-and-game-accessories
# '''