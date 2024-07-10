import numpy as np


directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] #right, down, left, up
def task1(grid):
    dist = np.ones(grid.shape)*grid.shape[0]*grid.shape[1]*10
    prev = np.zeros(grid.shape)

    Q = [(0, 0, 0)]
    dist[0, 0] = 0

    while len(Q) > 0:
        u = Q.pop(0)

        for idx, dir in enumerate(directions):
            x = u[0]+dir[0]
            y = u[1]+dir[1]
            if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
                continue
            v = grid[x, y]
            alt = u[2]+v
            if alt < dist[x, y]:
                dist[x, y] = alt
                prev[x, y] = idx+1
                Q.append((x, y, alt))
        Q.sort(key = lambda x: x[2])
    
    return dist[-1, -1]

def task2(grid):
    new_grid = np.zeros((grid.shape[0]*5, grid.shape[1]*5))
    for i in range(5):
        for j in range(5):
            new_grid[i*grid.shape[0]:(i+1)*grid.shape[0], j*grid.shape[1]:(j+1)*grid.shape[1]] = grid+i+j
    wh = np.where(new_grid > 9)
    while wh[0].shape[0] > 0:
        new_grid[wh] -= 9
        wh = np.where(new_grid > 9)
    grid = new_grid

    dist = np.ones(grid.shape)*grid.shape[0]*grid.shape[1]*10
    prev = np.zeros(grid.shape)

    Q = [(0, 0, 0)]
    dist[0, 0] = 0

    while len(Q) > 0:
        u = Q.pop(0)

        for idx, dir in enumerate(directions):
            x = u[0]+dir[0]
            y = u[1]+dir[1]
            if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
                continue
            v = grid[x, y]
            alt = u[2]+v
            if alt < dist[x, y]:
                dist[x, y] = alt
                prev[x, y] = idx+1
                Q.append((x, y, alt))
        Q.sort(key = lambda x: x[2])
    
    return dist[-1, -1]

if __name__ == "__main__":
    grid = list()
    with open("2021/day_15.in", "r") as f:
        for l in f.readlines():
            grid.append(np.array([int(c) for c in l.split("\n")[0]]))
    grid = np.array(grid)

    print(f"Task 1: {task1(grid)}")
    print(f"Task 2: {task2(grid)}") #2009 low