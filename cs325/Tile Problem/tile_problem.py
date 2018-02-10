#!/bin/python3
from random import randint
import statistics
import math
import sys

#################### Globals ####################
tileCount_g = 1
n = -1

def main():
   global n
   print("Welcome to the tiling problem")
   width = 4
   height = 4
   tileLevel = 1

   if len(sys.argv) != 2:
       print("Usage: python3 " + sys.argv[0] + " [Size of matrix]")
       exit(1)
   n = math.log(float(sys.argv[1]), 2)
   height = [0, int(sys.argv[1])]
   width = [0, int(sys.argv[1])]

   offset = 0
   graph = createGraph(width[1], height[1])
   initalizeDeadSpace(graph, width[1], height[1])

   placeTiles(graph, width, height)
   printGraph(graph)


def placeTiles(graph, width, height):
   global n
   global tileCount_g
   tileLevel = 0
   offset = 0
   
   # For accessing width/height tuple
   minn = 0
   maxx = 1


   # Inital tile drop

   quadrant = getDeadQuadrant(graph, width, height)
   print("QUADRANT: " + str(quadrant))
   placeTile(graph, quadrant, width, height)
   tileCount_g = tileCount_g + 1
   printGraph(graph)
   
   # 2nd quadrant tile drop

   offset = n - 0
   if (width[maxx] / 2) < 2 or (height[maxx] / 2) < 2:
       return None

   width[maxx] = width[maxx] / 2
   height[maxx] = height[maxx] / 2
   
   print("width: " + str(width[maxx] / 2) + "\nheight: " + str(height[maxx] / 2))
   placeTiles(graph, width, height)
   printGraph(graph)
   placeTiles(graph, width, height)
   placeTiles(graph, [width[minn] + 2, width[maxx]], height)
   placeTiles(graph, width, height)
   placeTiles(graph, width, [height[minn] + 2, height[maxx]])
   placeTiles(graph, width, height)
   placeTiles(graph, [width[minn] + 2, width[maxx]], \
                    [height[minn] + 2, height[maxx]])
   placeTiles(graph, width, height)
   #print("width: " + str(width) + "\nheight: " + str(height / 2))
   #placeTiles(graph, width / 2, height / 2)

   tileLevel = 0
   #offset = n - tileLevel
   #print("N: " + str(n))
   #print("Offset: " + str(offset))
   #quadrant = getDeadQuadrant(graph, width - offset, height - offset)
   #placeTile(graph, quadrant, width - offset, height - offset)
   #printGraph(graph, width, height)
   #tileCount_g = tileCount_g + 1


def placeTile(graph, quadrant, width, height):
   global tileCount_g
   xCord = math.floor(width[1] / 2)
   yCord = math.floor(height[1] / 2)
   if 1 == 1:
      print("x:" + str(xCord) + " Y: " + str(yCord))
      if quadrant == 1:
         xCord = math.ceil(xCord)
         yCord = math.floor(xCord)
         graph[xCord][yCord] = tileCount_g
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
         #tileCount_g = tileCount_g + 1
         #printGraph(graph, int(width), int(height))
         #print("Tile cnt: " + str(tileCount_g))
      elif quadrant == 2:
         #print("x: " + str(xCord) + " y: " + str(yCord))
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord][yCord] = tileCount_g
         #printGraph(graph, int(width), int(height))
         #tileCount_g = tileCount_g + 1
         #print("Tile cnt: " + str(tileCount_g))
      elif quadrant == 3:
         graph[xCord][yCord] = tileCount_g
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
         #printGraph(graph, int(width), int(height))
      elif quadrant == 4:
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
         #printGraph(graph, int(width), int(height))
#   print("Quadrant: " + str(quadrant))
   print("TILE COUNT: " + str(tileCount_g))

def getDeadQuadrant(graph, width, height):
   x = -1

   # For accessing width/height tuple
   minn = 0
   maxx = 1
   print("width: " + str(width) + "\nheight: " + str(height))

   # Check x quadrant
   for x in range(4):
      # If first quadrant
      if x == 1:
         rowRange = (height[minn], (height[maxx] / 2)) # (min, max)
         colRange = ((width[maxx] / 2), width[maxx])
         if quadrantIsDead(graph, rowRange, colRange):
            return 1

      elif x == 2:
         rowRange = (height[minn], (height[maxx] / 2)) # (min, max)
         colRange = (width[minn], (width[maxx] / 2))
         if quadrantIsDead(graph, rowRange, colRange):
            return 2
      elif x == 3:
         rowRange = ((height[maxx] / 2), height[maxx]) # (min, max)
         colRange = (width[minn], (width[maxx] / 2))
         if quadrantIsDead(graph, rowRange, colRange):
            return 3
      elif x == 4:
         rowRange = ((height[maxx] / 2), height[maxx]) # (min, max)
         colRange = ((width[maxx] / 2), width[maxx])
         if quadrantIsDead(graph, rowRange, colRange):
            return 4


   return 4


# rangeMin can be as low as 0 and rangeMax should be 
# the width - 1 maxium
def quadrantIsDead(graph, rowRange, colRange):
    #print("Ranges")
   print(rowRange)
   print(colRange)
   for x in range(int(rowRange[0]), int(rowRange[1])):
       for y in range(int(colRange[0]), int(colRange[1])):
           print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
           if graph[x][y] != 0:
              return True
   return False

def initalizeDeadSpace(graph, width, height):
   w = randint(0, width - 1)
   h = randint(0, height - 1)

   print("Dead Spot: [" + str(w) + "][" + str(h) + "]")

   graph[w][h] = "X"



def createGraph(width, height):
   graph = [[0 for x in range(width)] for y in range(height)]
   return graph

def printGraph(graph, width = None, height = None):
    global n
    if width == None:
        for x in range(int(2**n)):
            for y in range(int(2**n)):
                print(graph[x][y], end=" ")
            print("")
    else:
        for x in range(width):
            for y in range(height):
                print(graph[x][y], end=" ")
            print("")



if __name__ == "__main__":
    main()
