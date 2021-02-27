import random
import dictionary
from dictionary import add

def print_board(status):
   board_visible = (" " + str(status["board"][0]) + " | " + str(status["board"][1]) + " | " + str(status["board"][2]) + "\n" +
                    " ---------\n" +
                    " " + str(status["board"][3]) + " | " + str(status["board"][4]) + " | " + str(status["board"][5]) + "\n" +
                    " ---------\n" +
                    " " + str(status["board"][6]) + " | " + str(status["board"][7]) + " | " + str(status["board"][8]))
   print(board_visible)

def createState(status):
   return str(status["board"])
   
def Agent(status):
   entscheidung = False
   versuch = 0
   state = createState(status)
   #print(state)
   while entscheidung == False:
      Wahl = dictionary.highest(state, versuch)
      if belegt(status, Wahl) == False:
            entscheidung = True
      else:
         versuch = versuch + 1
   dictionary.save()    
   return Wahl

def Kacheln_voll(status):
   anfangs_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   leer = False
   wert = 0
   while leer == False and wert < 9:
      if anfangs_board[wert] == status["board"][wert]:
         leer = True
      wert = wert + 1
   if leer == True:
      return False
   else:
      return True

def Sieger(status):
   sieger = "none"
   for zeichen in ["X", "O"]:
      if status["board"][0] == zeichen:
         
         if status["board"][1] == zeichen and status["board"][2] == zeichen:
            sieger = zeichen
         if status["board"][4] == zeichen and status["board"][8] == zeichen:
            sieger = zeichen
         if status["board"][3] == zeichen and status["board"][6] == zeichen:
            sieger = zeichen
            
      if status["board"][4] == zeichen:
         if status["board"][1] == zeichen and status["board"][7] == zeichen:
            sieger = zeichen
         if status["board"][2] == zeichen and status["board"][6] == zeichen:
            sieger = zeichen
         if status["board"][3] == zeichen and status["board"][5] == zeichen:
            sieger = zeichen
         
      if status["board"][8] == zeichen:
         if status["board"][6] == zeichen and status["board"][7] == zeichen:
            sieger = zeichen
         if status["board"][2] == zeichen and status["board"][5] == zeichen:
            sieger = zeichen
   return sieger
 

def check_end(status):
   status["sieger"] = Sieger(status)
   if status["sieger"] != "none":
      return status["sieger"]
   elif Kacheln_voll(status) == True:
      return "draw"
   else:
      return "none"
       
def belegt(status, feld):
   if status["board"][feld] != feld:
      return True
   else:
      return False

#ef anpassung(sieger):
#   global gewichtungen
#   if sieger == "O":
#      i = 0
#      for zeichen in board:
#         if zeichen == "O":
#            gewichtungen[i][0] = gewichtungen[i][0] + 1
#         i = i + 1
#         
#   elif sieger == "X":
#      i = 0
#      for zeichen in board:
#         if zeichen == "O":
#            gewichtungen[i][0] = gewichtungen[i][0] - 1
#         i = i + 1
  
def spiel_c():
   status = {"board": [0, 1, 2, 3, 4, 5, 6, 7, 8], "sieger": "none", "spieler": random.choice(("X", "X")), "WegO": []}
   if status["spieler"] == "X":
      print_board(status)
      print("\n")

   while check_end(status) == "none":
      #print("Aktueller Spieler: " + spieler + "\n")
      if status["spieler"] == "X":
         entscheidung = False
         while entscheidung == False:
            Wahl = int(input("Welche Kachel belegen? "))
            if belegt(status, Wahl) == False:
               status["board"][Wahl] = "X"
               entscheidung = True
               status["spieler"] = "O"
            else:
               print("Dieses Feld ist belegt. Wähle ein anderes!")
      else:
         entscheidung = False
         while entscheidung == False:
            Wahl = Agent(status)
            if belegt(status, Wahl) == False:
               status["WegO"].insert(0, [createState(status), Wahl])
               status["board"][Wahl] = "O"
               entscheidung = True
               print("\n")
               print_board(status)
               print("\n")
               status["spieler"] = "X"

   anpassung(status, 1)
         
   if check_end(status) == "draw":
      print("Es ist unentschieden!")
   else:
      print("Gewonnen hat: " + check_end(status))
   nochmal = input("Nochmal spielen? (j/n): ")

   if nochmal == "j":
      print("\n")
      Spielstart("c")
   else:
      print("Dann nicht")



def spiel_m():
   status = {"board": [0, 1, 2, 3, 4, 5, 6, 7, 8], "sieger": "none", "spieler": random.choice(("X", "O"))}
   print_board(status)
   print("\n")

   while check_end(status) == "none":
      print("Aktueller Spieler: " + status["spieler"] + "\n")
      if status["spieler"] == "X":
         entscheidung = False
         while entscheidung == False:
            Wahl = int(input("Welche Kachel belegen? "))
            if belegt(status, Wahl) == False:
               status["board"][Wahl] = "X"
               entscheidung = True
               status["spieler"] = "O"
               print("\n")
               print_board(status)
               print("\n")
            else:
               print("Dieses Feld ist belegt. Wähle ein anderes!")
      else:
         entscheidung = False
         while entscheidung == False:
            Wahl = int(input("Welche Kachel belegen? "))
            if belegt(status, Wahl) == False:
               status["board"][Wahl] = "O"
               entscheidung = True
               status["spieler"] = "X"
               print("\n")
               print_board(status)
               print("\n")
            else:
               print("Dieses Feld ist belegt. Wähle ein anderes!")
         
   if check_end(status) == "draw":
      print("Es ist unentschieden!")
   else:
      print("Gewonnen hat: " + check_end(status))
   nochmal = input("Nochmal spielen? (j/n): ")
   if nochmal == "j":
      print("\n")
      Spielstart("m")
   else:
      print("Dann nicht")


         
   
def Spielstart(gegner):
   if gegner == "c":
      spiel_c()
   elif gegner == "m":
      spiel_m()

def setup():
   dictionary.init()
   gegner = ""
   while gegner != "c" and gegner != "m":
      gegner = input("Willst du gegen den Computer oder einen menschlichen Gegner spielen oder trainieren? (c/m/t): ")
      if gegner != "c" and gegner != "m"and gegner != "t":
         print("Das ist keine valide Antwort. Bitte nochmal!")
      elif gegner == "t":
         Train.dauer(int(input("Wieviele Wiederholungen? ")))
      else:
         Spielstart(gegner)
   
setup()


   
