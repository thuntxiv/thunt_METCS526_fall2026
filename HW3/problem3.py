# METCS 526 Fall 2026 - HOMEWORK 3
# Author: Tyler Hunt; Professor: Dr. David Mellor

import numpy as np

#------------------------------PROBLEM 3----------------------------

class Stack:
    '''
    A parent class representing a Stack structure that contains elements and uses
    LIFO (Last-in, First-out) order for adding and removing elements.

    This class by itself is not functional; It is implemented in its child classes:
        StackArray
        StackSinglyLinked
        StackDoublyLinked

    FIELDS
        size:INT
            An integer count of how many elements are currently held in the stack
    '''
    size = 0

    def push(self, value):
        '''
        Adds an element to the top of the stack.

        PARAMETERS
            value:Any
                The value to add to the stack
        RETURN
            None
        '''
        pass

    def pop(self):
        '''
        Removes the element from the top of the stack and returns its value

        PARAMETERS
            None
        RETURN
            Any
                The value of the element that was removed from the stack
        '''
        pass

    def peek(self):
        '''
        Returns the value currently at the top of the stack. Does not modify the stack.

        PARAMETERS:
            None
        RETURN
            Any
                The value of the element at the top of the stack
        '''
        val = self.pop()
        self.push(val)
        return val

    def is_empty(self):
        '''
        Returns a boolean indicating whether the Stack is empty or not.

        PARAMETERS
            None
        RETURN
            True if the stack is empty
            False if the stack has at least one element
        '''
        return self.size == 0

    def __len__(self):
        '''
        Returns an integer representing the number of elements currently contained in the stack

        PARAMETERS
            None
        RETURN
            INT
                The number of elements currently present in the stack
        '''
        return self.size
    
    def print_stack(self):
        '''
        Prints the contents of the stack from bottom-to-top
            (i.e. for stack 1, 2, 3, 4: 1 is at the bottom of the stack, and 4 is at the top)
        
        PARAMETERS
            None
        RETURN
            None
        '''
        pass

class StackArray(Stack):
    '''
    A Stack implemented as a fixed-size array.
    Contains integers and uses a LIFO order for adding and removing values.
    Stores empty slots in the stack as the value -1.
    Cannot be expanded.

    FIELDS
        size:INT
            An integer count of how many elements are currently held in the stack
        maxsize:INT
            An integer representing the maximum number of elements that the stack can hold
        stack:ARRAY<INT>
            A fixed-size array of integers representing the stack structure
    '''
    
    def __init__(self, size):
        '''
        Initializes the empty stack as an array with the given initial maximum size

        PARAMETERS
            size:INT
                The maximum size of the array before it must be expanded
        '''
        self.size = 0
        self.maxsize = size
        self.stack = np.array([-1] * size) # Use -1 to represent empty stack cells

    def push(self, value):
        '''
        Adds an element to the top of the stack if the stack is not full.

        PARAMETERS
            value:INT
                An integer value to add to the stack
        RETURN
            None
            Raises IndexError if the stack is full and cannot be pushed onto
        '''
        if self.size == self.maxsize: # Raise an error if full
            raise IndexError("Stack is full")
        self.stack[self.size] = value # Replace the value at the next available index
        self.size += 1

    def pop(self):
        '''
        Removes the element from the top of the stack and returns its value

        PARAMETERS
            None
        RETURN
            INT
                The integer value of the element that was removed from the stack
        '''
        if self.size > 0:
            # Use indexing, a placeholder value of -1, and decrementing the stack's size to effectively remove the element
            val = self.stack[self.size - 1]
            self.stack[self.size - 1] = -1
            self.size -= 1
            return val

    def print_stack(self):
        '''
        Prints the contents of the stack from bottom-to-top
            (i.e. for '1, 2, 3, 4': 1 is at the bottom of the stack, and 4 is at the top)
        
        PARAMETERS
            None
        RETURN
            None
        '''
        for i in range(self.size):
            if i != 0:
                print(", ", end = "")
            print(self.stack[i], end="")
        print()

class Node:
    '''
    Represents a node object that holds a value and stores pointers to the previous
    and next nodes in its encapsulating structure.
    If used in a singly-linked list, prev will always be None.
    '''
    value = None
    prev = None
    next = None

    def __init__(self, val):
        '''
        Initializes a node with None pointers and the given value

        PARAMETERS
            val:Any
                The value to store in the node
        RETURN
            None
        '''
        self.value = val

class StackSinglyLinked(Stack):
    '''
    A Stack implemented as a singly-linked list.
    Contains elements of any value and uses a LIFO order for adding and removing values.
    Can contain any number of elements.

    FIELDS
        size:INT
            An integer count of how many elements are currently held in the stack
        head:Node
            A pointer to the node at the head of the linked list
        tail:Node
            A pointer to the node at the end of the linked list
    '''

    size = 0
    head = None
    tail = None

    def push(self, value):
        '''
        Adds an element to the top of the stack.

        PARAMETERS
            value:INT
                An integer value to add to the stack
        RETURN
            None
        '''
        new_node = Node(value)
        if self.head != None: # Add to top of stack (aka end of list)
            self.tail.next = new_node
            self.tail = new_node
        else: # No elements present
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        '''
        Removes the element from the top of the stack and returns its value

        PARAMETERS
            None
        RETURN
            INT
                The integer value of the element that was removed from the stack
        '''
        if self.is_empty(): # Stack is empty
            return None
        popped_node = None
        if self.size == 1: # Removing the last element in the list
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            curr_node = self.head
            while curr_node.next != self.tail: # Iterate to the second to last node
                curr_node = curr_node.next
            popped_node = self.tail # Adjust the tail and next pointer
            curr_node.next = None
            self.tail = curr_node
        self.size -= 1
        return popped_node.value

    def print_stack(self):
        '''
        Prints the contents of the stack from bottom-to-top
            (i.e. for '1, 2, 3, 4': 1 is at the bottom of the stack, and 4 is at the top)
        
        PARAMETERS
            None
        RETURN
            None
        '''
        if self.is_empty():
            print("(empty)")
            return
        curr_node = self.head
        while curr_node != None:
            if curr_node != self.head:
                print(", ", end = "")
            print(curr_node.value, end="")
            curr_node = curr_node.next
        print()


class StackDoublyLinked(Stack):
    
    size = 0
    head = None
    tail = None

    def push(self, value):
        '''
        Adds an element to the top of the stack.

        PARAMETERS
            value:INT
                An integer value to add to the stack
        RETURN
            None
        '''
        new_node = Node(value)
        if self.head != None: # Add to top of stack (aka end of list)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else: # No elements present
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        '''
        Removes the element from the top of the stack and returns its value

        PARAMETERS
            None
        RETURN
            INT
                The integer value of the element that was removed from the stack
        '''
        if self.is_empty(): # Empty stack
            return None
        popped_node = None
        if self.size == 1: # Removing last element in the stack
            popped_node = self.head
            self.head = None
            self.tail = None
        else: # Still elements remaining after the pop
            popped_node = self.tail
            popped_node.prev.next = None
            self.tail = popped_node.prev
            popped_node.prev = None
        self.size -= 1
        return popped_node.value

    def print_stack(self):
        '''
        Prints the contents of the stack from bottom-to-top
            (i.e. for '1, 2, 3, 4': 1 is at the bottom of the stack, and 4 is at the top)
        
        PARAMETERS
            None
        RETURN
            None
        '''
        if self.is_empty():
            print("(empty)")
            return
        curr_node = self.head
        while curr_node != None:
            if curr_node != self.head:
                print(", ", end = "")
            print(curr_node.value, end="")
            curr_node = curr_node.next
        print()

    def reverse_doubly(self):
        '''
        An alternative reversing method that reverses the order of all nodes' pointers
        (i.e. the head becomes the tail and vice versa, and all nodes' prev and next pointers are swapped)

        PARAMETERS
            None
        RETURN
            None
        '''
        self.head, self.tail = self.tail, self.head
        self.rec_reverse_doubly(self.head)

    def rec_reverse_doubly(self, tail):
        '''
        A recursive helper function for reverse_doubly that reverses the direction of the
        current node's pointers (i.e. next becomes prev and vice versa), then recurses
        backwards through the list until all nodes have been flipped.

        PARAMETERS
            tail:Node
                The tail of the remaining stack to be reversed
        RETURN
            None
        '''
        if tail != None:
            curr_node = tail
            # Flip the direction of the prev and next pointers
            next_node = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = next_node
            curr_node = next_node
            self.rec_reverse_doubly(curr_node) # Keep recursing backwards through the list

def push_bottom(stack:Stack, val):
    '''
    Helper function for reverse_stack that adds the given value to the *bottom* of the stack recursively,
    unlike push which adds to the top of the stack

    PARAMETERS
        stack:STACK
            The stack to push the given value into
        val:ANY
            A value to add to the bottom of the stack
    RETURN
        None
    '''
    if stack.is_empty(): # Base case: When the stack is empty, we can just push and that adds val to the bottom
        stack.push(val)
    else: # Recursive case: We need to temporarily pop the current top and move downward to reach the bottom of the stack
        temp_val = stack.pop()
        push_bottom(stack, val) # Keep moving down the stack
        stack.push(temp_val) # Put the temp value back after performing the push to the bottom

def reverse_stack(stack:Stack):
    '''
    Reverses the order of the given stack so that the bottom is now the top, and vice versa

    PARAMETERS
        stack:STACK
            The stack to have its elements reversed
    RETURN
        None
    '''
    if not stack.is_empty(): # Recursively pop nodes, then push nodes to the bottom as we fold the recursion back up
        val = stack.pop()
        reverse_stack(stack)
        # Once we have reached the bottom (the top of the old stack), push to the bottom of the stack starting
        # at the former top elements
        push_bottom(stack, val) 

def main():
    #print("Array Implementation:")
    stack = StackArray(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    print("Before: ", end="")
    stack.print_stack()
    reverse_stack(stack)
    print("After: ", end="")
    stack.print_stack()

    #print("Singly-Linked List Implementation:")   
    stack1 = StackSinglyLinked()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    stack1.push(6)
    stack1.push(7)
    stack1.push(8)
    stack1.push(9)
    stack1.push(10)
    print("Before: ", end="")
    stack1.print_stack()
    reverse_stack(stack1)
    print("After: ", end="")
    stack1.print_stack()

    #print("Doubly-Linked List Implementation:")
    stack2 = StackDoublyLinked()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    stack2.push(4)
    stack2.push(5)
    stack2.push(6)
    stack2.push(7)
    stack2.push(8)
    stack2.push(9)
    stack2.push(10)
    print("Before: ", end="")
    stack2.print_stack()
    stack2.reverse_doubly()
    print("After: ", end="")
    stack2.print_stack()

    #print(stack2.peek())

    #stack2.reverse_doubly()
    #reverse_stack(stack2)
    #print("After (doubly-linked reverse method): ", end="")
    #stack2.print_stack()

if __name__ == "__main__":
    main()