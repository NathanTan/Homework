#!/bin/python3
from random import randint

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
        low = 0
        high = 1
        weight1 = 0
        weight2 = 0
        for x in range(range1[low], range1[high]):
            weight1 = weight1 + self.bag[x].weight
        print("Weight1: " + str(weight1))


class Coin:
    weight = 1.0

    def __init__(self, n = None):
        if n is not None:
            self.weight = n

def main():
    print("In main")
    x = CoinBag(9)
    c = Coin()
    c2 = Coin(5.0)
    x.printBag()
    x.compareRange((0, 9), ())

if __name__ == "__main__":
    main()
