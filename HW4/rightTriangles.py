# METCS 526 Fall 2026 - HOMEWORK 4
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys
import math
from collections import defaultdict

#------------------------------PROBLEM 3----------------------------

def check_right_triangles(points):
    '''
    Determines the maximum number of unique right triangles that can be made using the given list of points,
    and returns an integer representing that amount.

    PARAMETERS
        points:LIST<(int, int)>
            A list of integer tuples representing (x,y) points on a 2-dimensional plane
    RETURN
        INT
            An integer count of the total unique right triangles that can be produced from the given list of points
    '''
    triangles = 0

    # Consider each point as the vertex where the right triangle's perpendicular lines might meet
    for vertex1 in points:
        x1, y1 = vertex1[0], vertex1[1]

        # Contains frequencies that each vector direction (outward from vertex1) occurs
        direction_count = defaultdict(int) 

        # Calculate vectors from the current vertex to every other possible vertex, then compare pairs to see if any are perpendicular
        for vertex2 in points:
            if vertex1 == vertex2:
                continue

            x2, y2 = vertex2[0], vertex2[1]

            # Distance vector from vertex1 to vertex2
            dx = x2 - x1
            dy = y2 - y1

            # Normalize the vector using the greatest common divisor
            gcd = math.gcd(abs(dx), abs(dy))
            dx = dx // gcd
            dy = dy // gcd

            # Update the vector's frequency in the dictionary accordingly
            direction_count[(dx, dy)] += 1

        # Find perpendicular vectors by rotating each vector 90 degrees counterclockwise (dx, dy -> -dy, dx),
        # then check if those vectors exist in the dictionary
        for (dx, dy), count in direction_count.items():
            perpendicular = (-dy, dx)

            # If we've recorded the perpendicular vector in the previous loop, a right triangle can be made,
            # so add the frequency to the total count
            triangles += count * direction_count.get(perpendicular, 0)
    return triangles


def check_input():
    '''
    Checks stdin for a count of how many points are present in the 2-D space, then compiles each point on subsequent
    lines before determining and printing out how many right triangles can be produced given the input points.

    PARAMETERS
        None
    RETURN
        None
    '''
    num_points = 0 # Unused since I'm using a python List to store the point tuples
    points = []
    for line in sys.stdin:
        line = line.strip().split(" ")
        if len(line) == 1: # First line giving the number of points
            num_points = int(line[0])
        elif len(line) > 1: # All following lines contaning a pair of x and y coordinates
            points.append((int(line[0]), int(line[1])))
    count = check_right_triangles(points)
    print(f"The number of right triangles is: {count}")

if __name__ == "__main__":
    check_input()