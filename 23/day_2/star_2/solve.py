import time

file_root = "23/day_2/star_2"
with open(f"{file_root}/input.txt", 'r') as f:
    data = f.readlines()

start = time.time()

power_sum = 0
for line in data:
    game_cube_min = {'red': 0, 'green': 0, 'blue': 0}
    
    pulls = [pull.split(', ') for pull in line.rstrip().split(': ')[-1].split('; ')]
    
    # For each pull, find the largest pull of each color
    for pull in pulls:
        for cube_str in pull:
            cube_count, color = cube_str.split(' ')
            game_cube_min[color] = max(game_cube_min[color], int(cube_count))
    
    power_sum += game_cube_min['red'] * game_cube_min['green'] * game_cube_min['blue']

duration = time.time() - start

print(power_sum, f"In {duration} seconds")