"""
CP1404/CP5632 - Practical 1
Broken program to determine score status\

score must be between 0 and 100 inclusive;
90 or more is excellent;
50 or more is a pass;
below 50 is bad.
There is no intention to do any repetition.


"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
