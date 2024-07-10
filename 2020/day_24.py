import numpy as np

TILE_DIRS = {"e": np.array([1, 0]),
             "se": np.array([1, -1]),
             "sw": np.array([0, -1]),
             "w": np.array([-1, 0]),
             "nw": np.array([-1, 1]),
             "ne": np.array([0, 1])}

def fillLobby(arr):
    tiles = dict()
    for ins in arr:
        coords = np.array([0, 0])
        start = 0
        for end in range(1, len(ins)+1):
            dir = ins[start:end]
            if dir in TILE_DIRS.keys():
                coords = coords+TILE_DIRS[dir]
                start = end
        c = (coords[0], coords[1])
        if c in tiles.keys():
            del tiles[c]
        else:
            tiles[c] = True
    return tiles

def blackNeighbors(tiles, coords):
    neighbors = 0
    for dir in TILE_DIRS:
        tmp = coords+TILE_DIRS[dir]
        c = (tmp[0], tmp[1])
        if c in tiles.keys():
            neighbors += 1
    return neighbors

def flipTiles(tiles):
    next_day = dict()
    for key in tiles.keys():
        coords = np.array([key[0], key[1]])

        # number of black neighbors
        neighbors = blackNeighbors(tiles, coords)
        if neighbors > 0 and neighbors < 3:
            next_day[key] = True

        # check for white neighbors
        for dir in TILE_DIRS:
            neigh = coords+TILE_DIRS[dir]
            c_neigh = (neigh[0], neigh[1])
            if c_neigh not in tiles.keys() and c_neigh not in next_day.keys():
                neighbors = blackNeighbors(tiles, neigh)
                if neighbors == 2:
                    next_day[c_neigh] = True
    return next_day

def task1(arr):
    tiles = fillLobby(arr)
    return len(tiles.keys())

def task2(arr):
    tiles = fillLobby(arr)

    for i in range(100):
        tiles = flipTiles(tiles)
    
    return len(tiles.keys())

def main():
    lst = list()
    with open("2020/day_24.in", "r") as f:
        for l in f:
            lst.append(l.split('\n')[0])
    arr = np.array(lst)

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()