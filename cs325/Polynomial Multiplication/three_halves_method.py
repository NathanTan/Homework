#!/bin/python2
import numpy as np

# Three Halves method for multiplying polynomials
# Author: Nathan Tan
# Date: 2/15/2018

# NOTE: Currently set up for 2 polynomials of power 3
#       and 0's will break numpy

def main():

   #Gather data from the user
   l1, len1 = getList()
   l2, len2 = getList()
   lenMax = int(len1) + int(len2)
   c = [0] * (lenMax + 1)

   # Execute the algorithm
   c = three_halves_execute(l1, l2)


def getList():
   length = 3
   l = []

   for x in range(length, -1, -1):
      val = input("X^" + str(x) + ": ")
      l.append(int(val))
   
   print("")
   return l, length

def three_halves_execute(l1, l2):
      p = np.array_split(l1, 2)
      q = np.array_split(l2, 2)


      ar1 = np.polymul(p[0], q[0])
      ar2 = np.polymul(np.add(p[0], p[1]), np.add(q[0], q[1]))
      ar3 = np.polymul(p[1], q[1])
   
      ar2 = np.subtract(ar2, ar1)
      ar2 = np.subtract(ar2, ar3)


      ans = []
      ans.append(ar1[0])
      ans.append(ar1[1])
      ans.append(ar1[2] + ar2[0])
      ans.append(ar2[1])
      ans.append(ar3[0] + ar2[2])
      ans.append(ar3[1])
      ans.append(ar3[2])

      print(ans)
      

if __name__ == "__main__":
   main()
