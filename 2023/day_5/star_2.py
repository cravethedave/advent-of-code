
def extract_values(data: 'list[str]', i: int) -> ('list[dict]', int):
    result = []
    while i < len(data) and not data[i].endswith(':'):
        values = data[i].split()
        result.append({'dest': int(values[0]), 'source': int(values[1]), 'length': int(values[2])})
        i += 1
    return result, i

def convert_value(converter: 'list[dict]', value: int):
    for line in converter:
        if value >= line['source'] and value < line['source'] + line['length']:
            return value - line['source'] + line['dest']
    return value

with open("day_5/input.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data if line != '\n']

sum = 0
seed_line = [int(val) for val in data[0].split(':')[1].split()]
seeds = [(seed_line[i], seed_line[i+1]) for i in range(0,len(seed_line),2)]

i = 2
seed_to_soil, i = extract_values(data, i)
soil_to_fertilizer, i = extract_values(data, i + 1)
fertilizer_to_water, i = extract_values(data, i + 1)
water_to_light, i = extract_values(data, i + 1)
light_to_temp, i = extract_values(data, i + 1)
temp_to_humidity, i = extract_values(data, i + 1)
humidity_to_location, i = extract_values(data, i + 1)

min_loc = float('inf')
for seed_range in seeds:
    start = seed_range[0]
    stop = start + seed_range[1]
    for seed in range(start, stop):
        print(seed)
        soil = convert_value(seed_to_soil, seed)
        fertilizer = convert_value(soil_to_fertilizer, soil)
        water = convert_value(fertilizer_to_water, fertilizer)
        light = convert_value(water_to_light, water)
        temperature = convert_value(light_to_temp, light)
        humidity = convert_value(temp_to_humidity, temperature)
        location = convert_value(humidity_to_location, humidity)
        if location < min_loc:
            min_loc = location

print(min_loc)