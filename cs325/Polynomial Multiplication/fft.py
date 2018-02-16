#!/bin/python3

# Classical Iterative method for multiplying polynomials
# Author: Nathan Tan
# Date: 2/15/2018

import fftlib as fft

def main():
   l1, len1 = getList()
   l2, len2 = getList()
   lenMax = int(len1) + int(len2)
   c = [0] * (lenMax + 1)
   
   # Execute the algorithm
   c = fft.FPM(l1, l2)
   
   for x, val in enumerate(c):
      if ((lenMax - x) > 0):
         print(str(val) + "x^" + str(lenMax - x) + " + ", end = "")
      else:
         print(str(val))
   print("")

def getList():
   inp = input("Enter higest degree power: ")
   length = int(inp)
   l = []

   for x in range(length, -1, -1):
      val = input("X^" + str(x) + ": ")
      l.append(int(val))
   
   print("")
   return l, length


if __name__ == "__main__":
   main()
