# Advent of Code

This repository includes my solutions to [Advent of Code](https://adventofcode.com/).

## Reproducibility

Python code uses two external libraries: numpy and nltk.

2025 day 10 part 2 requires docker and Z3 image from https://github.com/Z3Prover/z3/pkgs/container/z3.

## Structure

The code is sorted in folders by year. The code for each day is in file `day_<day>.py`. The input for each day must be placed in the same folder and named `day_<day>.in`. The code must be run from the root folder. The output of each program is formatted as:
```
--- Day <day>: <title> ---
Task 1: <result for task 1>
Task 2: <result for task 2>
```