def towerHanoi(n, sourceRod, destinationRod, auxiliaryRod):
    if(n==0):
        return
    towerHanoi(n-1, sourceRod, auxiliaryRod, destinationRod)
    print "Move the disk " + str(n) + " from the " + sourceRod + "  to " + destinationRod
    towerHanoi(n-1, auxiliaryRod, destinationRod, sourceRod)


towerHanoi(3, "A", "C", "B")
