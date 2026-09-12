"""Calculate a user's birth year from their name and age.

Input:
User's name as a string, entered at the keyboard.
User's age as an integer, entered at the keyboard.
    

Process:
Calculate the approximate birth year by subtracting age from the current year.

Output:
Personalized birth-year message as text, displayed to the user.

Typical usage example:
What is your name? Alex
How old are you? 24
Hello Alex! You were born in 2002.
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

