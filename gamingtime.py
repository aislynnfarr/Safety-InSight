#WARNING: this sucks!
#"C:\Users\baked\Desktop\Organization\Other\smu\testsmutwo.py"
import streamlit
import streamlit as st
import os.path
import pandas as pd
import numpy as np
import csv
temp = 0
st.title("Welcome to Saftey InSight!")
st.header("Current Building: Hotel_1")
listing = []
def workorder():
  fix_req = line[7]
  anum = float("1." + str(fix_req))
  return anum
def repairs(ord):
  hour_work = line[6]
  rep = line[8]
  bnum = 0
  if int(rep) - 1 >= 0:
    bnum = 1 + ((int(int(hour_work) / (int(rep)*2)/1000))/10)
    return bnum
  elif int(rep) > ord:
    return 1
  else:
    return 5
def dateop():
  redate = line[9].split("/")
  cnum = abs(int(redate[-1]) - 2024)
  dnum =  1 + (cnum * (int(redate[0]) / 10))
  return dnum
def fixrec():
  fix_rec = int(line[7])
  fnum = 1 + fix_rec
  return fnum
def startdate():
  stdt = line[4].split("/")
  gnum = 1 + ((abs(int(stdt[-1]) - 2023)))
  return gnum
def calcing(ord, sta, fix, rep,oper):
  global temp
  a_id = line[0]
  a_type = line[1]
  l_floor = line[2]
  room_num = line[3]
  manu = line[5]
  
  finncal = finn(finorder, finstart, finfix, finrep, finoper)
  finncal, findate = finncal[0], finncal[1]
  fin = str(line[0]) + "| " + str(line[1])+ " . Current risk of malfunction (100 point scale): " + str(finncal) + ". Projected for matinence in " +str(findate)+ " days. Floor and Room number: " + str(room_num) + " on floor " + str(l_floor) + ". Manufacturer Name: " + str(manu) +"."
  #print(fin)
  st.divider()
  st.write(str(fin))


  #if int(line[0]) >1:

    ## listing.insert(0,str(line[0]) + "| Current risk of malfunction (100 point scale): " + str(finncal) + ". Projected for matinence in " +str(findate)+ " days. Floor and Room number: " + str(room_num) + " on floor " + str(l_floor) + ". Manufacturer Name: " + str(manu) +".")
      
  listing.append(str(line[0]) + "- Current risk of malfunction (100 point scale): " + str(finncal) + " . Projected for matinence in " +str(findate)+ " days. Floor and Room number: " + str(room_num) + " on floor " + str(l_floor) + ". Manufacturer Name: " + str(manu) +".")
  return finncal
def finn(ord, sta, fix, rep,oper):
  findate = 0
  ren = int(line[8]) + 1
  
  #CUT
  caldate = 0
  if ren > fix or ren == fix:
    findate += 6
    caldate += 2
  elif (ren == 0 and fix > 1) or (fix >= 2*ren):
    findate +2
    caldate += 6
  else:
    findate += 4
    caldate += 4
  #findate = int(float(str("%.2f"%((10 * ren * findate / (fix))))))
  finncal = int(float("%.2f"%((50 + (ord * rep * ord *oper*caldate))))/2)
  if finncal > 100:
    finncal = 100
  findate = int((101 - finncal) * 2.3)
  return finncal, findate
def yeah(m):
  return len(m)
  
  
#calling!
with open(r"C:\\Users\\baked\Desktop\\Organization\\CSVfiles\\Dataset_-_CBRE_Challenge_-_HackSMU_2023.csv", 'r') as file:
  t_csv = csv.reader(file)
  for line in t_csv:
    finorder = workorder()
    
    finstart = startdate()
    manu = line[5]
    finfix = fixrec()
    finrep = repairs(finorder)
    finoper = dateop()
    
    rening = calcing(finorder, finstart, finfix, finrep, finoper)
    finn(finorder, finstart, finfix, finrep, finoper)
    
    #listing.sort(key=yeah)

    
    #calcing(finorder, finstart, finfix, finrep, finoper)
    #latest_d = line[9]
#num = listing.count("")
#for w in num:
#    pass
#listtwo = []
#for type in listing:
#    ty = type.split(" ")
#    nu = ty[0]
#    ya = int(ty[8]), "is the current risk factor. " + ty[9] +  ty[10] +  ty[11] +  ty[9] +  ty[9] + 
#    listtwo.append(ya)
#listtwo.sort(reverse = True)
#print(listtwo)

