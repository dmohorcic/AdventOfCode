def toRemove(poly, ml, ll):
    return (1 if ml == poly[0] or ll == poly[0] else 0)-(1 if ml == poly[-1] or ll == poly[-1] else 0)

def task1(poly, ins):
    for _ in range(10):
        i = 0
        while i < len(poly)-1:
            if poly[i:i+2] in ins.keys():
                poly = poly[:i+1]+ins[poly[i:i+2]]+poly[i+1:]
                i += 2
            else:
                i += 1
    count = {c: 0 for c in poly}
    for c in count.keys():
        count[c] = poly.count(c)
    most = max([c for c in count.values()])
    least = min([c for c in count.values()])
    return most-least

def task2(poly, ins):
    doubles = {poly[i:i+2]: 0 for i in range(len(poly)-1)}
    for d in doubles.keys():
        doubles[d] = poly.count(d)

    for _ in range(40):
        tmp = {}
        a = -1
        for key, val in doubles.items():
            if key in ins.keys():
                key_left = key[0]+ins[key]
                if key_left in tmp.keys():
                    tmp[key_left] += val
                else:
                    tmp[key_left] = val
                key_right = ins[key]+key[1]
                if key_right in tmp.keys():
                    tmp[key_right] += val
                else:
                    tmp[key_right] = val
        doubles = tmp

    count = {}
    for key, val in doubles.items():
        if key[0] in count.keys():
            count[key[0]] += val
        else:
            count[key[0]] = val
        if key[1] in count.keys():
            count[key[1]] += val
        else:
            count[key[1]] = val
    most = max([c for c in count.values()])
    ml = [key for key in count.keys() if count[key] == most][0]
    least = min([c for c in count.values() if c > 0])
    ll = [key for key in count.keys() if count[key] == least][0]
    
    return (most-least-toRemove(poly, ml, ll))//2 # everything is counted twice, except possibly first and last

if __name__ == "__main__":
    polymer = ""
    instructions = {}
    with open("2021/day_14.in", "r") as f:
        polymer = f.readline().split("\n")[0]
        f.readline()
        for l in f.readlines():
            tmp = l.split("\n")[0].split(" -> ")
            instructions[tmp[0]] = tmp[1]
    
    print(f"Task 1: {task1(polymer[::-1][::-1], instructions)}")
    print(f"Task 2: {task2(polymer, instructions)}")