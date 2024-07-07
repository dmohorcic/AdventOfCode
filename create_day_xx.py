import os

YEAR = "2023"

def main():
    try:
        raw_input = input("Day: ")
        day_number = int(raw_input)
        if day_number < 1 or day_number > 25:
            raise ValueError()
    except ValueError:
        print(f"Day should be an integer between 1 and 25 inclusive, but you gave '{raw_input}'")
        exit()

    if not os.path.isdir(YEAR):
        os.mkdir(YEAR)
    
    day_str = "0"+str(day_number) if day_number < 10 else str(day_number)
    if os.path.isfile(f"{YEAR}/day_{day_str}.py"):
        print(f"Files for day {day_number} already exist")
        exit()

    with open(f"{YEAR}/day_{day_str}.py", "w") as f:
        f.write(f'def main():\n    \n    with open("{YEAR}/day_{day_str}.in", "r") as file:\n        for line in file:\n            pass\n\n\nif __name__ == "__main__":\n    main()\n')
    with open(f"{YEAR}/day_{day_str}.in", "w") as f:
        pass


if __name__ == "__main__":
    main()
