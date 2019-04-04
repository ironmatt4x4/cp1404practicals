colours = {'aliceblue': '#f0f8ff', 'antiquewhite': '#faebd7', 'antiquewhite1': '#ffefdb',
           'antiquewhite2': '#eedfcc', 'antiquewhite3': '#cdc0b0', 'antiquewhite4': '#8b8378',
           'aquamarine1': '#7fffd4', 'aquamarine2': '#76eec6', 'aquamarine4': '#458b74',
           'beige': '#f5f5dc'}
while True:
    what_colour = input('Enter the colour').lower()
    try:
        if len(what_colour) < 1:
            print('thank you')
            break
        else:
            print(colours[what_colour])
    except KeyError:
        print('enter a valid colour')

# 'bisque1': '#ffe4c4'
