with open("day_1/input.txt", 'r') as f:
    data = f.readlines()

first = 0
last = 0
sum = 0
# I am not proud of this but it works and i have school work :(
numbers = {
    "one": 'one1one',
    "two": 'two2two',
    "three": 'three3three',
    "four": 'four4four',
    "five": 'five5five',
    "six": 'six6six',
    "seven": 'seven7seven',
    "eight": 'eight8eight',
    "nine": 'nine9nine'
}

for line in data:
    for key in numbers.keys():
        line = line.replace(key, numbers[key])
    for char in line:
        if not char.isdigit():
            continue
        first = char
        break
    for char in line[::-1]:
        if not char.isdigit():
            continue
        last = char
        break
    value = int(first) * 10 + int(last)
    print(value)
    sum += value
print(sum)
    