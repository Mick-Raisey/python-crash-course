# 4-13. Buffet

# Think of five simple foods, and store them in a tuple.
# 1. Use a for loop to print each food the restaurant offers.
# 2. Try to modify one of the items, and make sure that Python rejects the change.
# 3. The restaurant changes its menu, replacing two of the items with different
#    foods. Add a line that rewrites the tuple, and then use a for loop to print
#    each of the items on the revised menu.

menu = ('beef schnitzel', 'garlic prawns', 'fish and chips', 'carbonara', 'lasagna')

print('\n====== MENU ======')
for item in menu:
    print(item.title())

# Intentional Error
# menu[0] = 'beef schnitzel'

menu = ('chicken schnitzel', 'garlic prawns', 'fish and chips', 'bolognese', 'lasagna')

print('\n====== REVISED MENU ======')
for item in menu:
    print(item.title())
