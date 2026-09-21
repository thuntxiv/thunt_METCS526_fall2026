# Author: Tyler A. Hunt; Class: METCS 526; Professor: Dr. David Mellor

# Homework 1

fname = ""
outfile = ""

# Continuously read a file name or full file path from the user and attempt to open the file
#   The file *must* be present in the working directory to be passed in without a full path
#   Otherwise, the file name must have the full path preceding it.
while fname == "":
    try:
        # I would usually put a descriptive prompt in the input statement, but I decided to exclude it for the sake
        #   of matching the given example in the homework pdf.
        fname = input()
        outfile = open(fname, mode='r')
    
    # If the file could not be opened, print out some messages giving examples of correct input, then allow the user
    #   to try again.
    except FileNotFoundError:
        print("\nFailed to open file. Please make sure that the file is in the working directory," +
        " or that the file path is valid.")
        print("Example file (in working directory): myfile.txt\n")
        print("Example path: C:\\Users\\tyler\\myfile.txt")
        fname = ""
        
# Print out the whole contents of the file to stdout at once, then close the file stream
print("\n" + outfile.read())
outfile.close()