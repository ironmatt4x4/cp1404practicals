for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 100, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

stars = int(input("enter the number of stars: "))

for m in range(0, stars, 1):
    print('*', end=' ')
print()
print()
stars1 = stars + 1
for n in range(0, stars1, 1):
    for o in range(0, n, 1):
        print('*', end='')
    print()
print()