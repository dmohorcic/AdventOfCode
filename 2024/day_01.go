package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strings"
)

func Day01() {
	file, err := os.Open("day_01.in")
	if err != nil {
		return
	}
	defer file.Close()
	fmt.Println("--- Day 1: Historian Hysteria ---")

	var lists_raw []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lists_raw = append(lists_raw, scanner.Text())
	}

	var list_a, list_b []int
	for _, line := range lists_raw {
		values := strings.Fields(line)
		num_a := StringToInt(values[0])
		list_a = append(list_a, num_a)
		num_b := StringToInt(values[1])
		list_b = append(list_b, num_b)
	}

	sort.Ints(list_a)
	sort.Ints(list_b)

	var distance int
	for i, val_a := range list_a {
		val_b := list_b[i]
		distance += int(math.Abs(float64(val_a - val_b)))
	}
	fmt.Printf("Task 1: %d\n", distance)

	map_b := make(map[int]int)
	for _, val_b := range list_b {
		map_b[val_b] = map_b[val_b] + 1
	}

	var similarity int
	for _, val_a := range list_a {
		val_b, ok := map_b[val_a]
		if !ok {
			val_b = 0
		}
		similarity += val_a * val_b
	}
	fmt.Printf("Task 2: %d\n", similarity)
}
