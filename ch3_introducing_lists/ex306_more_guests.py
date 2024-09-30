# 3-6. More Guests

# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
#   end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guests = ['malcolm young', 'ace frehley', 'john lennon', 'freddie mercury']

guest1 = guests[0].title()
print(f"{guest1}, You are invited to the party")

guest2 = guests[1].title()
print(f"{guest2}, You are invited to the party")

guest3 = guests[2].title()
print(f"{guest3}, You are invited to the party")

guest4 = guests[3].title()
print(f"{guest4}, You are invited to the party")


name = guests[1].title()
print(f"\nSorry, {name} can't make it to the party.")

print("\n====== New Invitations ======")

# ace cant make it lets invite david bowie instead
guests[1] = 'david bowie'
guest1 = guests[0].title()
print(f"{guest1}, You are invited to the party")

guest2 = guests[1].title()
print(f"{guest2}, You are invited to the party")

guest3 = guests[2].title()
print(f"{guest3}, You are invited to the party")

guest4 = guests[3].title()
print(f"{guest4}, You are invited to the party")

print("\n====== I have found a bigger venue ======")
guests.insert(0, 'gary moore')
guests.insert(2, 'tina turner')
guests.append('janis joplin')

print(f"{guests[0].title()}, You are invited to the party")
print(f"{guests[1].title()}, You are invited to the party")
print(f"{guests[2].title()}, You are invited to the party")
print(f"{guests[3].title()}, You are invited to the party")
print(f"{guests[4].title()}, You are invited to the party")
print(f"{guests[5].title()}, You are invited to the party")
print(f"{guests[6].title()}, You are invited to the party")
