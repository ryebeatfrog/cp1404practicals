"""
CP1404/CP5632 - Practical
Program to determine score status

Your main function should ask the user for their score and print the result.

Write a new function that takes in the user's score as a parameter
and returns the result to be printed.

Follow SRP: This function must not print the result.

Now add a new part to the bottom of your main function that generates a random score and prints the result.
You do NOT need to write a different function to determine the result for the random score.



"""

import random

def main():
    score = float(input("Enter score: "))
    determines_result(score)

    # random_score = random.randint(0, 100)
    # print(f"random: {random_score} = ")


def determines_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
