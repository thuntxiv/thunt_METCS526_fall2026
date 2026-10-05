# METCS 526 Fall 2026 - HOMEWORK 2
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 2----------------------------

class Node:
    '''
    An object representing a node in an any abstract linked structure that
    contains any type of value and a pointer to the next node 
    (None if it's the final node in the structure).
    '''
    value = None
    next = None

    def __init__(self, value):
        self.value = value

class SinglyLinkedList:
    '''
    An object representing a singly-linked list as a container. 
    Supports all standard CRUD operations.

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

    # CREATE operations

    def append(self, value):
        '''
        Adds a new node containing the given value to the end of the linked list
        as the new tail.

        PARAMETERS
            value:Any
                A value of any type to be stored in the node
        RETURN
            None
        '''
        new_node = Node(value)
        if self.head == None: # No nodes yet; make node the head and tail
            self.head = new_node
            self.tail = new_node
        else: # One or more nodes present; Extend from tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        '''
        Adds a new node containing the given value to the start of the linked list
        as the new head.

        PARAMETERS
            value:Any
                A value of any type to be stored in the node
        RETURN
            None
        '''
        new_node = Node(value)
        if self.head == None: # No nodes yet; make node the head and tail
            self.head= new_node
            self.tail = self.head
        else: # One or more nodes present; Insert before head
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert(self, index:int, value):
        '''
        Adds a new node containing the given value at the given index within the
        list. Raise an IndexError if the given index is out of the list's bounds

        PARAMETERS
            index:INT
                An integer index indicating which position in the list to insert
                the new node into
                May be a negative number (-1 = [len - 1], -2 = [len - 2], etc.)
            value:Any
                A value of any type to be stored in the node
        RETURN
            None
            IndexError
                If the parameter index is outside of the list's bounds
        '''
        if index < 0: # Check if the index is negative; adjust to the corresponding positive index
            index = self.size + index
        if index > self.size or index < 0: # Check if the index is valid; Raise an error if so
            raise IndexError("Index out of bounds")
        if index == self.size: # If inserting at the end, just call append to save time
            self.append(value)
            return

        current_index = 0
        current_node = self.head
        previous_node = None
        while current_node != None:
            if current_index == index:
                if previous_node == None:
                    self.head = Node(value)
                    self.head.next = current_node
                else:
                    previous_node.next = Node(value)
                    previous_node.next.next = current_node
                self.size += 1
                return
            previous_node = current_node
            current_node = current_node.next
            current_index += 1

    # READ operations

    def get(self, index:int): #return the value at the given position
        '''
        Returns the value of the node at the given index.
        Raises an IndexError if the given index is out of bounds

        PARAMETERS
            index:INT
                The index of the node to have its value retrieved
                May be a negative number (-1 = [len - 1], -2 = [len - 2], etc.)
        RETURN
            Any
                The value of the node at the given index
        '''
        if index >= self.size or index < -1 * self.size:
            raise IndexError("Index out of bounds")
        if index < 0: # Check if the index is negative; adjust to the corresponding positive index
            index = self.size + index

        current_index = 0
        current_node = self.head
        # Iterate through the list until the given index is reached, then return the node's value
        while current_node != None:
            if current_index == index:
                return current_node.value
            current_node = current_node.next
            current_index += 1

    def find(self, value):
        '''
        Returns the position of the first node containing the given value, or -1 if the value isn't found in the list.

        PARAMETERS
            value:Any
                The value to have the index of its encapsulating node searched for in the list
        RETURN
            INT
                The positive index of the first node containing the given value
                -1 if the value was not found
                (Note: despite allowing for negative indices in other functions' parameters, this -1 does *not* correspond to [len-1].
                    it only indicates that the value was not found)
        '''
        current_index = 0
        current_node = self.head
        # Iterate through the list, searching each node until the value is found or the end of the list is reached.
        # Return the index if the value is found
        while current_node != None:
            if current_node.value == value:
                return current_index
            current_index += 1
            current_node = current_node.next
        return -1 # The value was not found, so return -1

    def __len__(self):
        '''
        Returns the number of nodes currently held in the list

        PARAMETERS:
            None
        RETURN
            INT
                The number of nodes currently in the list
        '''
        return self.size
    
    # UPDATE operations
    
    def update(self, index:int, value):
        '''
        Replaces the value of the node at the given index with the given value
        Raises an IndexError if the given index is out of bounds
        
        PARAMETERS
            index:INT
                The index of the node to have its value updated
                May be a negative number (-1 = [len - 1], -2 = [len - 2], etc.)
            value:Any
                The value to replace the node's old value with
        RETURN
            None
        '''
        if index >= self.size or index < -1 * self.size:
            raise IndexError("Index out of bounds")
        if index < 0: # Check if the index is negative; adjust to the corresponding positive index
            index = self.size + index

        current_index = 0
        current_node = self.head
        # Iterate through the list until the desired index is found, then update the node's value
        while current_node != None:
            if current_index == index:
                current_node.value = value
                return
            current_index += 1
            current_node = current_node.next
    
    # DELETE operations

    def delete(self, value):
        '''
        Removes the first node holding the given value, and returns a boolean according to whether the value was found and deleted or not.

        PARAMETERS
            value:Any
                The value of the node to be searched for and deleted if found
        RETURN
            BOOL
                True if the value was found in the list and the node was successfully deleted
                False if the value was not found and no nodes were deleted
        '''
        current_node = self.head
        previous_node = None
        # Iterate through each node and keep track of the previous node to update its 'next' pointer accordingly
        while current_node != None:
            if current_node.value == value:
                if previous_node == None: # Deleting the head
                    self.head = current_node.next
                else: # Deleting a middle or tail node
                    previous_node.next = current_node.next
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    def delete_at(self, index:int):
        '''
        Removes the node at the given index and returns its value.
        Raises an IndexError if the given index is out of bounds

        PARAMETERS
            index:INT
                The index of the node to be removed
                May be a negative number (-1 = [len - 1], -2 = [len - 2], etc.)
        RETURN
            Any
                The value of the node that was removed
        '''
        if index >= self.size or index < -1 * self.size:
            raise IndexError("Index out of bounds")
        if index < 0: # Check if the index is negative; adjust to the corresponding positive index
            index = self.size + index

        current_index = 0
        current_node = self.head
        previous_node = None
        # Iterate through each node, keeping track of the previous node to fix its next pointer upon node deletion
        while current_node != None:
            if current_index == index:
                if previous_node == None: # Deleting the head
                    self.head = current_node.next
                else: # Deleting a node in the middle or at the tail
                    previous_node.next = current_node.next
                self.size -= 1
                return current_node.value
            current_index += 1
            previous_node = current_node
            current_node = current_node.next

    # Printing

    def print_list(self):
        '''
        Prints the list to stdout in the format "(value) -> (value) -> (value)" and so on

        PARAMETERS
            None
        RETURN
            None
        '''
        if self.head == None:
            print("(empty)")
        else:
            current_node = self.head
            while current_node != None:
                if current_node != self.head: # Print an arrow before every node after the head
                    print(" -> ", end='')
                print(current_node.value, end='')
                current_node = current_node.next
            print()

def main():
    # Initial testing
    L1 = SinglyLinkedList()
    L1.append(12)
    L1.append(3)
    L1.append(5)
    L1.prepend(1)
    L1.get(2)
    L1.delete(3)
    L1.update(0,8)
    L1.append(7)
    L1.print_list()


if __name__ == "__main__":
    main()