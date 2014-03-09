import random
import time

class Game:
   def __init__(self, m=10, n=10, fertility=False):
      print 'new game created'
      #Start by defining a m x n grid size
      self.m = m  #m rows
      self.n = n  #n columns
      
      #If the fertility parameter was not passed at initialization, get it from the user
      if not fertility:
         fertility = input("Enter, as decimal, the land's fertility:  ")
      assert fertility>0 and fertility<1 , 'fertility set to ' + str(fertility) + '. Must be between 0 and 1'
      
      #Initializes the grid with randomly generated cells according to fertility probability
      def seedCellsToGrid():
         #Initialize the cells in the starting grid
         self.grid = []
         for cell in range(0,self.m*self.n):
            self.grid.append(random.random()<fertility)
      seedCellsToGrid()
   
   #Get the array index given i,j
#   def cellIndex(self, i, j):
#      assert i>=0 and j>=0 and i<self.m and j<self.n, 'Grid is ' + str(self.m) + 'x' +str(self.n)+ ', cannot access cell ' + str(i)+','+str(j)
#      return i*self.n + j

   #Get the value of cell at location i,j
   def cell(self,i,j):
       #If the cell asked for is outside of hte grid, return false
       if i<self.m and j<self.n and i>=0 and j>=0:
         return self.grid[i*self.n + j]
       else:
         return False

   #Print the grid of cells
   def printGrid(self):
      #Print the mxn grid of cells
      str= '\n'
      for i in range (0,self.m):
         for j in range(0,self.n):
            if self.cell(i,j):
               str = str + '*  '
            else:
               str = str + '   '
         str = str + '\n'
      print str

   #Given the (i,j)th cell, count its live neighbors
   def getAdj(self,i,j):
      assert i>=0 and j>=0 and i<self.m and j<self.n, 'Attempted to count adjacent cells to invalid location ' + str(i) + ',' + str(j)
      #print('Counting neighbors for cell at ' + str(i) + ',' + str(j))
      neighbors=sum([self.cell(i-1,j-1),self.cell(i,j-1),self.cell(i+1,j-1),self.cell(i-1,j),
         self.cell(i+1,j),self.cell(i-1,j+1),self.cell(i,j+1),self.cell(i+1,j+1)])
      #print(str(neighbors) + ' found')
      return neighbors

   #Check to see whether a given cell will support live next turn  
   def supportsLife(self,i,j):
      if self.getAdj(i,j) == 3:
         return True
      elif self.getAdj(i,j) == 2 and self.cell(i,j):
         return True
      else:
         return False

   #Update self.grid to the next step, given the rules of the game
   def nextStep(self):
      #initialize a brand new grid
      newGrid = []
      
      #Check each location to see if it will be alive or dead, and append to grid array
      for i in range(0,self.m):
         for j in range(0,self.n):
            newGrid.append(self.supportsLife(i,j))
      try:
         self.past2grid = self.lastGrid
         self.lastGrid = self.grid
         self.grid = newGrid
      except: 
         self.lastGrid = self.grid
         self.grid = newGrid

   def historyRepeats(self):
      try:
         if self.grid == self.lastGrid or self.grid == self.past2grid:
            return True
         else:
            return False
      except:
         return False


if __name__ == '__main__':
   sleep=.07
   width=50
   height=40
   density=.2
   
   def runSimulation(sleep,width,height,density):
      game = Game(height,width,density)
      game.printGrid()
      #wait=raw_input('Press enter to begin')
      while(not game.historyRepeats()):
         game.printGrid()
         game.nextStep()
         time.sleep(sleep)
   
      for i in range(0,20):
         game.printGrid()
         game.nextStep()
         time.sleep(sleep)
      print 'The game has ended. Restarting in 5 seconds'
      time.sleep(5)
   
   while True:
      runSimulation(sleep,width,height,density)
   
