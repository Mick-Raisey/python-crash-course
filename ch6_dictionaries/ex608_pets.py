# 6-8. Pets

mimi = {
    'name': 'mimi',
    'breed': 'cat',
    'owner': 'viv'
}

wilma = {
    'name': 'wilma',
    'breed': 'dog',
    'owner': 'jessica'
}

archie = {
    'name': 'archie',
    'breed': 'dog',
    'owner': 'dani'
}

nugget = {
    'name': 'nugget',
    'breed': 'bird',
    'owner': 'viv'
}

frank = {
    'name': 'frank',
    'breed': 'lizard',
    'owner': 'mick'
}

pets = [mimi, wilma, archie, nugget, frank]

for pet in pets:
    name = pet['name']
    breed = pet['breed']
    owner = pet['owner']

    print(f"\n{name.title()} is a {breed} owned by {owner.title()}")
