input_file = 'input.txt'

def parse_answers(file):
    groups = []
    people = []
    with open(file) as f:
        for line in f:
            if line != "\n":
                people.append(line.strip())
            else:
                groups.append(people)
                people = []
        groups.append(people)
    return groups

group_answers = parse_answers(input_file)

group_results = []

for group in group_answers:
    group_result = {}
    for answer_string in group:
        for answer in answer_string:
            group_result[answer] = 1
    group_results.append(len(group_result))

result = 0
for i in group_results:
    result += i

print('The sum of the recors id %s' %(result))
