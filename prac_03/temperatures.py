"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
C_OR_F = """type in the value :"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    print(C_OR_F)
    value = float(input(">"))

    if choice == 'C':
        convert_celsius_to_fahrenheit(value)
    elif choice == 'F':
        convert_fahrenheit_to_celsius(value)
    elif choice == 'Q':
        print('Thank you')
    else:
        print('Please only enter C, F or Q')


def convert_celsius_to_fahrenheit(value):
    fahrenheit = value * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(value):
    celsius = 5 / 9 * (value - 32)
    return celsius

main()