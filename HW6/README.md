# METCS 526 Fall 2026 - HOMEWORK 6

### Author: Tyler Hunt; Professor: Dr. David Mellor

## Introduction
<p>For this homework, I implemented my own Priority Queue and Binary Heap to solve a couple of problems requiring those data structures.</p>

<p>In problem1.py, I made a Priority Queue class with the less-than comparator (<) as each item's priority, then I used the queue to merge
an arbitrary number of sorted lists of timestamped transactions from multiple registers.</p>

<p>In binaryMinHeap.py (problem 2), I implemented a binary minimum heap with a linked-tree structure of nodes with parent and children pointers.
The class has numerous functions to support inserting, deleting, extracting the minimum, obtaining a sorted list, etc.</p>

<p>In runningMedian.py (problem 3), I used my binary min heap along with an extension class for a binary max heap to efficiently solve the
running medians problem in the context of sales accrued over a given day.</p>

## Algorithm

### Problem 1
<p>For my priority queue, I decided to use a linked list structure. Even though the queue size is fixed to 'k', I figured a linked list is
still a pretty intuitive way to hold a priority queue because of the O(1) dequeuing at the top of the list despite the O(n) insertion. I think
managing pointers and not worrying about indices is also just easier than using an array and needing to do the latter.</p>

<p>My enqueue operation is very simple: it just uses each item's value as its priority and places items of lower numerical values higher up in
the queue, so that those lower valued items are dequeued first. My dequeue operation just removes the head of the linked list and moves the head
pointer down the list by one position.</p>

<p>In terms of my solution to the problem, I started by initializing a priority queue of max capacity 'k' (the number of registers) and populated
the queue with the first transaction in each register. Then, I enter a loop in which I dequeue the transaction with the most priority in the queue, add it
to the result list, and then check if the same register that provided this current transaction still has more transactions to provide. Since each individual
register is sorted, this approach ensures that transactions with time values bigger than the previously dequeued transaction but smaller than the other
transactions currently in the queue are accounted for (due to the queue's priority allowing items of lesser value to be placed at the head of the queue).
Conflicts between transactions with the same time are naturally resolved, since each transaction tuple is in the format (time, register #), and that lets the
comparator (<) automatically move to the register number if the time values between two transactions are the same. This process repeats until all transactions 
from the registers have been processed, resulting in the desired merged, sorted list of transactions.</p>

<p>The time complexity of my solution is O(nk) (or technically O(n^2)), since for each transaction, I need to enqueue the value which is an O(k) operation (the 
queue can only be as large as 'k'). Dequeuing is an O(1) operation, so I just multiply the enqueue operation by n, giving me O(nk). The space complexity should 
be O(n) from my understanding, since the queue is transferring values from one list into the queue, then into a final list. I only ever need space to hold one 
version of each transaction.</p>

### Problem 2
<p>For my Binary Min Heap, I tried to follow the logic provided in the lecture slides as closely as possible. In accordance with the problem specification, the
heap is implemented as a tree of nodes, each with parent, left child, and right child pointers as well as a contained value. The heap itself contains a reference
to its root and an integer insertion position, which gives the path to the next place to insert a node when converted into binary</p>

<p>For insertion, I converted the insertion position counter into binary and read the value as a string, traversing left for a 0 digit and right for a 1 digit, then
I made a helper function for bubbling up that does so recursively as long as the node's value can still travel upward to maintain the heap order property.</p>

<p>For extracting the min, I used the insertion position minus 1 to get the most recently added node, then I moved that node in place of the root that I just
extracted before bubbling down as far as I need to so that the heap order is maintained. Deleting uses similar logic, but that requires me to first do an O(n)
search (performed in the find() helper function) for the given value before removing it and performing the replacement with bubbling up or down as needed.</p>

<p>For heap sort, I used a small recursive function to first traverse the heap object and populate a copy of the heap with the same values. This doesn't result 
in the same heap structure as the original, but since I'm just extracting the min repeatedly, the structure doesn't matter, and the function results in the
correct sorted list of values as long as the heap properties are maintained.</p>

<p>The printing function was provided by ChatGPT. All other code is my own unless stated otherwise.</p>

### Problem 3

<p>For this running Median problem, I started by making a Binary Max Heap class that inherits from my min heap. It has all the same functionality, but the
heap order is reversed so that the maximum value is at the root, and all parent values are larger than their childrens' values.</p>

<p>My solution utilizes both of my heap classes to effectively keep the list of sales in two parts: one heap with smaller values and one heap with larger values.
The max heap is used for the smaller values so that the largest of the small values is easily accessible via peek(), and the min heap is used for the larger values
so that the smallest of the large values is easily accessible with the same function. For this O(1) median computation to hold, the heaps must have a difference of
sizes between 0 and 1, or else peek() won't target the middle of the hypothetical sorted list of all sale amounts seen so far. If this size difference threshold
is maintained, then the heaps should always give me either the sole middle value or both middle values depending on if the number of sales so far is odd or even.</p>

<p>With this heap approach, my algorithm starts by inserting the first value into the lower heap (max heap) and then compares each subsequent value to the max of the
lower heap. If a value is greater than that maximum, then it gets inserted into the upper heap (min heap), otherwise it's added to the lower heap. After inserting, I
need to check to maintain the 0-1 size difference threshold between each heap. If the lower heap has two more elements than the upper heap, I extract the max of the lower
heap and insert into the upper heap. If the upper heap has two more elements, I extract the min and insert into the lower heap. After that, I can calculate the median
of all the sales I've seen so far based on the relative sizes of the heaps. If the lower heap is larger, then the total number of sales so far is odd, so I take the
max of the lower heap as the median. Similarly, if the upper heap is larger, I can take the min of the upper heap as the median. If the heaps' sizes are equal, then
the number of sales I've compiled is even, so I need to take the average between the max of the lower heap and the min of the upper heap. Then, I rinse and repeat
until all sales have been processed.</p>

<p>The time complexity of my algorithm is O(n log n), since inserting into the heap is a log(n) operation, and my median calculation only uses peek(), which is O(1).
I insert into either of the heaps n times, so that results in O(n log n). The space complexity is O(2n), since the two heaps store all sales, which is O(n), and my
running median array has a median for each element, which is also O(n).</p>

## Notable Aspects

### Problem 1
The most notable aspect is just how I decided to use a linked list to represent the Priority Queue.

### Problem 2
The most notable thing is probably how I used the binary string to determine where to add each new node. It's
pretty cool and intuitive to use binary for something like that to get log(n) insertion.

### Problem 3
This solution took me a bit to figure out but this is a pretty cool method to make running median calculation
extremely efficient using heap order properties.

## How to run

### Problem 1
    python problem1.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python problem1.py < test_files\merge_input1.txt

### Problem 2
    python binaryMinHeap.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python binaryMinHeap.py < test_files\heap_input1.txt

### Problem 3
    python runningMedian.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python runningMedian.py < test_files\median_input1.txt
