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
    people_amount = len(group)
    total_group_result = {}
    res = 0
    # collect answers
    for answer_string in group:
        for answer in answer_string:
            total_group_result[answer] = 0
    # count amount per answer
    for answer_string in group:
        for answer in answer_string:
            total_group_result[answer] += 1
    for result in total_group_result:
        if total_group_result[result] == people_amount:
            res += 1
    group_results.append(res)

result = 0
for i in group_results:
    result += i

print('The sum of the recors id %s' %(result))
