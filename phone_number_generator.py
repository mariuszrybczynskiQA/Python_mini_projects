def create_phone_number(numbers):
    # List length check
    if len(numbers) != 10:
        return "Invalid list length!"

    # number formatting
    formatted_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

    return formatted_number


print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
