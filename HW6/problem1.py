# METCS 526 Fall 2026 - HOMEWORK 6
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys

#------------------------------PROBLEM 1----------------------------

class Node:
    '''
    A simple node class for a singly-linked structure, with a contained value and a pointer to the next node.
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class priorityQueue:
    '''
    A container representing a Priority Queue, supporting operations to enqueue and dequeue items based on a
    priority defined by comparing elements and assigning a higher priority to those with lower (<) values.

    FIELDS
        pQueue:NODE
            A pointer to the node at the head of the priority queue (i.e. the next element in line to be dequeued)
        size:INT
            The number of elements currently in the queue
        maxCapacity:INT
            The maximum number of elements that can be present in the queue at any given time
    '''
    def __init__(self, k:int):
        self.pQueue = None
        self.size = 0
        self.maxCapacity = k

    def isEmpty(self):
        '''
        Returns a boolean indicating whether the queue is empty or not.

        PARAMETERS
            None
        RETURN
            BOOL
                True if there are no elements currently in the queue
                False if there is at least one element in the queue
        '''
        return self.size == 0

    def isFull(self):
        '''
        Returns a boolean indicating whether the queue has reached its maximum capacity or not.

        PARAMETERS
            None
        RETURN
            BOOL
                True if the number of elements in the queue is equal to its maximum capacity
                False if the queue still has room to enqueue elements
        '''
        return self.size == self.maxCapacity

    def enqueue(self, value):
        '''
        Adds an element with the given value to the queue at its correct position with a priority
        based on its comparative value to other elements currently in the queue. Elements of lower
        value (<) are given more priority and are positioned to be dequeued first.

        PARAMETERS
            value:Any<Comparable>
                Any comparable value (must be the same type as other values currently in the queue)
        RETURN
            None
        '''
        if self.isFull(): # Cannot enqueue any more items
            raise ValueError("Priority Queue is full")
        if self.isEmpty(): # No items in the queue yet
            self.pQueue = Node(value)
        else: # >1 item present: find correct position to enqueue
            new_node = Node(value)
            if value < self.pQueue.value: # Insert at head of queue
                new_node.next = self.pQueue
                self.pQueue = new_node
            else: # Search for the first item greater than the given value
                curr_node = self.pQueue
                while curr_node.next is not None:
                    if new_node.value < curr_node.next.value:
                        new_node.next = curr_node.next
                        break
                    curr_node = curr_node.next
                curr_node.next = new_node
        self.size += 1

    def dequeue(self):
        '''
        Removes the element at the head of the priority queue

        PARAMETERS
            None
        RETURN
            Any<Comparable>
                The value of the item at the head of the priority queue
        '''
        if self.isEmpty():
            raise ValueError("Priority Queue is Empty")
        popped_node = self.pQueue
        self.pQueue = self.pQueue.next # Update the pointer to the head of the queue
        self.size = self.size - 1
        return popped_node.value

    def peek(self):
        '''
        Returns the value at the top of the priority queue without removing it.

        PARAMETERS
            None
        RETURN
            Any<Comparable>
                The value of the item at the head of the priority queue
        '''
        return self.pQueue.value

    def print_queue(self):
        '''
        Prints the contents of the priority queue to stdout, separated by spaces

        PARAMETERS
            None
        RETURN
            None
        '''
        if self.isEmpty():
            print("(empty)")
        else:
            print(self.pQueue.value, end="")
            curr_node = self.pQueue.next
            while curr_node is not None:
                print(f", {curr_node.value}", end="")
                curr_node = curr_node.next
            print()

#-----------------------------------------------------------------------------------------------------------

def sort_registers(registers):
    '''
    Populates and returns a list of sorted transactions (denoted by time integer values) from the given numbered registers.
    The list elements are in the format (time, register).
    '''
    sorted_log = []
    k = len(registers)
    pqueue = priorityQueue(k)

    # Populate the queue with the first transaction from each sorted register (if it exists)
    for i in range(k):
        if len(registers[i]) > 0:
            pqueue.enqueue((registers[i].pop(0), i+1))

    while not pqueue.isEmpty():
        # Dequeue the transaction at the head of the queue and append it
        time, register = pqueue.dequeue()
        sorted_log.append((time, register))

        # Take the next transaction from the same register as the dequeued transaction (if there are more to grab)
        if len(registers[register - 1]) > 0:
            pqueue.enqueue((registers[register - 1].pop(0), register))
    return sorted_log

def main():
    '''
    Reads the 'k' lists of registers with sorted transaction lists, then returns the merged sorted list of
    transactions.
    '''
    registers = []
    for line in sys.stdin:
        log = line.strip()
        log = log[1:len(log) - 1].split(", ")
        if log[0] != '':
            log = [int(x) for x in log]
        else:
            log = []
        registers.append(log)
    sales = sort_registers(registers)
    print(f"Registers: {len(registers)}")
    print(f"Total sales: {len(sales)}")
    print(f"Merged log: {sales}")

if __name__ == "__main__":
    main()
    