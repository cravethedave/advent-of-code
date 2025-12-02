with open("day_2/input.txt", 'r') as f:
    data = f.readlines()


sum = 0
for line in data:
    minimum = {'red': 0, 'green': 0, 'blue': 0}
    
    split_line = line.rstrip().split(': ')
    game_id = int(split_line[0].split('Game ')[1])
    pulls = split_line[1].split('; ')
    
    valid_game = True
    for pull in pulls:
        cubes = [p.split(' ') for p in pull.split(', ')]
        cubes = {cube[1] : int(cube[0]) for cube in cubes}
        for color in cubes.keys():
            if cubes[color] > minimum[color]:
                minimum[color] = cubes[color]
    
    sum += minimum['red'] * minimum['green'] * minimum['blue']
    
print(sum)