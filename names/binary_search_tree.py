"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1 value is less than self.value
        if value < self.value:
            # if no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)

            # ELSE
            else:
                # repeat process on left subtree
                self.left.insert(value)

        # Case 2 value is greater than or equal self.value
        elif value >= self.value:
            # if no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)

            # ELSE
            else:
                # repeat process on right subtree
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isnt in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # have to iterate through the nodes with a loop construct
        if self.right is None:
            return self.value
        else:
            current = self.right
            while current is not None:
                if current.right is not None:
                    current = current.right
                else:
                    return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print(self)
        # visit the node by printing its value
        print(self.value)

        if self.right is not None:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # You should import the queue class from earlier in the
    #     # week and use that class to implement this method
    #     # Use a queue to form a "line" 
    #     # for the nodes to "get in"
    #     queue = Queue()
    #     queue.enqueue(self)

    #     # need a while loop to iterate
    #     # what are we checking in the while statement?
    #     # while length of queue is greater than 0
    #     while len(queue) > 0:
    #         # dequeue item from front of queue
    #         val = queue.dequeue()
    #         # print that item
    #         print(val.value)

    #         # place current item's left node in queue if not None
    #         if val.left:
    #             queue.enqueue(val.left)
    #         # place current item's right node in queue if not None
    #         if val.right:
    #             queue.enqueue(val.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # initialize an empty stack
    #     # push the root node onto the stack
    #     stack = Stack()

    #     stack.push(self)

    #     # need a while loop to manager our iteration
    #     # if stack is not empty enter the while loop
    #     while len(stack) > 0:
    #         # pop top item off the stack
    #         val = stack.pop()
    #         # print that item's value
    #         print(val.value)

    #         # if there is a right subtree
    #         if val.right:
    #             # push right item onto the stack
    #             stack.push(val.right)
                
    #         # if there is a left subtree
    #         if val.left:
    #             # push left item onto the stack
    #             stack.push(val.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
