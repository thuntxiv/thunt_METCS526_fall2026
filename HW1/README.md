# METCS 526 Fall 2026 - HOMEWORK 1

## Author: Tyler Hunt

### Part 1: Introduce yourself

How many programming classes have you taken?
    <p>- 11
        <br>Computer Science 1
        <br>Data Structures
        <br>Computer Organization
        <br>Principles of Software
        <br>Operating Systems
        <br>Logic Systems and Logical Programming
        <br>Functional Programming
        <br>Software Design and Documentation
        <br>Introduction to Artificial Intelligence
        <br>Database Systems
        <br>Network Programming
    <br>- 13 if you count stuff like Foundations of Computer Science and
        Introduction to Algorithms that are more conceptual and 
        don't involve much actual programming
    <br>- 14 if you count purely project-based classes, since I took an
        Open-Source project development class a couple of times.</p>
Do you know Java or Python or both?
    <p>- I know both but I'm pretty rusty in my programming skills with them.</p>
What year are you in?
    <p>- 1st year M.S. in Software Development</p>
What is your experience level with algorithms and data structures?
    <p>- I have taken Data Structures and Introduction to Algorithms in my undergraduate,
        so I'm pretty experienced with them. In fact, I'm experienced enough to be scared
        at the mention of Dynamic Programming. However, I've forgotten a lot of what
        I learned, especially things like basic programming skills, so I'm very out of practice.</p>

### Part 2: Coding Assignment

    How to run from command line: 
        python helloworld.py

        if using a text file as the input stream: python helloworld.py < myfile
            (myfile is any text-based file, i.e. .txt, .md, .py, etc.)
    
    Directions: 
        Enter either the name of a text-based file within the working directory, or enter in the full 
        path of the file that you wish to have its contents printed to the standard output stream. If passing 
        a file to standard input, make sure the input file's first line matches the path or name of the desired file.

        Examples of expected input:
            myfile.txt
            C:\Users\tyler\myfile.txt

    Algorithm implementation:
        This algorithm is designed mainly to account for user error related to the computer's file system.
        Since the input file path needs to precisely match an existing file, I used a while loop and a nested
        try-except block to prevent the program from crashing when the user enters input that Python can't match
        to a file on the user's computer. This case results in a FileNotFoundError, and upon receiving this error,
        my program prints out some helpful text that gives examples of correct input, then it continues the while
        loop and lets the user try again.

        Once the program receives a file name or path that it can successfully open, it reads the entirety of the
        file's text and prints it out to the standard output stream. Lastly, the program closes the file to prevent
        any complications from leaving the file open.
