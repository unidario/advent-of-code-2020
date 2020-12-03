def parse_file(file):
    array = []
    with open(file) as f:
        for line in f:
            array.append(line.strip())
    return array

input_file = 'input.txt'

tree_count = []

moves = [
    {'x': 3,'y': 1},
    {'x': 1,'y': 1},
    {'x': 5,'y': 1},
    {'x': 7,'y': 1},
    {'x': 1,'y': 2}
]
map = parse_file(input_file)

for move in moves:
    count = 0
    coordinates = {
        'x': 0,
        'y': 0
    }

    while coordinates['y'] < len(map) - 1 :
        coordinates['y'] += move['y']
        coordinates['x'] += move['x']
        if coordinates['x'] > len(map[coordinates['y']]) - 1:
            coordinates['x'] = coordinates['x'] % len(map[coordinates['y']])
        if map[coordinates['y']][coordinates['x']] == '#':
            count += 1

    print('Encountered %s trees on the way' %(count))
    tree_count.append(count)

result = 1
for num in tree_count:
    result *= num

print('The result is %s' %(result))
