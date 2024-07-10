import numpy as np

def task1(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == 2020:
                return arr[i]*arr[j]

def task2(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]+arr[k] == 2020:
                    return arr[i]*arr[j]*arr[k]    

def main():
    lst = list()
    with open("2020/day_1.in", "r") as f:
        for l in f:
            lst.append(int(l.split('\n')[0]))
    arr = np.array(lst)

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()