print('enter the numbers')
the_list = []
list_total = 0
for i in range(0, 5, 1):
    temp = int(input("please enter a  number"))
    the_list.append(temp)

for i in range(len(the_list)):
    list_total += the_list[i]

print('the first number is', the_list[0])
print('the last number is', the_list[-1])
print('the smallest number is', min(the_list))
print('the largest number is', max(the_list))
print('the average of the numbers is', list_total/len(the_list))
