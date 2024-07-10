import numpy as np

def adaptMask(mask, andMask):
    if andMask:
        return ''.join(['0' if c == '0' else '1' for c in mask])
    else:
        return ''.join(['1' if c == '1' else '0' for c in mask])

def maskAddress(addr, mask):
    adr = addr.zfill(len(mask))
    out = ""
    for a, m in zip(adr, mask):
        if m == '0':
            out += a
        else:
            out += m
    return ''.join(out)


def allAddresses(addr, idx):
    if idx == len(addr):
        return [addr]
    if addr[idx] == 'X':
        msk = list(addr)
        msk[idx] = '1'
        tmp = allAddresses("".join(msk), idx+1)
        if len(tmp) == 1:
            lst = tmp
        else:
            lst = [m for m in tmp]
        msk[idx] = '0'
        tmp = allAddresses("".join(msk), idx+1)
        if len(tmp) == 1:
            lst.append(tmp[0])
        else:
            for m in tmp:
                lst.append(m)
        return lst
    return allAddresses(addr, idx+1)


def task1(arr):
    mem = dict()
    mask = ""
    for l in arr:
        if "mask" in l[0]:
            mask = str(l[1])
        else:
            idx = int(l[0][:-1].split('[')[1])
            val = int(l[1])
            val |= int(adaptMask(mask, False), 2)
            val &= int(adaptMask(mask, True), 2)
            mem[idx] = val
    return sum([val for val in mem.values()])

def task2(arr):
    mem = dict()
    mask = ""
    for l in arr:
        if "mask" in l[0]:
            mask = str(l[1])
        else:
            idx = format(int(l[0][:-1].split('[')[1]), 'b')
            val = int(l[1])
            addr = maskAddress(idx, mask)
            addrs = allAddresses(addr, 0)
            for a in addrs:
                mem[int(a, 2)] = val
    return sum([val for val in mem.values()])

def main():
    lst = list()
    with open("2020/day_14.in", "r") as f:
        for l in f:
            lst.append(l.split('\n')[0].split(" = "))
    arr = np.array(lst)
    
    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()