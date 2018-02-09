#!/bin/python3
from random import randint
import sys
import math

greaterThan = "Greater than"
lessThan = "Less than"
equal = "Equal to"


class CoinBag:
    bag = [] #smallest possible bag
    length = 0
    def __init__(self, n):
       self.length = n
       rand = randint(0, n - 1)
       for x in range(n):
           if x == rand:
               self.bag.append(Coin(1.2))
           else:
               self.bag.append(Coin())
    def printBag(self):
        for x in range(self.length):
            print("   bag[" + str(int(x)) + "]: " + str(self.bag[x].weight))
    # This function takes in 2 tuples and signals 
    # which range of coins weights more.
    def compareRange(self, range1, range2):
        print("RANGE:" + str(range1) + " " + str(range2))
        global greaterThan
        global lessThan
        global equal
        low = 0
        high = 1
        weight1 = 0
        weight2 = 0

        # Make sure we are doing at least 1 comparison
        r1 = range(int(range1[low]), int(range1[high])) or [int(range1[low])]
        r2 = range(int(range2[low]), int(range2[high])) or [int(range2[low])]
        print("R1: " + str(r1))
        
        for x in r1:
            print("x1: " + str(x))
            weight1 = weight1 + self.bag[x].weight
        for x in r2:
            print("x2: " + str(x))
            weight2 = weight2 + self.bag[x].weight
        print("Weight1: " + str(weight1))
        print("Weight2: " + str(weight2))
        if weight1 > weight2:
            return greaterThan
        elif weight2 > weight1:
            return lessThan
        else:
            return equal

class Coin:
    weight = 1.0

    def __init__(self, n = None):
        if n is not None:
            self.weight = n

def main():
    global greaterThan
    global lessThan
    global equal

    if len(sys.argv) != 2:
        print("Usage: python3 " + sys.argv[0] + " [Number of coins]") 
        exit(1)

    numOfCoins = int(sys.argv[1])
    if (numOfCoins % 3) != 0:
        print("Entered number of coins: " + str(numOfCoins))
        print("Number of coins must be a factor of 3")
        exit(1)

    # Start the search for the odd coin
    coinRange = numOfCoins / 3
    coinFound = False
    searchStartIndex = 0
    numOfWeighs = 0
    oddCoinIndex = -1

    while coinFound == False:
        print("Coin range: " + str(coinRange))
        range1 = (searchStartIndex, int(coinRange + searchStartIndex))
        range2 = (int(coinRange + searchStartIndex), int(coinRange + coinRange + searchStartIndex))
        print("Range1: " + str(range1))
        print("Range2: " + str(range2))
        x = CoinBag(numOfCoins)
        x.printBag()
        result = x.compareRange(range1, range2)
        print("Range1 is " + result + " to range2.")

        #if coinRange == 1 and result != equal:
        if coinRange == 1 and result != equal:
            oddCoinIndex = searchStartIndex
            print("exiting loop\n\n")
            break
        elif coinRange < 3 and result == equal:
            print("                     Case 1")
            searchStartIndex = searchStartIndex + 1
        elif result == equal:
            print("                     Case 2")
            searchStartIndex = coinRange * 2
            coinRange = math.ceil(coinRange / 3)
        else:
            print("                     Case 3")
            coinRange = coinRange - 1
            pass
        numOfWeighs = numOfWeighs + 1


    searchStartIndex = searchStartIndex - 1
    print("Odd coin guess: " + str(oddCoinIndex))

    print("\nNew start index:" + str(searchStartIndex))
    if oddCoinIndex == 0: # Edge case
        result = x.compareRange((1, 1), (2, 2))
        if result != equal:
            oddCoinIndex = 1
        #oddCoinIndex = oddCoinIndex - 1 # Should be setting it to -1
    else:
        print("Comparing: " + str(searchStartIndex) + " and " + str(searchStartIndex + 1))
        result = x.compareRange((searchStartIndex, searchStartIndex), \
            (searchStartIndex + 1, searchStartIndex + 1))
    print("Result: " + str(result))
    if result == equal and oddCoinIndex == 0:
        print("Odd coin index is " + str(oddCoinIndex))
    elif result == equal:
        oddCoinIndex = oddCoinIndex + 1
        print("Odd coin index is " + str(oddCoinIndex))
    
    else:
        print("Odd coin index is " + str(oddCoinIndex))



if __name__ == "__main__":
    main()
