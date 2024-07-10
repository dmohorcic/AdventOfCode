def findPath1(node, edges, visited):
    paths = 0
    for neighbor in edges[node]:
        if neighbor == "end":
            paths += 1
            # print(visited+["end"])
        elif neighbor == "start":
            continue
        elif (neighbor.islower() and neighbor not in visited) or neighbor.isupper():
            visited.append(neighbor)
            paths += findPath1(neighbor, edges, visited)
            visited.pop()
    return paths

def allOnce(visited):
    for node in visited:
        if node.islower() and visited.count(node) > 1:
            return False
    return True

def findPath2(node, edges, visited):
    paths = 0
    for neighbor in edges[node]:
        if neighbor == "end":
            paths += 1
            # print(visited+["end"])
        elif neighbor == "start":
            continue
        elif (neighbor.islower() and (neighbor not in visited or allOnce(visited))) or neighbor.isupper():
            visited.append(neighbor)
            paths += findPath2(neighbor, edges, visited)
            visited.pop()
    return paths

def task1(edges):
    visited = list(["start"])
    return findPath1("start", edges, visited)

def task2(edges):
    visited = list(["start"])
    return findPath2("start", edges, visited)

if __name__ == "__main__":
    edges = dict()
    with open("2021/day_12.in", "r") as f:
        for l in f.readlines():
            tmp = l.split("\n")[0].split("-")
            if tmp[0] in edges.keys():
                edges[tmp[0]].append(tmp[1])
            else:
                edges[tmp[0]] = [tmp[1]]
            if tmp[1] in edges.keys():
                edges[tmp[1]].append(tmp[0])
            else:
                edges[tmp[1]] = [tmp[0]]
    
    print(f"Task 1: {task1(edges)}")
    print(f"Task 2: {task2(edges)}")