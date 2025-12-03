with open("day_4/input.txt", 'r') as f:
    data = f.readlines()

# 6857330

sum = 0

split_data = [
    [set(number_list.split()) for number_list in line.split(': ')[1].strip().split(' | ')]
    for line in data
]
numbers = [
    [number for number in line[1] if number in line[0]]
    for line in split_data
]
card_count = [[1, len(line)] for line in numbers]

for i in range(len(card_count)):
    for j in range(1, card_count[i][1] + 1):
        card_count[i+j][0] += card_count[i][0]

for line in card_count:
    sum += line[0]

print(sum)