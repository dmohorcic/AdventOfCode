package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func (ir1 Range) HasIntersection(ir2 Range) bool {
	return ir1.Start <= ir2.End && ir2.Start <= ir1.End
}

func (ir1 Range) Merge(ir2 Range) Range {
	start := ir1.Start
	if ir2.Start < start {
		start = ir2.Start
	}
	end := ir1.End
	if ir2.End > end {
		end = ir2.End
	}
	return Range{
		Start: start,
		End:   end,
	}
}

func Day05() {
	file, err := os.Open("day_05.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 5: Cafeteria ---")

	var ingredientIdRanges []Range
	var ingredientIds []int
	scanningRanges := true
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		if row == "" {
			scanningRanges = false
			continue
		}
		if scanningRanges {
			splitRow := strings.Split(row, "-")
			if len(splitRow) != 2 {
				panic("splitRow != 2")
			}
			ingredientIdRanges = append(ingredientIdRanges, Range{
				Start: StringToInt(splitRow[0]),
				End:   StringToInt(splitRow[1]),
			})
		} else {
			ingredientIds = append(ingredientIds, StringToInt(row))
		}
	}

	freshIngredients := 0
	for _, id := range ingredientIds {
		for _, ir := range ingredientIdRanges {
			if ir.Start <= id && id <= ir.End {
				freshIngredients += 1
				break
			}
		}
	}
	fmt.Printf("Task 1: %d\n", freshIngredients)

	// merge ranges
	var newRange Range
	merged := true
	for merged {
		merged = false
		var idx1, idx2 int
		for i, ir1 := range ingredientIdRanges {
			for j, ir2 := range ingredientIdRanges[i+1:] {
				if ir1.HasIntersection(ir2) {
					newRange = ir1.Merge(ir2)
					merged = true
					idx1 = i
					idx2 = j + i + 1
					break
				}
			}
			if merged {
				break
			}
		}
		if merged {
			// remove both indexes
			if idx2+1 == len(ingredientIdRanges) {
				ingredientIdRanges = ingredientIdRanges[:idx2]
			} else {
				ingredientIdRanges = append(ingredientIdRanges[:idx2], ingredientIdRanges[idx2+1:]...)
			}
			if idx1+1 == len(ingredientIdRanges) {
				ingredientIdRanges = ingredientIdRanges[:idx1]
			} else {
				ingredientIdRanges = append(ingredientIdRanges[:idx1], ingredientIdRanges[idx1+1:]...)
			}
			ingredientIdRanges = append(ingredientIdRanges, newRange)
		}
	}

	freshIngredients = 0
	for _, ir := range ingredientIdRanges {
		freshIngredients += ir.End - ir.Start + 1
	}
	fmt.Printf("Task 2: %d\n", freshIngredients)
}
