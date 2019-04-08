the_string = input('Enter the string')

print('Text:', the_string)

list_string = the_string.split()
final_list = {}

for item in list_string:
    if item in final_list:
        final_list[item] += 1
    else:
        final_list.update({item: 1})

sorted_list = []

for item in final_list:
    sorted_list.append([item, final_list[item]])
sorted_list.sort()

for row in sorted_list:
    print(row[0], ':', row[1])
