from typing import List


class Solution:
    def addToOnes(self,item):
        self.ones.append(item);
    
    def addToZeroes(self,item):
        self.ones.append(item)      
    
    def checkNaibors(self,x,y,isIsland):
            # bala
            if x != 0:
                if self.grid[x-1][y] == '0':
                    self.zeroes.append([x-1,y])
                if  self.grid[x-1][y] == '1':
                    self.ones.append([x-1,y])
                
                self.grid[x-1][y] = '2';
            
            if not isIsland and len(self.ones) != 0: 
                return 1
                
            # jelo
            if y+1 != len(self.grid[0]):
                if self.grid[x][y+1] == '0':
                    self.zeroes.append([x,y+1])
                if self.grid[x][y+1] == '1':
                    self.ones.append([x,y+1])
                
                self.grid[x][y+1] = '2'
            
            if not isIsland and len(self.ones) != 0: 
                return 1
                
            # payin
            if x != len(self.grid)-1:
                if self.grid[x+1][y] == '0':
                    self.zeroes.append([x+1,y])
                if  self.grid[x+1][y] == '1':
                    self.ones.append([x+1,y])
                
                self.grid[x+1][y] = '2';
            
            if not isIsland and len(self.ones) != 0: 
                return 1
                
            # agab
            if y!=0:
                if self.grid[x][y-1] == '0':
                    self.zeroes.append([x,y-1])
                if self.grid[x][y-1] == '1':
                    self.ones.append([x,y-1])
                
                self.grid[x][y-1] = '2'
            
            return 0
    
    def numIslands(self, grid):
        self.grid = grid;
        self.ones = [];
        self.zeroes = [];
        count = 0;
        if len(grid) == 0:
            return 0
        
        if self.grid[0][0] == '0':
            self.zeroes.append([0,0])
        else:
            self.ones.append([0,0])    
        self.grid[0][0] = '2'

        while len(self.ones)!= 0 or len(self.zeroes) != 0:
            if len(self.ones)!= 0:
                x,y = self.ones.pop()
                self.checkNaibors(x,y,True)    
                if len(self.ones) == 0:
                    count +=1
            elif len(self.zeroes)!= 0:
                x,y = self.zeroes.pop()
                if self.checkNaibors(x,y,False) == 1:
                    self.zeroes.append([x,y]);

        return count;