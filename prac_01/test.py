items = int(input('Enter the number of items: '))
itemtab = []
if items > 0:
    for i in range(items):
        item = float(input('Enter the price of item: $'))
        itemtab.append(item)
    totalprice = sum(itemtab)
    if totalprice > 100:
        print('Total cost for', items, 'items: $', totalprice * 0.9)
    elif totalprice <= 100:
        print('Total cost for', items, 'items: $', totalprice)
else:
    print('dont enter a neg number :(')
