# METCS 526 Fall 2026 - HOMEWORK 5
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 3----------------------------

import sys

def longest_alternating_sequence(A:list, B:list):
    '''
    Finds the length of the longest alternating increasing sequence between the integer lists A
    and B such that: 
        - The elements of the resulting sequence have even-indexed elements
            from only list A or B, and odd-indexed elements from the other list (i.e. odd A,
            even B, or odd B even A)
        - The elements are in strictly increasing order
        - The elements from each sequence A and B preserve the order from their original
            sequences within their even/odd groups
    
    PARAMETERS
        A:LIST<INT>
            A list of integers
        B:LIST<INT>
            Another list of integers
    RETURN
        INT
            The length of the longest alternating increasing sequence found using the elements 
            of sequences A and B
    '''
    m = len(A)
    n = len(B)

    # Create the lookup lists; Each element can form a sequence of length >= 1
    ls_A = [1] * m
    ls_B = [1] * n

    # Process both arrays in order of position
    for pos in range(max(m, n)):

        # Find the longest sequence ending at A[pos]
        if pos < m:
            for j in range(min(pos, n)):
                if B[j] < A[pos]:
                    ls_A[pos] = max(ls_A[pos], ls_B[j] + 1)

        # Find the longest sequence ending at B[pos]
        if pos < n:
            for i in range(min(pos, m)):
                if A[i] < B[pos]:
                    ls_B[pos] = max(ls_B[pos], ls_A[i] + 1)

    # The answer is the length of the longest sequence ending at any element in either array
    return max(ls_A + ls_B)

def main():
    '''
    Parses the text file provided as a command line argument for the sizes of both integer
    sequences followed by each sequence, then finds the length of the longest increasing alternating
    sequence between both integer sequences.
    '''
    file_name = sys.argv[1]
    with open(file_name, mode='r') as seq_input:
        sizes = (int(seq_input.readline().strip()), int(seq_input.readline().strip()))
        seq_A = seq_input.readline().strip().split(" ")
        seq_A = [int(x) for x in seq_A]
        seq_B = seq_input.readline().strip().split(" ")
        seq_B = [int(x) for x in seq_B]
    if "test_files" in file_name:
            file_name = file_name.split('\\')[1]
    print(f"File Input: {file_name}")
    print(f"Longest Sequence: {longest_alternating_sequence(seq_A, seq_B)}")


if __name__ == "__main__":
    main()