# 3-8. Seeing the World
bands = ['deep purple', 'ac/dc', 'iron maiden', 'black sabbath']

print("\n====== Original Order ======")
print(bands)

print("\n====== Sorted Order ======")
print(sorted(bands))

print("\n====== Original Order ======")
print(bands)

print("\n====== Reverse Sorted Order ======")
print(sorted(bands, reverse=True))

print("\n====== Original Order ======")
print(bands)

print("\n====== Reverse Order Permanent ======")
bands.reverse()
print(bands)

print("\n====== Original Order ======")
bands.reverse()
print(bands)

print("\n====== Alphabetical Order Permanent ======")
bands.sort()
print(bands)

print("\n====== Reverse Alphabetical Order Permanent ======")
bands.sort(reverse=True)
print(bands)
