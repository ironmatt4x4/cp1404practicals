while True:
    try:
        itemtemp = int(input('Enter the number of items: '))
        if itemtemp >= 0:
            items = itemtemp
            itemtab = []

            for i in range(items):
                item = float(input('Enter the price of item: $'))
                itemtab.append(item)

            print("Number of items:", items)
            #for i in range(len(itemtab)):
            #    j = itemtab[i]
            #    print('Item price: $', j)
            totalprice = sum(itemtab)
            if totalprice > 100:
                print('Total cost for', items, 'items: $', totalprice * 0.9)
            else:
                print('Total cost for', items, 'items: $', totalprice)
            break
        else:
            print('Please enter a number')

    except ValueError:
        print('Please enter only numbers (e.g. 5)')
        tryagain = input('Try again? (y or n)')
        if tryagain == 'y':
            continue
        elif tryagain == 'n':
            break
        else:
            print('Enter y or n')
