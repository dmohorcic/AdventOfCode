scoring1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scoring2 = {")": 1, "]": 2, "}": 3, ">": 4}
closing = [")", "]", "}", ">"]
pair = {"(": ")", "[": "]", "{": "}", "<": ">"}

def task1(expressions):
    score = 0
    incomplete = list()
    for exp in expressions:
        stack = list()
        is_broken = False
        for e in exp:
            if e in closing:
                last = stack.pop()
                if e != pair[last]:
                    score += scoring1[e]
                    is_broken = True
                    break
            else:
                stack.append(e)
        if not is_broken:
            incomplete.append(exp)
    return incomplete, score

def task2(incomplete):
    score = list()
    for exp in incomplete:
        stack = list()
        for e in exp:
            if e in closing:
                stack.pop()
            else:
                stack.append(e)
        tmp_score = 0
        for s in stack[::-1]:
            tmp_score *= 5
            tmp_score += scoring2[pair[s]]
        score.append(tmp_score)
    score.sort()
    idx = (len(score)//2)
    return score[idx]

if __name__ == "__main__":
    expressions = list()
    with open("2021/day_10.in", "r") as f:
        for i, l in enumerate(f.readlines()):
            expressions.append(l.split("\n")[0])
    incomplete, score = task1(expressions)
    print(f"Task 1: {score}")
    print(f"Task 2: {task2(incomplete)}")
