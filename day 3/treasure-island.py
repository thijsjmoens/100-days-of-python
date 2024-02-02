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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Start with the crossroad
print("You are on a crossroad. Do you want to go left or right?") 
crossroad = input()
crossroad.lower()

if crossroad == "left":
    
    # Next question
    print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" for a boat. Type \"swim\" to swim across.") 
    lake = input()
    lake.lower()

    if lake == "wait":

        # Next question
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?") 
        door = input()
        door.lower()

        if door == "yellow":
            print("You win! 🎉")
        elif door == "red":
            print("You have been burned by a huge fire. Game Over.")
        elif door == "blue":
            print("You have been eaten by beasts. Game Over.")
        else: 
            print("Game over!")
        
    else:
        print("You are attacked by a trout. Game Over.") 

else:
    print("You fall into a hole. Game Over.") 



