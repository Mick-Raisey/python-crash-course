# 4-11. My Pizzas, Your Pizzas
# 1. Make a copy of the list of pizzas, and call it friend_pizzas.
# 2. Add a new pizza to the original list.
# 3. Add a different pizza to the list friend_pizzas.
# 4. Print both pizzas

my_pizzas = ['bbq chicken', 'hawaiian', 'pepperoni']
friend_pizzas = my_pizzas[:]

my_pizzas.append('meat lovers')
friend_pizzas.append('supreme')

print(my_pizzas)
print(friend_pizzas)
