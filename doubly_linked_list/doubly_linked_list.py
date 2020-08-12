"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def __str__(self):
        return f"{self.prev} <-| {self.value} |-> {self.next}".format(self=self)
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    #dunder method 
    def __len__(self):
        return self.length
   
#  * The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            #new_node should point to current head
            temp = self.head 
            new_node.next = temp
            #move head to new node
            self.head = new_node
            #`add_to_head` replaces the head of the list with a new value that is passed in.
            temp.prev = self.head
            self.length += 1       
       
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #* `remove_from_head` removes the head node and returns the value stored in it.
        oldHead = self.head
        if self.head.next == None:
            print("inside if condition")
            self.head = None
            self.tail = None
            self.length = 0 
            return oldHead.value
        temp = self.head.next
        #temp.prev = None
        self.head = temp 
        self.length -= 1
        #self.delete(self.head)
        return oldHead.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # * `add_to_tail` replaces the tail of the list with a new value that is passed in.
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # otherwise, the list had at least one node
        else:
            # store the old tail
            temp = self.tail 
            # point the node at the current tail, to the new node
            new_node.prev = temp
            self.tail = new_node
            temp.next = self.tail
            #increase the length
            self.length += 1
      
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #* `remove_from_tail` removes the tail node and returns the value stored in it.
        oldTail = self.tail
        if self.tail.prev == None:
            self.head = None
            self.tail = None
            self.length = 0 
            return oldTail.value
        temp = self.tail.prev
        self.tail = temp
        self.length -= 1
        return oldTail 
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
        temp = node 
        self.delete(node)
        temp2 = self.head
        self.head = temp 
        self.head.next = temp2 
        temp2.prev = self.head
        temp.prev = None
        self.length += 1
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #  * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
        temp = node 
        self.delete(node)
        temp2 = self.tail
        self.tail = temp 
        self.tail.prev = temp2
        temp2.next = self.tail
        temp.next = None
        self.length += 1
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List. (delete from anywhere in list)
    """
    def delete(self, node):
        #steps
        #edge cases:
        #Empty list return none
        if self.length == 0:
            return None
        #only one element delete the one element
        # decrement the length by 1 
        if node == self.tail and node == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
        
        #find the node
        # loop through the nodes 
        # start with the head and continue while the node is not found
        
        if node == self.head:
            temp = self.head.next
            self.head = temp
            temp.prev = None
            self.length -= 1
            return
        if node == self.tail:
            temp = self.tail.prev
            self.tail = temp
            temp.next = None
            self.length -= 1
            return


        current_node = self.head
        while current_node is not None:
            ##Head
            #if the node is head remove the pointer for the next node that points back to the head
            #make the next node the new head
            # decrement the length by 1
           
             ##Tail
            #if the node is tail remove the pointer from the prev node that points to tail
            #make the prev node the new tail
            # decrement the length by 1
        
          
            #if the node is found and it is not the head or tail 
            # store the found node into a variable
            #point the prev node to the found node to the next node to the found node 
            #point the next node to the found node back to the prev node to the found node
            # decrement the length by 1

            if node == current_node:
                temp1 = current_node.next
                temp2 = current_node.prev
                temp2.next = temp1
                temp1.prev =  temp2
                self.length -= 1
                break

            current_node = current_node.next
            #check if this is the node we are looking for 
            # if element is never found return None
            

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = 0
        # * `get_max` returns the maximum value in the list.
        current_node = self.head #create a tracker node variable
        while current_node is not None: #loop until its None
            if(current_node.value > max):
                max = current_node.value
            current_node = current_node.next # update the tracker node to the next node 
        return max

    def __str__(self):
        output = ''
        current_node = self.head #create a tracker node variable
        while current_node is not None: #loop until its None
            # output += f'{current_node.prev if current_node.prev is not None else -1}<- {current_node.value} ->{current_node.next}'
            output += f'<- {current_node.value} ->'
            current_node = current_node.next # update the tracker node to the next node 
        return output.format(self=self)


    #UPER method

double = DoublyLinkedList()
double.add_to_head(10)
double.add_to_head(11)
double.add_to_head(12)
double.add_to_tail(100)
print(double)