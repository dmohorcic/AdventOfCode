from collections import Counter
from enum import Enum
from functools import cmp_to_key


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OAK = 3
    FULL_HOUSE = 4
    FOUR_OAK = 5
    FIVE_OAK = 6


def hand_type(hand: str):
    count = list(Counter(hand).values())
    if len(count) == 5:
        return HandType.HIGH_CARD
    if len(count) == 4:
        return HandType.ONE_PAIR
    if len(count) == 3:
        if max(count) == 3:
            return HandType.THREE_OAK
        return HandType.TWO_PAIR
    if len(count) == 2:
        if max(count) == 4:
            return HandType.FOUR_OAK
        return HandType.FULL_HOUSE
    # len(count) == 1
    return HandType.FIVE_OAK


def hand_type_joker(hand: str):
    jokers = hand.count("J")
    if jokers == 0:
        return hand_type(hand)
    if jokers >= 4:
        return HandType.FIVE_OAK
    hand = hand.replace("J", "")
    count = list(Counter(hand).values())
    max_count = max(count)
    if jokers == 3:
        if max_count == 2: # [2]
            return HandType.FIVE_OAK
        return HandType.FOUR_OAK # [1, 1]
    if jokers == 2:
        if max_count == 3: # [3]
            return HandType.FIVE_OAK
        if max_count == 2: # [2, 1]
            return HandType.FOUR_OAK
        return HandType.THREE_OAK # [1, 1, 1]
    # joker == 1
    if max_count == 4: # [4]
        return HandType.FIVE_OAK
    if max_count == 3: # [3, 1]
        return HandType.FOUR_OAK
    if max_count == 2: # [2, 2] or [2, 1, 1]
        if len(count) == 2: # [2, 2]
            return HandType.FULL_HOUSE
        return HandType.THREE_OAK # [2, 1, 1]
    return HandType.ONE_PAIR


VALUES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for i in range(2, 10):
    VALUES[str(i)] = i

VALUES_JOKER = {"A": 13, "K": 12, "Q": 11, "T": 10, "J": 1}
for i in range(2, 10):
    VALUES_JOKER[str(i)] = i

def compare_hands(hand1, hand2):
    if hand1[1].value != hand2[1].value:
        return -1 if hand1[1].value < hand2[1].value else 1
    for i, j in zip(hand1[0], hand2[0]):
        if VALUES_JOKER[i] != VALUES_JOKER[j]:
            return -1 if VALUES_JOKER[i] < VALUES_JOKER[j] else 1
    return 0


def main(): 
    with open("2023/day_07.in") as f:
        hands = list()
        for line in f:
            hand, bid = line.strip().split(" ")
            hands.append((hand, hand_type_joker(hand), int(bid)))
    
    # task 1 & 2
    hands = sorted(hands, key=cmp_to_key(compare_hands))
    print(sum(i*h[2] for i, h in enumerate(hands, start=1)))

if __name__ == "__main__":
    main()
