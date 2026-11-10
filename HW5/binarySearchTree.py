# METCS 526 Fall 2026 - HOMEWORK 5
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 1----------------------------

import random

class Node:
    '''
    An abstract data type representing a node that contains some value and holds pointers
    to its left and right children. Can be used for nodes in a binary tree.

    FIELDS
        value:Any
            A value of any type
        left:Node
            This Node object's left child Node
        right:Node
            This Node object's right child Node
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    '''
    An abstract data type representing a Binary Search Tree, containing nodes where every
    value in a given node's left subtree is less than the parent node's value, and every value
    in the node's right subtree is greater than or equal to that value. All values must be integers.

    FIELDS
        root:Node<INT>
            The node at the root of the binary search tree
    '''

    def __init__(self):
        self.root = Node(None)
        
    def add_Node(self, value:int):
        '''
        Adds a node with the given integer value to the Binary Search Tree at its
        appropriate position to maintain the sorted nature of the tree.
        If there are currently no values in the tree, this value becomes the root.

        PARAMETERS
            value:INT
                The integer value to add to the Binary Search Tree
        RETURN
            None
        '''
        # No values in the tree: Make this the root
        if self.root.value == None:
            self.root = Node(value)
            # Initialize sentinel nodes for the root
            self.root.left = Node(None)
            self.root.right = Node(None)
        else:
            # Need to search for the new node's correct sorted position
            curr_node = self.root
            while curr_node.value != None:
                # If a sentinel node is reached, then update the sentinel node's value
                # and extend new sentinel nodes. Otherwise, keep traversing down the subtree
                if value < curr_node.value: # Less than = left subtree
                    if curr_node.left.value == None:
                        curr_node.left.value = value
                        curr_node.left.left = Node(None)
                        curr_node.left.right = Node(None)
                        break
                    else:
                        curr_node = curr_node.left
                else: # Greater than or equal to = right subtree
                    if curr_node.right.value == None:
                        curr_node.right.value = value
                        curr_node.right.left = Node(None)
                        curr_node.right.right = Node(None)
                        break
                    else:
                        curr_node = curr_node.right


    def delete_Node(self, value:int):
        '''
        Deletes the first node found with the given value from the Binary Search Tree,
        then repairs the tree by moving nodes from the deleted node's subtree until
        the hole in the tree is patched and the sorted order is maintained.
        Returns a boolean indicating whether the node was found and deleted or not.

        PARAMETERS
            value:INT
                The value of the node to delete from the tree
        RETURN
            BOOl
                True if a node with the given value was found and successfully deleted
                    from the tree.
                False if no node with the given value exists in the tree, and no nodes
                    were deleted.
        '''
        # Check if the value exists in the tree
        if not self.find_Node(value):
            return False

        # Update the root in case the root itself is deleted
        self.root = self.rec_delete_node(self.root, value)
        return True


    def rec_delete_node(self, node:Node, value:int):
        '''
        A recursive helper function for delete_Node that handles searching for and deleting
        the node with the given value, as well as patching the hole in the tree that is
        created upon deletion.

        PARAMETERS
            node:NODE
                The current node to check for a value match for deletion
            value:INT
                The current integer value to be deleted from the tree
        RETURN
            NODE
                The node to replace the deleted node in the tree (at the current level,
                depending on if multiple nodes need to be moved up)
        '''
        # Empty node
        if node.value is None:
            return node

        # Search the left subtree and reconnect it
        if value < node.value:
            node.left = self.rec_delete_node(node.left, value)

        # Search the right subtree and reconnect it
        elif value > node.value:
            node.right = self.rec_delete_node(node.right, value)

        # Value found: check number of children
        else:
            # Node has no left child: delete and replace with right child
            if node.left.value is None:
                return node.right

            # Node has no right child: delete and replace with left child
            elif node.right.value is None:
                return node.left

            # Node has two children: need to search for a replacement
            else:
                # Find the in-order predecessor (largest value of left subtree)
                predecessor = node.left
                while predecessor.right.value is not None:
                    predecessor = predecessor.right

                # Replace the current value with the predecessor
                node.value = predecessor.value

                # Recursively delete the predecessor from its original location
                node.left = self.rec_delete_node(node.left, predecessor.value)

        return node


    def find_Node(self, value:int):
        '''
        Searches the Binary Search Tree for a node with the given value and returns a
        boolean indicating whether or not the value exists in the tree.

        PARAMETERS
            value:INT
                The value to search for in the tree
        RETURN
            BOOL
                True if the value exists in the tree
                False if the value does not exist in the tree
        '''
        curr_node = self.root
        # Use the sorted nature of the BST to traverse the appropriate subtree
        while curr_node.value != None:
            if curr_node.value == value:
                return True
            # Less than = left subtree
            if value < curr_node.value:
                curr_node = curr_node.left
            # Greater than = right subtree
            else:
                curr_node = curr_node.right
        # If a sentinel node is reached, the value does not exist
        return False

    def print_tree(self):
        '''
        Prints the Binary Search Tree to stdout in a horizontal hierarchical structure,
        with the root at the leftmost position and all following child nodes progressing
        to the right.

        PARAMETERS
            None
        RETURN
            None
        '''
        if self.root.value is None:
            print("(empty)")
        else:
            self.rec_print_tree(self.root)
    
    def rec_print_tree(self, node, level=0, prefix="Root: "):
        '''
        
        '''
        if node.value != None:
            # Print the right subtree first (appears on top)
            self.rec_print_tree(node.right, level + 1, "R--- ")
            
            # Print the current node with indentation
            print(" " * 4 * level + prefix + str(node.value))
            
            # Print the left subtree (appears on bottom)
            self.rec_print_tree(node.left, level + 1, "L--- ")

def main():
    '''
    Runs randomized tests of all functions of the Binary Search Tree
    '''
    tree = BST()

    # Size: randomized from 5-50
    size = random.randint(5, 50)
    node_vals = []

    # Add random integers to the tree from 1-1000
    for _ in range(size):
        num = random.randint(1, 1000)
        tree.add_Node(num)
        print(f"Add Node: {num}")
        node_vals.append(num) # Keep track of nodes for find and delete tests
        tree.print_tree()
        print()
    # Attempt to find randomized values
    for _ in range(size // 2):
        num = random.randint(1, 1000)
        print(f"find_Node ({num}): {tree.find_Node(num)}")
    # Find random values that exist in the tree
    for _ in range(size // 2):
        num = node_vals[random.randint(0, len(node_vals) - 1)]
        print(f"find_Node ({num}): {tree.find_Node(num)}")
    # Attempt to delete randomized values
    for _ in range(size // 2):
        num = random.randint(1, 1000)
        deleted = tree.delete_Node(num)
        print(f"delete_Node ({num}): {deleted}")
        if deleted:
            tree.print_tree()
    # Delete all remaining values in the tree
    #   Note: despite iterating through node_vals in order, this still effectively
    #   deletes values at "random" points in the tree because its sorted nature
    #   places each node at a spot not fully dependent on the order it was added.
    for value in node_vals:
        deleted = tree.delete_Node(value)
        print(f"delete_Node ({value}): {deleted}")
        if deleted:
            tree.print_tree()


if __name__ == "__main__":
    main()