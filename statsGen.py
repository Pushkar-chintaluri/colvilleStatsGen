import random

def getStats():
    return [sum(stat) for stat in [sorted([random.randint(1,6) for roll in range(1,5)])[1:] for att in range(1,7)]]

def printStats(stats):
    if len([stat for stat in stats if stat>=15])>=2:
        print (stats)
    else:
        printStats(getStats())
        
printStats(getStats())
