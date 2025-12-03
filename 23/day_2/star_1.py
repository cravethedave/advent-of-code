with open("day_2/input.txt", 'r') as f:
    data = f.readlines()


limits = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
for line in data:
    temp = line.rstrip().split(': ')
    game_id = int(temp[0].split('Game ')[1])
    pulls = temp[1].split('; ')
    valid_game = True
    for pull in pulls:
        cubes = [p.split(' ') for p in pull.split(', ')]
        cubes = {cube[1] : int(cube[0]) for cube in cubes}
        for color in cubes.keys():
            if cubes[color] > limits[color]:
                valid_game = False
                break
        if not valid_game:
            break
    if valid_game:
        sum += game_id
    
print(sum)