package main

import (
	"bufio"
	"fmt"
	"os"
)

type dial struct {
	Right bool
	Count int
}

func Day01() {
	file, err := os.Open("01.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 1: Secret Entrance ---")

	var dialMovements []dial
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		right := row[0] == 'R'
		count := StringToInt(row[1:])
		dialMovements = append(dialMovements, dial{
			Right: right,
			Count: count,
		})
	}

	dialPosition := 50
	dialAtZero := 0
	for _, movement := range dialMovements {
		if movement.Right {
			dialPosition += movement.Count
			for dialPosition > 99 {
				dialPosition -= 100
			}
		} else {
			dialPosition -= movement.Count
			for dialPosition < 0 {
				dialPosition += 100
			}
		}
		if dialPosition == 0 {
			dialAtZero += 1
		}
	}
	fmt.Printf("Task 1: %d\n", dialAtZero)

	dialPosition = 50
	dialAtZero = 0
	for _, movement := range dialMovements {
		if movement.Right {
			for range movement.Count {
				dialPosition += 1
				if dialPosition == 100 {
					dialPosition = 0
					dialAtZero += 1
				}
			}
		} else {
			for range movement.Count {
				dialPosition -= 1
				if dialPosition == 0 {
					dialAtZero += 1
				}
				if dialPosition == -1 {
					dialPosition = 99
				}
			}
		}
	}
	fmt.Printf("Task 2: %d\n", dialAtZero)
}
