#!/bin/python3

class CoinBag:
    bag = [0, 0, 0] #smallest possible bag

    def __init__(self, n):
       self.bag = list([0] * n)

class Coin:
    weight = 1.0

    def __init__(self, n = None):
        if n is not None:
            self.weight = n

def main():
    print("In main")
    x = CoinBag(9)
    print(x.bag)
    c = Coin()
    c2 = Coin(5.0)
    print(c.weight)
    print(c2.weight)

if __name__ == "__main__":
    main()
