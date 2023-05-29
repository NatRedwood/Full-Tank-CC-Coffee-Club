from measureWeight import currWeight
from chooseContainerSize import containerSize

oneCupWeight = 9          # weight of coffee beans per cup

maxCups = round(containerSize / oneCupWeight)       # max cups of coffee based on coffee habits and size of the container

moreHalfTankCups =round(0.7 * maxCups)

halfTankCups = round(0.55 * maxCups)

lessHalfTankCups = round(0.45 * maxCups)

lowTankCups = round(0.3 * maxCups)

numCupsLeft = round(currWeight / oneCupWeight)        # number of cups left


# test
#print(numCupsLeft)
#print(currWeight)
#print(lessHalfTankCups)