def task1(arr):
    return max(sum(x) for x in arr)

def task2(arr):
    tmp = [sum(x) for x in arr]
    tmp.sort()
    return sum(tmp[-3:])

def main():
    arr = list()
    with open("2022/day_01.in", "r") as f:
        tmp = list()
        for l in f.readlines():
            if "\n" != l:
                tmp.append(int(l))
            else:
                arr.append(tmp)
                tmp = list()
        arr.append(tmp)

    print(f"Task 1: {task1(arr)}")
    print(f"Task 1: {task2(arr)}")


if __name__ == "__main__":
    main()