import math

def get_winning_range(time, distance):
    D = math.sqrt(time**2 - 4*distance)
    x1 = (time + D) / 2
    x2 = (time - D) / 2
    winning_range = [x1, x2] if x1 < x2 else [x2, x1]
    winning_range[0] = int(math.ceil(winning_range[0]+1e-3)) # small perturbation in case of exact distance
    winning_range[1] = int(math.floor(winning_range[1]-1e-3))
    return winning_range


def main():
    times = list()
    distances = list()
    with open("2023/day_06.in", "r") as f:
        timeline = f.readline().strip()[9:]
        for tline in timeline.split(" "):
            if not tline:
                continue
            times.append(int(tline))
        distline = f.readline().strip()[9:]
        for dline in distline.split(" "):
            if not dline:
                continue
            distances.append(int(dline))
    
    # task 1
    mul = 1
    for t, d in zip(times, distances):
        wrange = get_winning_range(t, d)
        mul *= wrange[1]-wrange[0]+1
    print(mul)

    # task 2
    time = int("".join(str(t) for t in times))
    distance = int("".join(str(d) for d in distances))
    wrange = get_winning_range(time, distance)
    print(wrange[1]-wrange[0]+1)


if __name__ == "__main__":
    main()
