import time

filename = "23/day_1/star_1/input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()
lines = [iter.rstrip() for iter in lines]

start = time.time()

# Finds all numeric characters in the string
numeric = [[iter for iter in line if iter.isdigit()] for line in lines]
# Sums up the number made of the first and last digit
total = sum(int(''.join([line[0],line[-1]])) for line in numeric)

duration = time.time() - start

print(total, f"In {duration} seconds")
