input_file = 'input.txt'

def parse_input(file):
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())
    return lines

input = parse_input(input_file)

success = False

# brute force
for a in input:
    if success == True:
        break
    for b in input:
        if success == True:
            break
        for c in input:
            if success == True:
                break
            if a + b + c == 2020:
                success = True
                print('%s + %s + %s = %s' %(a, b, c, (a * b * c)))
