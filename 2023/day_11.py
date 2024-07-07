from dataclasses import dataclass
import numpy as np

@dataclass
class Galaxy:
    x: int
    y: int


# Task 1: 2
# Task 2: 1000000
EMPTY_VALUE = 1000000


def main():
    galaxies = list()
    empty_columns = set()
    max_cols = 0
    with open("2023/day_11.in", "r") as file:
        line = file.readline().strip()
        for i, c in enumerate(line):
            if c == "#":
                galaxies.append(Galaxy(i, 0))
            else:
                empty_columns.add(i)
        max_cols = i+1

        j = 1
        galaxies_before = len(galaxies)
        for line in file:
            for i, c in enumerate(line):
                if c == "#":
                    galaxies.append(Galaxy(i, j))
                    if i in empty_columns:
                        empty_columns.remove(i)
            # empty row - counts as two
            if galaxies_before == len(galaxies):
                j += EMPTY_VALUE
            else:
                j += 1
            galaxies_before = len(galaxies)

    # calculate empty column map for double counts
    empty_col_map = dict()
    x_map = 0
    for i in range(max_cols):
        empty_col_map[i] = x_map
        if i in empty_columns:
            x_map += EMPTY_VALUE
        else:
            x_map += 1

    for galaxy in galaxies:
        galaxy.x = empty_col_map[galaxy.x]

    total_dist = 0
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i+1:]:
            total_dist += (abs(g1.x - g2.x) + abs(g1.y - g2.y))
    print(total_dist)


if __name__ == "__main__":
    main()
