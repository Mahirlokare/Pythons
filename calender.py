import calendar

def print_calendar(month, year):
    # Print the calendar header
    print(f"\n     {calendar.month_name[month]} {year}")
    print(" Su Mo Tu We Th Fr Sa")

    # Get the starting day of the week and the number of days in the month
    first_day, num_days = calendar.monthrange(year, month)

    # Print leading spaces for the first week
    for _ in range(first_day):
        print("   ", end="")

    # Print the days of the month
    for day in range(1, num_days + 1):
        print(f"{day:2}", end=" ")
        if (first_day + day) % 7 == 0:
            print()

    print()

# Input month and year
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

# Print the calendar for the given month and year
print_calendar(month, year)