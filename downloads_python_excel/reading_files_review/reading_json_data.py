import json

with open('data/data-text.json', 'r') as who_file:
    json_data = who_file.read()

data = json.loads(json_data)
print(f'data is a {type(data)}\n')

# Just print out the first few items
for item in data[:2]:
    print(item)

print(f'\nEach item is a {type(item)}')