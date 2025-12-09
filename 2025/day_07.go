package main

import (
	"bufio"
	"fmt"
	"os"
)

func tachyonBeamTotalSplits(tachyonManifold []string) int {
	beam := make([]bool, len(tachyonManifold[0]))
	for i, c := range tachyonManifold[0] {
		if c == 'S' {
			beam[i] = true
		}
	}

	splitCount := 0
	for _, row := range tachyonManifold {
		nextBeam := make([]bool, len(row))
		for i, b := range beam {
			if !b {
				continue
			}
			if row[i] == '^' {
				splitCount += 1
				if i+1 < len(row) {
					nextBeam[i+1] = true
				}
				if i-1 >= 0 {
					nextBeam[i-1] = true
				}
			} else {
				nextBeam[i] = true
			}
		}
		copy(beam, nextBeam)
	}
	return splitCount
}

func tachyonBeamQuantumSplits(tachyonManifold []string) int {
	beam := make([]int, len(tachyonManifold[0]))
	for i, c := range tachyonManifold[0] {
		if c == 'S' {
			beam[i] = 1
		}
	}

	for _, row := range tachyonManifold {
		nextBeam := make([]int, len(row))
		for i, b := range beam {
			if b == 0 {
				continue
			}
			if row[i] == '^' {
				if i+1 < len(row) {
					nextBeam[i+1] += b
				}
				if i-1 >= 0 {
					nextBeam[i-1] += b
				}
			} else {
				nextBeam[i] += b
			}
		}
		copy(beam, nextBeam)
	}
	splitCount := 0
	for _, b := range beam {
		splitCount += b
	}
	return splitCount
}

func Day07() {
	file, err := os.Open("day_07.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 7: Laboratories ---")

	var tachyonManifold []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		tachyonManifold = append(tachyonManifold, row)
	}

	splitCount := tachyonBeamTotalSplits(tachyonManifold)
	fmt.Printf("Task 1: %d\n", splitCount)

	splitCount = tachyonBeamQuantumSplits(tachyonManifold)
	fmt.Printf("Task 2: %d\n", splitCount)
}
