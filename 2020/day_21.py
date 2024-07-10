import numpy as np

def possibleTranslations(ingredients, alergens, alergen):
    possible = list()
    for key, val in alergens.items():
        if alergen in val:
            possible.append(set(ingredients[key]))
    ing = possible[0]
    for i in range(1, len(possible)):
        ing = ing.intersection(possible[i])
    return ing

def getTranslation(ingredients, alergens):
    translation = dict()
    lst_alergens = {a for aler in alergens.values() for a in aler}
    found = 0
    while found < len(lst_alergens):
        for alergen in lst_alergens:
            if alergen in translation.keys():
                continue
            else:
                poss = possibleTranslations(ingredients, alergens, alergen)
                for key in translation.values():
                    try:
                        poss.remove(key)
                    except:
                        pass
                if len(poss) == 1:
                    translation[alergen] = poss.pop()
                    found += 1
                    break
    return translation

def task1(ingredients, alergens):
    translation = getTranslation(ingredients, alergens)

    s = 0
    for meal in ingredients:
        for item in meal:
            if item not in translation.values():
                s += 1
    return s

def task2(ingredients, alergens):
    translation = getTranslation(ingredients, alergens)

    keys = list(translation.keys())
    keys.sort()
    s = ""
    for key in keys:
        s += translation[key]+","
    return s[:-1]


def main():
    lst = list()
    alergens = dict()
    with open("2020/day_21.in", "r") as f:
        i = 0
        for l in f:
            args = l.split(" (contains ")
            lst.append(np.array(args[0].split(' ')))
            alergens[i] = np.array(args[1].split(')')[0].split(", "))
            i += 1
    ingredients = np.array(lst)

    res1 = task1(ingredients, alergens)
    print("Task 1: %d" % res1)

    res2 = task2(ingredients, alergens)
    print("Task 2: %s" % res2)

if __name__ == "__main__":
    main()