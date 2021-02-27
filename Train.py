import Tic_Tac_Toe as game
import dictionary
import random

def dauer(wiederholungen):
    x = 0
    dictionary.init()
    while x < wiederholungen:
        print(x)
        dictionary.change("Info", 0, 1)
        Spiel(x, wiederholungen)
        x = x + 1
        dictionary.save()
    
def anpassung(status, typ):
    print(status["sieger"])
    gesamtdurchlaeufe = dictionary.read("Info", 0)
    
    alpha = 0.01
    gamma = 0.9
    reward = 1

    if status["sieger"] == "O":
        reward = -1 * reward


    #print(status["WegX"])
    
    if status["sieger"] != "none" and status["sieger"] != "draw":
        if typ == 0:
            i = 0
            for element in status["WegX"]:
                Qalt = dictionary.read(str(status["WegX"][i][0]), status["WegX"][i][1])

                if i > 0:
            
                    maxFeld = dictionary.highest(str(status["WegX"][i-1][0]), 0)    
                    Qmax = dictionary.read(str(status["WegX"][i-1][0]), maxFeld)

                    Qneu = (1-alpha) * Qalt + alpha * (reward + gamma * Qmax)


                else:
                    Qneu = (1-alpha) * Qalt + alpha * reward

                #print(Qneu)
                dictionary.change(str(status["WegX"][i][0]), status["WegX"][i][1], Qneu)
                #reward = reward / 2
                i = i + 1

        i = 0

        for element in status["WegO"]:
            Qalt = dictionary.read(str(status["WegO"][i][0]), status["WegO"][i][1])

            if i > 0:
            
                maxFeld = dictionary.highest(str(status["WegO"][i-1][0]), 0)    
                Qmax = dictionary.read(str(status["WegO"][i-1][0]), maxFeld)

                Qneu = (1-alpha) * Qalt + alpha * (-1 * reward + gamma * Qmax)

            else:
                Qneu = (1-alpha) * Qalt + alpha * -1 * reward
                
            print(Qneu)

            dictionary.change(str(status["WegO"][i][0]), status["WegO"][i][1], Qneu)
            #reward = reward / 2
            i = i + 1
        
        
    #if status["sieger"] == "X":
        
        
        #for element in status["Weg"]:
            #dictionary.change(str(status["Weg"][i][0]), status["Weg"][i][1], bewertung)
            
            #bewertung = bewertung / 2
            #i = i + 1
    #if status["sieger"] == "O":
        #print("Niederlage")
        #bewertung = -(0.9999 ** gesamtdurchlaeufe)
        #i = 0
        #for element in status["Weg"]:
            #dictionary.change(str(status["Weg"][i][0]), status["Weg"][i][1], bewertung)
            #print(status["Weg"][i], bewertung, i)
            #print(dictionary.read(str(status["Weg"][i][0]), status["Weg"][i][1]))
            #bewertung = bewertung / 2
            #i = i + 1
   
        
        
    
def createState(status):
   return str(status["board"])

def Spiel(spiele, wiederholungen):
    status = {"board": [0, 1, 2, 3, 4, 5, 6, 7, 8], "sieger": "none", "spieler": random.choice(("X", "O")), "WegX": [], "WegO": []}
    while game.check_end(status) == "none":
      if status["spieler"] == "X":
         entscheidung = False
         if random.randint(0, 30) == 1:
            while entscheidung == False:
                Wahl = random.randint(0,8)
                if game.belegt(status, Wahl) == False:
                   status["WegX"].insert(0, [createState(status), Wahl])
                   status["board"][Wahl] = "X"
                   entscheidung = True
                   status["spieler"] = "O"
         else: 
            while entscheidung == False:
                Wahl = game.Agent(status)
                #print(Wahl, "x; ")
                if game.belegt(status, Wahl) == False:
                   status["WegX"].insert(0, [createState(status), Wahl])
                   status["board"][Wahl] = "X"
                   entscheidung = True
                   status["spieler"] = "O"
               
      else:
         entscheidung = False
         while entscheidung == False:
            #Wahl = random.randint(0,8)
            Wahl = game.Agent(status)
            if game.belegt(status, Wahl) == False:
               status["WegO"].insert(0, [createState(status), Wahl])
               status["board"][Wahl] = "O"
               entscheidung = True
               status["spieler"] = "X"
    status["sieger"] = game.check_end(status)
    anpassung(status, 0)



