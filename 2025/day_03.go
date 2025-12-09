package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func largestSubset2(batteryArray []int) int {
	if len(batteryArray) < 2 {
		return 0
	}
	first := batteryArray[0]
	second := batteryArray[1]
	largest := 10*first + second
	for i := 2; i < len(batteryArray); i++ {
		potentialFirst := 10*first + batteryArray[i]
		potentialSecond := 10*second + batteryArray[i]
		if potentialFirst > potentialSecond {
			if potentialFirst > largest {
				largest = potentialFirst
				second = batteryArray[i]
			}
		} else {
			if potentialSecond > largest {
				largest = potentialSecond
				first = second
				second = batteryArray[i]
			}
		}
	}
	return largest
}

func largestSubsetN(batteryArray []int, n int) int {
	subnumber := 0
	start := 0
	for i := range n {
		end := len(batteryArray) - n + i
		maxDigit := 0
		maxIndex := 0
		for j := start; j < end+1; j++ {
			number := batteryArray[j]
			if number > maxDigit {
				maxDigit = number
				maxIndex = j
			}
		}
		subnumber = 10*subnumber + maxDigit
		start = maxIndex + 1
	}
	return subnumber
}

func Day03() {
	file, err := os.Open("day_03.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 3: Lobby ---")

	var batteries [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		digits := strings.Split(row, "")
		var batteryArray []int
		for _, d := range digits {
			i := StringToInt(d)
			batteryArray = append(batteryArray, i)
		}
		batteries = append(batteries, batteryArray)
	}

	voltage := 0
	for _, batteryArray := range batteries {
		subint := largestSubset2(batteryArray)
		voltage += subint
	}
	fmt.Printf("Task 1: %d\n", voltage)

	voltage = 0
	for _, batteryArray := range batteries {
		subint := largestSubsetN(batteryArray, 12)
		voltage += subint
	}
	fmt.Printf("Task 2: %d\n", voltage)
}
