import sys
import time
import numpy as np

file_root = "25/day_10/star_1"

file_name = "test_input"
if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        file_name = 'test_input'
    elif sys.argv[1] == 'input':
        file_name = 'input'

with open(f"{file_root}/{file_name}.txt") as f:
    data = f.readlines()

start = time.time()

# Preprocessing data into matrix format and in arrays
machine_buttons: list[np.ndarray] = []
machine_jolts: list[np.ndarray] = []
for line in data:
    split_line = line.rstrip().split(' ')
    
    joltage = np.array([int(iter) for iter in split_line[-1][1:-1].split(',')])
    machine_jolts.append(joltage)
    
    buttons = [[int(iter) for iter in button[1:-1].split(',')] for button in split_line[1:-1]]
    buttons = np.array([[1 if i in button else 0 for i in range(len(joltage))] for button in buttons])
    machine_buttons.append(buttons)

# Sort by least affected position OR by smallest int in joltage
# Sort by span
# All possibilities?

for i, joltage in enumerate(machine_jolts):
    # We classify buttons by their spans
    # np.sum(buttons, axis=0)
    buttons = machine_buttons[i]
    button_spans: dict[int,list[int]] = {}
    for b, button in enumerate(buttons):
        span = sum(button)
        if span not in button_spans.keys():
            button_spans[span] = []
        button_spans[span].append(b)
    
    initial_head = np.array([0] * len(buttons))
    heads = [initial_head]
    solutions = []
    heads_set = set(initial_head.tobytes())
    sorted_spans = sorted(button_spans.keys(), reverse=True)
    for span in sorted_spans:
        for b in button_spans[span]:
            added_heads = []
            for current in heads:
                # Evaluate how many times this button can be pressed
                distance_to_goal = joltage - current @ buttons
                index_of_min = np.ma.argmin(np.ma.masked_array(distance_to_goal, mask=np.array([1] * len(joltage))-buttons[b]))
                max_clicks = distance_to_goal[index_of_min] // buttons[b][index_of_min]
                if max_clicks == 0:
                    continue
                
                # Create a vector with the new button sequence of buttons pressed
                added_head = current.copy()
                added_head[b] += max_clicks
                if added_head.tobytes() in heads_set:
                    continue
                new_distance = joltage - added_head @ buttons
                if sum(new_distance) == 0:
                    solutions.append(added_head)
                heads_set.add(added_head.tobytes())
                added_heads.append(added_head)
            heads.extend(added_heads)
    
    # while any(joltage - current):
    #     possible_next = []
    #     for button in machine_buttons[i]:
    #         distance_to_goal = joltage - current
    #         index_of_min = np.ma.argmin(np.ma.masked_array(distance_to_goal, mask=np.array([1] * len(joltage))-button))
    #         max_clicks = joltage[index_of_min] // button[index_of_min]
    #         print(max_clicks)

duration = time.time() - start

print("total_steps", f"In {duration} seconds")
