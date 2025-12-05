import time

file_root = "23/day_2/star_1"
with open(f"{file_root}/input.txt", 'r') as f:
    data = f.readlines()

start = time.time()
n = len(data)
limits = {'red': 12, 'green': 13, 'blue': 14}
invalid_games_sum = 0
for line in data:
    # Get the game Id in case games are not in order
    split_line = line.rstrip().split(': ')
    game_id = int(split_line[0].lstrip('Game '))
    pulls = split_line[1].split('; ')
    
    # For each pull, break as soon as the game is invalid
    for pull in pulls:
        cubes = [p.split(' ') for p in pull.split(', ')]
        if any(limits[cube[1]] < int(cube[0]) for cube in cubes):
            invalid_games_sum += game_id
            break

# Valid sum = Sum of all ids - Invalid Ids
valid_games_sum = int(n * (n+1) / 2) - invalid_games_sum

duration = time.time() - start

print(valid_games_sum, f"In {duration} seconds")