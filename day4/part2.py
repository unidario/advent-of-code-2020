import string

input_file = 'input.txt'

def parse_file(file):
    result_array = []
    passport_data_raw = ''
    with open(file) as f:
        for line in f:
            if line != "\n":
                passport_data_raw += str(line)
            else:
                result_array.append(passport_data_raw)
                passport_data_raw = ''
        result_array.append(passport_data_raw)
    return result_array

def parse_passport_data(file):
    raw_data = parse_file(file)
    result_array = []
    for passport_string in raw_data:
        tmp_dict = {}
        passport_string = passport_string.replace('\n', ' ').strip()
        tmp_data = passport_string.split(' ')
        for field in tmp_data:
            tmp_dict[field.split(':')[0]] = field.split(':')[1]
        result_array.append(tmp_dict)
    return(result_array)

def _check_required_fields(data):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in data:
            return False
    return True

def _valid_byr(data):
    if len(str(data)) == 4:
        if (int(data) >= 1920 and int(data) <= 2002):
            return True
    print('invalid byr')
    return False

def _valid_iyr(data):
    if len(str(data)) == 4:
        if (int(data) >= 2010 and int(data) <= 2020):
            return True
    print('invalid iyr')
    return False

def _valid_eyr(data):
    if len(str(data)) == 4:
        if int(data) >= 2020 and int(data) <= 2030:
            return True
    print('invalid eyr')
    return False

def _valid_hgt(data):
    if 'cm' in data:
        if int(data.replace('cm', '')) >= 150 and int(data.replace('cm', '')) <= 193:
            return True
    elif 'in' in data:
        if int(data.replace('in', '')) >= 59 and int(data.replace('in', '')) <= 76:
            return True
    print('invalid hgt')
    return False

def _valid_hcl(data):
    if data[0] == '#' and len(data) == 7:
        if all(char in string.hexdigits for char in data[1:-1]):
            return True
    print('invalid hcl')
    return False

def _valid_ecl(data):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if data in valid_ecl and len(data) == 3:
        return True
    print('invalid ecl')
    return False

def _valid_pid(data):
    if len(str(data)) != 9 and str(data)[0] != '0':
        print('invalid pid')
        return False
    return True

def check_validity(passport):
    if _check_required_fields(passport):
        if _valid_byr(passport['byr']) and _valid_iyr(passport['iyr']) and _valid_eyr(passport['eyr']) and _valid_hgt(passport['hgt']) and _valid_hcl(passport['hcl']) and _valid_ecl(passport['ecl']) and _valid_pid(passport['pid']):
            return True
    return False

valid_count = 0
passport_data = parse_passport_data(input_file)

for passport in passport_data:
    print(passport)
    if check_validity(passport):
        valid_count += 1

print('%s passports are valid' %(valid_count))
