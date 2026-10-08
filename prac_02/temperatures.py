"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            calculate_celcius_to_fahrenheit()
        elif choice == "F":
            calculate_fahrenheit_to_celcius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celcius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def calculate_fahrenheit_to_celcius():
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()
