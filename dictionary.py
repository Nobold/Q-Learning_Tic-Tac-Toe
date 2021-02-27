import json
import random as r
import ast

dictionary = {}

def init():
   global dictionary
   with open('dict.txt') as f: 
       data = f.read()
   dictionary = ast.literal_eval(data) 

def save():   
   string = str(dictionary)
   with open('dict.txt', 'w') as f:
       f.write(string)

def add(key):
   dictionary[key] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
   #dictionary[key] = [r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1), r.uniform(-1, 1)]

def read(key, field):
   try:
      dictionary[key][field]
   except:
       add(key)

   return dictionary[key][field]

def change(key, field, value):
   try:
      dictionary[key]
   except:
      add(key)
   dictionary[key][field] = value

def highest(key, Try):
   try:
      dictionary[key]
   except:
      add(key)

   mittupel = []
   i = 0
   for zahlen in dictionary[key]:
      mittupel.append([zahlen, i])
      i = i + 1

   mittupel.sort(reverse=True)

   return mittupel[Try][1]
      
      
   #i = [-100, 0]
   #c = 0
   #for feld in dictionary[key]:
    #  if feld > i[0]:
     #    i = [feld, c]
      #c = c + 1

   #durchlauf = 0
   #while durchlauf < Try:
    #  c = 0
     # h = [-100, 0]
      #for feld in dictionary[key]:
       #  if h[0] < feld:
        #    if feld < i[0]:
         #      h = [feld, c]
         #c = c + 1
   
      #i = h.copy()
      #durchlauf = durchlauf + 1

   #print("Vor return")
      
   #return i[1]

#print(highest("[0, 1, 2, 3, 4, 5, 6, 7, 'O']", 1))

