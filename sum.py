#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can find the sum of numbers using a while loop


def main():
    # This function can find the sum of numbers using a while loop

    # Variables
    sum_ = 0
    counter = 1

    # Input
    positive_integer = int(input("Enter a positive integer here: "))

    # Process
    while positive_integer >= counter:
        sum_ = sum_ + counter
        counter += 1

    # Output
    print("The sum is", sum_)


if __name__ == "__main__":
    main()
