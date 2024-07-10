import numpy as np

def isNeighbor(this, other):
    for e1 in this.values():
        for e2 in other.values():
            if (e1 == e2).all() or (e1[::-1] == e2).all():
                return True
    return False

def findNeighbors(edges):
    neighbors = dict()
    ids = list(edges.keys())
    for key in ids:
        neighbors[key] = list()

    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            if isNeighbor(edges[ids[i]], edges[ids[j]]):
                neighbors[ids[i]].append(ids[j])
                neighbors[ids[j]].append(ids[i])
    return neighbors

def mapParts(neighbors):
    corner = list()
    edge = list()
    middle = list()
    for key, val in neighbors.items():
        if len(val) == 2:
            corner.append(key)
        elif len(val) == 3:
            edge.append(key)
        else:
            middle.append(key)
    return corner, edge, middle

def matchingEdges(id, neighbors, edges):
    alignment = list()
    for key1, val1 in edges[id].items():
        for n in neighbors:
            for key2, val2 in edges[n].items():
                if (val1 == val2).all() or (val1 == val2[::-1]).all():
                    alignment.append(key1)
                    break
    return alignment

def getRightEdge(id, neighbors, edges):
    for n in neighbors:
        for key, val in edges[n].items():
            if (edges[id]['r'] == val).all():
                return n, key
            elif (edges[id]['r'] == val[::-1]).all():
                return n, '-'+key

def getBottomEdge(id, neighbors, edges):
    for n in neighbors:
        for key, val in edges[n].items():
            if (edges[id]['d'] == val).all():
                return n, key
            elif (edges[id]['d'] == val[::-1]).all():
                return n, '-'+key

def rotateTileAndEdges(tiles, edges, tile_id):
    grid = np.full((10, 10), '.')
    for j in range(10):
        grid[:, 9-j] = tiles[tile_id][j, :]
    tiles[tile_id] = grid
    edge = dict()
    edge['l'] = grid[:, 0]
    edge['r'] = grid[:, 9]
    edge['u'] = grid[0, :]
    edge['d'] = grid[9, :]
    edges[tile_id] = edge

def flipTileAndEdges(tiles, edges, tile_id, vertical):
    if vertical:
        tiles[tile_id] = np.flip(tiles[tile_id], 1)
        edges[tile_id]['u'] = edges[tile_id]['u'][::-1]
        edges[tile_id]['d'] = edges[tile_id]['d'][::-1]
        tmp = edges[tile_id]['l'].copy()
        edges[tile_id]['l'] = edges[tile_id]['r']
        edges[tile_id]['r'] = tmp
    else:
        tiles[tile_id] = np.flip(tiles[tile_id], 0)
        edges[tile_id]['l'] = edges[tile_id]['l'][::-1]
        edges[tile_id]['r'] = edges[tile_id]['r'][::-1]
        tmp = edges[tile_id]['u'].copy()
        edges[tile_id]['u'] = edges[tile_id]['d']
        edges[tile_id]['d'] = tmp

def alignBottom(tiles, edges, id, e):
    if e == 'r':
        flipTileAndEdges(tiles, edges, id, True)
        rotateTileAndEdges(tiles, edges, id)
        flipTileAndEdges(tiles, edges, id, True)
    elif e == '-r':
        flipTileAndEdges(tiles, edges, id, True)
        rotateTileAndEdges(tiles, edges, id)
    elif e == '-u':
        flipTileAndEdges(tiles, edges, id, True)
    elif e == 'l':
        rotateTileAndEdges(tiles, edges, id)
        flipTileAndEdges(tiles, edges, id, True)
    elif e == '-l':
        rotateTileAndEdges(tiles, edges, id)
    elif e == 'd':
        flipTileAndEdges(tiles, edges, id, False)
    elif e == '-d':
        flipTileAndEdges(tiles, edges, id, False)
        flipTileAndEdges(tiles, edges, id, True)

def alignRight(tiles, edges, id, e):
    if e == 'r':
        flipTileAndEdges(tiles, edges, id, True)
    elif e == '-r':
        for k in range(2):
            rotateTileAndEdges(tiles, edges, id)
    elif e == 'u':
        rotateTileAndEdges(tiles, edges, id)
        flipTileAndEdges(tiles, edges, id, True)
    elif e == '-u':
        flipTileAndEdges(tiles, edges, id, True)
        rotateTileAndEdges(tiles, edges, id)
        flipTileAndEdges(tiles, edges, id, True)
    elif e == '-l':
        flipTileAndEdges(tiles, edges, id, False)
    elif e == 'd':
        rotateTileAndEdges(tiles, edges, id)
    elif e == '-d':
        flipTileAndEdges(tiles, edges, id, True)
        rotateTileAndEdges(tiles, edges, id)

def task1(edges):
    neighbors = findNeighbors(edges)
    s = int(1)
    for key, val in neighbors.items():
        if len(val) == 2:
            s *= int(key)
    return s

def printMtx(image):
    for row in image:
        for x in row:
            print(x, end='')
        print()

def task2(edges, tiles):
    neighbors = findNeighbors(edges)
    map_corners, map_edges, map_middle = mapParts(neighbors)

    image = np.full((96, 96), '.')
    tile_id = map_corners[0]
    matches = matchingEdges(tile_id, neighbors[tile_id], edges)
    while 'r' not in matches or 'd' not in matches:
        rotateTileAndEdges(tiles, edges, tile_id)
        matches = matchingEdges(tile_id, neighbors[tile_id], edges)
    image[0:8, 0:8] = tiles[tile_id][1:9, 1:9]

    prev_id = tile_id
    upper_id = tile_id
    for j in range(12):
        for i in range(12):
            if i == 0 and j == 0:
                continue
            if i == 0:
                next_id, e = getBottomEdge(upper_id, neighbors[upper_id], edges)
                alignBottom(tiles, edges, next_id, e)
                upper_id = next_id
            else:
                next_id, e = getRightEdge(prev_id, neighbors[prev_id], edges)
                alignRight(tiles, edges, next_id, e)
            image[8*j:8*j+8, 8*i:8*i+8] = tiles[next_id][1:9, 1:9]
            prev_id = next_id
    
    monst = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    monster = np.array([[c for c in x] for x in monst])
    
    rotated = 0
    monsters = 0
    while monsters == 0:
        for j in range(len(image)-len(monster)):
            for i in range(len(image[0])-len(monster[0])):
                match = True
                for k in range(len(monster)):
                    for l in range(len(monster[0])):
                        if monster[k, l] == '#' and image[j+k, i+l] != '#':
                            match = False
                            break
                    if not match:
                        break
                if match:
                    monsters += 1
        if monsters == 0:
            tmp = np.full((96, 96), '.')
            for j in range(96):
                tmp[:, 95-j] = image[j, :]
            image = tmp
            rotated += 1
            if rotated == 4:
                image = np.flip(image, 1)
    h = np.count_nonzero(image == '#')
    m = np.count_nonzero(monster == '#')
    return h-m*monsters

def main():
    tiles = dict()
    edges = dict()
    with open("2020/day_20.in", "r") as f:
        while True:
            l = list()
            for i in range(11):
                l.append(f.readline().split('\n')[0])
            f.readline()
            if l[0] == '':
                break

            id = int(l[0].split(' ')[1].split(':')[0])
            grid = np.array([[c for c in x] for x in l[1:]])
            edge = dict()
            edge["l"] = grid[:, 0]
            edge["r"] = grid[:, 9]
            edge["u"] = grid[0, :]
            edge["d"] = grid[9, :]
            tiles[id] = grid
            edges[id] = edge
    
    res1 = task1(edges)
    print("Task 1: %d" % res1)

    res2 = task2(edges, tiles)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()