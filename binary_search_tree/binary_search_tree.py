"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
​
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.


   Rules:
    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.

"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # another way to do this part 1   
            # base case 
            # if value < self.value:
            #     if self.left is None:
            #         self.left = BSTNode(value)
            #     else:
            #         self.left.insert(value)
            # base case
            # else:
            #     if self.right is None:
            #         self.right = BSTNode(value)
            #     else:
            #         self.right.insert(value)
            # another way to do this    
            
            # another way to do this part 2
            #if value < self.value and self.left is None:
            #   self.left = BSTNode(value)
            #if value >= self.value and self.right is None:
            #   self.right = BSTNode(value)
            #else:
                # if value < self.value 
                # self.left.insert(value)
                # else 
                # self.right.insert(value)
            # 
            # another way to do this  
        
            #take the current value of our node (self.value)
            #compare to the new value we want to insert
            # if new value < self.value
                #if self.left is already taken by a node
                #make that node, call insert
                #set the left to the new node with the new value
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            else:
                # otherwise, it doesn't have a left child 
                # we can park the new node here 
                self.left = BSTNode(value)
         #if new value >= self.value
                #if self.right is already taken by a node
                    #make that node call insert
                #set the right child to the new node with new value    
        else:  
            # does the current node have a right child?
            if self.right:
                self.right.insert(value)
            # otherwise, it doesn't have a right child 
            # we can park the new node here         
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        found = False 
        #compare the target to current value
        #if current value < target
        if  target >= self.value:
            #check the left subtree (self.left.contains(target))
            if self.right is None:
                return False
            found = self.right.contains(target)
        if target < self.value:
            #check if right subtree contains target
            if self.left is None:
                return False 
            found = self.left.contains(target)
        return found


    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        if self.right is None: 
            return self.value

        if self.right.get_max() > self.value:
            print(f"Inside the recursive call {self.value}")
            max_value = self.right.get_max()
        #else:
            # print(f"Inside the base case {self.value}")
            # max_value = self.value
        print(max_value)
        return max_value
            

    # Call the function `fn` on the value of each node
    # This method doesn't return anything 
    def for_each(self, fn):
            

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass
    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_print(self):
        pass
    # Print Post-order recursive DFT
    def post_order_print(self):
        pass

"""
This code is necessary for testing the `print` methods
"""


bst = BSTNode(1) #root node
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
#bst.get_max()
bst.bft_print()
bst.dft_print()
print("elegant methods")
print("pre order")
bst.pre_order_print()
print("in order")
#bst.in_order_print()
print("post order")
bst.post_order_print()
