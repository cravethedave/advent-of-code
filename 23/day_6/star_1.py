with open("day_6/input.txt", 'r') as f:
    data = f.readlines()

times = data[0].split(':')[1].split()
distances = data[1].split(':')[1].split()
races = [(int(times[i]), int(distances[i])) for i in range(len(times))]

sum = 1
for race in races:
    count = 0
    for v in range(1, race[0]):
        if (race[0] - v) * v > race[1]:
            count += 1
    sum *= count
        
print(sum)