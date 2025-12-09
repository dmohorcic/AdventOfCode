package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func Day03() {
	fmt.Println("--- Day 3: Mull It Over ---")

	file, err := os.Open("03.in")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var memory_raw []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		memory_raw = append(memory_raw, scanner.Text())
	}

	var results int64
	r_mul := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	for _, line := range memory_raw {
		matches := r_mul.FindAllStringSubmatch(line, -1) // [mul(aaa,bbb), aaa, bbb]
		for _, match := range matches {
			if len(match) == 3 {
				a := StringToInt(match[1])
				b := StringToInt(match[2])
				results += int64(a) * int64(b)
			}
		}
	}
	fmt.Printf("Task 1: %d\n", results)

	var enabled int64
	r_do := regexp.MustCompile(`do\(\)`)
	r_dont := regexp.MustCompile(`don't\(\)`)
	is_do := true
	for _, line := range memory_raw {
		matches_mul := r_mul.FindAllStringSubmatchIndex(line, -1)   // [full_start, full_end, a_start, a_end, b_start, b_end]
		matches_do := r_do.FindAllStringSubmatchIndex(line, -1)     // [full_start, full_end]
		matches_dont := r_dont.FindAllStringSubmatchIndex(line, -1) // [full_start, full_end]
		var idx_mul, idx_do, idx_dont int
		for i := 0; i < len(line); i++ {
			if matches_mul[idx_mul][0] == i {
				if is_do {
					a := StringToInt(line[matches_mul[idx_mul][2]:matches_mul[idx_mul][3]])
					b := StringToInt(line[matches_mul[idx_mul][4]:matches_mul[idx_mul][5]])
					enabled += int64(a) * int64(b)
				}
				idx_mul++
				if idx_mul == len(matches_mul) { // we consumed all matches
					break
				}
			} else if matches_do[idx_do][0] == i {
				is_do = true
				idx_do++
				if idx_do == len(matches_do) {
					idx_do--
				}
			} else if matches_dont[idx_dont][0] == i {
				is_do = false
				idx_dont++
				if idx_dont == len(matches_dont) {
					idx_dont--
				}
			}
		}
	}
	fmt.Printf("Task 2: %d\n", enabled)
}
