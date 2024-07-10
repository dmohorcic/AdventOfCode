def bags_rec(rules, bag_name):
    sub_bags = 0
    for key, val in rules[bag_name].items():
        sub_bags += val*(bags_rec(rules, key)+1)
    return sub_bags

def task1(rules):
    outer_bags = set()
    parents = set()
    for key, val in rules.items():
        if "shiny gold" in val.keys():
            parents.add(key)
            outer_bags.add(key)
    
    prev_len = 0
    while len(outer_bags) > prev_len:
        prev_len = len(outer_bags)
        new_parents = set()
        for key, val in rules.items():
            for k in val.keys():
                if k in parents:
                    new_parents.add(key)
                    outer_bags.add(key)
        parents = new_parents

    return len(outer_bags)

def task2(rules):
    return bags_rec(rules, "shiny gold")

def main():
    rules = dict()
    with open("2020/day_7.in") as f:
        for l in f:
            name = ' '.join(l.split(' ')[:2])
            contain = l.split("contain ")[1]
            content = contain.split(", ")
            tmp = dict()
            if content[0][:2] != "no":
                for bag in content:
                    bag_conf = bag.split(' ')
                    tmp[" ".join(bag_conf[1:3])] = int(bag_conf[0])
            rules[name] = tmp
    
    res1 = task1(rules)
    print("Task 1: %d" % res1)

    res2 = task2(rules)
    print("Task 2: %d" % res2)

if __name__ == "__main__":
    main()