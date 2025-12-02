with open("day_4/input.txt", 'r') as f:
    data = f.readlines()

sum = 0
for line in data:
    line = line.split(': ')[1].strip()
    [winning_numbers, numbers] = [set(n_list.split()) for n_list in line.split(' | ')]
    numbers = [n for n in numbers if n in winning_numbers]
    if len(numbers) == 0:
        continue
    sum += 2 ** (len(numbers) - 1)

print(sum)