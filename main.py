from time import sleep as w
import random
from random import randint as r

inventory = []

def openinv():
    print("Inventory:", inventory, "\n")

#Dialogue 001
print("...")
w(2)
print("It's dark...")
w(2)
print("You reach for the light switch.")
w(0.5)
print("Click!")

#Choice 001
while True:
    choice = int(input("You're in 001: BEDROOM. What do you want to do? 0=Inventory 1=Open drawers 2=Look under bed 3=Look in closet 4=Open door: \n"))
    if choice == 0:
        openinv()
    elif choice == 1:
        print("You find some shattered glasses and a few tissues with blood splattered on them. Best to leave those there.\n")
    elif choice == 2:
        print("You find a cat's dead body! There is a blood-stained knife next to it. \nYou got the BLOODY KNIFE.\n")
        inventory.append("BLOODY KNIFE")
    elif choice == 3:
        print("You find two dead bodies! They are a couple, it seems like. You find a key in their pockets.\nYou got the KEY.\n")
        inventory.append("001 KEY")
    elif choice == 4:
        if "001 KEY" in inventory:
            print("You unlocked the door.\nYou're now in 002: CORRIDOR.\n")
            inventory.remove("001 KEY")
            break
        else:
            print("The door is locked.\n")
    else:
        print("That's not an option.\n")

#Dialogue 002
print("The corridor seems never ending. The dim lights are flickering. Doors are dotted across the walls, streaked with knife marks and blood stains. You can see a slight glimpse of an elevator at the end of the corridor.\n")
w(5)

#Choice 002
while True:
    choice = int(input("You're in 002: CORRIDOR. What do you want to do? 0=Inventory 1=Go to other side 2=Go to elevator"))
    if choice == 0:
        openinv()
    elif choice == 1:
        print("You tiptoe down the corridor. You hear creaking sounds, and foosteps. But no one is there.")
    elif choice == 2:
        print("The elevator is at your floor. The lights in the elevator are off. It's safe to go in.")