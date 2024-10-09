# 6-7. People

ace = {
    'first': 'ace',
    'last': 'frehley',
    'instrument': 'lead',
    'persona': 'spaceman'
}

peter = {
    'first': 'peter',
    'last': 'criss',
    'instrument': 'drums',
    'persona': 'catman'
}

paul = {
    'first': 'paul',
    'last': 'stanley',
    'instrument': 'rhythm',
    'persona': 'star child'
}

gene = {
    'first': 'gene',
    'last': 'simmons',
    'instrument': 'bass',
    'persona': 'demon'
}

kiss = [ace, peter, paul, gene]

for member in kiss:
    fullname = f"{member['first']} {member['last']}"
    instrument = member['instrument']
    persona = member['persona']
    
    print(f"\n{fullname.title()}")
    print(f"\tPersona: \t{persona.title()}")
    print(f"\tInstrument: \t{instrument.title()}")
