package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func (ir1 Range) SumInvalidIDsRepeated() int {
	// round start up
	startString := fmt.Sprint(ir1.Start)
	start := ir1.Start
	if len(startString)%2 == 1 {
		start = int(math.Pow10(len(startString)))
	}
	// round end down
	endString := fmt.Sprint(ir1.End)
	end := ir1.End
	if len(endString)%2 == 1 {
		end = int(math.Pow10(len(endString)-1)) - 1
	}
	if end < start {
		return 0
	}

	// get first half digits of start and end
	startDigits := fmt.Sprint(start)
	startDigits = startDigits[:len(startDigits)/2]
	startInt := StringToInt(startDigits)
	endDigits := fmt.Sprint(end)
	endDigits = endDigits[:len(endDigits)/2]
	endInt := StringToInt(endDigits)

	invalidSum := 0
	for i := startInt; i <= endInt; i++ {
		doubleI := StringToInt(fmt.Sprintf("%d%d", i, i))
		if doubleI >= start && doubleI <= end {
			invalidSum += doubleI
		}
	}
	return invalidSum
}

func (ir1 Range) splitRange() []Range {
	startDigits := fmt.Sprint(ir1.Start)
	endDigits := fmt.Sprint(ir1.End)
	if len(startDigits) == len(endDigits) {
		return []Range{ir1}
	}
	if len(endDigits)-len(startDigits) == 1 {
		return []Range{
			{Start: ir1.Start, End: int(math.Pow10(len(startDigits))) - 1},
			{Start: int(math.Pow10(len(startDigits))), End: ir1.End},
		}
	}
	panic("difference too large")
}

func (ir1 Range) SumInvalidIDsMultiple() int {
	invalidIDs := map[int]struct{}{}
	rangeLen := len(fmt.Sprint(ir1.Start))
	for i := 1; i < rangeLen; i++ {
		if rangeLen%i != 0 { // not a divisor
			continue
		}
		subpatternLen := rangeLen / i

		// construct first digit of length i
		numberStr := fmt.Sprint(ir1.Start)[:i] //fmt.Sprint(math.Pow10(i - 1))
		number := StringToInt(numberStr)
		for {
			numberStr = fmt.Sprint(number)
			// repeat the number subpatternLen times
			if len(numberStr) > i {
				break
			}
			multipleStr := strings.Repeat(numberStr, subpatternLen)
			multiple := StringToInt(multipleStr)
			if ir1.Start <= multiple && multiple <= ir1.End {
				invalidIDs[multiple] = struct{}{}
			}
			if multiple > ir1.End {
				break
			}
			number += 1
		}

	}
	invalidIDSum := 0
	for invalidID := range invalidIDs {
		invalidIDSum += invalidID
	}
	return invalidIDSum
}

func Day02() {
	file, err := os.Open("02.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 2: Gift Shop ---")

	var idRanges []Range
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	inputData := scanner.Text()
	productRanges := strings.Split(inputData, ",")
	for _, productRange := range productRanges {
		startEndRanges := strings.Split(productRange, "-")
		if len(startEndRanges) != 2 {
			panic(fmt.Sprintf("%d != 2", len(startEndRanges)))
		}
		start := StringToInt(startEndRanges[0])
		end := StringToInt(startEndRanges[1])
		idRanges = append(idRanges, Range{
			Start: start,
			End:   end,
		})
	}

	invalidIDs := 0
	for _, ir := range idRanges {
		invalidCount := ir.SumInvalidIDsRepeated()
		invalidIDs += invalidCount
	}
	fmt.Printf("Task 1: %d\n", invalidIDs)

	var splitIdRanges []Range
	for _, ir := range idRanges {
		split := ir.splitRange()
		splitIdRanges = append(splitIdRanges, split...)
	}
	invalidIDs = 0
	for _, ir := range splitIdRanges {
		invalidCount := ir.SumInvalidIDsMultiple()
		invalidIDs += invalidCount
	}
	fmt.Printf("Task 2: %d\n", invalidIDs)
}
