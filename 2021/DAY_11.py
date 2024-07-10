import numpy as np

def task1(octopuses):
    flashes = 0
    for idx in range(100):
        octopuses += 1 # every octopus increases its energy level

        # higher than 9 flash, update energy of adjecent
        flashed_now = list()
        where = np.where(octopuses > 9)
        possible_flashes = [(i, j) for i, j in zip(where[0], where[1])]
        # get all the flash locations
        while len(possible_flashes) > 0:
            loc = possible_flashes.pop(0)
            if loc not in flashed_now:
                flashed_now.append(loc)
                for i in range(max(0, loc[0]-1), min(loc[0]+2, octopuses.shape[0])):
                    for j in range(max(0, loc[1]-1), min(loc[1]+2, octopuses.shape[1])):
                        if i == loc[0] and j == loc[1]:
                            continue
                        octopuses[i, j] += 1
                        if octopuses[i, j] > 9:
                            possible_flashes.append((i, j))

        flashes += len(flashed_now)
        octopuses[np.where(octopuses > 9)] = 0

    return flashes

def task2(octopuses):
    idx = 0
    while True:
        idx += 1
        octopuses += 1 # every octopus increases its energy level

        # higher than 9 flash, update energy of adjecent
        flashed_now = list()
        where = np.where(octopuses > 9)
        possible_flashes = [(i, j) for i, j in zip(where[0], where[1])]
        # get all the flash locations
        while len(possible_flashes) > 0:
            loc = possible_flashes.pop(0)
            if loc not in flashed_now:
                flashed_now.append(loc)
                for i in range(max(0, loc[0]-1), min(loc[0]+2, octopuses.shape[0])):
                    for j in range(max(0, loc[1]-1), min(loc[1]+2, octopuses.shape[1])):
                        if i == loc[0] and j == loc[1]:
                            continue
                        octopuses[i, j] += 1
                        if octopuses[i, j] > 9:
                            possible_flashes.append((i, j))

        octopuses[np.where(octopuses > 9)] = 0
        if np.sum(octopuses != 0) == 0:
            return idx

if __name__ == "__main__":
    octopuses = list()
    with open("2021/day_11.in", "r") as f:
        for l in f.readlines():
            octopuses.append(np.array([int(c) for c in l.split("\n")[0]]))
    
    octopuses = np.array(octopuses)

    print(f"Task 1: {task1(np.copy(octopuses))}")
    print(f"Task 2: {task2(octopuses)}")