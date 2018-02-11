#!/bin/python3
from random import randint
import statistics
import math
import time
import sys

#################### Globals ####################
tileCount_g = 1
n = -1
alteredQuadrant_g = 0
size_g = 4

def main():
   global n
   global size
   print("Welcome to the tiling problem")
   width = 4
   height = 4
   tileLevel = 1

   n = math.log(size_g, 2)
   height = [0, int(sys.argv[1]) - 1]
   width = [0, int(sys.argv[1]) - 1]

   offset = 4 / 2
   graph = createGraph(width[1] + 1, height[1] + 1)
   initalizeDeadSpace(graph, width[1] + 1, height[1] + 1)
   
   printGraph(graph) 
   start = time.time()  
   placeTiles(graph, width, height, offset)
   end = time.time()
   printGraph(graph)

   print("Elpased time: " + str(end - start))


def placeTiles(graph, width, height, offset):
   global n
   global tileCount_g
   global alteredQuadrant_g
   if int(tileCount_g)   == 6:
       return

   #Set n for smaller examples, secifically a 4x4
   if (tileCount_g == 1): n = 2
   elif (tileCount_g >= 2) and (tileCount_g <= 5): n = 1
   #print("n: "+ str(n))
   #Set offset
   if (n == 1): offset = 2
   elif (n == 2): offset = 0 
   
   # For accessing width/height tuple
   minn = 0
   maxx = 1

   quadrant = getDeadQuadrant(graph, width, height, offset)

   placeTile(graph, quadrant, width, height, offset)
   tileCount_g = tileCount_g + 1
   
   if (width[maxx] / 2) < 1 or (height[maxx] / 2) < 1:
       return None
   if tileCount_g == (2**n + 2):
       return

   half = math.ceil(height[maxx] / 2)
    
   width[maxx] = width[maxx] - half
   height[maxx] = height[maxx] - half
   placeTiles(graph, width, height, 1)

   width[maxx] = width[maxx] + half
   width[minn] = width[minn] + half
   alteredQuadrant_g = 1
   placeTiles(graph, width, height, 1)
   
   height[minn] = height[minn] + half
   height[maxx] = height[maxx] + half
   alteredQuadrant_g = 2
   placeTiles(graph, width, height, 1)




def placeTile(graph, quadrant, width, height, offset):
   global tileCount_g
   global n
   global alteredQuadrant_g
   minn = 0
   maxx = 1
   offset = abs(offset)
   xCord = abs(int(width[1] + 1 - n - offset))
   yCord = abs(int(height[1] + 1 - n - offset))
   if tileCount_g == 5:
       xCord = xCord + 2
   elif int(alteredQuadrant_g) == 1:
       yCord = yCord + 2
   elif int(alteredQuadrant_g) == 2:
       yCord = yCord + 2
       xCord = xCord + 2




   if 1 == 1:
      if quadrant == 1:
         graph[xCord][yCord] = tileCount_g
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
        #  print("Placing tile " + str(tileCount_g) + " on")
        #  print("\t[" + str(xCord) + "][" + str(yCord) + "]")
        #  print("\t[" + str(xCord) + "][" + str(yCord - 1) + "]") 
        #  print("\t[" + str(xCord - 1) + "][" + str(yCord - 1) + "]") 
      elif quadrant == 2:
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord][yCord] = tileCount_g
        #  print("Placing tile " + str(tileCount_g) + " on")
        #  print("\t[" + str(xCord - 1) + "][" + str(yCord) + "]")
        #  print("\t[" + str(xCord) + "][" + str(yCord - 1) + "]") 
        #  print("\t[" + str(xCord) + "][" + str(yCord) + "]") 
      elif quadrant == 3:
         graph[xCord][yCord] = tileCount_g
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
        #  print("Placing tile " + str(tileCount_g) + " on")
        #  print("\t[" + str(xCord) + "][" + str(yCord) + "]")
        #  print("\t[" + str(xCord -1) + "][" + str(yCord) + "]") 
        #  print("\t[" + str(xCord - 1) + "][" + str(yCord - 1) + "]") 
      elif quadrant == 4:
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
        #  print("Placing tile " + str(tileCount_g) + " on")
        #  print("\t[" + str(xCord) + "][" + str(yCord - 1) + "]")
        #  print("\t[" + str(xCord - 1) + "][" + str(yCord) + "]") 
        #  print("\t[" + str(xCord - 1) + "][" + str(yCord - 1) + "]") 
   printGraph(graph)

def getDeadQuadrant(graph, width, height, offset):
   x = -1
   global n

   # For accessing width/height tuple
   minn = 0
   maxx = 1

   rangelen = width[maxx]
   if (width[maxx] - width[minn]) == 1 and \
      (height[maxx] - height[minn]) == 1:
      rangelen = 1

   if str(rangelen) == "1":
       return specialCase(graph, height, width)
   

   # Check x quadrant
   for x in range(4):
      # If first quadrant
      if x == 1:
          half = math.ceil(height[maxx] / 2)
          if half == 1: half = 0 #Base case
          
          rowRange = (height[minn], height[maxx] - half)
          half = math.ceil(width[maxx] / 2)
          if half == 1: half = 0 #Base case
          
          colRange = (width[minn] + half, width[maxx])

          if quadrantIsDead(graph, rowRange, colRange):
            return 1

      elif x == 2:
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         rowRange = (height[minn], height[maxx] - half)
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         
         colRange = (width[minn], width[maxx] - half)
         if quadrantIsDead(graph, rowRange, colRange):
            return 2
      elif x == 3:
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         rowRange = (height[minn] + half, height[maxx])
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         colRange = (width[minn], width[maxx] - half)
         if quadrantIsDead(graph, rowRange, colRange):
            return 3
      elif x == 4:
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         
         rowRange = (height[minn] + half, height[maxx])
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         
         colRange = (width[minn] + half, width[maxx])
       
         if quadrantIsDead(graph, rowRange, colRange):
            return 4

   return 4


# rangeMin can be as low as 0 and rangeMax should be 
# the width - 1 maxium
def quadrantIsDead(graph, rowRange, colRange):
   xl = int(rowRange[0])
   xh = int(rowRange[1]) + 1

   yl = int(colRange[0])
   yh = int(colRange[1]) + 1

  
#    print(range(xl, xh))
#    print(range(yl, yh))
   for x in range(xl, xh):
       for y in range(yl, yh):
           # print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
           if graph[x][y] != 0:
              return True
   return False

def specialCase(graph, rowRange, colRange):
    x = int(rowRange[0])
    y = int(colRange[0])
    # print("Checking: graph[" + str(x) + "][" + str(y + 1) + "]: " + str(graph[x][y]))
    if graph[x][y + 1] != 0:
        return 1
    # print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
    if graph[x][y] != 0:
        return 2
    # print("Checking: graph[" + str(x + 1) + "][" + str(y) + "]: " + str(graph[x][y]))
    if graph[x + 1][y] != 0:
        return 3
    # print("Checking: graph[" + str(x + 1) + "][" + str(y + 1) + "]: " + str(graph[x][y]))
    if graph[x + 1][y + 1] != 0:
        return 4
    return -1
   

def initalizeDeadSpace(graph, width, height):
   w = randint(0, width - 1)
   h = randint(0, height - 1)

   graph[w][h] = "X"


def createGraph(width, height):
   graph = [[0 for x in range(width)] for y in range(height)]
   return graph

def printGraph(graph, width = None, height = None):
    global size_g
    if width == None:
        for x in range(size_g):
            for y in range(size_g):
                print(graph[x][y], end=" ")
            print("")
    else:
        for x in range(width):
            for y in range(height):
                print(graph[x][y], end=" ")
            print("")
    print("")



if __name__ == "__main__":
    main()
