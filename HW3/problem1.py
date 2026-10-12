# METCS 526 Fall 2026 - HOMEWORK 3
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys

#------------------------------PROBLEM 1----------------------------

def isPalindrome(str):
    '''
    Checks if the given string is a palindrome, i.e. reads the same forwards and backwards, then returns
    True or False accordingly.

    PARAMETERS
        str:STRING
            A string to check whether it's a palindrome or not
    RETURN
        BOOL
            True if the given string is a palindrome
            False if the given string is not a palindrome
    '''
    if len(str) <= 1: # Empty strings and single-char strings are palindromes
        return True
    # Compare the first and last characters (still works for strings with spaces between chars)
    #   Lower and uppercase letters are treated as unique (i.e. Aa will fail the check)
    if str[0] == str[-1]: 
        return isPalindrome(str[1:-1])
    return False

def check_input():
    '''
    Checks each line of input from the stdin file for a string, then prints whether that string is a palindrome or not.
    At the end of the file, prints out the number of palindromes found.

    PARAMETERS
        None
    RETURN
        None
    '''
    palindromes = 0
    for line in sys.stdin:
        line = line.strip()
        if isPalindrome(line):
            palindromes += 1
            print(True)
        else:
            print(False)
    print(palindromes)

def main():
    check_input()

if __name__ == "__main__":
    main()