"""TODO: Greet users by name and the year they were born. (<73 chars).

Input:
    TODO: from datetime import datetime
    TODO: print("What is your name?")
    TODO: user_name = input()
    print("How old are you " + user_name + "?")

Process:
    TODO: age = int(input())
current_year = datetime.now().year

Output:
    TODO: birth_year = current_year - age
print("Hello " + user_name + "! You were born in " + str(birth_year) + ".")

Typical usage example:
    TODO: Amanda
    TODO: 15
    TODO: Hello Amanda you were born in 2011
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # TODO: Replace with code to get user's name as a string. See zyBooks 1.3.
    # TODO: Replace with code to get user's age as an integer. See zyBooks 2.6.

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.

    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
