# METCS 526 Fall 2026 - MIDTERM
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys


#------------------------------PROBLEM 2----------------------------

def simulate_pandemic(counties:list, infected:int):
    '''
    Runs a simulation of a pandemic involving counties within an NxN grid representing a state,
    printing the grid of healthy and infected counties for each day of the pandemic and spreading
    the infection accordingly. For a county to be infected, it must neighbor at least two infected
    counties in cardinal directions. The simulation ends when no more counties can be infected, and
    a message is printed according to whether any healthy counties are left in the state or not.

    PARAMETERS
        counties:LIST<LIST<STRING>>
            The matrix of '.' and 'X' representing healthy and infected counties, respectively
        infected:INT
            The inital number of infected counties in the matrix on Day 1
    RETURN
        None
    '''
    prev_infected = infected # Used to determine whether new infected counties appear on each day
    size = len(counties)
    day = 1
    while True: # Run the simulation until counties can't be infected anymore
        print(f"Day {day}")
        print_counties(counties)
        infection_candidates = []

        # Loop through the matrix and check every healthy cell for possible infection
        for row in range(size):
            for col in range(size):
                if counties[row][col] != "X":
                    if can_infect(counties, row, col):
                        infection_candidates.append((row, col))
        # Update the newly infected counties
        for (row, col) in infection_candidates:
            counties[row][col] = "X"
        infected += len(infection_candidates)

        # Check if the simulation has ended (i.e. no new infected counties)
        if prev_infected == infected:
            break
        prev_infected = infected
        day += 1
    print(f"There are{" no" * (infected == len(counties)**2)} healthy counties left")

def can_infect(counties:list, row:int, col:int):
    '''
    Determines if the county at the given row, col coordinates is eligible to be infected, i.e. there are
    at least two vertical and/or horizontal neighbors that are infected. Returns True or False according to
    whether the county can be infected.

    PARAMETERS
        counties:LIST<LIST<STRING>>
            The matrix of healthy and infected counties represented by '.' and 'X' respectively
        row:INT
            The row index of the county to be checked
        col:INT
            The column index of the county to be checked
    RETURN
        BOOL
            True if at least two infected counties neighbor the current county in cardinal directions, and thus
                the county can be infected
            False otherwise, and the county can't be infected
    '''
    # Neighbors in each cardinal direction
    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    size = len(counties)
    neighboring_infected = 0
    # Out-of-bounds checks
    if up >= 0:
        if counties[up][col] == "X":
            neighboring_infected += 1
    if down < size:
        if counties[down][col] == "X":
            neighboring_infected += 1
    if left >= 0:
        if counties[row][left] == "X":
            neighboring_infected += 1
    if right < size:
        if counties[row][right] == "X":
            neighboring_infected += 1
    if neighboring_infected >= 2:
        return True
    return False


def print_counties(counties:list):
    '''
    Prints the matrix of counties to stdout.

    PARAMETERS
        counties:LIST<LIST<STRING>>
            The matrix of healthy and infected counties
    RETURN
        None
    '''
    for row in counties:
        for county in row:
            print(county, end=" ")
        print()


def check_input():
    '''
    Checks every line of input for the size of the state grid and the x,y coordinates of each initial infected county,
    then simulates a pandemic where counties are infected when vertically or horizontally neighboring two or more
    counties. Each day of the pandemic is printed to stdout, then a message is printed stating whether or not there
    are any healthy counties left in the state.

    PARAMETERS
        None
    RETURN
        None
    '''
    n = int(input()) # Line 1: Dimensions of counties grid
    counties = [['.' for _ in range(n)] for _ in range(n)] # Initialize grid of healthy counties

    infected = 0
    # Lines 2...: Coordinates of initial infected counties
    for line in sys.stdin:
        line = line.strip().split(" ")
        counties[int(line[0])][int(line[1])] = "X"
        infected += 1
    simulate_pandemic(counties, infected)


if __name__ == "__main__":
    check_input()