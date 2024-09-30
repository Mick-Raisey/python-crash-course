# 3-7. Shrinking Guest List

# • Start with your program from Exercise 3-6. Add a new line that prints a
#   message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
#   names remain in your list. Each time you pop a name from your list, print a
#   message to that person letting them know you’re sorry you can’t invite them.
# • Print a message to each of the two people still on your list, letting them
#   know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
#   list. Print your list to make sure you actually have an empty list at the end of
#   your program.

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

print("\n====== Sorry but the venue is already booked out ======")

print(f"I can only invite two people to the party")
guest = guests.pop()
print(f"Sorry, {guest.title()} there is no room at the party ")
guest = guests.pop()
print(f"Sorry, {guest.title()} there is no room at the party ")
guest = guests.pop()
print(f"Sorry, {guest.title()} there is no room at the party ")
guest = guests.pop()
print(f"Sorry, {guest.title()} there is no room at the party ")
guest = guests.pop()
print(f"Sorry, {guest.title()} there is no room at the party ")

guest = guests[0].title()
print(f"{guest}, please come to the party ")
guest = guests[1].title()
print(f"{guest}, please come to the party ")

del guests[0]
del(guests[0])

print("\n====== Empty List ======")
print(guests)
