class ArrayStack:
    def __init__(self, size):
        self.__N = size
        self.__stack = []
    
    def push(self, item):
        self.__stack[self.__N] = item
        self.__N = self.__N + 1
    
    def pop(self):
        item = self.__stack[self.__N]
        self.__N = self.__N - 1
        return item

    def size(self):
        return self.__N
    
    def isEmpty(self):
        return self.__N == 0