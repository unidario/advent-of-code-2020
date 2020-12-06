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

def check_validity(passport):
    if not _check_required_fields(passport):
        return False
    return True

valid_count = 0
passport_data = parse_passport_data(input_file)

for passport in passport_data:
    if check_validity(passport):
        valid_count += 1

print('%s passports are valid' %(valid_count))
