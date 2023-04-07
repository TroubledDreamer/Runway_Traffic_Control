#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the mkAircraft function below.
def mkAircraft(iD, fuelLvl):
    return ('Aircraft',[iD,fuelLvl])



# Complete the getiD function below.
def getiD(node):
    if node[0] == 'Aircraft':
        return node[1][0]
    



# Complete the getFuelLvl function below.
def getFuelLvl(node):
    if node[0] == 'Aircraft':
        return int(node[1][1])




# Complete the mkPriorityQueue function below.
def mkPriorityQueue():
    return ('PriQueue',[])



# Complete the getContents function below.
def getContents(priQueue):
    if  priQueue[0] == 'PriQueue':
        return priQueue[1]



# Complete the isPriQueueEmpty function below.
def isPriQueueEmpty(priqContents):
    if type(priqContents) == type([]):
        return priqContents == []
        



# Complete the getPos function below.
def getPos(aircraft, priqContents):
    fuel = getFuelLvl(aircraft)
    Aid = getiD(aircraft)

    if isPriQueueEmpty(priqContents):
        return 0
    first_p = priqContents[0]
    fuel_p = getFuelLvl(first_p)
    Aid_p = getiD(first_p)
    if fuel < fuel_p:
        return 0
    else:
        return 1 + getPos(aircraft,priqContents[1:])
        



# Complete the addAirCraftToQueue function below.
def addAirCraftToQueue(priQueue, aircraft):
    postion = getPos(aircraft,getContents(priQueue))
    content = getContents(priQueue)
    content.insert(postion,aircraft)




# Complete the popAirCraftFromQueue function below.
def popAirCraftFromQueue(priQueue):
    if not isPriQueueEmpty(getContents(priQueue)):
        return getContents(priQueue).pop(0)

# Complete the main code below that makes use of the functions above and operationalizes the Runway Traffic Control.
# As per the instructions above, complete the following starter code below that uses the Priority Queue data structure to organize the aircrafts added to the queue. After each `land` command, print the ID of the aircraft that has landed.
if __name__ == '__main__':
    c = int(input().strip())
    
    
    que = mkPriorityQueue()
    for c_itr in range(c):
        command = input()
        
        if 'add' in command:
            data = command.split()
            aircraft = mkAircraft(data[1],data[2])
            addAirCraftToQueue(que, aircraft)
                        
        if 'land' in command:
            print(getiD(popAirCraftFromQueue(que)))
