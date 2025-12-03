from enum import Enum

class Hand(Enum):
    HIGHEST = 0,
    ONE_PAIR = 1,
    TWO_PAIR = 2,
    THREE = 3,
    FULL_HOUSE = 4,
    FOUR = 5,
    FIVE = 6

def evaluate_hand(hand: str) -> Hand:
    cards = {}
    for card in hand:
        if not card in cards.keys():
            cards[card] = 0
        cards[card] += 1
    
    n = len(cards)
    if not 'a' in cards.keys():
        wildcards = 0
    else:
        wildcards = cards['a']
    
    if n == 5:
        if wildcards == 0:
            return Hand.HIGHEST # no wildcards, all different
        return Hand.ONE_PAIR # all different, but there is a wildcard
    if n == 4:
        if wildcards == 0:
            return Hand.ONE_PAIR
        return Hand.THREE

    max = 0
    for v in cards.values():
        if v > max:
            max = v

    if n == 3:
        if wildcards == 0:
            if max == 2:
                return Hand.TWO_PAIR
            return Hand.THREE
        if wildcards == 1:
            if max == 2:
                return Hand.FULL_HOUSE
            return Hand.FOUR
        # 2 wildcards -> 2 2 1
        return Hand.FOUR
    if n == 2: # 4 1, 3 2
        if wildcards != 0:
            return Hand.FIVE
        if max == 4:
            return Hand.FOUR
        if max == 3:
            return Hand.FULL_HOUSE
        pass
    return Hand.FIVE

def sort_hands(hands: 'list[str]'):
    if len(hands) <= 1:
        return hands
    n = len(hands)
    half = int(n/2)
    left_sorted = sort_hands(hands[:half])
    right_sorted = sort_hands(hands[half:])
    i = 0
    j = 0
    result = []
    while len(result) < n:
        if left_sorted[i] > right_sorted[-1]:
            result.extend(right_sorted[j:])
            result.extend(left_sorted[i:])
        elif right_sorted[j] > left_sorted[-1]:
            result.extend(left_sorted[i:])
            result.extend(right_sorted[j:])
        else:
            if left_sorted[i] < right_sorted[j]:
                result.append(left_sorted[i])
                i += 1
            else:
                result.append(right_sorted[j])
                j += 1
    return result

with open("day_7/input.txt", 'r') as f:
    data = f.readlines()

converter = {
    'J': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    'T': 'j',
    'Q': 'k',
    'K': 'l',
    'A': 'm'
}
data = [line.rstrip().split() for line in data]
converted = {''.join([converter[c] for c in line[0]]): int(line[1]) for line in data}

hand_types = {
    Hand.HIGHEST: [],
    Hand.ONE_PAIR: [],
    Hand.TWO_PAIR: [],
    Hand.THREE: [],
    Hand.FULL_HOUSE: [],
    Hand.FOUR: [],
    Hand.FIVE: []
}
for key in converted.keys():
    hand_types[evaluate_hand(key)].append(key)

sorted_hands = []
for key in hand_types.keys():
    sorted_hands.extend(sort_hands(hand_types[key]))

sum = 0
for index, hand in enumerate(sorted_hands):
    sum += converted[hand] * (index + 1)
print(sum)