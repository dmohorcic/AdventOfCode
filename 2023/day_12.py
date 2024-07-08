"""
# first attempt

def get_next_unknown(springs: list, idx: int) -> int:
    for i, c in enumerate(springs[idx:]):
        if c == "?":
            return i+idx
    return -1


def is_possible(springs: list, groups: list) -> bool:
    group_iter = iter(groups)
    group_size = next(group_iter, None)
    found_group = False
    group_trace = 0
    for s in springs:
        if s == "#":
            if not found_group:  # start tracing broken springs
                found_group = True
                group_trace = 1
            else:
                group_trace += 1
        elif s == ".":
            if found_group:  # check if group size matches
                if group_size is None:
                    return False
                if group_trace == group_size:
                    group_size = next(group_iter, None)
                    found_group = False
                else:
                    return False
        elif s == "?":
            if found_group:  # check if group size matches
                if group_size is None:
                    return False
                if group_trace <= group_size:
                    return True
                return False
            return True
    if found_group:
        if group_size is None:
            return False
        if group_trace == group_size:
            group_size = next(group_iter, None)
            if group_size is None:
                return True
            return False
        return False
    if group_size is None:
        return True
    return False


def _pa(springs: list, groups: list, idx: int) -> int:
    if len(springs) <= idx or idx == -1:
        if is_possible(springs, groups):
            # print("".join(springs))
            return 1
        return 0
    p = 0
    new_idx = get_next_unknown(springs, idx+1)
    # change ? to .
    springs[idx] = "."
    if is_possible(springs, groups):
        p += _pa(springs, groups, new_idx)
    # change ? to #
    springs[idx] = "#"
    if is_possible(springs, groups):
        p += _pa(springs, groups, new_idx)
    # change back to ?
    springs[idx] = "?"
    return p


def possible_arrangements(springs: str, groups: list) -> int:
    _springs = [c for c in springs]
    idx = get_next_unknown(_springs, 0)
    return _pa(_springs, groups, idx) """


def pa(springs: list, groups: list, s_idx: int, g_idx: int, c_group_size: int, memo: dict) -> int:
    key = (s_idx, g_idx, c_group_size)
    if key in memo:
        return memo[key]

    # check if we are at the end
    if len(springs) == s_idx:
        # we have already found all groups
        if len(groups) == g_idx and c_group_size == 0:
            return 1
        # we just now found all groups
        elif len(groups) == g_idx+1 and c_group_size == groups[g_idx]:
            return 1
        # wrong combination
        else:
            return 0

    p = 0
    # for . and hypothetical . from ?
    if springs[s_idx] == "." or springs[s_idx] == "?":
        # just continue parsing if we are not in a group
        if c_group_size == 0:
            p += pa(springs, groups, s_idx+1, g_idx, 0, memo)
        # we just finished a group
        elif g_idx < len(groups) and groups[g_idx] == c_group_size:
            p += pa(springs, groups, s_idx+1, g_idx+1, 0, memo)
    # for # and hypothetical # from ?
    if springs[s_idx] == "#" or springs[s_idx] == "?":
        # continue current group
        p += pa(springs, groups, s_idx+1, g_idx, c_group_size+1, memo)

    memo[key] = p
    return p


def main():
    records = list()
    with open("2023/day_12.in", "r") as file:
        for line in file:
            springs, groups = line.strip().split(" ")
            records.append((springs, [int(x) for x in groups.split(",")]))

    # task 1
    count = 0
    for (springs, groups) in records:
        count += pa(springs, groups, 0, 0, 0, dict())
    print(count)

    # task 2
    records = [
        ("?".join([springs]*5), groups*5)
        for (springs, groups) in records
    ]
    count = 0
    for (springs, groups) in records:
        count += pa(springs, groups, 0, 0, 0, dict())
    print(count)

if __name__ == "__main__":
    main()
