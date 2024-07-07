from collections import defaultdict

def is_number_next_to_symbol(number, symbol):
    (nrow, ncol1, ncol2, num) = number
    (srow, scol, sym) = symbol
    if abs(nrow-srow) > 1:
        return False
    return (ncol1-1 <= scol <= ncol2+1)

def main():
    numbers = list()
    symbols = list()
    with open("2023/day_03.in") as f:
        curr_num = 0
        is_reading_number = False
        number_start = -1
        for j, line in enumerate(f):
            for i, c in enumerate(line.strip()):
                if c in "0123456789":
                    if not is_reading_number:
                        curr_num = int(c)
                        number_start = i
                        is_reading_number = True
                    else:
                        curr_num = 10*curr_num + int(c)
                elif is_reading_number:
                    numbers.append((j, number_start, i-1, curr_num))
                    curr_num = 0
                    is_reading_number = False
                if c not in "0123456789" and c != ".":
                    symbols.append((j, i, c))
            if is_reading_number:
                numbers.append((j, number_start, i-1, curr_num))

    num_to_sym = defaultdict(list)
    sym_to_num = defaultdict(list)
    for number in numbers:
        for symbol in symbols:
            if is_number_next_to_symbol(number, symbol):
                num_to_sym[number].append(symbol)
                sym_to_num[symbol].append(number)

    # task 1
    part_number_sum = 0
    for number in numbers:
        if len(num_to_sym[number]):
            part_number_sum += number[-1]
    print(part_number_sum)

    # taks 2
    gear_ratio_sum = 0
    for symbol in symbols:
        if symbol[-1] == "*" and len(sym_to_num[symbol]) == 2:
            gear_ratio_sum += sym_to_num[symbol][0][-1] * sym_to_num[symbol][1][-1]
    print(gear_ratio_sum)

if __name__ == "__main__":
    main()
