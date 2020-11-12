print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

q1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right." ').lower()

if q1 == "left":
  print("You\'ve come to a lake. There is an island in the middle of the lake.")
  q2 = input('Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
  
  if q2 == "wait":
    print("You arrived at the island unharmed. There is a house with 3 doors.")
    q3 = input("One red, one yellow and one blue. Which colour do you choose? ").lower()
    
    if q3 == "blue":
      print("You enter a room full of beasts. Game over.") 
    elif q3 == "red":
      print("Burned by fire. Game over.")
    elif q3 == "yellow":
      print("You win!")
    else:
      print("Game over.")

  else:
    print("You were attacked by trout. Game over.")

else:
  print("You fell into a hole. Game over.")

