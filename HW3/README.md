# METCS 526 Fall 2026 - HOMEWORK 3

### Author: Tyler Hunt; Professor: Dr. David Mellor

## Introduction
<p>For this homework, we were tasked with writing multiple recursive algorithms and solving a unique problem involving ghostbusters
and their streams.</p>

<p>In problem1.py, my code implements a recursive check for strings from stdin to determine whether or not they count as palindromes, 
i.e. they read the same forwards and backwards, such as 'racecar' or 'peep'. For each string, "True" or "False" is printed on a
newline to stdout corresponding to whether the string was a palindrome, and once all strings have been processed, the total number of
palindromes found is printed at the end.</p>

<p>In problem2.py, I implemented a recursive function to obtain all unique substrings given one string from stdin, after which
all of those substrings found are printed in alphabetical order to stdout followed by the total number of substrings.</p>

<p>In problem3.py, I first implemented a Stack in three different ways: with Array, Singly-Linked List, and Doubly-Linked list
representations. Then, I made a recursive function that reverses any given stack regardless of how it was implemented.</p>

<p>In problem4.py, I made a function that solves the problem of ghostbusters and ghosts, determining whether all ghosts
were eliminated given an input file of buster and ghost coordinate pairs that indicate the direction that each stream
is being fired in.</p>

## Algorithm

### Problem 1

<p>For this palindrome problem, I implemented what is likely the simplest version of the recursive palindrome algorithm.
The recursion repeatedly checks both the front and back ends of the string and compares the characters in the recursive case,
calling the function on the string with those characters removed if they are equal and returning False otherwise. In the base
cases, the empty string and a string of length 1 are both palindromes by definition, so they were suitable ends to the recursion
that work with both even and odd length strings. This function structure also works for strings with spaces in between each
character, since as long as the formatting is consistent, those spaces will always be compared to another space, so they wouldn't
affect the logic whatsoever.</p>

<p>To read input, I just used a for loop to continously read lines from stdin to repeatedly check for palindromes and keep track of
the amount of palindromes found so far. I made sure to strip the input to make sure there weren't any issues related to whitespace on
either end of the strings.</p>

### Problem 2

<p>For the substring problem, I decided to use a driver function that calls the recursive function to make it easier to use a set
to keep track of all the unique substrings. The driver function creates an empty set and calls the recursive function before turning
the set into a list and sorting it, then the function outputs everything as needed.</p>

<p>In the recursive function, there are two base cases: either the input string is empty, or it's already in the set given by the
second parameter. In the recursive case, the function adds the current input string to the set of found substrings and calls itself
twice, once with the beginning character removed, and once with the ending character removed. This allows the function to expand across
the whole string and recursively narrow down the string at every possible position, effectively finding each substring of consecutive 
characters. This does result in a lot of redundant function calls, but I suppose it's the tradeoff for obtaining every possible substring.</p>

<p>Since the input is only one line containing a string, I allowed the user to run the program without a file input if they so desired. Only
one line is ever read from stdin, so that was an easy consideration to make.</p>

<p>When sorting the list of unique substrings, I opted to just use the built-in list sort function because I didn't think making my own sorting
algorithm was necessary for the purposes of this problem.</p>

### Problem 3

<p>For this stack problem, I first had to make some decisions regarding each separate implementation. Since I had to make three classes based around
the core concept of a stack, I opted to use inheritance with a parent Stack class that gives some functions to its children like is_empty() and len(),
while providing templates for things like push(), pop(), and peek().</p>

<p>In my Array-based stack, I used the numpy package's Array structure to have the most accurate representation without needing to do a lot of work
to keep a List that emulates an array. In the StackArray class, I used the stack's current size as a way to index the next available position on the
top of the stack when pushing or popping. I couldn't quite figure out how to copy over a numpy array to a new array, so I decided not to implement
array expansion as a function of this class. The given size at the object's initialization is its permanent max capacity.</p>

<p>In my Singly-Linked List-based stack, I used a Node class that has both next and prev pointers so that I could just use one class for both this
and the doubly-linked list representation. Here, the prev pointer just remains unused. Otherwise, this linked list implementation is quite simple:
it iterates to the end (the top of the stack) via next pointers whenever it needs to push or pop, then adjusts the tail as needed</p>

<p>In my Doubly-Linked List-based stack, the implementation allowed me to pop the tail off and patch things via the prev pointers without iterating 
through the entire stack. Additionally, I was able to make a unique recursive reversing algorithm for just this representation that doesn't use pop 
or push at all. It simply starts at the tail and reverses the direction of every next and prev pointer moving all the way to the head, resulting 
in the head becoming the tail and vice versa. The base case is the input Node being a None object, which indicates that the new tail has been passed,
and all the pointers in the stack have been adjusted. The recursive case performs operations to reverse the directions of the current node's next and 
prev pointers before calling the function recursively on the next node moving towards the old head (old bottom) of the stack. This does not change how 
the following algorithm functions with this representation, so both methods work for reversing the stack.</p>

<p>In the more general reversing algorithm, I needed to make two recursive functions to fully reverse each stack. In reverse_stack(), the function
recursively pops off the current top of the stack and calls itself recursively until the stack is empty. Then, once the recursion begins folding up,
the function calls its recursive helper function push_bottom(), which is needed because just using push() would result in the stack not changing at all.
In push_bottom(), the function pops off every element in the stack before pushing its input value to the bottom and placing all of the pre-existing
elements on top of that new value. By using push_bottom(), reverse_stack() can take the bottom of the list and make it the new top by pushing the
following elements to the bottom instead of the top of the stack.</p>

<p>Input is not taken from stdin at all. The test cases are hardcoded into main, since the problem specification didn't say to expect a file.</p>

### Problem 4

<p>In this Ghostbusters problem, I realized that for none of the lines to intersect, they all need to have the same slope, and none of the lines
can be equivalent. So, I operated on two adjacent lists of tuples giving the coordinates of each ghostbuster and ghost, calculating the slope of
every stream trajectory and keeping track of their intersections with the x-axis to check for equivalence. I used basic algebra equations relating
to 2-d lines such as (y-y_0)/(x-x_0), the slope equation, and y = mx + b, the line equation, to compare lines and make sure none of them intersect
or are equivalent.</p> 

<p>There were some edge cases I needed to consider like horizontal and vertical lines, since those could result in zero division if I performed 
my calculations on those lines. To handle those, I just used if statements and a bit of extra checking to make sure those cases avoided my 
computation expressions.</p>

<p>Input is read line-by-line from the stdin file as usual. I didn't need the 'n' value at the beginning of each file since my input-reading loop 
runs until EOF for stdin. Since the input follows a well-defined format, I could easily use string.split() and indexing to quickly obtain all the
relevant information for the problem.</p>

## Notable Aspects

### Problem 1

<p>None. This palindrome algorithm seems pretty standard.</p>

### Problem 2

<p>I mentioned in the Algorithm section that I made a tradeoff of efficiency in exchange for breadth of search. I'm not sure if
there is another way to get all the substrings recursively, but I can at least observe that there's a lot of redundant checking
happening with this method.</p>

### Problem 3
<p>The first interesting thing is my reverse_doubly() function that I implemented for my Doubly-Linked List stack representation.
The general reversing algorithm uses functions that all of the stack representations have, so it works for all three, but this
specific algorithm seems to be quite a bit more efficient. I want to say that the general algorithm is somewhere around O(n^2)
because push_bottom() has to remove everything in the stack before pushing the current value, but the doubly linked reversing
method is definitely O(n) because it only operates on each element in the stack once to change its pointers.</p>

<p>The other interesting thing is just the necessity for push_bottom() being quite ironic with the whole purpose of a stack being
to only allow values to be pushed to the top. If there's a way to do this without a push_bottom(), I would like to see it.</p>

<p>I also didn't need to use peek() at all, but I still implemented it as the problem required as a Stack parent function.</p>

### Problem 4
<p>The most notable thing is how I needed to handle horizontal and vertical lines, since I can't let them reach my computations
or else I'd be dividing by zero. I used the strings "Vertical" and "Horizontal" in place of the slopes for those lines, since
a number divided by zero can't be represented in Python (as far as I'm aware), and I wanted horizontal lines to also avoid
future computations where I worked with the y = mx + b equation, so I used the string instead of a 0 value. In my x-axis
intersections list, I needed to replace those with y-axis intersections when the lines are completely horizontal, so the name
'x_intersections' isn't always accurate, but it doesn't quite matter as long as the axis stays consistent within each test
case.</p>

## How to run

### Problem 1
    python problem1.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python problem1.py < test_files\palendrome_0.txt

### Problem 2
    python problem2.py
        If providing input directly from the console (no file stdin), type the string in and press Enter.
    (or)
    python problem2.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python problem2_driver.py < test_files\unique_substrings_input_0.txt

### Problem 3
    pip install numpy
        The numpy package is required since I used its array structure for one of the implementations
    python problem3.py

### Problem 4
    python problem4.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python problem4.py < test_files\ghostbusters_input_0.txt
