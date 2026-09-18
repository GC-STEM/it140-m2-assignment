from datetime import date 

CURRENT_YEAR = date.today().year 

def main() -> None: 
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    birth_year = CURRENT_YEAR - age
    print(f"Hello {name}! You were born in {birth_year}.")

if __name__ == "__main__": 
    main()
