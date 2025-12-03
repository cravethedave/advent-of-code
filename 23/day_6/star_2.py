with open("day_6/input.txt", 'r') as f:
    data = f.readlines()

time = int(''.join(data[0].split(':')[1].split()))
distance = int(''.join(data[1].split(':')[1].split()))

count = 0
for v in range(1, time):
    if (time - v) * v > distance:
        count += 1
        
print(count)