# 6-4. Glossary 2

# add five more Python terms to your glossary. from exercise 603
# use a for loop to loop throught each item and its value

glossary = {
    'list': 'a collection of item in order',
    'comment': 'a note that is ignored by the interpreter',
    'loop': 'go through a collection of items one at a time',
    'dictionary': 'a collection of items with a key value pair',
    'integer': 'represent a whole number positive or negative',
    'float': 'represent a number with a decimal positive or negative',
    'boolean': 'represent a True or False value',
}

for term, description in glossary.items():
    print(f"\n{term.title()}:\n\t{description}")
