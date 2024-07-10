import numpy as np

def countArrangements(arr, idx, memo=dict()):
    if idx in memo.keys():
        return memo[idx]
    if idx == len(arr)-1:
        return 1
    c = 0
    adv = [x for x in range(1, min(len(arr)-idx, 4))]
    for x in adv:
        if arr[idx+x]-3 <= arr[idx]:
            c += countArrangements(arr, idx+x)
    memo[idx] = c
    return c


def task1(arr):
    arr.sort()
    diff = [0, 0, 0]
    for i in range(1, len(arr)):
        diff[arr[i]-arr[i-1]-1] += 1
    return diff[0]*diff[2]

def task2(arr):
    return countArrangements(arr, 0)

def main():
    lst = [0]
    with open("2020/day_10.in") as f:
        for l in f:
            lst.append(int(l.split('\n')[0]))
    lst.append(max(lst)+3)
    arr = np.array(lst)
    arr.sort()

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()