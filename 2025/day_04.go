package main

import (
	"bufio"
	"fmt"
	"os"
)

type position struct {
	x int
	y int
}

var directions = []position{
	{-1, -1},
	{-1, 0},
	{-1, 1},
	{0, 1},
	{1, 1},
	{1, 0},
	{1, -1},
	{0, -1},
}

func findRemovablePaperRolls(paperGrid [][]bool) []position {
	var accessiblePaperRolls []position
	for i, paperRow := range paperGrid {
		for j, cell := range paperRow {
			if !cell {
				continue
			}
			adjecentCount := 0
			for _, d := range directions {
				k := i + d.x
				if k < 0 || k >= len(paperGrid) {
					continue
				}
				l := j + d.y
				if l < 0 || l >= len(paperRow) {
					continue
				}
				if paperGrid[k][l] {
					adjecentCount++
				}
				if adjecentCount >= 4 {
					break
				}
			}
			if adjecentCount < 4 {
				accessiblePaperRolls = append(accessiblePaperRolls, position{i, j})
			}
		}
	}
	return accessiblePaperRolls
}

func removePaperRolls(paperGrid [][]bool, removable []position) [][]bool {
	for _, r := range removable {
		paperGrid[r.x][r.y] = false
	}
	return paperGrid
}

func Day04() {
	file, err := os.Open("day_04.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 4: Printing Department ---")

	var paperGrid [][]bool
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		var paperRow []bool
		for _, c := range row {
			switch c {
			case '.':
				paperRow = append(paperRow, false)
			case '@':
				paperRow = append(paperRow, true)
			}
		}
		paperGrid = append(paperGrid, paperRow)
	}

	removablePaperRolls := findRemovablePaperRolls(paperGrid)
	fmt.Printf("Task 1: %d\n", len(removablePaperRolls))

	var removedPaperRolls []position
	for len(removablePaperRolls) > 0 {
		removedPaperRolls = append(removedPaperRolls, removablePaperRolls...)
		paperGrid = removePaperRolls(paperGrid, removablePaperRolls)
		removablePaperRolls = findRemovablePaperRolls(paperGrid)
	}
	fmt.Printf("Task 2: %d\n", len(removedPaperRolls))
}
