# METCS 526 Fall 2026 - HOMEWORK 4

### Author: Tyler Hunt; Professor: Dr. David Mellor

## Introduction
<p>For this homework, I needed to solve some tree traversal problems then implement some algorithms involving integer arrays and points in
a two-dimensional space that form right triangles.</p>

<p>In smallestNumber.py (problem 2), I used a recursive Quicksort algorithm on the given array of integers to put it in descending
order, from which I could add up the biggest values until the sum is greater than the given target. After determining the smallest sum
cardinality, I print the input array to stdout followed by the target and the smallest number of values that can be added up to
exceed the target's value.</p>

<p>In rightTriangles.py (problem 3), I implemented a O(n^2) solution to the right triangles problem that uses math related to perpendicular 
vectors to determine what right triangles can be made from any given vertex and the rest of the given points. The count of possible right 
triangles is printed to stdout following the computation.</p>

<p>Below are my answers for problem 1:</p>

### Problem 1 Answers

#### Tree 1
 
                 A
             /   |   \
           B     C     D
          / \          |
         E   F         G
         |   |
         H   I
 
    (A has children B, C, D;  B has children E, F;  D has child G;
     E has child H;  F has child I)

<p>Pre-order traversal: A -> B -> E -> H -> F -> I -> C -> D -> G</p>
<p>Breadth-first traversal: A -> B -> C -> D -> E -> F -> G -> H -> I</p>
<p>Post-order traversal: H -> E -> I -> F -> B -> C -> G -> D -> A</p>

#### Tree 2
 
                 A
               /   \
             B       C
            / \       \
           D   E       F
            \         / \
             G       H   I
 
    (A: left B, right C;  B: left D, right E;  D: right G;
     C: right F;  F: left H, right I)
 
<p>In-order traversal: D -> G -> B -> E -> A -> C -> H -> F -> I</p>

## Algorithm

### Problem 2
<p> For this smallest sum problem, my code uses a sorting solution to find the smallest number of elements that add up to a sum
greater than the given target. If I add up the largest values in the array, I logically should obtain the smallest cardinality
sum on the first pass, so I opted to make a copy of the array (O(2n) space requirement) and sort that in-place using the Quicksort
method for arrays. I used Quicksort just because it was fresh in my mind from my python class that I just took. It doesn't seem like
too bad of a sorting algorithm, since its average case is O(n log n) and worst case is O(n^2) if the given array is already sorted. 
Definitely not the best, but it seems to work fine for the purposes of this problem</p>

<p>Once the array copy is sorted, I add the values starting from the top of the list (which we determined to be the largest via reverse
sorting) until the current sum exceeds the given target's value, then I return the count of how many numbers were added to achieve that sum. 
In worst case, this is O(n) time if the entire array needs to be added together to make a sum greater than target. In the average case, it's 
significantly faster than trying to brute force different sums. The sorting algorithm takes precedence for the overall program's time 
complexity since Quicksort's Big O is larger than O(n), so my program is O(n log n) in average case and O(n^2) in worst case.</p>

### Problem 3

<p>To find all possible right triangles in a reasonable amount of time, my code uses vector math and perpendicular lines to cut
down on how many times the input is iterated through. If I choose one point out of the bunch and decide that it should be the vertex where the
right angle is present, I can find whether a right triangle can be produced if I check each line extending from that vertex to each other point
and see if the corresponding perpendicular line was passed over at any point in my vector compilation. So, I'm looping once through all the points to 
consider each right angle vertex, then I'm looping again to compile the lines between the vertex and every other point, and once that second loop 
terminates, I loop through the lines I just found to look up if their perpendicular complement was found or not.</p>

<p>To store each vector between the current right angle vertex and every other point, I used a Default Dictionary from the Python Collections
module. From my understanding, a Python Dictionary has O(1) average lookup complexity, so it's ideal to use when trying to reduce overall
runtime. A Default Dictionary in particular was useful to me because the default value on an empty lookup made it easy to determine if there
were no perpendicular lines found for a given vector. This structure is effectively a hash map, so if I were to do this problem in another language,
I'd use a hash map in place of a default dict. In terms of space complexity, the dictionary at maximum capacity will have n-1 vectors, since
a.) the current right angle vertex isn't processed, and b.) the dictionary is wiped when moving on to the next right angle vertex. Therefore,
this program's space complexity is O(n). For time complexity, the algorithm comes out to O(n(n + n)) based on the loop parameters I established
above, which equates to O(n^2)</p>

<p>Related to my use of a dictionary, there's a part in my code where I normalize each vector using the greatest common divisor of its x and y
components. Instead of keeping each individual vector and worrying about vector length when finding each perpendicular vector, I found that I could
instead perform a small calculation using the math.gcd() function to keep each vector's direction but reduce its components down to a normalized value.
This way, vectors with the same direction but differing lengths are compiled into the same vector with a corresponding frequency integer, which is a
large gain in efficiency when dealing with such a large dataset.</p>

## Notable Aspects

### Problem 2

<p>Using a sorting algorithm is the highlight of my solution here. It seemed like the path that made the most sense and that was the easiest
to implement. My choice of sorting algorithm was explained above, but to review, Quicksort was the first thing that came to mind, and it seemed
like it was reasonably faster than something like Bubble Sort that is always O(n^2) time complexity.</p>

### Problem 3
<p>The most notable thing about my solution, also explained above, is how vectors between the current right angle vertex and every other point are
normalized and compiled into a dictionary of frequencies when applicable (i.e. vectors have the same direction, but might not have the same length).</p>

## How to run

### Problem 2
    pip install numpy
        The numpy package is required since I used its array structure for this problem
    python smallestNumber.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python smallestNumber.py < test_files\fewest_1.txt

### Problem 3
    python rightTriangles.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python rightTriangles.py < test_files\rightangles_1.txt
