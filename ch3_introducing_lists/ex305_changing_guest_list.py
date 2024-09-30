# 3-5. Changing Guest List
# • Start with your program from Exercise 3-4. Add a print() call at the end of
#   your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
#   name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
#   your list.

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
