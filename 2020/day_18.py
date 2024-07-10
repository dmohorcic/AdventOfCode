import numpy as np

class Expression:
    def __init__(self, formula, addition_first):
        self.left, self.op, self.right = parse(formula, addition_first)

    def evaluate(self):
        if self.op == '+':
            return self.left.evaluate()+self.right.evaluate()
        else:
            return self.left.evaluate()*self.right.evaluate()

class Number:
    def __init__(self, number):
        self.number = int(number)
    
    def evaluate(self):
        return self.number

def parse(formula, addition_first):
    if len(formula) == 1:
        return Number(int(formula))
    # remove brackets
    while formula[0] == '(' and formula[-1] == ')':
        brackets = 0
        remove_brackets = True
        for i in range(len(formula)):
            if formula[i] == '(':
                brackets += 1
            elif formula[i] == ')':
                brackets -= 1
                if brackets == 0 and i != len(formula)-1:
                    remove_brackets = False
                    break
        if remove_brackets:
            formula = formula[1:-1]
        else:
            break
    # find rightmost outer operator
    brackets = 0
    if addition_first:
        for i in range(len(formula)-1, -1, -1):
            if formula[i] == ')':
                brackets += 1
            elif formula[i] == '(':
                brackets -= 1
            elif formula[i] == '*' and brackets == 0:
                left_formula = formula[:i]
                right_formula = formula[i+1:]
                if len(left_formula) == 1:
                    left_e = Number(left_formula)
                else:
                    left_e = Expression(left_formula, addition_first)
                if len(right_formula) == 1:
                    right_e = Number(right_formula)
                else:
                    right_e = Expression(right_formula, addition_first)
                return left_e, formula[i], right_e
        for i in range(len(formula)-1, -1, -1):
            if formula[i] == ')':
                brackets += 1
            elif formula[i] == '(':
                brackets -= 1
            elif formula[i] == '+' and brackets == 0:
                left_formula = formula[:i]
                right_formula = formula[i+1:]
                if len(left_formula) == 1:
                    left_e = Number(left_formula)
                else:
                    left_e = Expression(left_formula, addition_first)
                if len(right_formula) == 1:
                    right_e = Number(right_formula)
                else:
                    right_e = Expression(right_formula, addition_first)
                return left_e, formula[i], right_e
    else:
        for i in range(len(formula)-1, -1, -1):
            if formula[i] == ')':
                brackets += 1
            elif formula[i] == '(':
                brackets -= 1
            elif formula[i] in ['+', '*'] and brackets == 0:
                left_formula = formula[:i]
                right_formula = formula[i+1:]
                if len(left_formula) == 1:
                    left_e = Number(left_formula)
                else:
                    left_e = Expression(left_formula, addition_first)
                if len(right_formula) == 1:
                    right_e = Number(right_formula)
                else:
                    right_e = Expression(right_formula, addition_first)
                return left_e, formula[i], right_e

def task1(arr):
    s = 0
    for exp in arr:
        e = Expression(exp, False)
        s += e.evaluate()
    return s

def task2(arr):
    s = 0
    for exp in arr:
        e = Expression(exp, True)
        s += e.evaluate()
    return s

def main():
    lst = list()
    with open("2020/day_18.in", "r") as f:
        for l in f:
            lst.append(''.join(l.split('\n')[0].split(' ')))
    arr = np.array(lst)

    res1 = task1(arr)
    print("Task 1: %d" % res1)

    res2 = task2(arr)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()