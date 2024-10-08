# 6-5. Rivers

# Make a dictionary containing three bands 
# and a song from that band

bands = {
    'ac/dc': 'highway to hell',
    'deep purple': 'machine head',
    'kiss': 'love gun',
}

# Use a loop to print a sentence about each band
# and the album they have

for band, album in bands.items():
    print(f"{band.upper()} have an album called {album.title()}")

print("-----------------------------------")
# Use a loop to print the name of each band included in the dictionary
for band in bands.keys():
    print(band.upper())

print("-----------------------------------")
# Use a loop to print the name of each album included in the dictionary
for album in bands.values():
    print(album.title())
