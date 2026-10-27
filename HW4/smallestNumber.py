# METCS 526 Fall 2026 - HOMEWORK 4
# Author: Tyler Hunt; Professor: Dr. David Mellor

import numpy

#------------------------------PROBLEM 2----------------------------

def partition(arr, low:int, high:int):
    '''
    A helper function for reverse_quicksort() that partitions the given array based around a pivot point
    obtained from the very last element of the array. At the end of this partition, elements greater than
    the pivot are placed before the pivot in the array, and elements less than the pivot are placed after
    the pivot.

    PARAMETERS
        arr:ARRAY<Comparable>
            An array of comparable elements to be partitioned
        low:INT
            The beginning index of the array to be partitioned
        high:INT
            The ending index of the array to be partitioned
    RETURN
        INT
            The index of the pivot point between the partitioned sections of the array
    '''
    pivot = arr[high] # Use the last element as the pivot
    i = low - 1

    # Iterate through the array and move elements greater than pivot to the left side.
    for j in range(low,high):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Move the pivot to the index directly after the group of larger elements
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def reverse_quicksort(arr, low:int, high:int):
    '''
    Sorts the given array in-place in descending order using the quicksort method

    PARAMETERS
        arr:ARRAY<Comparable>
            Any array with elements that are comparable using the > and < operators
        low:INT
            The starting index of the array or array portion to be sorted
        high:INT
            The ending index of the array or array portion to be sorted
    RETURN
        None
    '''
    if low < high: # Base case: low = high means the array is 1 or 0 elements and already sorted
        pi = partition(arr, low, high) # Recursive case: Partition the array and call quicksort on the two unsorted halves
        reverse_quicksort(arr ,low, pi - 1)
        reverse_quicksort(arr, pi + 1, high)

def smallest_sum(arr, target:int, size:int):
    '''
    Computes and returns the smallest amount of numbers in the given array that can be added up to a value greater than
    target.

    PARAMETERS
        arr:ARRAY<INT>
            An array of integers
        target:INT
            The target value that the sum should be greater than
        size:INT
            The integer size of arr
    RETURN
        INT
            An integer count of the fewest number of elements in arr that can be added up to a value greater than target.
    '''
    sorted_arr = arr.copy() # Leave the original array intact for printing
    reverse_quicksort(sorted_arr, 0, size - 1) # Sort the array in descending order to get the biggest values at the top
    sum = 0
    count = 0
    for n in sorted_arr: # Add the largest elements until the sum is greater than target. This should always result in the smallest amount of numbers added
        if sum > target:
            break
        sum += n
        count += 1
    return count

def check_input():
    '''
    Checks the first three lines of stdin for an array size, a target integer value, and an array of integers,
    then computes the smallest number of values that can be added to make a sum greater than target. After,
    the input array, target value, and smallest number of values are printed to stdout.

    PARAMETERS
        None
    RETURN
        None
    '''
    size = int(input()) # Line 1: array size
    target = int(input()) # Line 2: target
    arr = input().strip().split(" ") # Line 3: array of ints
    arr = numpy.array([int(x) for x in arr])
    count = smallest_sum(arr, target, size)

    # Print out input array followed by the target and the smallest sum cardinality
    print("Input: ", end="")
    for n in arr:
        if n != arr[0]:
            print(",", end="")
        print(n, end="")
    print(f" Target: {target}, Answer: {count}")

if __name__ == "__main__":
    check_input()