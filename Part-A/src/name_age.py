Ask for name and age and calculates the birth year

Input:
    User's name -string, enteredby the user
    Users age - integer, entered by the user
    Current calender year -integer, obtained by the system date

Process:
    Subtract the user age from the current year to calculate the approx birth year

Output:
    User name and approx birth year -displayed to the user in the system

Typical usage example:
    Enter your name: 
EX:Paloma
    Enter your age: 
EX:24
    Paloma was born around 2002
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"{name} was born around {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

