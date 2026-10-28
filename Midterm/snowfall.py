# METCS 526 Fall 2026 - MIDTERM
# Author: Tyler Hunt; Professor: Dr. David Mellor

import numpy

#------------------------------PROBLEM 1----------------------------

def check_snowfall(snowfall, size):
    '''
    Checks if any three consecutive days exist in the given array of cumulative snowfall totals where
    the combined snowfall across those three days exceed half of the total snowfall for the entire array.
    Returns True or False accordingly.

    PARAMETERS
        snowfall:ARRAY<INT>
            An array of integers representing the cumulative snowfall from the beginning of the period until
            the given day represented by each element.
        size:INT
            The number of elements in the array
    RETURN
        BOOL
            True if three consecutive days exist that have a combined snowfall total greater than half of the
                entire time period's cumulative snowfall total
            False otherwise
    '''
    if size >= 3:
        half_total_snowfall = float(snowfall[size - 1]) / 2
        prev_total = 0 # Using a variable for A[i-1] since it's out of bounds on the first loop pass
        # Check each sequence of three consecutive days
        for i in range(size - 2):
            consecutive_total = snowfall[i + 2] - prev_total # Snowfall for days i, i+1, i+2 = A[i+2] - A[i-1]
            if consecutive_total > half_total_snowfall: # Strictly greater than half the total snowfall
                return True
            prev_total = snowfall[i]
    return False

def check_input():
    '''
    Checks the first 2 lines of input for the number of days and the array of cumulative snowfall totals,
    then prints out whether three days exist that have a total greater than half of the overall total.

    PARAMETERS
        None
    RETURN
        None
    '''
    num_days = int(input()) # Line 1: Number of days
    snow_totals = input().strip().split(" ") # Line 2: Array of snowfall totals
    snow_totals = numpy.array([int(x) for x in snow_totals])

    # Print out input array followed by whether or not three days exist in the array with a large enough
    # cumulative snowfall total
    for n in snow_totals:
        print(n, end=" ")
    if check_snowfall(snow_totals, num_days):
        print("solution: YES")
    else:
        print("solution: NO")

if __name__ == "__main__":
    check_input()