class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

    #method to get the value of the node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node

    #method to get the node's `next_node`
    def get_next(self):
        return self.next_node

   # method to update the node's value
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    # head node and tail node 
    def __init__(self):
        self.head = None # node, that corresponds to our first node in the list
        self.tail = None #stores a node that is the end of the list

    def add_to_head(self, value):
        #create a node to add
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail =  new_node
        else:
            #new_node should point to current head
            new_node.next_node = self.head
            #move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # otherwise, the list had at least one node
        else: 
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            # update self.tail to point the new node we just added 
            self.tail = new_node

    #remove the head and return its' value
    def remove_head(self):
        #if list is empty, do nothing
        if not self.head:
            return None
        #if list only has one element, set head and tail to none
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
            #otherwie we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    
    def contains(self, value):
        if self.head is None:
            return False
        # loop through each node, until we see the value or we cannot go further 
        current_node = self.head
        while current_node is not None:
            #check if this is the node we are looking for 
            if current_node.value == value:
                return True
            #otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def remove_tail(self):
        # check if the linked list is empty 
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node 
        if self.head == self.tail:
            # store the node we're going to remove's value 
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, the linked list has more than one Node 
        else:
            # store the last Node's value in a nother variable so we can return it 
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning 
            
            # starting from the head, we'll traverse down to the second-to-last Node 
            # init another reference to keep track of where we are in the linked 
            # list as we're iterating 
            current = self.head 

            # keep iterating until the node after `current` is the tail
            while current.get_next() != self.tail:
                # keep iterating 
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None) 
            return val
        
    def __str__(self):
        return f"\n\n: Head {self.head}\n{self.tail}".format(self=self)
        
linked_list = LinkedList()
linked_list.add_to_head(0)
linked_list.add_to_tail(10)
# print(f"does our LL contain 0? {linked_list.contains(0)}")
# print(f"does our LL contain 1? {linked_list.contains(1)}")

linked_list.add_to_head(2)
#print(f"the start of the list is {linked_list.head.value}")
linked_list.add_to_head(3)
#print(f"the start of the list is {linked_list.head.value}")

linked_list.remove_head()
#print(f"This is the new head {linked_list.head.value}")
