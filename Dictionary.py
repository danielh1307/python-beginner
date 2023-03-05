alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['newKey'] = 'newValue'

print(alien_0)

del alien_0['newKey']

print(alien_0)

color_value = alien_0.get('color', 'not found')
blah_value = alien_0.get('blah', 'not found')
print(f"{color_value} and {blah_value}")

for key,value in alien_0.items():
    print(f"Key is {key} and value is {value}")