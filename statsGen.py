import random

def getStats():
    return [sum(i) for i in [sorted([random.randint(1,6) for a in range(1,5)])[1:] for each in range(1,7)]]

def printStats(stats):
    if len([s for s in stats if s>=15])>=2:
        print (stats)
    else:
        printStats(getStats())
        
printStats(getStats())
