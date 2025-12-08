import time
from math import prod

file_root = "25/day_6/star_1"

with open(f"{file_root}/input.txt") as f:
    data = [iter.rstrip() for iter in f.readlines()]

start = time.time()

numbers = []
for line in data[:-1]:
    numbers.append([int(iter) for iter in line.split(' ') if iter != ''])
operations = [iter for iter in data[-1].split(' ') if iter != '']

total_of_all_operations = 0
for i in range(len(operations)):
    method_to_use = sum if operations[i] == '+' else prod
    
    values_to_use = []
    for values in numbers:
        values_to_use.append(values[i])
    
    total_of_all_operations += method_to_use(values_to_use)

duration = time.time() - start

print(total_of_all_operations, f"In {duration} seconds")
