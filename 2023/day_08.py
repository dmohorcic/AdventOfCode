import math


def get_steps_az(start, condition, network, instructions):
    inst_idx = 0
    instruction = instructions[inst_idx]
    next = network[start][instruction]
    steps = 1
    while not condition(next):
        inst_idx += 1
        if inst_idx == len(instructions):
            inst_idx = 0
        instruction = instructions[inst_idx]
        next = network[next][instruction]
        steps += 1
    return steps


def main():
    with open("2023/day_08.in") as f:
        instructions = f.readline().strip()
        instructions = [1 if x == "R" else 0 for x in instructions]
        f.readline()
        network = dict()
        for line in f:
            line = line.strip()
            source, target = line.split(" = ")
            left, right = target[1:-1].split(", ")
            network[source] = [left, right]

    # task 1
    steps = get_steps_az("AAA", lambda x: x == "ZZZ", network, instructions)
    print(steps)

    # task 2
    start_nodes = [key for key in network.keys() if key.endswith("A")]
    path_len = [get_steps_az(node, lambda x: x.endswith("Z"), network, instructions) for node in start_nodes]
    print(math.lcm(*path_len))


if __name__ == "__main__":
    main()
