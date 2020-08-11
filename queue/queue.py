import sys
sys.path.append('../singly_linked_list/')
from singly_linked_list import LinkedList
from singly_linked_list import Node 

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def len (self):
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

    def enqueue(self, value):
        # * `enqueue` adds an element to the back of the queue.
        new_node = Node(value)
        self.storage.add_to_tail(value)
        return self.storage

    def dequeue(self):
        #* `dequeue` removes and returns the element at the front of the queue.
        return self.storage.remove_head()


    
newQ = Queue()
newQ.enqueue(1)
newQ.enqueue(2)

print(newQ.len())
print(newQ.dequeue())

    
  