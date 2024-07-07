import re

def get_number(s: str):
    first, last = 0, 0
    for c in s:
        try:
            c = int(c)
            if first == 0:
                first = last = c
            else:
                last = c
        except:
            pass
    return 10 * first + last

TRANSLATE = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}
def get_spelled_numbers(s: str):
    # get locations of ints
    ints = dict() # index -> number
    for i, c in enumerate(s):
        if c in {str(_i) for _i in range(0, 10)}:
            ints[i] = int(c)
    # get locations of spelled ints
    for spelled_int in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        locs = [m.start() for m in re.finditer(spelled_int, s)]
        if locs:
            for l in locs:
                ints[l] = TRANSLATE[spelled_int]
    lowest_key = min(ints.keys())
    highest_key = max(ints.keys())
    return 10 * ints[lowest_key] + ints[highest_key]

def main():
    with open("2023/day_01.in") as f:
        lst = [l.strip() for l in f]
    
    arr = [get_number(l) for l in lst]
    print(sum(arr))

    arr = [get_spelled_numbers(l) for l in lst]
    print(sum(arr))


if __name__ == "__main__":
    main()
