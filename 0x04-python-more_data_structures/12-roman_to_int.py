#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previousValue = 0

    for a in range(len(roman_string) - 1, -1, -1):
        currentValue = roman_number[roman_string[a]]

        if currentValue >= previousValue:
            total += currentValue
        else:
            total -= currentValue


        previousValue = currentValue

    return total
