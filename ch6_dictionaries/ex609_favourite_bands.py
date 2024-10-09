# 6-9. Favorite Places (Bands)

fav_bands = {
    'mick': ['ac/dc', 'kiss', 'black sabbath'],
    'viv': ['pink', 'skyhooks'],
    'jessica': ['oasis']
}

for name, bands in fav_bands.items():
    if len(bands) > 1:
        print(f"{name.title()}'s favourite bands are:")
    else:
        print(f"{name.title()}'s favourite band is:")
    
    for band in bands:
        if band == 'ac/dc':
            print(f"\t{band.upper()}")
        else:
            print(f"\t{band.title()}")
