"""Check whether a Gregorian calendar year is a leap year."""

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Invalid input: enter a whole-number year.")
        return
    if year < 1:
        print("Invalid input: enter a positive year.")
        return
    print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}.")

if __name__ == "__main__":
    main()
