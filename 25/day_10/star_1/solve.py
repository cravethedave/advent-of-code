import sys
import time
import numpy as np

file_root = "25/day_10/star_1"

file_name = "input"
if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        file_name = 'test_input'
    elif sys.argv[1] == 'input':
        file_name = 'input'

with open(f"{file_root}/{file_name}.txt") as f:
    data = f.readlines()

start = time.time()

# Preprocessing data into matrix format and in arrays
machine_diagrams: list[np.ndarray] = []
machine_buttons: list[np.ndarray] = []
for line in data:
    split_line = line.rstrip().split(' ')
    
    diagram = np.array([1 if iter == '#' else 0 for iter in split_line[0][1:-1]])
    machine_diagrams.append(diagram)
    
    buttons = [[int(iter) for iter in button[1:-1].split(',')] for button in split_line[1:-1]]
    buttons = np.array([[1 if i in button else 0 for i in range(len(diagram))] for button in buttons])
    machine_buttons.append(buttons)

total_steps = 0
for i, diagram in enumerate(machine_diagrams):
    current_heads = [diagram]
    found = False

    # We search for a path to create the desired sequence by progressively exploring the tree
    steps = 0
    while not found:
        steps += 1
        next_heads = []
        for current in current_heads:
            for button in machine_buttons[i]:
                # By adding and mod 2, adding two 1s become a 0
                next_heads.append((current + button) % 2)
                # If the last head is all zeroes, we found a path
                if not np.any(next_heads[-1]):
                    found = True
                    break
            if found:
                break
        current_heads = next_heads

    total_steps += steps

duration = time.time() - start

print(total_steps, f"In {duration} seconds")
