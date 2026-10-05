# METCS 526 Fall 2026 - HOMEWORK 2
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 3----------------------------

def ways(n):
    '''
    A recursive function that, given the number of steps n in a staircase,
    returns the maximum number of different ways that the stairs can be
    climbed in steps of 1, 2, and 3 stairs at a time.

    PARAMETERS
        n:INT
            The total number of steps in the staircase to be climbed
    RETURN
        INT
            The number of unique ways that the staircase can be climbed
            in 1, 2, and 3 step increments.
    '''

    if n < 0: # Stepped too far; Not a valid way
        return 0
    if n == 0: # No more steps to take; Valid way
        return 1
    # Attempt to take one, two, and three steps repeatedly until the staircase is climbed
    return ways(n-1) + ways(n-2) + ways(n-3)

def print_steps(n, combos):
    '''
    Simple printing function for the input number of steps and the resulting ways to climb
    '''
    print(f"Step combinations for an input of {n} steps: {combos}")


def main():
   print_steps(1, ways(1))
   print_steps(2, ways(2))
   print_steps(3, ways(3))
   print_steps(4, ways(4))
   print_steps(5, ways(5))
   print_steps(7, ways(7))
   print_steps(10, ways(10))

if __name__ == "__main__":
    main()