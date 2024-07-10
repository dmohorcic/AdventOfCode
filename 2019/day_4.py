import numpy as np

def isOK1(pswd):
    d = [int(i) for i in pswd]
    if d[0] > d[1] or d[1] > d[2] or d[2] > d[3] or d[3] > d[4] or d[4] > d[5]:
        return False
    s = np.array([0 for i in range(10)])
    for i in range(len(d)):
        s[d[i]] += 1
    if sum(s >= 2) >= 1:
        return True
    return False

def isOK2(pswd):
    d = [int(i) for i in pswd]
    if d[0] > d[1] or d[1] > d[2] or d[2] > d[3] or d[3] > d[4] or d[4] > d[5]:
        return False
    s = np.array([0 for i in range(10)])
    for i in range(len(d)):
        s[d[i]] += 1
    if sum(s == 2) >= 1:
        return True
    return False

def task1(rng):
    ok_pswds = 0
    for pswd in range(rng[0], rng[1]+1):
        if isOK1(str(pswd)):
            ok_pswds += 1
    return ok_pswds

def task2(rng):
    ok_pswds = 0
    for pswd in range(rng[0], rng[1]+1):
        if isOK2(str(pswd)):
            ok_pswds += 1
    return ok_pswds

def main():
    rng = list()
    with open("2019/day_4.in", "r") as f:
        rng = [int(x) for x in f.readline().split("\n")[0].split('-')]

    res1 = task1(rng)
    print("Task 1: %d" % res1)

    res2 = task2(rng)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    isOK2("112444")
    isOK2("123444")
    main()