# 4-3. Counting to Twenty

# Use a for loop to print the numbers from 1 to 20, inclusive.

numbers = [i for i in range(1, 21)]
print(numbers)


# 4-4. One Million
# Make a list of the numbers from one to one hundred thousand, and then
# use a for loop to print the numbers.
one_hundred_thousand = [i for i in range(1, 100_001)]
for number in one_hundred_thousand:
    print(number)
