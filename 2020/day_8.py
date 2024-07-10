import numpy as np

def simulate(arr):
    accumulator = 0
    i = 0
    executed = np.array([False for x in arr])
    while True:
        if i >= len(arr):
                return True, accumulator
        if executed[i]:
            return False, accumulator
        else:
            executed[i] = True
            args = arr[i]
            if args[0] == "nop":
                i += 1
            elif args[0] == "acc":
                accumulator += int(args[1])
                i += 1
            elif args[0] == "jmp":
                i += int(args[1])

def task1(arr):
    terminated, acc = simulate(arr)
    return acc

def task2(arr):
    for i in range(len(arr)):
        tmp = np.copy(arr)
        if tmp[i][0] == "nop":
            tmp[i][0] = "jmp"
            terminated, acc = simulate(tmp)
            if terminated:
                return acc
        elif tmp[i][0] == "jmp":
            tmp[i][0] = "nop"
            terminated, acc = simulate(tmp)
            if terminated:
                return acc

def main():
    lst = list()
    with open("2020/day_8.in") as f:
        for l in f:
            args = l.split(' ')
            lst.append([args[0], args[1]])
    arr = np.array(lst)

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()