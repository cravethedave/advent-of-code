import time

file_root = "25/day_3/star_1"

with open(f"{file_root}/input.txt") as f:
    banks = f.readlines()

banks = [iter.rstrip() for iter in banks]

start = time.time()
total_jolts = 0
for bank in banks:
    first_value = '0'
    first_index = 0
    for i in range(len(bank) - 1):
        if bank[i] > first_value:
            first_index = i
            first_value = bank[i]
    second_value = '0'
    for battery in bank[first_index+1:]:
        if battery > second_value:
            second_value = battery
    joltage = int(first_value + second_value)
    total_jolts += joltage
duration = time.time() - start

print(total_jolts, f"In {duration} seconds")
