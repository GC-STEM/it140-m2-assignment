"""
name_age.py

Prompts the user for their name and age, then calculates and displays
the birth year. Assumes the user has already had their birthday this year.

Author: [Your Name]
Course: IT 140
"""

from datetime import datetime


def main():
    """Prompt for name and age, then display the year the user was born."""
    current_year = datetime.now().year

    name = input("What is your name? ")
    age = int(input("How old are you? "))

    birth_year = current_year - age

    print(f"Hello {name}! You were born in {birth_year}.")


if __name__ == "__main__":
    main()

