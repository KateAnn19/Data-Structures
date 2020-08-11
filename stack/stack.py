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

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        
    def __len__(self):
        size = 0
        if(self.head == None and self.tail == None):
            size = 0
           

        elif(self.head == self.tail):
            size = 1
            
        else:
            current_node = self.head
            while current_node is not None:
                size += 1
                current_node = current_node.next_node
            
        return size

        
    def push(self, value):
        new_node = Node(value)
        self.add_to_tail(value)
        
        
    def pop(self):
        return self.remove_tail()

    def __str__(self):
        return f"Inside stack self.head and self.tail {self.head} {self.tail}\n\n".format(self=self)

   


newStack = Stack()
newStack.push(1)
print(newStack)
newStack.push(2)
print(f"THIS IS LENGTH {len(newStack)}")
print(newStack)
newStack.push(3)
print(f"THIS IS LENGTH {len(newStack)}")

# print(newStack.pop())
# print(newStack)
# print(newStack.pop())
# print(newStack)
# print(newStack.pop())
# print(newStack)
# print(newStack.pop())
# print(newStack)
# print(newStack.__len__())

#newStack.pop()
#print(newStack.__len__())
#newStack.pop()
#print(newStack.__len__())


