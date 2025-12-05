import time
import re

file_root = "23/day_3/star_1"
with open(f"{file_root}/input.txt", 'r') as f:
    data = f.readlines()
data = [line.rstrip() for line in data]

start = time.time()

# Find all symbols and their place on their line
symbols: list[list[int]] = []
for line in data:
    line_symbols: list[int] = []
    for m in re.finditer(r"[^\d\.]", line):
        line_symbols.append(m.start())
    symbols.append(line_symbols)

# Sums all valid parts
part_sum = 0
for i, line in enumerate(data):
    for m in re.finditer(r"\d+", line):
        valid_part = False
        left_bound = m.start() - 1
        right_bound = m.end()
        value = m.group()
        for j in range(max(0,i-1),min(i+2,len(data))):
            for s in symbols[j]:
                if left_bound <= s <= right_bound:
                    valid_part = True
                    part_sum += int(value)
                    break
            if valid_part:
                break

duration = time.time() - start

print(part_sum, f"In {duration} seconds")