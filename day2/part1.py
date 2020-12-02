input_file = 'input.txt'

valid_count = 0
invalid_count = 0

def parse_file(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

def parse_line(line):
    tmp = line.strip().split()
    amount = tmp[0].split('-')
    key = tmp[1].strip(':')
    password = tmp[2]
    result = {
        'min': int(amount[0]),
        'max': int(amount[1]),
        'key': key,
        'password': password
    }
    return result

def check_validity(input_dict):
    key_count = input_dict['password'].count(input_dict['key'])
    if key_count >= input_dict['min'] and key_count <= input_dict['max'] :
        return True
    else:
        return False

lines = parse_file(input_file)
for line in lines:
    line_dict = parse_line(line)
    if check_validity(line_dict):
        valid_count += 1
    else:
        invalid_count += 1

print('Valid passwords: %s' %(valid_count))
print('Invalid passwords: %s' %(invalid_count))
