package main

import (
	"bufio"
	"fmt"
	"os"
)

func splitMultipleSpaces(text string) []string {
	var split []string
	trackingString := false
	startIdx := 0
	for i, c := range text {
		if trackingString && c == ' ' {
			split = append(split, text[startIdx:i])
			trackingString = false
		}
		if !trackingString && c != ' ' {
			startIdx = i
			trackingString = true
		}
	}
	if trackingString {
		split = append(split, text[startIdx:])
	}
	return split
}

func Day06() {
	file, err := os.Open("06.in")
	if err != nil {
		return
	}
	defer file.Close()
	fmt.Println("--- Day 6: Trash Compactor ---")

	numberTable := [][]int{}
	var operators []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var tableRow []int
		row := scanner.Text()
		splitRow := splitMultipleSpaces(row)
		isNumber := true
		for _, element := range splitRow {
			if element == "+" || element == "*" {
				isNumber = false
				operators = append(operators, element)
			} else {
				number := StringToInt(element)
				tableRow = append(tableRow, number)
			}
		}
		if isNumber {
			numberTable = append(numberTable, tableRow)
		}
	}

	grandTotal := 0
	for i := range len(operators) {
		operator := operators[i]
		var solution int
		switch operator {
		case "+":
			solution = 0
			for _, num := range numberTable {
				solution += num[i]
			}
		case "*":
			solution = 1
			for _, num := range numberTable {
				solution *= num[i]
			}
		}
		grandTotal += solution
	}
	fmt.Printf("Task 1: %d\n", grandTotal)

	file.Seek(0, 0)
	scanner = bufio.NewScanner(file)
	var table []string
	for scanner.Scan() {
		row := scanner.Text()
		table = append(table, row)
	}

	grandTotal = 0
	sign := "+"
	temporary := 0
	currentNumber := 0
	for j := range len(table[0]) {
		allEmpty := true
		for i := range len(table) {
			c := table[i][j]
			if c == '+' || c == '*' {
				sign = string(c)
				allEmpty = false
			} else if c != ' ' {
				value := StringToInt(string(c))
				currentNumber = 10*currentNumber + value
				allEmpty = false
			}
		}
		if allEmpty {
			grandTotal += temporary
			temporary = 0
		} else if temporary == 0 {
			temporary = currentNumber
		} else {
			switch sign {
			case "+":
				temporary += currentNumber
			case "*":
				temporary *= currentNumber
			}
		}
		currentNumber = 0
	}
	grandTotal += temporary
	fmt.Printf("Task 2: %d\n", grandTotal)
}
