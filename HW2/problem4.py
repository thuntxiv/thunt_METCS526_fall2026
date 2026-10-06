# METCS 526 Fall 2026 - HOMEWORK 2
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 4----------------------------

class Node:
    '''
    An object representing a node in an any abstract linked structure that
    contains any type of value and pointers to the previous and next nodes.
    '''
    value = None
    prev = None
    next = None

    def __init__(self, value):
        self.value = value

class SortedDoublyLinkedList:
    '''
    An object representing a sorted, doubly-linked list as a container.
    The values kept in its nodes must be numeric (int, float) because
    the class' statistical operations will not function otherwise.

    FIELDS
        head:Node
            A pointer to the node at the head of the list (i.e. the first node)
        tail:Node
            A pointer to the node at the tail of the list (i.e. the last node)
        size:INT
            The number of nodes that the list is currently holding
    '''
    head:Node = None
    tail:Node = None
    size = 0

    # No need for an init override since the fields are initialized already

    # Operations implemented in pdf order for better readability

    def rec_add(self, value, head):
        '''
        Recursive helper function for add() that traverses the list and adds a node with
        the given value to the list at its correct sorted position

        PARAMETERS
            value:INT or FLOAT
                A numeric value to be stored in the node.
            head:Node
                A pointer to the head of the remaining list to be traversed
        RETURN
            None
        '''
        if head == None: # No nodes yet; make node the head and tail
            new_node = Node(value) # Only make the node object if we know that this is the right spot
            self.head = new_node
            self.tail = new_node
        elif value < head.value: # If the head's value is greater, insert the new node before it
            new_node = Node(value)
            new_node.next = head
            if head == self.head: # Inserting at the beginning of the list
                self.head = new_node
            else:
                new_node.prev = head.prev # Inserting between nodes
                head.prev.next = new_node
            head.prev = new_node
        elif head.next == None: # Inserting at the end of the list
            new_node = Node(value)
            head.next = new_node
            new_node.prev = head
            self.tail = new_node
        else:
            self.rec_add(value, head.next)

    def add(self, value):
        '''
        Adds a new node containing the given value to the list at its correct
        position to maintain the sorted order of the list

        PARAMETERS
            value:INT or FLOAT
                A numeric value to be stored in the node.
        RETURN
            None
        '''
        self.rec_add(value, self.head)
        self.size += 1

    def rec_delete(self, value, head:Node):
        '''
        Recursive helper function for delete()
        Removes head if it contains the given value, and keeps searching the list otherwise
        Returns a boolean according to whether the value was found and deleted or not.

        PARAMETERS
            value:INT or FLOAt
                The numerical value of the node to be searched for and deleted if found
            head:Node
                a pointer to the head of the section of the list that still needs to be searched
        RETURN
            BOOL
                True if the value was found in the list and the node was successfully deleted
                False if the value was not found and no nodes were deleted
        '''
        if head == None: # Value not found; No nodes deleted
            return False
        elif value == head.value:
            if self.size == 1: # Deleting the only node in the list
                self.head = None
                self.tail = None
            elif head == self.head: # Deleting the head
                self.head = head.next
                head.next.prev = None
            elif head == self.tail: # Deleting the tail
                self.tail = head.prev
                head.prev.next = None
            else: # Deleting a middle node
                head.prev.next = head.next
                head.next.prev = head.prev
            head.next = None
            head.prev = None
            return True
        else: # Keep searching for value recursively
            return self.rec_delete(value, head.next)

    def delete(self, value):
        '''
        Removes the first node holding the given value, and returns a boolean according to whether the value was found and deleted or not.

        PARAMETERS
            value:INT or FLOAT
                The numerical value of the node to be searched for and deleted if found
        RETURN
            BOOL
                True if the value was found in the list and the node was successfully deleted
                False if the value was not found and no nodes were deleted
        '''
        removed = self.rec_delete(value, self.head)
        if removed:
            self.size -= 1
        return removed
    
    def rec_exists(self, value, head:Node):
        '''
        Recursive helper function for exists()
        Returns a boolean indicating whether the given head node's value matches the parameter value
        Otherwise, recursively searches further down the list.

        PARAMETERS
            value:INT or FLOAT
                The numerical value to have the index of its encapsulating node searched for in the list
            head:Node
                A pointer to the head of the remaining list to search
        RETURN
            INT
                The positive index of the first node containing the given value
                -1 if the value was not found
        '''
        # Value does not exist if we have searched all nodes or we have reached sorted values
        #   greater than the parameter value
        if head == None or head.value > value: 
            return False
        if value == head.value:
            return True
        return self.rec_exists(value, head.next)
        
    def exists(self, value):
        '''
        Returns a boolean indicating whether the given value exists in the list or not.

        PARAMETERS
            value:INT or FLOAT
                The numerical value to have the index of its encapsulating node searched for in the list
        RETURN
            INT
                The positive index of the first node containing the given value
                -1 if the value was not found
        '''
        return self.rec_exists(value, self.head)

    def rec_print_list(self, head:Node):
        '''
        Recursive helper function for print_list. 
        Prints the list to stdout in the format "(value) <-> (value) <-> (value)" and so on

        PARAMETERS
            head:Node
                The head of the remaining list to be printed
        RETURN
            None
        '''
        print(head.value, end='')
        if head.next != None:
            print(" <-> ", end='')
            self.rec_print_list(head.next)
        else:
            print()

    def print_list(self):
            '''
            Prints the list to stdout in the format "(value) <-> (value) <-> (value) <->..."
    
            PARAMETERS
                None
            RETURN
                None
            '''
            if self.size == 0:
                print("(empty)")
            else:
                self.rec_print_list(self.head)

    def rec_total(self, head:Node):
        '''
        Recursively computes the sum of all values from the given head to the tail of the list

        PARAMETERS
            head:Node
                A pointer to the head of the remaining list to traverse and sum up
        RETURN
            INT or FLOAT
                A number representing the sum of the values in the list following and including the given head
                node.
                Float if the list contains any floating point numbers, Int otherwise.
        '''
        if head == None:
            return 0
        return head.value + self.rec_total(head.next)
    
    def total(self):
        '''
        Returns the sum of all values contained in the nodes of the list

        PARAMETERS
            None
        RETURN
            INT or FLOAT
                A number representing the sum of all values contained in the list's nodes
                Float if any floats are contained in the list, Int otherwise
        '''
        return self.rec_total(self.head)

    def rec_sum_middle_three(self, head:Node, index):
        '''
        Recursively traverses the list until the middle is reached,
        where the sum of the middle three elements is returned.

        PARAMETERS:
            head:Node
                A pointer to the head of the remaining list to be traversed
            index:INT
                An integer representing the index of the current head node within the larger list
        '''
        if index == self.size // 2: # mid = n // 2
            if self.size % 2 == 0: # Even list size: mid-2 + mid-1 + mid
                return head.prev.prev.value + head.prev.value + head.value
            else: # Odd list size: mid-1 + mid + mid+1
                return head.prev.value + head.value + head.next.value
        return self.rec_sum_middle_three(head.next, index + 1) # Continue traversing until the middle is reached

    def sum_middle_three(self):
        '''
        Returns the sum of the middle three node values of the list.

        PARAMETERS:
            None
        RETURN:
            INT
                An integer representing the sum of the list's middle three values
        '''
        if self.size < 3:
            raise ValueError("sum_middle_three needs at least 3 nodes")
        return self.rec_sum_middle_three(self.head, 0)

    def rec_median(self, head:Node, index):
        '''
        Recursively traverses the list until the middle node is reached, then
        returns the median of the list found at that location.
        If the list has an even number of nodes, the median is the average of the
        middle two values.

        PARAMETERS
            head:Node
                A pointer to the head of the remaining list to be traversed
            index:INT
                An integer representing the index of the current head in the larger list
        RETURN
            FLOAT
                If the size of the list is even, since the median is an average of two values,
                or if the value at the middle index is a float
            INT
                If the size of the list is odd and the value at the middle index is an integer
        '''
        if index == self.size // 2:
            if self.size % 2 == 0: # Even list size: Take average
                return float(head.value + head.prev.value) / 2
            else: # Odd list size: Return value
                return head.value 
        return self.rec_median(head.next, index + 1)

    
    def median(self):
        '''
        Returns the median value of the list's held values.

        PARAMETERS:
            None
        RETURN
            FLOAT
                If the list has an even number of elements, since the median is an average of two values,
                or, with an odd number of elements, if the value at the list's middle index is of type float
            INT
                If the list has an odd number of elements, and the value at the middle index is an integer
        '''
        if self.size == 0:
            raise ValueError("List is empty")
        return self.rec_median(self.head, 0)

    def rec_count(self, value, head):
        '''
        Returns the number of times that the given value occurs within the list.
        
        PARAMETERS
            value:INT or FLOAT
                The numerical value to check for how many times it appears in the list's nodes
            head:Node
                The head pointer of the remaining list to be searched
        RETURN
            INT
                An integer representing the number of times that the value occurs in the list
        '''
        # The search ends when there are no more nodes left to check, or the values in
        # this sorted section of the list have exceeded the given value
        if head == None or head.value > value:
            return 0
        if head.value == value: # Keep counting, there could be duplicates
            return 1 + self.rec_count(value, head.next)
        return self.rec_count(value, head.next)

    def count(self, value):
        '''
        Returns the number of times that the given value occurs within the list.

        PARAMETERS
            value:INT or FLOAT
                The numerical value to check for how many times it appears in the list's nodes
        RETURN
            INT
                An integer representing the number of times that the value occurs in the list
        '''
        return self.rec_count(value, self.head)

    def __len__(self): # No reason not to keep this function
        '''
        Returns the number of nodes currently held in the list

        PARAMETERS:
            None
        RETURN
            INT
                The number of nodes currently in the list
        '''
        return self.size

def main():
    # Initial testing
    L1 = SortedDoublyLinkedList()
    L1.add(10)
    L1.add(4)
    L1.add(29)
    L1.add(8)
    L1.add(2)
    L1.add(15)
    L1.add(41)
    L1.print_list()

if __name__ == "__main__":
    main()