""" A building has 100 floors. One of the floors is the highest floor an egg can 
be dropped from without breaking.

If an egg is dropped from above that floor, it will break. 
If it is dropped from that floor or below, it will be completely undamaged and 
you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking, 
with as few drops as possible. """

# Start coding from here
import sys

# Function to get minimum number of trials
# needed in worst case with n eggs and k floors


def eggDrop(n, k):

    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (k == 1 or k == 0):
        return k

    # We need k trials for one egg
    # and k floors
    if (n == 1):
        return k

    min = sys.maxsize

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):

        res = max(eggDrop(n - 1, x - 1),
                  eggDrop(n, k - x))
        if (res < min):
            min = res

    return min + 1
