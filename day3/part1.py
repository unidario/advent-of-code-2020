def parse_file(file):
    array = []
    with open(file) as f:
        for line in f:
            array.append(line.strip())
    return array

input_file = 'input.txt'

tree_count = 0

move = {
    'x': 3,
    'y': 1
}

coordinates = {
    'x': 0,
    'y': 0
}

map = parse_file(input_file)

while coordinates['y'] < len(map) - 1 :
    coordinates['y'] += move['y']
    coordinates['x'] += move['x']
    if coordinates['x'] > len(map[coordinates['y']]) - 1:
        coordinates['x'] = coordinates['x'] % len(map[coordinates['y']])
    if map[coordinates['y']][coordinates['x']] == '#':
        tree_count += 1

print('Encountered %s trees on the way' %(tree_count))
