import time

file_root = "25/day_3/star_2"

with open(f"{file_root}/input.txt") as f:
    banks = f.readlines()

banks = [iter.rstrip() for iter in banks]

start = time.time()
total_jolts = 0
for bank in banks:
    max_jolts = ['0'] * 12
    
    for i in range(0,len(bank)):
        candidate = bank[i]
        for j in range(max(0,12-len(bank)+i),12):
            current = max_jolts[j]
            if max_jolts[j] < bank[i]:
                max_jolts[j] = bank[i]
                for k in range(j+1,12):
                    max_jolts[k] = '0'
                break
    
    joltage = int(''.join(max_jolts))
    total_jolts += joltage
duration = time.time() - start

print(total_jolts, f"In {duration} seconds")
