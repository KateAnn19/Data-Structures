import sys
sys.path.append('../singly_linked_list/')
from singly_linked_list import LinkedList
from singly_linked_list import Node 
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

4. last in first out
"""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()
        # self.new_node = Node(value)

    def len(self):
        if(self.storage.head == None and self.storage.tail == None):
            return self.size
        if(self.storage.head == self.storage.tail):
            self.size = 1
            return self.size
        current = self.storage.head 
        # keep iterating until the node after `current` is the tail
        while current.get_next() != self.storage.tail:
             # keep iterating 
            current = current.get_next()
            self.size += 1
        self.size += 2 # one for the head and one for the tail
        return self.size

        while self.storage.get_next() != self.storage.tail:
            # keep iterating 
            self.size += 1
        self.size += 1    
        return self.size
        
    def push(self, value):
        new_node = Node(value)
        self.storage.add_to_tail(value)
        return self.storage
        
    def pop(self):
        return self.storage.remove_tail()

   


newStack = Stack()
newStack.push(1)
newStack.push(2)
newStack.push(3)
print(newStack.len())
print(newStack.pop())
