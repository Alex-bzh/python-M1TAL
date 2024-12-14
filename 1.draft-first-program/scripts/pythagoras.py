#!/usr/bin/env python

#
#  Libraries
#
import argparse
import math

#
#  User functions
#
def hypotenuse(a, o):
    """Calculates the hypotenuse thanks to
    the Pythagorean theorem in a right triangle.
    
    Positional arguments:
    a -- adjacent side
    o -- opposite side
    """
    square = (a ** 2) + (o ** 2)
    hypotenuse = math.sqrt(square)

    # rounded to two digits from the decimal point
    return round(hypotenuse, 2)

def main():
    # create the argument parser
    parser = argparse.ArgumentParser(description="Calculate the hypotenuse of a right triangle.")
    
    # add argument for the opposite side
    parser.add_argument('-o', '--opposite', type=float, required=True, help="Length of the opposite side")
    
    # create a mutually exclusive group for adjacent side and slope
    group = parser.add_mutually_exclusive_group(required=True)
    
    # add argument for the adjacent side
    group.add_argument('-a', '--adjacent', type=float, help="Length of the adjacent side")
    
    # add argument for slope
    group.add_argument('-s', '--slope', type=float, help="Slope in percentage")
    
    # parse the arguments
    args = parser.parse_args()
    
    # calculate the adjacent side if slope is given
    adjacent = (args.opposite / args.slope) * 100 if args.slope else args.adjacent
    
    # call the function with the provided arguments
    result = hypotenuse(adjacent, args.opposite)
    
    # print the result
    print(f"The hypotenuse is: {result}")

#
#   Main procedure
#
if __name__ == "__main__":
    main()
