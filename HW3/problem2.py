# METCS 526 Fall 2026 - HOMEWORK 3
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 2----------------------------

def rec_substrings(in_str, unique_substrs):
    '''
    Recursively finds all unique substrings of the given string and stores them in the given set

    PARAMETERS
        str:STRING
            A string to find all of its unique substrings
        unique_substrs:SET
            A set containing all unique substrings found so far
    RETURN
       None
    '''
    if in_str == "" or in_str in unique_substrs: # Base case: Ignore empty strings and already-counted strings
        return
    # Recursive case: attempt to add the current string to the set and recursively remove characters from
    # both ends in separate recursive calls. Handles all possibilities but is a bit costly in operations
    # due to redundant checking
    unique_substrs.add(in_str)
    rec_substrings(in_str[1:], unique_substrs) # Take a char off the front and call
    rec_substrings(in_str[:-1], unique_substrs) # Take a char off the back and call

def substrings(in_str):
    '''
    Finds and prints all unique substrings of the given string, then prints an integer count of the total
    number of substrings found

    PARAMETERS
        in_str:STRING
            A string to have all of its unique substrings printed
    RETURN
        None
    '''
    substrs = set() # Set to remove duplicates
    rec_substrings(in_str, substrs)
    substrs = list(substrs)
    substrs.sort() # Using built-in list sort because the problem isn't focused on sorting
    for s in substrs: # Print each substring in alphabetical order on separate lines
        print(s)
    print(len(substrs))

def check_input():
    '''
    Checks the first line of input from stdin for a string, then prints to the console all unique substrings
    of that string followed by the integer number of substrings found.

    PARAMETERS
        None
    RETURN
        None
    '''
    in_str = input()
    substrings(in_str)

def main():
    check_input()

if __name__ == "__main__":
    main()