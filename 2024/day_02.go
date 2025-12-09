package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func Day02() {
	file, err := os.Open("day_02.in")
	if err != nil {
		return
	}
	defer file.Close()
	fmt.Println("--- Day 2: Red-Nosed Reports ---")

	var reports_raw []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		reports_raw = append(reports_raw, scanner.Text())
	}

	var reports [][]int
	for i, line := range reports_raw {
		values := strings.Fields(line)
		reports = append(reports, []int{})
		for _, value := range values {
			num := StringToInt(value)
			reports[i] = append(reports[i], num)
		}
	}

	// Task 1
	count1 := CountSafe(reports)
	fmt.Printf("Task 1: %d\n", count1)

	// Task 2
	count2 := CountSafeWithTolerance(reports)
	fmt.Printf("Task 2: %d\n", count2)
}

func CountSafeWithTolerance(reports [][]int) int {
	var count int
	for _, report := range reports {

		for i := 0; i < len(report); i += 1 {
			copy_report := make([]int, len(report))
			copy(copy_report, report)
			new_report := append(copy_report[:i], copy_report[i+1:]...)
			if IsSafe(new_report) {
				count += 1
				break
			}
		}
	}
	return count
}

func CountSafe(reports [][]int) int {
	var count int
	for _, report := range reports {
		//fmt.Println(report)
		if IsSafe(report) {
			//fmt.Println("safe")
			count += 1
		}
	}
	return count
}

func IsSafe(values []int) bool {
	if len(values) < 2 {
		return true
	}

	var increasing bool
	if values[0] < values[1] {
		increasing = true
	}

	prev_value := values[0]
	i := 0
	for i < len(values)-1 {
		i += 1
		next_value := values[i]
		// check increasing/decreasing
		if increasing {
			if prev_value >= next_value {
				return false
			}
		} else {
			if prev_value <= next_value {
				return false
			}
		}

		// check difference
		if diff := math.Abs(float64(prev_value - next_value)); (1 > diff) || (diff > 3) {
			return false
		}

		prev_value = next_value
	}

	return true
}
