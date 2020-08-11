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


#queue with an array data structure 
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
        
#     def __len__(self):
#         return self.size
               
#     def push(self, value):
#        self.size += 1
#        self.storage.append(0, value)
        
#     def pop(self):
#         check if empty
#         if len(self.storage) == 0:
#             return None            
#         self.size -= 1
#         node = self.storage.pop(0)
#         return node

class Queue(LinkedList):
    def __init__(self):
        self.storage = LinkedList()
        super().__init__()
    
    def __len__ (self):
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

    def enqueue(self, value):
        # * `enqueue` adds an element to the back of the queue.
        new_node = Node(value)
        self.add_to_tail(value)
        

    def dequeue(self):
        #* `dequeue` removes and returns the element at the front of the queue.
        return self.remove_head()


    
newQ = Queue()
newQ.enqueue(1)
newQ.enqueue(2)


print(newQ.dequeue())

    
  