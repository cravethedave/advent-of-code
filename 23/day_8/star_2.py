def all_nodes_done(nodes: 'list[str]'):
    for node in nodes:
        if not node.endswith('Z'):
            return False
    return True

with open("day_8/input.txt", 'r') as f:
    data = f.readlines()

converter = {'L': 0, 'R': 1}
steps = [converter[c] for c in data[0].rstrip()]
n = len(steps)

data = [line.split(' = ') for line in data[2:]]
paths = {line[0] : line[1].split('(', maxsplit=1)[1].rsplit(')', maxsplit=1)[0].split(', ', maxsplit=1) for line in data}

nodes = []
for key in paths.keys():
    if key.endswith('A'):
        nodes.append(key)
ghosts = len(nodes)
print(nodes)

i = 0
counter = 0
while not all_nodes_done(nodes):
    step = steps[i]
    if counter % 100000 == 0:
        print(counter)
    nodes = [paths[node][step] for node in nodes]
    i = (i + 1) % n
    counter += 1
print(counter)