
dial_head = 50
filename = "25/day_1/star_2/input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()

password = 0
for line in lines:
    turn_left = line[0] == 'L'
    turn_nb = int(line[1:])
    
    if dial_head == 0:
        dist_to_zero = 100
    else:
        dist_to_zero = dial_head if turn_left else 100 - dial_head
    
    # Counts all occurences of passing or landing on zero
    if turn_nb >= dist_to_zero:
        password += (turn_nb - dist_to_zero) // 100 + 1
    
    # Recalculates the head
    dial_head = (dial_head + (-1 if turn_left else 1) * turn_nb + 100) % 100

print(password)
