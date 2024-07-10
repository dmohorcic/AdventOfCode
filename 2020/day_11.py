import numpy as np

def nbhTask1(mtx, i, j):
    s = mtx.shape
    nbh = mtx[max(0, i-1):min(i+1, s[0])+1, max(0, j-1):min(j+1, s[1])+1]
    return np.count_nonzero(nbh == '#')

def nbhTask2(mtx, i, j):
    full = 0
    s = mtx.shape
    dirs = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
    for dir in dirs:
        for k in range(1,100):
            ir = i+k*dir[0]
            jr = j+k*dir[1]
            if ir < 0 or ir >= s[0] or jr < 0 or jr >= s[1]:
                break
            else:
                if mtx[ir][jr] == "#":
                    full += 1
                    break
                elif mtx[ir][jr] == "L":
                    break
    return full

def simulate(mtx, nbhF):
    s = mtx.shape
    while True:
        next = np.full_like(mtx, '.')
        for i in range(s[0]):
            for j in range(s[1]):
                seat = mtx[i][j]
                full = nbhF(mtx, i, j)
                if seat == 'L' and full == 0:
                    next[i][j] = '#'
                elif seat == '#' and full > 4:
                    next[i][j] = 'L'
                else:
                    next[i][j] = seat
        if np.array_equal(next, mtx):
            return np.count_nonzero(next == '#')
        else:
            mtx = next.copy()

def task1(mtx):
    return simulate(mtx, nbhTask1)

def task2(mtx):
    return simulate(mtx, nbhTask2)

def main():
    lst = list()
    with open("2020/day_11.in", "r") as f:
        for l in f:
            lst.append(list(l.split('\n')[0]))
    mtx = np.array(lst)
    
    res1 = task1(mtx.copy())
    print("Task 1: %d" % res1)

    res2 = task2(mtx.copy())
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()