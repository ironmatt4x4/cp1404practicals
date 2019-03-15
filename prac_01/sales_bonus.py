"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
while True:

    sales = float(input("Enter sales: $"))
    if 0 <= sales < 1000.0:
        print("Your bonus is 10% or $", sales * 0.1)
    elif sales >= 1000:
        print("Your bonus is 15% or $", sales * 0.15)
    elif sales < 0:
        break