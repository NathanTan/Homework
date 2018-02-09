#!/bin/python3
from random import randint

greaterThan = "Greater than"
lessThan = "Less than"
equal = "Equal to"


class CoinBag:
    bag = [] #smallest possible bag
    length = 0
    def __init__(self, n):
       self.length = n
       rand = randint(0, n - 1)
       print("int: " + str(rand))
       for x in range(n):
           if x == rand:
               self.bag.append(Coin(1.2))
           else:
               self.bag.append(Coin())
    def printBag(self):
        for x in range(self.length):
            print(self.bag[x].weight)
    # This function takes in 2 tuples and signals 
    # which range of coins weights more.
    def compareRange(self, range1, range2):
        global greaterThan
        global lessThan
        global equal
        low = 0
        high = 1
        weight1 = 0
        weight2 = 0
        for x in range(range1[low], range1[high]):
            weight1 = weight1 + self.bag[x].weight
        for x in range(range2[low], range2[high]):
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
    print("In main")
    x = CoinBag(9)
    c = Coin()
    c2 = Coin(5.0)
    x.printBag()
    result = x.compareRange((0, 4), (4, 9))
    print("Range1 is " + result + " to range2.")

if __name__ == "__main__":
    main()
