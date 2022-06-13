# Created by Hugo Nolte for course PA1414 - DoBot Magician Project
# 2019

import threading
import DoBotArm as Dbt
import time

#Example of bundling functions
def payload():
    homeX, homeY, homeZ = 250, 0, 50
    ctrlBot = Dbt.DoBotArm(homeX, homeY, homeZ, False) #Create DoBot Class Object with home position x,y,z
    #time.sleep(30)
    #print("Moving a")
    #ctrlBot.moveArmXY(250, 0)
    #for i in range (5):
    #    ctrlBot.moveArmXYZ(250, 0, -i*11)
    #    print(i)
    #    time.sleep(1)
    #ctrlBot.moveHome()
    #ctrlBot.pickToggle(-44)
    #ctrlBot.toggleSuction()
    #ctrlBot.pickToggle(-44)
    #ctrlBot.moveHome()
    #ctrlBot.moveArmXY(250, 100)
    #ctrlBot.pickToggle(-44)
    #ctrlBot.toggleSuction()
    #ctrlBot.pickToggle(-44)
    print("Belt")
    ctrlBot.SetConveyor(1, 283*60)
    time.sleep(5)
    print("sp")
    ctrlBot.SetConveyor(1, 283*50)
    time.sleep(5)
    ctrlBot.SetConveyor(0, 0)

#An example combining the functions into a manual control mode
def manualMode():
    homeX, homeY, homeZ = 250, 0, 50
    ctrlBot = Dbt.DoBotArm(homeX, homeY, homeZ) #Create DoBot Class Object with home position x,y,z

    print("---Manual Mode---")
    print("move to move to location")
    print("pick - toggles picking at certain height")
    print("suct - toggles suction on and off")
    print("q - exit manual mode")
    while True:
        inputCoords = input("$ ")
        inputCoords = inputCoords.split(",")
        if(inputCoords[0] == "move"):
            x = int(inputCoords[1])
            y = int(inputCoords[2])
            ctrlBot.moveArmXY(x,y)
        elif(inputCoords[0] == "pick"):
            height = int(inputCoords[1])
            ctrlBot.pickToggle(height)
        elif(inputCoords[0] == "suct"):
            ctrlBot.toggleSuction()
        elif(inputCoords[0] == "q"):
            break
        else:
            print("Unrecognized command")


#--Main Program--
def main():
    payload()

main()