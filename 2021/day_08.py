toDictKey = lambda x: "".join(sorted([c for c in x]))

def createDisplayDict(display):
    """ 1. get translations for 1, 4, 7, 8
    Numbers 1, 4, 7, and 8 have unique representation length
    """
    translation = dict()
    rev_trans = dict()
    for i, num in zip([2, 3, 4, 7], [1, 7, 4, 8]):
        lenStr = [d for d in display if len(d) == i][0]
        translation[lenStr] = num
        rev_trans[num] = lenStr

    """ 2. get translation for 6
    If we calculate the difference between 8 and 1 (U), and then the difference
    between 6, 9, and 0 to U, only 6 has difference of 1
    """
    eight_one = set(rev_trans[8])-set(rev_trans[1]) # set
    len6 = [d for d in display if len(d) == 6]
    diff = [0, 0, 0] # difference in lighted segments
    for i in range(3):
        set_i = set(len6[i])
        diff[i] = (set_i-eight_one).union(eight_one-set_i)
    idx6 = [i for i in range(3) if len(diff[i]) == 1][0]
    segment6 = diff[idx6]
    translation[len6[idx6]] = 6
    rev_trans[6] = len6[idx6]
    len6.pop(idx6)

    """ 3. get translation for 3
    The difference between 2, 3, and 5 to 7, only 3 has difference of 2 (others have 4)
    """
    seven = set(rev_trans[7])
    len5 = [d for d in display if len(d) == 5]
    diff = [0, 0, 0]
    for i in range(3):
        set_i = set(len5[i])
        diff[i] = (set_i-seven).union(seven-set_i)
    idx3 = [i for i in range(3) if len(diff[i]) == 2][0]
    translation[len5[idx3]] = 3
    rev_trans[3] = len5[idx3]
    len5.pop(idx3)

    """ 4. get translations for 5 and 2
    From 2 we get the segment for number 6, 5 has it, 2 does not
    """
    if segment6.issubset(set(len5[0])): # Found 5
        translation[len5[0]] = 5
        rev_trans[5] = len5[0]
        translation[len5[1]] = 2
        rev_trans[2] = len5[1]
    else:
        translation[len5[0]] = 2
        rev_trans[2] = len5[0]
        translation[len5[1]] = 5
        rev_trans[5] = len5[1]

    """ 5.
    Difference of 9 and 0 to 3 can differentiate them, 9 has diff 1, 0 has 3
    """
    three = set(rev_trans[3])
    if len(set(len6[0])-three) == 1: # Found 9
        translation[len6[0]] = 9
        rev_trans[9] = len6[0]
        translation[len6[1]] = 0
        rev_trans[0] = len6[1]
    else:
        translation[len6[0]] = 0
        rev_trans[0] = len6[0]
        translation[len6[1]] = 9
        rev_trans[9] = len6[1]

    corrected = dict()
    for key, val in translation.items():
        new_key = toDictKey(key)
        corrected[new_key] = val
    return corrected

def task1(output):
    count = 0
    for out in output:
        for o in out:
            if len(o) in [2, 3, 4, 7]:
                count += 1
    return count

def task2(display, output):
    s = 0
    for d, o in zip(display, output):
        trans = createDisplayDict(d)
        num = 0
        for i in range(4):
            num = num*10 + trans[toDictKey(o[i])]
        s += num
    return s

if __name__ == "__main__":
    display = list()
    output = list()
    with open("2021/day_08.in", "r") as f:
        for l in f.readlines():
            tmp = l.split("\n")[0].split(" | ")
            display.append(tmp[0].split(" "))
            output.append(tmp[1].split(" "))
    
    print(f"Task 1: {task1(output)}")
    print(f"Task 2: {task2(display, output)}")