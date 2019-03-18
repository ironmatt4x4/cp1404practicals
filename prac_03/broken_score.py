"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    determine_status(score)


def determine_status(score):
    result = 0
    if score < 0:
        return 'Invalid score'
    elif score > 100:
        return 'Invalid score'
    else:
        if score > 100:
            result = "Invalid score"
        if 90 > score >= 50:
            result = "Passable"
        if score >= 90:
            result = "Excellent"
        if score < 50:
            result = "Bad"
        return result


main()
