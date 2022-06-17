# Created by Hugo Nolte for course PA1414 - DoBot Magician Project
# 2019

import threading
import DoBotArm as Dbt
import time
from serial.tools import list_ports

#--Main Program--
def main():
    # Choosing port
    available_ports = list_ports.comports()
    print('Available COM-ports:')
    for i, port in enumerate(available_ports):
        print(f"  {i}: {port.description}")

    choice = int(input('Choose port by typing a number followed by [Enter]: '))
    port = available_ports[choice].device
    
    # Preprogrammed sequence
    homeX, homeY, homeZ = 250, 0, 50
    ctrlBot = Dbt.DoBotArm(homeX, homeY, homeZ, True) #Create DoBot Class Object with home position x,y,z
    print("Moving")
    ctrlBot.moveArmXY(250, 0)
    for i in range (5):
        ctrlBot.moveArmXYZ(250, 0, -i*11)
        print(i)
        time.sleep(1)
    ctrlBot.moveHome()
    print("Picking")
    ctrlBot.pickToggle(-44)
    ctrlBot.toggleSuction()
    ctrlBot.pickToggle(-44)
    print("Moving")
    ctrlBot.moveHome()
    ctrlBot.moveArmXY(250, 100)
    print("Dropping")
    ctrlBot.pickToggle(-44)
    ctrlBot.toggleSuction()
    ctrlBot.pickToggle(-44)
    print("Disconnecting")

if __name__ == "__main__":
    main()