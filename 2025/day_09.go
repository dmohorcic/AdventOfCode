package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func maxArea(coords []Point) int {
	var maxArea float64
	for i, c1 := range coords {
		for _, c2 := range coords[i+1:] {
			area := math.Abs(float64(c1.X-c2.X+1)) * math.Abs(float64(c1.Y-c2.Y+1))
			if area > maxArea {
				maxArea = area
			}
		}
	}
	return int(maxArea)
}

func Day09() {
	file, err := os.Open("day_09.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 9: Movie Theater ---")

	var coords []Point
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		splitRow := strings.Split(row, ",")
		if len(splitRow) != 2 {
			panic("len(splitRow) != 2")
		}
		x := StringToInt(splitRow[0])
		y := StringToInt(splitRow[1])
		coords = append(coords, Point{X: x, Y: y})
	}

	area := maxArea(coords)
	fmt.Printf("Task 1: %d\n", area)
}
