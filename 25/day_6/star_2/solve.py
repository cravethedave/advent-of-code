import time
from math import prod

file_root = "25/day_6/star_2"

with open(f"{file_root}/input.txt") as f:
    data = [iter.rstrip('\n') for iter in f.readlines()]

start = time.time()

operations = [iter for iter in data[-1].split(' ') if iter != '']
numbers = [[]]
for i in range(len(data[0])):
    forming_number = ''
    for line in data[:-1]:
        if line[i] != ' ':
            forming_number += line[i]

    if forming_number == '':
        numbers.append([])
    else:
        numbers[-1].append(int(forming_number))

total_of_all_operations = 0
for i in range(len(operations)):
    method_to_use = sum if operations[i] == '+' else prod
    total_of_all_operations += method_to_use(numbers[i])

duration = time.time() - start

print(total_of_all_operations, f"In {duration} seconds")
