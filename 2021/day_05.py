import numpy as np

def task1(data):
    grid = np.zeros((1000, 1000))
    for d in data:
        if d[0][0] != d[1][0] and d[0][1] != d[1][1]: # line is diagonal
            continue
        i, j = d[0][0], d[0][1]
        di = 0 if d[1][0]-d[0][0] == 0 else (1 if d[1][0]-d[0][0] > 0 else -1)
        dj = 0 if d[1][1]-d[0][1] == 0 else (1 if d[1][1]-d[0][1] > 0 else -1)
        while i != d[1][0] or j != d[1][1]:
            grid[i, j] += 1
            i += di
            j += dj
        grid[i, j] += 1 # while doesn't cover last
    return np.sum(grid >= 2)

def task2(data):
    grid = np.zeros((1000, 1000))
    for d in data:
        i, j = d[0][0], d[0][1]
        di = 0 if d[1][0]-d[0][0] == 0 else (1 if d[1][0]-d[0][0] > 0 else -1)
        dj = 0 if d[1][1]-d[0][1] == 0 else (1 if d[1][1]-d[0][1] > 0 else -1)
        while i != d[1][0] or j != d[1][1]:
            grid[i, j] += 1
            i += di
            j += dj
        grid[i, j] += 1 # while doesn't cover last
    return np.sum(grid >= 2)

if __name__ == "__main__":
    data = list()
    with open("2021/day_05.in", "r") as f:
        for l in f.readlines():
            l = l.split("\n")[0].split(" -> ")
            data.append(([int(i) for i in l[0].split(",")], [int(i) for i in l[1].split(",")]))
    
    print(f"Task 1: {task1(data)}")
    print(f"Task 2: {task2(data)}")