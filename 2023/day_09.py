def difference_and_prediction_forward(values: list):
    if all(x == 0 for x in values):
        return 0
    differences = [x-y for x, y in zip(values[1:], values[:-1])]
    val = difference_and_prediction_forward(differences)
    return val + values[-1]


def difference_and_prediction_backward(values: list):
    if all(x == 0 for x in values):
        return 0
    differences = [x-y for x, y in zip(values[1:], values[:-1])]
    val = difference_and_prediction_backward(differences)
    return values[0] - val


def main():
    with open("2023/day_09.in") as f:
        polynomes = list()
        for line in f:
            line = line.strip().split(" ")
            polynomes.append([int(x) for x in line])
    
    # task 1
    print(sum(difference_and_prediction_forward(polynome) for polynome in polynomes))

    # task 1
    print(sum(difference_and_prediction_backward(polynome) for polynome in polynomes))


if __name__ == "__main__":
    main()
