# 4-10. Slices

# Print the first 3 items in the list
# Print the three items in the middle
# Print the three last items

items = ['boots', 'gloves', 'socks', 'coat', 'pants']

print('The first three item inthe list are:')
for item in items[:3]:
    print(item)

print('\nThre items from the middle are:')
for item in items[1:4]:
    print(item)

print('\nThe last three items are:')
for item in items[-3:]:
    print(item)
