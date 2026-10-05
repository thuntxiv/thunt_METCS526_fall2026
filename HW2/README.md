# METCS 526 Fall 2026 - HOMEWORK 2

### Author: Tyler Hunt

## Introduction
<p>For this homework, we are focused on building well-known data structures from scratch and implementing
some recursive functions. </p>

<p>In problem2.py, my code implements a Singly-Linked List structure with all of
the requisite CRUD operations, then tests its functionality with well-defined commands from a text
file using problem2_driver.py</p>

<p>In problem3.py, my code builds a function that compiles the unique number of ways that a staircase
with a given number of steps 'n' can be climbed in step increments of 1, 2, and 3.</p>

<p>In problem4.py (TODO)</p>

<p>Below are my answers to questions 1 and 3 (a & b):</p>

### Problem 1
<p>Some advantages to using a tail pointer in a linked list are that value searches could potentially
have their runtime cut in half, and append operations are much faster than if only the head pointer
was kept.</p>

<p>When searching for a value inside of a linked list, the approach without a tail pointer is usually
to iterate from the head all the way down to the tail, comparing each node's value until the desired
value is found. With a tail pointer, one could search from both the head and the tail at the same time,
moving inward toward the middle of the list. The same amount of comparisons are made, but for a list of
size n, the total iterations for the search are 1/2 * n instead of n.</p>

<p>Additionally, append operations are O(1) instead of O(n). Without a tail pointer, one must iterate from the
head through the entire list until the tail is reached, then add the new node. With a tail pointer, one can perform
the operation without a loop or recursion by just accessing the tail and updating its next pointer along with
the list's tail pointer. Easy access to the list's tail allows the append to be performed in constant time.</p>

### Problem 3
#### a.)
<p>The base cases are n = 0 and n < 0. For n = 0, we have reached the top of the staircase exactly, and there are no 
more stairs left to climb, so we count this as a valid way and return 1 to represent this combination. For n < 0,
we have overstepped past the final stair with the current combination of steps. We don't count this way, so we return 
0 so that it doesn't add to the total way count.</p>

#### b.)
<p>If we could only climb 1 or 2 stairs at a time, this would just be the fibonacci sequence, since in that recursive
function, we use fib(n-1) + fib(n-2) just like how we'd use ways(n-1) + ways(n-2).</p>


## Algorithm

### Problem 2
<p>My SinglyLinkedList class is designed to hold any value type, not just integers, even though the driver program
only provides integers as values. This is to preserve its integrity as a container akin to lists and arrays that
can hold other container structures as values, so if a user desired, they could put lists and even other singly-
linked lists as values in my class' nodes.</p>

<p>I used mostly O(n) implementations of its operations for simplicity and the constraints of the singly linked 
list structure. For its append and prepend operations, the head and tail pointers are used so that the functions 
run in O(1) time, but for most other operations that require searching or accessing a middle index, I opted to 
iterate through each node in O(n) time. In most cases, there isn't a faster way to access middle nodes because the 
nodes don't have pointers to their previous node.</p>

<p>For some operations, most relevantly the delete operations, I needed to keep track of both the current node
and the previous node when iterating through the linked list. This is so that I can perform the requisite patching
once I find the node to be deleted, since I would have to update the previous node's next pointer to the node
following the deleted node. If this were a doubly-linked list, that extra pointer would be unnecessary since
the pointer would already be kept within each node.</p>

<p>Perhaps the most notable addition I made to the class is that negative indices can be passed into the functions
that require an index such as get, update, and delete_at. This is to emulate the same functionality for indexing
in standard python structures like the List data type. If a user desired, they could easily indicate the nodes
at indices near the end of the linked list with -1, -2, etc.</p>

<p>For the driver function, I used a match case statement because that's what comes most naturally in my thought
process. I read lines repeatedly from stdin and match them to the defined commands as outlined in the assignment
specification, then make sure the formatting and arguments are all correct before either printing a warning or
calling the corresponding SinglyLinkedList operation.</p>

<p>I also added the functionality to quit out of the process_commands() function in case the user wishes to
type in commands directly into stdin through the terminal. To do this, the user must type "quit" and enter
it as a line of input. I like to add flexibility with how my program is used, so when we expect an input
file to be piped into stdin, I tend to also account for typed input.</p>

<p>Something a bit annoying was determining whether a string was a negative integer when I still had to account
for non-number characters. I needed to make a helper function is_negative_int() to encapsulate all of that logic
and keep it from cluttering my case statements even more. I couldn't just use a predefined string function like 
is_digit() or is_numeric() since negative numbers return false for those, so I made sure that the string had a 
negative sign in the first position, it could be cast to an integer without erroring, and the number it represents 
could be evenly divided by 1 (i.e. is an integer).</p>

### Problem 3
<p>I built my recursive function with the aforementioned base cases in mind for complete and incomplete ways to climb
the stairs, then I made a recursive case that combines three recursive calls to explore all possibilities with the
increments of 1, 2, and 3 steps. At each step, we have the choice of which amount of steps we want to take. From the
first step, we can choose to either take one step, two steps, or three steps. And within each of those choices, we
can keep making that same decision over and over until we reach one of the base cases. So, I decided to make the 
recursive case out of the addition of the ways compiled from all three starting choices.</p>

<p>I don't really see any other places I could deviate and create a different solution, so I'll just leave it at that.</p>

### Problem 4

## Notable Aspects
### Problem 2
    The only notable aspects in my opinion are how I implemented negative index support for all linked list operations that
    need an index, and how I made a small optimization in insert() to use append() instead of iterating through the list all
    the way to the end upon receiving an index equal to the size of the list. This turns the operation from O(n) time to O(1)
    time in that singular case.

### Problem 3
    I don't think anything is notable about my implementation. It seems like the intended way to code this problem.

### Problem 4
    TODO: Write stuff here

## How to run
### Problem 2
    python problem2_driver.py
    (or)
    python problem2_driver.py < (input file)

### Problem 3
    python problem3.py

### Problem 4
    python problem4_driver.py < (input file)
