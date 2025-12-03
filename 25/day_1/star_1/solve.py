
dial_head = 50
filename = "25/day_1/star_1/input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()

password = 0
for line in lines:
    turn_left = line[0] == 'L'
    turn_nb = int(line[1:])
    
    dial_head = (dial_head + (-1 if turn_left else 1) * turn_nb + 100) % 100
    if dial_head == 0:
        password += 1

print(password)
