with open("day_3/input.txt", 'r') as f:
    data = f.readlines()

data = [[c for c in line.rstrip()] for line in data]

sum = 0
previous_line_numbers = {}
for line in range(len(data)):
    line_len = len(data[line])
    current_line_numbers = {}
    
    x = 0
    while x < line_len:
        c = data[line][x]
        
        # skip periods
        if c == '.':
            x += 1
            continue
        
        # read a number
        if c.isdigit():
            number = c
            base = x
            x += 1
            while x < line_len and data[line][x].isdigit():
                number += data[line][x]
                x += 1
            current_line_numbers[base] = number
            continue
        
        # must be a symbol
        # adds all numbers needed from previous line
        keys_to_remove = []
        for key in previous_line_numbers.keys():
            if key - 1 <= x and key + len(previous_line_numbers[key]) >= x:
                sum += int(previous_line_numbers[key])
                keys_to_remove.append(key)
        for key in keys_to_remove:
            previous_line_numbers.pop(key)
            
        # adds all numbers needed from next line
        if line + 1 < len(data):
            next_line = line + 1
            next_line_len = len(data[next_line])
            if data[next_line][x].isdigit():
                num = data[next_line][x]
                data[next_line][x] = '.'
                
                # left pass
                pos = x - 1
                left_num = ''
                while pos >= 0 and data[next_line][pos].isdigit():
                    left_num = data[next_line][pos] + left_num
                    data[next_line][pos] = '.'
                    pos -= 1
                num = left_num + num
                
                # right pass
                pos = x + 1
                while pos < next_line_len and data[next_line][pos].isdigit():
                    num += data[next_line][pos]
                    data[next_line][pos] = '.'
                    pos += 1
                
                sum += int(num)
            else:
                if data[next_line][x - 1].isdigit():
                    pos = x - 1
                    left_num = ''
                    while pos >= 0 and data[next_line][pos].isdigit():
                        left_num = data[next_line][pos] + left_num
                        data[next_line][pos] = '.'
                        pos -= 1
                    sum += int(left_num)
                if data[next_line][x + 1].isdigit():
                    pos = x + 1
                    right_num = ''
                    while pos < next_line_len and data[next_line][pos].isdigit():
                        right_num += data[next_line][pos]
                        data[next_line][pos] = '.'
                        pos += 1
                    
                    sum += int(right_num)
        
        # adds the number number to its left
        if len(current_line_numbers) > 0 and x - 1 >= 0 and data[line][x - 1].isdigit():
            max = 0
            for key in current_line_numbers.keys():
                if key > max:
                    max = key
            sum += int(current_line_numbers.pop(max))
        
        # adds numbers to the right
        if x + 1 < line_len and data[line][x + 1].isdigit():
            x += 1
            number = data[line][x]
            x += 1
            while x < line_len and data[line][x].isdigit():
                number += data[line][x]
                x += 1
            sum += int(number)
            continue
        
        # increase iterator
        x += 1
    
    previous_line_numbers = current_line_numbers

print(sum)