# METCS 526 Fall 2026 - HOMEWORK 5
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys

#------------------------------PROBLEM 2----------------------------

def count_vowels(morse):
    '''
    Computes and returns the total number of vowel-only sequences that can be 
    derived from the given morse code string.

    PARAMETERS
        morse:STRING
            A string containing a sequence of '.' and '-'
    RETURN
        INT
            The number of possible vowel-only sequences that the morse code string can produce
    '''
    n = len(morse)

    # P[i] = number of ways to decode with vowels up to offset i
    # This is the bottom row of the table from the lecture slides plus one cell at the start
    P = [0] * (n + 1)

    # Base case: Empty string holds 1 possible combination (to give a starting point for future offsets)
    P[0] = 1

    # Dictionary of valid morse code vowels and corresponding lengths
    vowels = {".": 1, ".-": 2, "..": 2, "---": 3,"..-": 3}

    # Visit each offset and populate the state table
    for i in range(n):

        # Check each possible vowel code
        for code, length in vowels.items():

            # Make sure the code doesn't extend past the string's last char
            if i + length <= n:
                # Look ahead: check whether the next 1/2/3 characters match a vowel
                if morse[i:i+length] == code:
                    # Add the current combinations to the state table at the offset 1/2/3 chars ahead
                    P[i+length] += P[i]
    return P[n]

def main():
    '''
    Parses the text file provided as a command line argument for the size of the morse code string
    and the string itself, then calculates the amount of vowel combinations that can be derived from
    the string.
    '''
    file_name = sys.argv[1]
    with open(file_name, mode='r') as morse_input:
        size = int(morse_input.readline().strip())
        code = morse_input.readline().strip()
    if "test_files" in file_name:
        file_name = file_name.split('\\')[1]
    print(f"File input: {file_name}")
    print(f"The Number of Vowel combinations is: {count_vowels(code)}")

if __name__ == "__main__":
    main()