# METCS 526 Fall 2026 - HOMEWORK 2
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 4 DRIVER----------------------------
import sys
from problem4 import SortedDoublyLinkedList

def is_number(str):
    '''
    Returns True or False according to whether the given string represents a number (including negatives and floats).

    PARAMETERS
        str:String
            A string to check if it represents a number or not
    RETURN
        INT
            0 if the string does not solely represent a number
            1 if the given string solely represents a positive or negative integer
            2 if the given string solely represents a positive or negative float
    '''
    if str[0] == '-': # Remove the negative sign for isdigit() to work
       str = str[1:]
    if str.isdigit(): # Integers will pass isdigit()
        return 1
    elif '.' in str: # Decimals need to be parsed differently
        str = str.split(".")
        if not False in [char.isdigit() for char in str]: # Separate by the decimal point and check if the components are digits
            return 2
    return 0

def process_commands(linkedlist:SortedDoublyLinkedList):
    '''
    Continuously read lines from stdin until the user quits or the EOF of the input file for stdin,
    and execute operations on a singly-linked list according to the given commands.

    PARAMETERS:
        linkedlist:SortedDoublyLinkedList
            An initialized sorted doubly-linked list
    RETURN:
        None
    '''
    l_num = 1 # Current line number
    for line in sys.stdin: # Repeatedly read lines from stdin
        line = line.strip().lower()
        parsed_line = line.split() 
        if len(parsed_line) == 0: # Ignore whitespace lines
            l_num += 1
            continue

        # Pull from well-defined directives corresponding to operations on the sorted doubly linked list object 
        match parsed_line[0]:
            case "add":
                if len(parsed_line) != 2: # Check every directive for proper format and number of arguments
                    print(f"line {l_num}: expected 'add <value>', got '{line}'")
                else:
                    # Make sure each given value is an integer or float
                    # Negative numbers and floats return false for isdigit(), so a helper function is needed
                    match is_number(parsed_line[1]):
                        case 0: # Non-number argument
                            print(f"line {l_num}: value must be a number, got '{line}'")
                            l_num += 1
                            continue 
                        case 1: # Integer argument
                            linkedlist.add(int(parsed_line[1]))
                        case 2: # Float argument
                            linkedlist.add(float(parsed_line[1]))                       
                    print(f"add({parsed_line[1]})")
            case "delete":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'delete <value>', got '{line}'")
                else:
                    deleted = False
                    match is_number(parsed_line[1]):
                        case 0: # Non-number argument
                            print(f"line {l_num}: value must be a number, got '{line}'")
                            l_num += 1
                            continue 
                        case 1: # Integer argument
                            deleted = linkedlist.delete(int(parsed_line[1]))
                        case 2: # Float argument
                            deleted = linkedlist.delete(float(parsed_line[1]))
                    if not deleted:
                        print(f"line {l_num}: {parsed_line[1]} not found, nothing deleted")
                    else:
                        print(f"delete({parsed_line[1]})")
            case "exists":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'exists <value>', got '{line}'")
                else:
                    exists = None
                    match is_number(parsed_line[1]):
                        case 0: # Non-number argument
                            print(f"line {l_num}: value must be a number, got '{line}'")
                            l_num += 1
                            continue 
                        case 1: # Integer argument
                            exists = linkedlist.exists(int(parsed_line[1]))
                        case 2: # Float argument
                            exists = linkedlist.exists(float(parsed_line[1]))
                    print(f"exists({parsed_line[1]}) = {exists}")
            case "print_list":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'print_list', got '{line}'")
                else:
                    linkedlist.print_list()
            case "len":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'len', got '{line}'")
                else:
                    print(f"len = {len(linkedlist)}")
            case "total":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'total', got '{line}'")
                else:
                    print(f"total = {linkedlist.total()}")
            case "sum_middle_three":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'sum_middle_three', got '{line}'")
                else:
                    try:
                        print(f"sum_middle_three = {linkedlist.sum_middle_three()}")
                    except ValueError: # sum_middle_three() raises a ValueError when there are < 3 nodes present
                        print(f"line {l_num}: sum_middle_three needs at least 3 nodes")
            case "median":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'median', got '{line}'")
                else:
                    try:
                        print(f"median = {linkedlist.median()}")
                    except ValueError: # median() raises a ValueError when the list is empty
                        print(f"line {l_num}: median of an empty list")
            case "count":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'count <value>', got '{line}'")
                else: 
                    count = None
                    match is_number(parsed_line[1]):
                        case 0: # Non-number argument
                            print(f"line {l_num}: value must be a number, got '{line}'")
                            l_num += 1
                            continue 
                        case 1: # Integer argument
                            count = linkedlist.count(int(parsed_line[1]))
                        case 2: # Float argument
                            count = linkedlist.count(float(parsed_line[1]))                    
                        
                    print(f"count({parsed_line[1]}) = {count}")
            case '#':
                pass
            case "quit": # Allows for exiting in cases when an input file is not used
                break
            case _:
                print(f"line {l_num}: unknown directive '{parsed_line[0]}'")
        l_num += 1
    print("Final list: ", end="")
    linkedlist.print_list()

def main():
    mylist = SortedDoublyLinkedList()
    process_commands(mylist)

if __name__ == "__main__":
    main()