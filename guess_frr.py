#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: September 2019
# This program runs the "Number Guessing Game" with a random number generator

import random


def main():
    # This function runs the random number guessing game

    # Variables
    random_number = random.randint(1, 10)

    # Input
    user_guess = int(input("Guess a number between 0 and (integer): "))
    print("")

    # process
    if user_guess == random_number:
        # Output 1
        print("You are correct!!! ")
    else:
        # Output 2
        print("Sorry, try again :) ")
        print("The number is: ", (random_number))


if __name__ == "__main__":
    main()
