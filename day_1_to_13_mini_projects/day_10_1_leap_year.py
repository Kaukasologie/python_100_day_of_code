# Helps to find out whether a certain year is a leap year or not.

# Year is a Leap Year:
# - on every year that is divisible by 4 with no remainder.
# - *except* every year that is evenly divisible by 100 with no remainder.
# - *unless* the year is also divisible by 400 with no remainder.

def is_leap_year(year):
    """Determines whether the entered year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True     # If year divisible without remainder by 4, 100 and 400, then it's Leap Year.
            else:
                return False    # If year divisible without remainder by 4 and 100, but not 400, then it's not Leap Year.
        else:
            return True         # If year divisible without remainder by 4, but not 100, then it's Leap Year.
    else:
        return False            # If year not divisible without remainder by 4, then it's not Leap Year.


try:
    chosen_year = int(input("\nHi! Input the year you are interested in and I will tell you whether it is a leap year or not.\n--->> "))
except ValueError:
    print("Invalid input. Start again and input a whole number.")
else:
    if is_leap_year(chosen_year):
        print(f"{chosen_year} is a Leap Year.")
    else:
        print(f"{chosen_year} is NOT a Leap Year.")
