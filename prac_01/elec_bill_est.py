print('Electricity bill estimator')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

select_tariff = input('Which tariff? 11 or 31: ')
if select_tariff == 11:
    cost = TARIFF_11

elif select_tariff == 31:
    cost = TARIFF_31

usage = float(input('Enter daily use in KWh: '))
days = float(input('Enter number of billing days: '))
total_cost = cost * usage * days
print('Estimated bill: $', round(total_cost, 2))
