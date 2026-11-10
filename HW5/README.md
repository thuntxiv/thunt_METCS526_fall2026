# METCS 526 Fall 2026 - HOMEWORK 5

### Author: Tyler Hunt; Professor: Dr. David Mellor

## Introduction
<p>For this homework, I had to implement a Binary Search Tree as an ADT followed by solutions for two
dynamic programming problems related to Morse Code and a longest alternating increasing sequence of
integers.</p>

<p>In binarySearchTree.py (problem 1), I implemented ADTs for a Binary Search Tree and the Nodes contained
within, accompanied by functions for adding, finding, and deleting nodes and printing the whole tree.</p>

<p>In morseVowels.py (problem 2), I implemented a solution using a condensed state table that solves the
total number of combinations of vowels that can be derived from a given string of morse code symbols.</p>

<p>In longestSequence.py (problem 3), I implemented a tabulation solution that keeps the longest increasing 
alternating sequence that starts at each index in the given sequences to eliminate redundant
sequence calculation.</p>

## Algorithm

### Problem 1
<p>The Node ADT is a very basic implementation with a value, left child, and right child.</p>

<p>In the Binary Search Tree ADT, the structural choices I made first include using the sentinel node 
approach. I thought it was an interesting design concept, and it did help avoid issues with NoneType 
errors when trying to check a node's child. In terms of sorting, I decided that the left subtree would
contain all values less than the parent, and the right subtree would contain all values greater than
or equal to the parent value. This seemed like the most natural choice for the BST ordering.</p>

<p>The problem didn't give any specific function definitions, so I did what made the most sense to me for 
each function. This mainly applies to find and delete, where I returned a boolean based on the success of the
search or deletion.</p> 

<p>The add_Node() function simply searches for the sentinel node at the appropriate sorted 
position in the tree before replacing that sentinel node's value and creating two new sentinel nodes. 
The find_Node() function uses similar logic to traverse the appropriate subtree based on the parameter's 
relative value to the root and each subsequent node, and False is returned if a sentinel node is ever reached.</p>

<p>For delete_Node(), I attempted to follow the pseudocode given in the lecture slides. I used a driver function that
calls a recursive helper function which handles most of the deletion logic. The helper function searches for the first
node with the given value, and at each step of the recursion, it returns the node that should replace the parameter
node. For most nodes, that will just be the same node since they don't fit the given value and thus shouldn't be deleted.
Once the desired node is found, I check each case of 0-1 child (no left child, no right child, no children (handled by the
previous two)), and either the left or right child becomes the replacement if any of those cases are true. If the node has
two children, I took the largest value from the left subtree as a suitable replacement, then I recursively
delete that replacement's original position until the hole in tree has been patched completely.</p>

<p>Since I follow mostly pre-established ways of working with a BST, the time complexities of these operations should be
O(log n) in best case and O(n) in worst case, where the tree's elements were added in sorted order and the structure
resembles a linked list.</p>

<p>The print function was an obstacle that I had a hard time figuring out, since I don't recall how to intuitively print a
binary tree of an arbitrary size. I looked up a printing algorithm online, and I ended up just using what the Google search
AI gave me because it seemed to work well enough.</p>

<p>For the tests, I implemented the randomized parameters according to the problem instructions, mixing in random searches
and deletions with those of values that I know are in the tree. Due to the nature of random test cases, I cannot include both
screenshots and an output file of the same test case, so I provided one test case in screenshot form from the terminal, followed
by two test cases in text file form with redirected output.</p>

### Problem 2
<p>For the morse code vowels problem, I adopted a state table approach very similar to the one in the lecture slides, but
I used a one-dimensional array representing the very last 'P' row in the lecture slides table. Before I explain further, let
me be transparent. I have a really hard time with Dynamic Programming problems, so I used ChatGPT to help me figure out the code
even though I did understand the big idea that you wanted to get across during lecture. In hindsight, it's easy to say that I
might have been able to figure the code out on my own, but I wasn't in a very good mental state this past week, and honestly,
I generally have a hard time believing that I can figure out hard algorithms organically.</p>

<p>This solution iterates through the entire morse code string, processing the possible combinations of vowels at each offset by
looking ahead and trying to match the next sequence of 1, 2, or 3 characters to one of the valid vowels. If a match is found, 
the number of combinations already computed at the index in the state table given by the current offset integer is added to the
state table index that is 1, 2, or 3 characters ahead depending on what vowel was matched.</p>

<p>At the state table's initialization, an extra cell is added at index 0 for the empty string with an initial value of 1 so that
the subsequent offsets can use that as a starting point to continuously compile the number of combinations. From my understanding,
this is what enables the single-dimensional solution to still obtain the correct number of combinations without using the two-
dimensional recurrence given in the slides.</p>

<p>The time complexity of this solution is O(5(n+1)) (5 possible vowels checked at each offset in the morse code string), which simplifies 
to O(n) overall. The space complexity is O(n+1) = O(n) for the state table, which is of similar size to the input string.</p>

### Problem 3
<p>Like problem 2, I needed to use ChatGPT to help me understand how to code the solution to this. I
intuitively understood where I needed to take things, but the details of implementation had me really stuck.</p>

<p>This solution uses two lookup tables, one for sequence A and one for sequence B, that represent the length of the longest
alternating increasing subsequence that ends at each table index corresponding to the elements in A and B. To obtain the
correct length, I loop through all indices up to the length either A or B, whichever is larger. Inside that loop, I loop
through each sequence individually to update the lookup tables if I find a value in the opposite sequence that is lesser in
both value and index. Since all of the tables' indices start at 1, adding the indices' values lets me calculate sequence
lengths ending at later indices based on the lengths of sequences ending at earlier indices that I already calculated. So,
I can connect sequences of varying lengths and eventually find the desired longest alternating increasing subsequence between
A and B.</p>

<p>The time complexity of this solution is, for m = len(A) and n = len(B), O(mn) since for each index in A, I'm checking every
index in B, and vice versa. The solution's space complexity is O(m + n) since the lookup tables need elements corresponding to
all indices in A and B.</p>

## Notable Aspects

### Problem 1

<p>Due to how Python passes class objects through functions, I needed to make it so that my delete function
returned a node object so I could actually update the parent node during deletion. If I just tried
to reassign the node during a lower function call, the parent's left/right fields wouldn't update properly.</p>

<p>As I mentioned, the print algorithm isn't mine. I just really didn't know what to do to make the print look
intuitive, since printing any of the node orders to the console wouldn't be easy to parse at all.</p>

### Problem 2
<p>
The most notable aspect is my single-dimensional state table that represents the 'P' row from the lecture slides'
state table. I also explained above the extra cell at the beginning corresponding to the empty string, which deviates
slightly from the solution presented in class.
</p>

### Problem 3
<p> Not sure if anything about my solution is of note. The idea of populating the lookup tables continously based on
sequence lengths ending at previous indices is pretty cool, I guess.</p>

## How to run

### Problem 1
    python binarySearchTree.py

### Problem 2
    python morseVowels.py (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python morseVowels.py test_files\vowel_input1.txt
        Note: Do NOT use the redirect ( < ) operator, since the file name is needed for the program.

### Problem 3
    python longestSequence.py (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python longestSequence.py test_files\longest_seq1.txt
        Note: Do NOT use the redirect ( < ) operator, since the file name is needed for the program.

 

 
 

 
 
