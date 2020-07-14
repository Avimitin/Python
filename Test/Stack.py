class Node:
    def __init__(self):
        self.item = None
        self.next = None

class Stack:
    def __init__(self):
        self.N = 0
        self.first = Node()

    def isNull(self):
        return self.N == 0
    
    def size(self):
        return self.N

    def push(self,item):
        self.oldFirst = self.first
        self.first = Node()
        self.first.item = item
        self.first.next = self.oldFirst
        self.N = self.N + 1

    def pop(self):
        self.item = self.first.item
        self.first = self.first.next
        self.N = self.N - 1
        return self.item
