class UnionFind:
    __grid = []
    __count = 0
    __size = []
    def __init__(self, n):
        i = 0
        while i <= n:
            self.__grid[i] = i
            self.__grid[i] = 1
    
    def find(self, index):
        while index != self.__grid[index]:
            index = self.__grid[index]
            self.__grid[index] = self.__grid[self.__grid[index]]
        
        return index
    
    def connected(self, i, j):
        if self.find(i) == self.find(j):
            return True
        else:
            return False
        
    def union(self, i, j):
        if self.connected(i, j):
            return
        
        if self.__size[i] >= self.__size[j]:
            self.__grid[i] = j
            self.__size[j] = self.__size[j] + self.__size[i]
        elif self.__size[i] < self.__size[j]:
            self.__grid[j] = i
            self.__size[i] = self.__size[j] + self.__size[i]
        
        self.__count = self.__count + 1
            