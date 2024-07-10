import numpy as np

def symmetry_row(pattern: np.array) -> int:
    #mirror = np.flipud(pattern)
    max_shape = pattern.shape[0]
    for i in range(1, pattern.shape[0]):
        # extract upper and lower image, divided by mirror
        upper = pattern[:i]
        lower = pattern[i:min(2*i, max_shape)]
        # match sizes
        upper_shape = upper.shape[0]
        lower_shape = lower.shape[0]
        if upper_shape > lower_shape:
            upper = upper[upper_shape-lower_shape:]
        elif upper_shape < lower_shape: # this cannot happen
            lower = lower[:lower_shape-upper_shape]
        assert upper.shape == lower.shape

        # check if they are mirror images
        lower_m = np.flipud(lower)
        if (lower_m == upper).all():
            return i
    return -1


def symmetry_row_smudge(pattern: np.array) -> int:
    #mirror = np.flipud(pattern)
    max_shape = pattern.shape[0]
    for i in range(1, pattern.shape[0]):
        # extract upper and lower image, divided by mirror
        upper = pattern[:i]
        lower = pattern[i:min(2*i, max_shape)]
        # match sizes
        upper_shape = upper.shape[0]
        lower_shape = lower.shape[0]
        if upper_shape > lower_shape:
            upper = upper[upper_shape-lower_shape:]
        elif upper_shape < lower_shape: # this cannot happen
            lower = lower[:lower_shape-upper_shape]
        assert upper.shape == lower.shape

        # check if they differ in only 1 symbol -> we found smudge
        lower_m = np.flipud(lower)
        if (lower_m != upper).sum() == 1:
            return i
    return -1


def find_symmetry(pattern: np.array) -> tuple:
    row = symmetry_row(pattern)
    if row > 0:
        return (row, 0)
    col = symmetry_row(pattern.T)
    if col > 0:
        return (0, col)
    return None


def find_symmetry_smudge(pattern: np.array) -> tuple:
    row = symmetry_row_smudge(pattern)
    if row > 0:
        return (row, 0)
    col = symmetry_row_smudge(pattern.T)
    if col > 0:
        return (0, col)
    return None


def task1(patterns: list) -> int:
    s = 0
    for pattern in patterns:
        res = find_symmetry(pattern)
        if res is None:
            raise ValueError("No symmetry found!")
        (row, col) = res
        if row > 0:
            s += 100 * row
        else:
            s += col
    return s


def task2(patterns: list) -> int:
    s = 0
    for pattern in patterns:
        res = find_symmetry_smudge(pattern)
        if res is None:
            raise ValueError("No symmetry found!")
        (row, col) = res
        if row > 0:
            s += 100 * row
        else:
            s += col
    return s


def main():
    patterns = list()
    with open("2023/day_13.in", "r") as file:
        pat = list()
        for line in file:
            line = line.strip()
            if line == "":
                patterns.append(np.array(pat, dtype="bool"))
                pat = list()
            else:
                pat.append([(int(x)) for x in line.replace(".", "0").replace("#", "1")])
        patterns.append(np.array(pat))

    print(task1(patterns))
    print(task2(patterns))


if __name__ == "__main__":
    main()
