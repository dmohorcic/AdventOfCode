import numpy as np

def task1(arr):
    return sum(arr)

def task2(arr):
    d = dict()
    f, i = 0, 0
    d[f] = 1
    while True:
        f += arr[i]
        i += 1
        if i == len(arr):
            i = 0
        if f in d.keys():
            return f
        else:
            d[f] = 1

def main():
    lst = list()
    with open("2018/day_1.in", "r") as f:
        for l in f:
            lst.append(int(l.split('\n')[0]))
    arr = np.array(lst)

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()