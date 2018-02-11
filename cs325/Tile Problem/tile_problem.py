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
   height = [0, int(sys.argv[1]) - 1]
   width = [0, int(sys.argv[1]) - 1]
   print("N: " + str(n))

   offset = 4 / 2
   graph = createGraph(width[1] + 1, height[1] + 1)
   initalizeDeadSpace(graph, width[1] + 1, height[1] + 1)
   #initalizeDeadSpace(graph, 1, 3)
   
   printGraph(graph)   
   placeTiles(graph, width, height, offset)
   printGraph(graph)


def placeTiles(graph, width, height, offset):
   global n
   global tileCount_g

   print("-----")
   print(width)
   print(height)
   print(offset)
   print(n)
   print(tileCount_g)
   print("-----")
   
   #print("TILEC: " + str(tileCount_g))
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

   # Inital tile drop
  # offset = 4 / 2
   #print("NNN: " + str(n))

   print("-----")
   print(width)
   print(height)
   print(offset)
   print(n)
   print(tileCount_g)
   print("-----")
   quadrant = getDeadQuadrant(graph, width, height, offset)
   print("QUADRANT: " + str(quadrant))
   placeTile(graph, quadrant, width, height, offset)
   tileCount_g = tileCount_g + 1
   #printGraph(graph)
   
   if (width[maxx] / 2) < 1 or (height[maxx] / 2) < 1:
       print("Returning")
       return None

   width[maxx] = width[maxx] - 2
   height[maxx] = height[maxx] - 2
   placeTiles(graph, width, height, 1)
   #printGraph(graph)
   
   
#    # 2nd quadrant tile drop
#    offset = -1

#    width[maxx] = width[maxx] - 3
#    height[maxx] = height[maxx] - 3

#    quadrant = getDeadQuadrant(graph, width, height, offset)
#    print("QUADRANT: " + str(quadrant))
#    placeTile(graph, quadrant, width, height, offset)
#    tileCount_g = tileCount_g + 1
#    printGraph(graph)

#    print("width: " + str(width[maxx] / 2) + "\nheight: " + str(height[maxx] / 2))
   

# #    offset = n - 1
#    if (width[maxx] / 2) < 1 or (height[maxx] / 2) < 1:
#        print("Returning")
#        return None

   
#    print("width: " + str(width[maxx] / 2) + "\nheight: " + str(height[maxx] / 2))
#    placeTiles(graph, width, height)
#    printGraph(graph)
#    #print("!!!width: " + str(width[minn] + 2)+ " " + str(width[maxx] + 2))
#    #print("!!!height: " + str(height))
#    placeTiles(graph, [width[minn] + 2, width[maxx] + 2], height)
#    placeTiles(graph, width, [height[minn] + 2, height[maxx]])
#    placeTiles(graph, [width[minn] + 2, width[maxx]], \
#                     [height[minn] + 2, height[maxx]])
#    #placeTiles(graph, width, height)
   #print("width: " + str(width) + "\nheight: " + str(height / 2))
   #placeTiles(graph, width / 2, height / 2)

   tileLevel = 0
   #offset = n - tileLevel
   #print("N: " + str(n))
   #print("Offset: " + str(offset))
   #quadrant = etDeadQuadrant(graph, width - offset, height - offset)
   #placeTile(graph, quadrant, width - offset, height - offset)
   #printGraph(graph, width, height)
   #tileCount_g = tileCount_g + 1


def placeTile(graph, quadrant, width, height, offset):
   global tileCount_g
   global n
   minn = 0
   maxx = 1
   offset = abs(offset)
   #print("!-!width: " + str(width[minn])+ " " + str(width[maxx]))
   #print("!-!height: " + str(height[minn]) + " " + str(height[maxx]))
   #print("Offset: " + str(offset))
#    xCord = int(width[1] - offset + 1)
#    yCord = int(height[1] - offset + 1)
   xCord = abs(int(width[1] + 1 - n - offset))
   yCord = abs(int(height[1] + 1 - n - offset))
   #print("n: " + str(n))
   print("xCord :" + str(xCord))
   print("xCord: " +str(width[1] + 1) + " - " +str(n) + " - " + str(offset))
   print("yCord :" + str(yCord))
   if 1 == 1:
      print("x:" + str(xCord) + " Y: " + str(yCord))
      if quadrant == 1:
        #  xCord = math.ceil(xCord)
        #  yCord = math.floor(xCord)
         graph[xCord][yCord] = tileCount_g
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
         print("Placing tile " + str(tileCount_g) + " on")
         print("\t[" + str(xCord) + "][" + str(yCord) + "]")
         print("\t[" + str(xCord) + "][" + str(yCord - 1) + "]") 
         print("\t[" + str(xCord - 1) + "][" + str(yCord - 1) + "]") 
#tileCount_g = tileCount_g + 1
         #printGraph(graph, int(width), int(height))
         #print("Tile cnt: " + str(tileCount_g))
      elif quadrant == 2:
         #print("x: " + str(xCord) + " y: " + str(yCord))
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord][yCord] = tileCount_g
         print("Placing tile " + str(tileCount_g) + " on")
         print("\t[" + str(xCord - 1) + "][" + str(yCord) + "]")
         print("\t[" + str(xCord) + "][" + str(yCord - 1) + "]") 
         print("\t[" + str(xCord) + "][" + str(yCord) + "]") 
#tileCount_g = tileCount_g + 1
         #printGraph(graph, int(width), int(height))
         #tileCount_g = tileCount_g + 1
         #print("Tile cnt: " + str(tileCount_g))
      elif quadrant == 3:
         graph[xCord][yCord] = tileCount_g
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
         print("Placing tile " + str(tileCount_g) + " on")
         print("\t[" + str(xCord) + "][" + str(yCord) + "]")
         print("\t[" + str(xCord -1) + "][" + str(yCord) + "]") 
         print("\t[" + str(xCord - 1) + "][" + str(yCord - 1) + "]") 
         #printGraph(graph, int(width), int(height))
      elif quadrant == 4:
         graph[xCord][yCord - 1] = tileCount_g
         graph[xCord - 1][yCord] = tileCount_g
         graph[xCord - 1][yCord - 1] = tileCount_g
         print("Placing tile " + str(tileCount_g) + " on")
         print("\t[" + str(xCord) + "][" + str(yCord - 1) + "]")
         print("\t[" + str(xCord - 1) + "][" + str(yCord) + "]") 
         print("\t[" + str(xCord - 1) + "][" + str(yCord - 1) + "]") 
#   print("Quadrant: " + str(quadrant))
   print("TILE COUNT: " + str(tileCount_g))
   printGraph(graph)

def getDeadQuadrant(graph, width, height, offset):
   x = -1
   global n
   print("w/h")
   print("Cols: " + str(width))
   print("Rows: " + str(height))
   print("Offset: " + str(offset))
   print("n: " + str(n))
#    if offset < 0:
#        offset = offset * (-1)

   # For accessing width/height tuple
   minn = 0
   maxx = 1
#    print("width: " + str(width) + "\nheight: " + str(height))
#    if (width[maxx] / 2) - width[minn] == 0 and (height[maxx] / 2) - height[minn] == 0:
#        offset = 0
   lenn = width[maxx]

   if str(lenn) == "1":
       return specialCase(graph, height, width)
   

   # Check x quadrant
   for x in range(4):
      # If first quadrant
      if x == 1:
          print("\t\t\tChecking: Q1")
          print(str(height))
          print(str(width))
          half = math.ceil(height[maxx] / 2)
          if half == 1: half = 0 #Base case
          
          print("half: " + str(half))
          rowRange = (height[minn], height[maxx] - half)
        #   print("Weirdness: " + str(height[minn]) + " + " +\
        #         str(height[maxx] - half) + " = " +\
        #         str(rowRange))
          half = math.ceil(width[maxx] / 2)
          if half == 1: half = 0 #Base case
          print("half: " + str(half))
          
          colRange = (width[minn] + half, width[maxx])
          print("rowRange: " + str(rowRange))
          print("colRange: " + str(colRange))
          

        #  rowRange = (height[minn], (height[maxx] - offset)) # (min, max)
        #  colRange = (width[minn]  + offset, width[maxx])
          if quadrantIsDead(graph, rowRange, colRange, lenn):
            return 1

      elif x == 2:
         print("\t\t\tChecking: Q2")
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         print("Half: " + str(half))
         #if height[maxx] > 2:
         rowRange = (height[minn], height[maxx] - half)
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         print("Half: " + str(half))
         #if height[maxx] > 2:
         
         colRange = (width[minn], width[maxx] - half)
         print("")
        #  rowRange = (height[minn], (height[maxx] - offset)) # (min, max)
        #  colRange = (width[minn], (width[maxx] - offset))
         print("----!!\nrowRange: " + str(rowRange))
         print("colRange: " + str(colRange))
         if quadrantIsDead(graph, rowRange, colRange, lenn):
            return 2
      elif x == 3:
         print("\t\t\tChecking: Q3")
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         rowRange = (height[minn] + half, height[maxx])
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         colRange = (width[minn], width[maxx] - half)
        #  rowRange = (height[minn] + offset, height[maxx]) # (min, max)
        #  colRange = (width[minn], (width[maxx] - offset))
         if quadrantIsDead(graph, rowRange, colRange, lenn):
            return 3
      elif x == 4:
         print("\t\t\tChecking: Q4")          
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         
         rowRange = (height[minn] + half, height[maxx])
         half = math.ceil(height[maxx] / 2)
         if half == 1: half = 0 #Base case
         
         colRange = (width[minn] + half, width[maxx])
        #  rowRange = (height[minn] + offset, height[maxx] + offset) # (min, max)
        #  colRange = (width[minn] + offset, width[maxx] + offset)
         if quadrantIsDead(graph, rowRange, colRange, lenn):
            return 4

   return 4


# rangeMin can be as low as 0 and rangeMax should be 
# the width - 1 maxium
def quadrantIsDead(graph, rowRange, colRange, lenn):
#    if rowRange[0] == rowRange[1]:
#        x = rowRange[0]
#        y = rowRange[1]       
#        print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
#        if graph[x][y] != 0:
#             return True
#    if colRange[0] == colRange[1]:
#        x = colRange[0]
#        y = colRange[1]       
#        print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
#        if graph[x][y] != 0:
#             return True
   #lenn = rowRange[1] - rowRange[0]
   #prin
   print("len: " + str(lenn))
   print("Ranges (r/c)")
   xl = int(rowRange[0])

   xh = int(rowRange[1])

   if str(lenn) != "1":
      xh = xh + 1

   yl = int(colRange[0])
   yh = int(colRange[1])

   if str(lenn) != "1":
      yh = yh + 1
 
#    if int(lenn) != "1": 
#        yh = int(colRange[1]) + 1
#    else:  
#        print("\t\t\t\t\tyhlen" + str(lenn))
#        yh = int(colRange[1])
 
   print(range(xl, xh))
   print(range(yl, yh))
   for x in range(xl, xh):
       print("X: " + str(x))
       for y in range(yl, yh):
           print("Y: "+str(y))
           print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
           if graph[x][y] != 0:
              return True
   return False

def specialCase(graph, rowRange, colRange):
    x = int(rowRange[0])
    y = int(colRange[0])
    print("Checking: graph[" + str(x) + "][" + str(y + 1) + "]: " + str(graph[x][y]))
    if graph[x][y + 1] != 0:
        return 1
    print("Checking: graph[" + str(x) + "][" + str(y) + "]: " + str(graph[x][y]))
    if graph[x][y] != 0:
        return 2
    print("Checking: graph[" + str(x + 1) + "][" + str(y) + "]: " + str(graph[x][y]))
    if graph[x + 1][y] != 0:
        return 3
    print("Checking: graph[" + str(x + 1) + "][" + str(y + 1) + "]: " + str(graph[x][y]))
    if graph[x + 1][y + 1] != 0:
        return 4
    return -1
   

def initalizeDeadSpace(graph, width, height):
   w = randint(0, width - 1)
   h = randint(0, height - 1)

   print("Dead Spot: [" + str(w) + "][" + str(h) + "]")

   graph[w][h] = "X"
   #graph[0][1] = "X"


def createGraph(width, height):
   graph = [[0 for x in range(width)] for y in range(height)]
   return graph

def printGraph(graph, width = None, height = None):
    global n
    # print(sys.argv[1])
    if width == None:
        for x in range(int(sys.argv[1])):
            for y in range(int(sys.argv[1])):
                print(graph[x][y], end=" ")
            print("")
    else:
        for x in range(width):
            for y in range(height):
                print(graph[x][y], end=" ")
            print("")



if __name__ == "__main__":
    main()
