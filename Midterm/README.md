# METCS 526 Fall 2026 - MIDTERM

### Author: Tyler Hunt; Professor: Dr. David Mellor

## Introduction
<p>For this Midterm exam, I needed to solve three problems involving an array of snowfall measurements, a pandemic spreading across
neighboring counties, and a symbol puzzle board.</p>

<p>In snowfall.py (problem 1), I used a simple iterative algorithm to check each possible triplet of consecutive days for a subtotal
greater than half of the cumulative snowfall total.</p>

<p>In pandemic.py (problem 2), I compiled the list of counties that could be infected by iterating through the matrix, then 
I updated their statuses accordingly for each day of the simulated pandemic until no more new counties could be infected.</p>

<p>In puzzle_game.py (problem 3), I used a few separate loops between helper functions to exhaustively check every condition for the game,
including duplicate symbols in rows/columns, duplicate symbols in the board's sub-boards, and invalid characters.</p>

## Algorithm

### Problem 1
<p>My solution to the snowfall problem is a simple iterative approach due to the constraint of needing consecutive totals in the given
array. I used an O(n) approach that loops through the array and checks the total at index i+2, subtracting the total from index i-1
(0 if at the beginning of the array, kept track of using a variable) to obtain the snowfall from only the three days being checked currently. 
From there, all I had to do was compare it to half of the array's final element, which represents the total cumulative snowfall over all n days,
and repeat the process until I either find a sum that is large enough or I reach the end of the array. The space requirement should also be O(n), 
since the only structure I need is the input array.</p>

### Problem 2
<p>I had initially thought about using a queue akin to tree search algorithms, but I figured that there wasn't much gain with a sequential
structure like a matrix where every index is easily accessible. So, I just decided on a simple iterative update algorithm that simulates
the pandemic on each day and checks every individual healthy county's neighbors to determine whether or not it needs to be infected. The
eligible counties to be infected are first added to a separate list to ensure that counties aren't infected by any newly infected counties
on that day, only counties that were infected the previous day. Then, once the list is compiled, I iterate through that list of candidate
counties to be infected and update their status in the matrix. This process repeats until the number of infected counties doesn't change
on the current day. The time complexity of this algorithm is O(d*n) where d is the number of days that the simulation runs and n is the
total number of counties in the grid, since my infection checking algorithm doesn't use any loops and the infection status updating loop
occurs after my first iteration through the matrix. The space complexity is probably O(2n), since I need the matrix for all of the counties,
and my list of infection candidate counties likely counts as n even though it can only contain a subset of the matrix's coordinates on any
given loop.</p>

### Problem 3
<p>To tackle this problem, I decided to make a couple passes over the whole game board, checking different conditions along the way. First,
I iterated over the entire game board and made sure rules 1, 2, and 4 were followed, i.e. no duplicate symbols in the same row or column, and
no invalid symbols. This logic is handled between the helper functions check_subboard() and check_symbol(). Check_subboard() is O(n), traversing
each game tile, and check_symbol is O(sqrt(n)), since it only loops from 0 to the side length of the game board while checking the row and column
as it moves. So, this initial board check is an O(sqrt(n)*n) = O(n^1.5) operation, where n is the total number of tiles in the game board 
(not the side length of the board, which is N = sqrt(n)). </p>

<p>Then, I moved on to the sub-boards of size sqrt(n) in a  new loop. Working with sqrt(n) as the size of each sub-board and multiple offsets to 
properly index each sub-board and slice the matrix's contents accordingly, I separated each sub-board using an O(sqrt(n)) loop and then looped 
over the contents of each sub-board via check_subboard() and a boolean flag to tell check_subboard() that it needs to check for duplicate symbols 
across the entier sub-board. This handles all cases in my testing, and I believe it amounts to O(sqrt(n) * n * sqrt(n)), which comes out to O(n^2).
Calling check_subboard() happens within the O(sqrt(n)) loop that separates the sub-boards, and as I established above, calling check_subboard() on
the whole board is O(n^1.5), so from my understanding, the total time complexity of this program comes out to O(n^2).</p>

<p>In terms of space complexity, the largest containers are an O(n) matrix to store the initial game board and a matrix of size O(sqrt(n)) that 
stores each initial game board. Technically, it does get larger than that when I'm first populating it with the entire set of rows I need preceding my 
slicing, so I'll just call it O(n) with some constant that we can ignore. Overall, my space requirement is probably O(2n).</p>

## Notable Aspects

### Problem 1
Nothing, really. It was a simple iterative array algorithm, so there's not much to say.

### Problem 2
Not much, to be honest. Maybe breaking down the problem with a helper function via my can_infect() function?

### Problem 3
The most notable thing was how figuring out the indices and offsets of the sub-boards and their data really gave me a headache. It was a mix of multiplying
my loop indices by the sub-board size and adding either the sub-board size or a whole separate row offset to slice the correct data I need for this particular
sub-board.

## How to run

### Problem 1
    pip install numpy
        The numpy package is required since I used its array structure for this problem
    python snowfall.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python snowfall.py < test_files\snowfall_input1.txt

### Problem 2
    python pandemic.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python pandemic.py < test_files\pandemic_input1.txt

### Problem 3
    python puzzle_game.py < (input file)
        To use the text files in the test_files directory, use the following (replacing the file name as needed):
            python puzzle_game.py < test_files\puzzle_game_input1.txt
