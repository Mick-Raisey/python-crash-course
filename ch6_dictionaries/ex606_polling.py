# 6-6. Polling
# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

should_take_poll = ['mimi', 'sid', 'sarah', 'jack', 'edward']

# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

for person in should_take_poll:
    if person in favorite_languages.keys():
        print(f"{person.title()}, Thanks for taking the poll!")
    else:
        print(f"{person.title()}, please take our poll")
