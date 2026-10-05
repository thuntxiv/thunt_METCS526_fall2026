# METCS 526 Fall 2026 - HOMEWORK 2
# Author: Tyler Hunt; Professor: Dr. David Mellor

#------------------------------PROBLEM 2 DRIVER----------------------------
import sys
from problem2 import SinglyLinkedList

def is_negative_int(str):
    '''
    Returns True or False according to whether the given string represents a negative integer.

    PARAMETERS
        str:String
            A string to check if it represents a negative integer
    RETURN
        BOOL
            True if the given string solely represents a negative integer
            False if the string contains any characters that don't make up a negative integer
    '''
    try:
        is_negative = str[0] == '-' and int(str) < 0 and float(str) % 1 == 0
    except: # If str is not a number, it will raise an error on the int() cast
        return False
    return is_negative

def process_commands(linkedlist:SinglyLinkedList):
    '''
    Continuously read lines from stdin until the user quits or the EOF of the input file for stdin,
    and execute operations on a singly-linked list according to the given commands.

    PARAMETERS:
        linkedlist:SinglyLinkedList
            An initialized singly-linked list
    RETURN:
        None
    '''
    l_num = 1 # Current line number
    # Repeatedly read lines from stdin
    for line in sys.stdin:
        line = line.strip()
        parsed_line = line.split() 
        if len(parsed_line) == 0: # Ignore whitespace lines
            l_num += 1
            continue
        # Pull from well-defined directives corresponding to operations on the linked list object 
        match parsed_line[0]:
            case "append":
                if len(parsed_line) != 2: # Check every directive for proper format and number of arguments
                    print(f"line {l_num}: expected 'append <value>', got '{line}'")
                else:
                    linkedlist.append(int(parsed_line[1]))
            case "prepend":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'prepend <value>', got '{line}'")
                else:
                    linkedlist.prepend(int(parsed_line[1]))
            case "insert":
                if len(parsed_line) != 3:
                    print(f"line {l_num}: expected 'insert <index> <value>', got '{line}'")
                else:
                    # Make sure each index is an integer (negative numbers allowed because of my implementation)
                    # Negative numbers return false for isdigit(), so a helper function is needed
                    if parsed_line[1].isdigit() or is_negative_int(parsed_line[1]): 
                        try:
                            linkedlist.insert(int(parsed_line[1]), int(parsed_line[2]))
                        except IndexError:
                            print(f"line {l_num}: index {parsed_line[1]} out of range") 
                    else:
                        print(f"line {l_num}: index must be an integer, got '{line}'")  
            case "get":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'get <index>', got '{line}'")
                else:
                    if parsed_line[1].isdigit() or is_negative_int(parsed_line[1]):
                        try:
                            val = linkedlist.get(int(parsed_line[1]))
                            print(f"get({parsed_line[1]}) = {val}")
                        except IndexError:
                            print(f"line {l_num}: index {parsed_line[1]} out of range") 
                    else:
                        print(f"line {l_num}: index must be an integer, got '{line}'")
            case "find":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'find <value>', got '{line}'")
                else:
                    index = linkedlist.find(int(parsed_line[1]))
                    print(f"find({parsed_line[1]}) = {index}")
            case "len":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'len', got '{line}'")
                else:
                    print(f"len = {len(linkedlist)}")
            case "update":
                if len(parsed_line) != 3:
                    print(f"line {l_num}: expected 'update <index> <value>', got '{line}'")
                else:
                    if parsed_line[1].isdigit() or is_negative_int(parsed_line[1]):
                        try:
                            linkedlist.update(int(parsed_line[1]), int(parsed_line[2]))
                        except IndexError:
                            print(f"line {l_num}: index {parsed_line[1]} out of range")
                    else:
                        print(f"line {l_num}: index must be an integer, got '{line}'") 
            case "delete":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'delete <value>', got '{line}'")
                else:
                    if not linkedlist.delete(int(parsed_line[1])):
                        print(f"line {l_num}: {parsed_line[1]} not found, nothing deleted")
            case "delete_at":
                if len(parsed_line) != 2:
                    print(f"line {l_num}: expected 'delete_at <index>', got '{line}'")
                else:
                    if parsed_line[1].isdigit() or is_negative_int(parsed_line[1]):
                        try:
                            val = linkedlist.delete_at(int(parsed_line[1]))
                            print(f"delete_at({parsed_line[1]}) = {val}")
                        except IndexError:
                            print(f"line {l_num}: index {parsed_line[1]} out of range")
                    else:
                        print(f"line {l_num}: index must be an integer, got '{line}'")
            case "print_list":
                if len(parsed_line) != 1:
                    print(f"line {l_num}: expected 'print_list', got '{line}'")
                else:
                    linkedlist.print_list()
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
    mylist = SinglyLinkedList()
    process_commands(mylist)

if __name__ == "__main__":
    main()