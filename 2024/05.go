package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Day05() {
	fmt.Println("--- Day 5: Print Queue ---")

	file, err := os.Open("05.in")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var rules_raw, prints_raw []string
	rules_end := false
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) < 2 {
			rules_end = true
			continue
		}
		if rules_end {
			prints_raw = append(prints_raw, line)
		} else {
			rules_raw = append(rules_raw, line)
		}
	}

	wrong_order := make(map[int]map[int]struct{})
	for _, rule := range rules_raw {
		r := strings.Split(rule, "|")
		a := StringToInt(r[0])
		b := StringToInt(r[1])

		if wrong_order[b] == nil {
			wrong_order[b] = make(map[int]struct{})
		}
		wrong_order[b][a] = struct{}{}
	}

	var wrong_prints [][]int
	var middle_correct int
	for _, print := range prints_raw {
		pages := strings.Split(print, ",")
		var arr []int
		for _, page := range pages {
			arr = append(arr, StringToInt(page))
		}

		is_ok := true
		for a := 0; a < len(arr); a++ {
			i := arr[a]
			wo_i, ok_i := wrong_order[i]
			if !ok_i {
				continue
			}
			for b := a + 1; b < len(arr); b++ {
				j := arr[b]
				_, ok_j := wo_i[j]
				if ok_j {
					is_ok = false
					break
				}
			}
			if !is_ok {
				break
			}
		}
		if is_ok {
			middle_correct += arr[(len(arr)-1)/2]
		} else {
			wrong_prints = append(wrong_prints, arr)
		}
	}
	fmt.Printf("Task 1: %d\n", middle_correct)

	var middle_wrong int
	for _, wrong_print := range wrong_prints {
		new_wrong_order := make(map[int]map[int]struct{})
		for _, page := range wrong_print {
			new_wrong_order[page] = make(map[int]struct{})
			for _, page_alt := range wrong_print {
				if _, ok := wrong_order[page][page_alt]; ok {
					new_wrong_order[page][page_alt] = struct{}{}
				}
			}
		}
		count_wrong_order := make(map[int]int)
		for page, count := range new_wrong_order {
			count_wrong_order[len(count)] = page
		}
		middle_wrong += count_wrong_order[(len(wrong_print)-1)/2]
	}
	fmt.Printf("Task 2: %d\n", middle_wrong)
}
