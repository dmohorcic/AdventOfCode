def main():
    lst = list()
    with open("2023/day_04.in") as f:
        for line in f:
            line = line.strip().split(": ")[1]
            winning, my = line.split(" | ")
            winning = {int(x) for x in winning.split(" ") if x}
            my = {int(x) for x in my.split(" ") if x}
            lst.append((winning, my))

    # task 1
    card_matches = list()
    total_points = 0
    for w, m in lst:
        inter = w.intersection(m)
        if len(inter) > 0:
            total_points += 2**(len(inter)-1)
        card_matches.append(len(inter))
    print(total_points)

    # task 2
    card_copies = [1 for _ in range(len(lst))]
    for i, (w, m) in enumerate(lst):
        copies = card_copies[i]
        matches = card_matches[i]
        for j in range(1, matches+1):
            card_copies[i+j] += copies
    print(sum(card_copies))


if __name__ == "__main__":
    main()
