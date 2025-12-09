package main

import (
	"bufio"
	"fmt"
	"os"
)

func Day04() {
	fmt.Println("--- Day 4: Ceres Search ---")

	file, err := os.Open("04.in")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var crossword_raw []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		crossword_raw = append(crossword_raw, scanner.Text())
	}

	directions := [][]int{
		{0, -1},
		{1, -1},
		{1, 0},
		{1, 1},
		{0, 1},
		{-1, 1},
		{-1, 0},
		{-1, -1},
	}

	var xmas_count int
	mas := []byte{'M', 'A', 'S'}
	for i := 0; i < len(crossword_raw); i++ {
		for j := 0; j < len(crossword_raw[i]); j++ {
			if crossword_raw[i][j] == 'X' {
				for _, dir := range directions {
					dx := dir[0]
					dy := dir[1]
					found := true
					for _, c := range mas {
						if 0 > i+dx || i+dx >= len(crossword_raw) {
							found = false
							break
						}
						if 0 > j+dy || j+dy >= len(crossword_raw[i]) {
							found = false
							break
						}
						if crossword_raw[i+dx][j+dy] != c {
							found = false
							break
						}
						dx += dir[0]
						dy += dir[1]
					}
					if found {
						xmas_count++
					}
				}
			}
		}
	}
	fmt.Printf("Task 1: %d\n", xmas_count)

	var mas_count int
	for i := 0; i < len(crossword_raw); i++ {
		for j := 0; j < len(crossword_raw[i]); j++ {
			if crossword_raw[i][j] == 'A' {
				found_m := make([]bool, 8)
				found_s := make([]bool, 8)
				for dir_idx, dir := range directions {
					dx := dir[0]
					dy := dir[1]
					if 0 > i+dx || i+dx >= len(crossword_raw) {
						break
					}
					if 0 > j+dy || j+dy >= len(crossword_raw[i]) {
						break
					}
					if crossword_raw[i+dx][j+dy] == 'M' {
						found_m[dir_idx] = true
					} else if crossword_raw[i+dx][j+dy] == 'S' {
						found_s[dir_idx] = true
					}
				}

				//n_s := (found_m[0] && found_s[4]) || (found_m[4] && found_s[0])
				ne_sw := (found_m[1] && found_s[5]) || (found_m[5] && found_s[1])
				//e_w := (found_m[2] && found_s[6]) || (found_m[6] && found_s[2])
				se_nw := (found_m[3] && found_s[7]) || (found_m[7] && found_s[3])
				// if n_s && e_w {
				// 	mas_count++
				// }
				if ne_sw && se_nw {
					mas_count++
				}
			}
		}
	}
	fmt.Printf("Task 2: %d\n", mas_count)
}
