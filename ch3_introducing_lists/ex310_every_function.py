# 3-10. Every Function
# Write a program that creates a list 
# and then uses each function introduced in this chapter at least once.
bands = ['iron maiden', 'ac/dc', 'kiss', 'zz top', 'cream', 'thin lizzy']

bands.append('green day')
bands.insert(2, 'foo fighters')

print(f"\n=== Length ===")
print(f"The length of the list is {len(bands)}")

print(f"\n=== Index ===")
print(f"AC/DC is at index {bands.index('ac/dc')}")

print(f"\n=== Sorted List ===")
print(sorted(bands))

print(f"\n=== Reverse Sorted List ===")
print(sorted(bands, reverse=True))


print(f"\n=== Pop ===")
band = bands.pop(3)
print(f"Popped band at index 3 is: {band.title()}")