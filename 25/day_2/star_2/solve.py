import time
from math import log,ceil,sqrt,floor

file_root = "25/day_2/star_2"

def find_primes(original_value: int) -> set[int]:
    """
    Finds prime numbers. We only need to check sequences that repeat that many times.
    """
    prime_dividers: set[int] = set()
    value = original_value
    
    # Makes the number odd
    while value % 2 == 0:
        prime_dividers.add(2)
        value /= 2
    
    # Avoids adding 1 to the list if the value was a power of 2
    if value == 1:
        return prime_dividers
    
    # Adds the value if it is too small to enter the loop
    if 3 > floor(sqrt(value)):
        prime_dividers.add(int(value))
        return prime_dividers
    
    # Divides by all odd numbers as much as it can (can only add primes)
    for i in range(3,floor(sqrt(value))+1,2):
        # Our remainder is a prime number
        if i > floor(sqrt(value)):
            prime_dividers.add(int(value))
            break
        while value % i == 0:
            prime_dividers.add(int(i))
            value /= i
        if value == 1:
            break
    
    return prime_dividers

with open(f"{file_root}/input.txt") as f:
    data = f.readline()

ids = [[int(iter) for iter in values.split('-')] for values in data.split(',')]

start = time.time()
total_of_ids = 0
for lower_val,upper_val in ids:
    # Adding 1 avoids 1000 having a length of 3, 999 still has a length of 3
    lower_len = ceil(log(lower_val+1,10))
    upper_len = ceil(log(upper_val+1,10))
    
    # A list of all possible invalid values encoded as tuples
    # The tuple contains: lower/upper bound to explore and number of times the sequence repeats
    possible_invalids: list[tuple[int,int,int]] = []
    if lower_len == upper_len:
        primes = list(find_primes(lower_len))
        for prime in primes:
            possible_invalids.append(
                (
                    int(lower_val // 10**(lower_len - lower_len/prime)),
                    int(upper_val // 10**(upper_len - upper_len/prime)),
                    prime
                )
            )
    else:
        lower_primes = list(find_primes(lower_len))
        upper_primes = list(find_primes(upper_len))
        for prime in lower_primes:
            possible_invalids.append(
                (
                    int(lower_val // 10**(lower_len - lower_len/prime)),
                    int(10**(lower_len/prime)) - 1,
                    prime
                )
            )
        for prime in upper_primes:
            possible_invalids.append(
                (
                    int(10**(upper_len/prime - 1)),
                    int(upper_val // 10**(upper_len - upper_len/prime)),
                    prime
                )
            )
    
    added_values = set()
    for lower, upper, repeat in possible_invalids:
        for seq in range(lower,upper+1):
            value = int(str(seq) * repeat)
            if lower_val <= value <= upper_val and value not in added_values:
                added_values.add(value)
                total_of_ids += value

duration = time.time() - start

print(total_of_ids, f"In {duration} seconds")
