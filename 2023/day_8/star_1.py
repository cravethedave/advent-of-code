

with open("day_8/input.txt", 'r') as f:
    data = f.readlines()

converter = {'L': 0, 'R': 1}
steps = [converter[c] for c in data[0].rstrip()]
n = len(steps)

data = [line.split(' = ') for line in data[2:]]
paths = {line[0] : line[1].split('(', maxsplit=1)[1].rsplit(')', maxsplit=1)[0].split(', ', maxsplit=1) for line in data}

i = 0
counter = 0
node = 'AAA'
while node != 'ZZZ':
    node = paths[node][steps[i]]
    i = (i + 1) % n
    counter += 1
print(counter)