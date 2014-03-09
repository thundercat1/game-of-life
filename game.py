import random

class Game:
   def __init__(self, fertility=False):
      print 'new game created'
      #Start by defining a m x n grid size
      self.m = 10 #m rows
      self.n = 10 #n columns
      
      #If the fertility parameter was not passed at initialization, get it from the user
      if not fertility:
         fertility = input("Enter, as decimal, the land's fertility:  ")
      assert fertility>0 and fertility<1 , 'fertility set to ' + str(fertility) + '. Must be between 0 and 1'
      
      #Initializes the grid with randomly generated cells according to fertility probability
      def seedCellsToGrid():
         #Initialize the cells in the starting grid
         self.grid = []
         for cell in range(0,self.m*self.n):
            self.grid.append(random.random()>fertility)
      seedCellsToGrid()
   
   #Get the array index given i,j
   def cellIndex(self, i, j):
      assert i<self.m and j<self.n, 'Grid is ' + str(self.m) + 'x' +str(self.n)+ ', cannot access cell ' + str(i)+','+str(j)
      return i*self.n + j

   #Get the value of cell at location i,j
   def cell(self,i,j):
      assert i<self.m and j<self.n, 'Grid is ' + str(self.m) + 'x' +str(self.n)+ ', cannot access cell ' + str(i)+','+str(j)
      return self.grid[i*self.n + j]

   #Print the grid of cells
   def printGrid(self):
      #Print the mxn grid of cells
      str= '\n'
      for i in range (0,self.m):
         for j in range(0,self.n):
            if self.cell(i,j):
               str = str + '*  '
            else:
               str = str + '-  '
         str = str + '\n'
      print str
      return False

   #Given the (i,j)th cell, count its neighbors
   def getAdj(self,i,j):
      return False

   #Update self.grid to the next step, given the rules of the game
   def nextStep(self):
      return False


      







if __name__ == '__main__':
   game = Game(.5)
   game.printGrid()
  
