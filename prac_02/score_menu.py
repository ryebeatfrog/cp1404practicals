'''

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit


'''

MENU = """G - Get Score
P - Print score
S - Shows Stars
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))  # prints invalid option for some reason but works fine
            print(score)
        elif choice == "P":
            print_score(score)
        elif choice == "S":
            show_stars(score)
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def print_score(score):
    '''determines score'''
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    '''displays number of stars'''
    for i in range(score):
        print("*", end=" ")
    print()


main()
