# METCS 526 Fall 2026 - HOMEWORK 3
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys

#------------------------------PROBLEM 4----------------------------

def ghosts_busted(busters:list, ghosts:list):
    '''
    Determines whether all ghosts have been successfully eliminated, i.e. no streams from the ghostbusters have
    intersected, and returns a boolean according to the result.
    A stream is defined as a line passing through both the ghostbuster's and their corresponding ghost's coordinates.

    PARAMETERS
        busters:LIST<TUPLE<INT>>
            a list containing tuples of the x,y coordinates of each ghostbuster,
            with each index corresponding to a ghost in ghosts.
        ghosts:LIST<TUPLE<INT>>
            a list containing tuples of the x,y, coordinates of each ghost,
            with each index corresponding to a ghostbuster in busters.
    RETURN
        True if none of the streams intersect (i.e. all have the same slope)
        False if any of the streams intersect (at least 1 stream has a different slope)
    '''
    # iterate through the lists and determine the slope of every stream. If they aren't all the same slope, the streams will
    # intersect and the ghosts will not be eliminated
    slope = None
    x_intersections = [] # Account for the same line being passed twice as input via tracking x-axis intersections
    for i in range(len(busters)):
        buster = busters[i]
        ghost = ghosts[i]
        if ghost[0] - buster[0] == 0: # Avoid dividing by zero
            new_slope = "Vertical"
        elif ghost[1] - buster[1] == 0:
            new_slope = "Horizontal"
        else:
            # Slope:    y_2 - y_1
            #           ---------
            #           x_2 - x_1
            new_slope = float(ghost[1] - buster[1]) / (ghost[0] - buster[0])

        if slope == None:
            slope = new_slope
            continue

        # Determine the line's intersection with the x-axis to rule out identical lines
        x_0 = None
        if new_slope == "Vertical":
            x_0 = ghost[0]
        elif new_slope == "Horizontal":
            x_0 = ghost[1] # If horizontal, use the y-axis intersection
        else:
            # y = mx + b; b = y - mx; x = (y - b) / m
            # for y = 0, x = -b / m
            b = float(ghost[1]) - new_slope * ghost[0]
            x_0 = -1 * b / new_slope
        # For infinite lines, all slopes must be equivalent, or else they will eventually intersect
        # If two lines have the same slope and same x-axis intersection, the lines are equivalent and therefore intersect
        if new_slope != slope or x_0 in x_intersections: 
            return False
        x_intersections.append(x_0)
    return True

def check_input():
    '''
    Reads an input file containing one line with an integer, 'n', describing the amount of ghosts and busters present,
    then reads lines 1 through n+1 before determining whether or not all ghosts were eliminated by the ghostbusters,
    i.e. none of the ghostbusters' streams (infinite lines stretching toward each buster's ghost and behind the buster) intersect.

    PARAMETERS
        None
    RETURN
        None
    '''
    # Each index in busters corresponds to the same index in ghosts
    busters = []
    ghosts = []
    for line in sys.stdin:
        parsed_line = line.strip().split(" ")
        if len(parsed_line) != 1: # Don't need the count of ghosts and busters
            busters.append((int(parsed_line[1]), int(parsed_line[2])))
            ghosts.append((int(parsed_line[4]), int(parsed_line[5])))
    print(f"All Ghosts: were{" not" * (not ghosts_busted(busters, ghosts))} eliminated")

def main():
    check_input()

if __name__ == "__main__":
    main()