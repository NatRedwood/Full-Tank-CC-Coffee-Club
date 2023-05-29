from calculateCoffeeCups import *
from replies import *
from activate import activated

# Main program loop
while activated:                # check that coffee container is activated

    sayNumCupsDays()
    
    # adjusted to the coffee habits settings

    # FullTank
    if numCupsLeft >= moreHalfTankCups:
        sayFullTank()
        sayAddQueue()

    # moreThanHalfTank
    elif numCupsLeft >= halfTankCups & numCupsLeft < moreHalfTankCups:
        sayMoreHalfTank()
        sayAddQueue()

    # HalfTank
    elif numCupsLeft >= lessHalfTankCups & numCupsLeft < halfTankCups:
        sayHalfTank()
        sayAddQueue()

    # LessThanHalfTank
    elif numCupsLeft >= lowTankCups & numCupsLeft < lessHalfTankCups:
        sayLessHalfTank()
        sayOrder()

    # LowTank
    elif numCupsLeft >= lowTankCups:
        sayLowTank()
        sayOrder()

    # NoCups
    elif numCupsLeft == 0:
        sayNoCups()
        sayOrder()

    break