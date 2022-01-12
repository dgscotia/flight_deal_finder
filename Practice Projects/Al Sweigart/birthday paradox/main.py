import datetime
import random

""" BIRTHDAY PARADOX"""

""" Requirements:
    1. Prompt for a number of birthdays to be generated (max 100)
    2. Generate these birthdays
    3. Note where the same birthday exists, and print the date.
    4. Run 100,000 more simulations with this same number of birthdays.
    5. Calculate how many times the group had a matching birthday.
    """


def get_birthdays(number):
    """Returns a list of number random date objects for birthdays."""
    birthday_list = []
    for i in range(number):
        year_start = datetime.date(2021, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = (year_start + random_number_of_days).strftime("%b %#d")
        birthday_list.append(birthday)
    birthday_list.sort()
    return birthday_list


def find_duplicates(birthday_list):
    """ Checks for duplicate birthdays in a list."""
    duplicate_birthdays = []
    working_list = birthday_list.copy()
    for birthday in working_list:
        if working_list.count(birthday) > 1:
            duplicate_birthdays.append(birthday)
            working_list.remove(birthday)
    return duplicate_birthdays


def simulate(number):
    print(f"Generating {number} random birthdays 100,000 times...")
    input("Press Enter to start...")
    count = 0
    print_list = [x for x in range(0, 100000, 10000)]
    for x in range(100000):
        bday_list = get_birthdays(number)
        duplicate_list = find_duplicates(bday_list)
        count += len(duplicate_list)
        if x in print_list:
            print(f"{x} simulations run")
    return count


def print_one(number, birthday_list):
    print(f"\nHere are {number} birthdays: ")
    print(", ".join(birthday_list))


def print_two(duplicates):
    if duplicates:
        print("In this simulation, multiple people have a birthday on " + ", ".join(duplicates))
        print('\n')
    else:
        print("In this simulation, there were no duplicate birthdays.\n")


def print_three(number_of_birthdays, duplicate_frequency, probability):
    print(
        f"""\nOut of 100,000 simulations of {number_of_birthdays} people, there was a matching birthday in that group {duplicate_frequency} times. 
    This means that {number_of_birthdays} people have a {probability}% chance of having a matching birthday in their group. """)


def run():
    while True:
        print("How many birthdays shall I generate? (Max 100) ")
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            number_of_birthdays = int(response)
            break

    starting_birthday_list = get_birthdays(number_of_birthdays)
    print_one(number_of_birthdays, starting_birthday_list)

    duplicates = find_duplicates(starting_birthday_list)
    print_two(duplicates)

    duplicate_frequency = simulate(number_of_birthdays)
    probability = round(duplicate_frequency / 10000, 2)
    print_three(number_of_birthdays, duplicate_frequency, probability)

    quit()


run()
