input_file = 'input.txt'

def parse_file(file):
    array = []
    with open(file) as f:
        for line in f:
            array.append(line.strip())
    return array

def get_row(row_string):
    min_row = 0
    max_row = 127
    for c in row_string:
        if c == "F":
            max_row -= (max_row - min_row + 1) / 2
        elif c == "B":
            min_row += (max_row - min_row + 1) / 2
    row = min_row
    return int(row)

def get_column(column_string):
    min_column = 0
    max_column = 7
    for c in column_string:
        if c == "L":
            max_column -= (max_column - min_column + 1) / 2
        elif c == "R":
            min_column += (max_column - min_column + 1) / 2
    column = min_column
    return int(column)

def get_seat_id(seat_string):
    seat_id = (get_row(seat_string[0:]) * 8) + get_column(seat_string[-3:])
    return seat_id

seat_ids = []
seats = parse_file(input_file)
for seat in seats:
    seat_ids.append(get_seat_id(seat))

print('Max seat ID is %s' %(max(seat_ids)))
