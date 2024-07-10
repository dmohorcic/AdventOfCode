import numpy as np

def task1(arr):
    coords = [0, 0]
    dir = 0
    for act in arr:
        ins = act[0]
        dis = int(act[1])
        if ins == 'L':
            dir += dis/90
        elif ins == 'R':
            dir -= dis/90
        elif ins == 'F':
            if dir%2 == 0:
                coords[0] += dis*(1 if dir == 0 else -1)
            else:
                coords[1] += dis*(1 if dir == 1 else -1)
        elif ins in ['E', 'W']:
            coords[0] += dis*(1 if ins == 'E' else -1)
        elif ins in ['N', 'S']:
            coords[1] += dis*(1 if ins == 'N' else -1)
        dir = (dir+4)%4
    return sum([abs(x) for x in coords])

def task2(arr):
    coords = [0, 0]
    waypoint = [10, 1]
    for act in arr:
        ins = act[0]
        dis = int(act[1])
        if ins == 'L':
            for i in range(abs(int(dis/90))):
                waypoint = [-waypoint[1], waypoint[0]]
        elif ins == 'R':
            for i in range(abs(int(dis/90))):
                waypoint = [waypoint[1], -waypoint[0]]
        elif ins == 'F':
            coords[0] += dis*waypoint[0]
            coords[1] += dis*waypoint[1]
        elif ins in ['E', 'W']:
            waypoint[0] += dis*(1 if ins == 'E' else -1)
        elif ins in ['N', 'S']:
            waypoint[1] += dis*(1 if ins == 'N' else -1)
    return sum([abs(x) for x in coords])

def main():
    lst = list()
    with open("2020/day_12.in", "r") as f:
        for l in f:
            ins = l[0]
            dist = (l[1:]).split('\n')[0]
            lst.append((ins, dist))
    arr = np.array(lst)

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()