def main():
    games = dict()
    with open("2023/day_02.in") as f:
        for line in f:
            line = line.strip()
            game_id, game_states = line.split(": ")
            game_id = int(game_id.split(" ")[-1])
            parsed_game_states = list()
            for game_state in game_states.split("; "):
                rgb = {"red": 0, "green": 0, "blue": 0}
                for gs in game_state.split(", "):
                    num, type_ = gs.split(" ")
                    rgb[type_] = int(num)
                parsed_game_states.append(rgb)
            games[game_id] = parsed_game_states

    # task 1
    possible_sum = 0
    for id, game in games.items():
        for play in game:
            if play["red"] > 12 or play["green"] > 13 or play["blue"] > 14:
                break
        else:
            possible_sum += id
    print(possible_sum)

    # task 2
    power_sum = 0
    for game in games.values():
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for play in game:
            min_cubes["red"] = max(min_cubes["red"], play["red"])
            min_cubes["green"] = max(min_cubes["green"], play["green"])
            min_cubes["blue"] = max(min_cubes["blue"], play["blue"])
        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        power_sum += power
    print(power_sum)

if __name__ == "__main__":
    main()
