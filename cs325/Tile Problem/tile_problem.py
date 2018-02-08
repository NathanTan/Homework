#!/bin/python3
from random import randint
import statistics
import math

#################### Globals ####################
tileCount_g = 1


def main():
   print("Welcome to the tiling problem")
   width = 4
   height = 4
   tileCount_g = 1

   graph = createGraph(width, height)
   initalizeDeadSpace(graph, width, height)

   printGraph(graph, width, height)
   placeTiles(graph, width, height)
   printGraph(graph, width, height)





def placeTiles(graph, width, height):
   quadrant = getDeadQuadrant(graph, width, height)
   placeTile(graph, quadrant, width, height)


def placeTile(graph, quadrant, width, height):
   global tileCount_g
   tileCount = tileCount_g
   xCord = math.floor(width / 2)
   yCord = math.floor(height / 2)
   if tileCount == 1:
      print("x:" + str(xCord) + " Y: " + str(yCord))
      if quadrant == 1:
         xCord = math.ceil(xCord)
         yCord = math.floor(xCord)
         graph[xCord][yCord] = tileCount
         graph[xCord][yCord - 1] = tileCount
         graph[xCord - 1][yCord - 1] = tileCount
         tileCount_g = tileCount_g + 1
         printGraph(graph, width, height)
         print("Tile cnt: " + str(tileCount_g))
      elif quadrant == 2:
         #print("x: " + str(xCord) + " y: " + str(yCord))
         graph[xCord - 1][yCord] = tileCount
         graph[xCord][yCord - 1] = tileCount
         graph[xCord][yCord] = tileCount
         tileCount_g = tileCount_g + 1
         print("Tile cnt: " + str(tileCount_g))
      elif quadrant == 3:
         graph[xCord][yCord] = tileCount
         graph[xCord - 1][yCord] = tileCount
         graph[xCord - 1][yCord - 1] = tileCount
      elif quadrant == 4:
         graph[xCord][yCord - 1] = tileCount
         graph[xCord - 1][yCord] = tileCount
         graph[xCord - 1][yCord - 1] = tileCount
   print("Quadrant: " + str(quadrant))


def getDeadQuadrant(graph, width, height):
   x = -1

   # Check x quadrant
   for x in range(4):
      # If first quadrant
      if x == 1:
         rowRange = (0, (height / 2)) # (min, max)
         colRange = ((width / 2), width)
         if quadrantIsDead(graph, rowRange, colRange):
            return 1

      elif x == 2:
         rowRange = (0, (height / 2)) # (min, max)
         colRange = (0, (width / 2))
         if quadrantIsDead(graph, rowRange, colRange):
            return 2
      elif x == 3:
         rowRange = ((height / 2), height) # (min, max)
         colRange = (0, (width / 2))
         if quadrantIsDead(graph, rowRange, colRange):
            return 3
      elif x == 4:
         rowRange = ((height / 2), height) # (min, max)
         colRange = ((width / 2), width)
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

def printGraph(graph, width, height):
    for x in range(width):
        for y in range(height):
           print(graph[x][y], end=" ")
        print("")



if __name__ == "__main__":
    main()
