package main

import (
	"bufio"
	"fmt"
	"maps"
	"math"
	"os"
	"slices"
	"strings"
)

type Point struct {
	X, Y, Z int
}

type DistanceTracker struct {
	P1, P2   int
	Distance float64
}

func distanceQueue(junctionBoxes []Point) []DistanceTracker {
	var distance []DistanceTracker
	for i, p1 := range junctionBoxes {
		for j, p2 := range junctionBoxes[i+1:] {
			j = j + (i + 1)
			diffX := float64(p1.X - p2.X)
			diffY := float64(p1.Y - p2.Y)
			diffZ := float64(p1.Z - p2.Z)
			dist := math.Sqrt(math.Pow(diffX, 2) + math.Pow(diffY, 2) + math.Pow(diffZ, 2))
			distance = append(distance, DistanceTracker{
				P1:       i,
				P2:       j,
				Distance: dist,
			})
		}
	}
	slices.SortFunc(distance, func(d1, d2 DistanceTracker) int {
		if d1.Distance < d2.Distance {
			return -1
		} else if d1.Distance > d2.Distance {
			return 1
		}
		return 0
	})
	return distance
}

func hierarchicalClustering(junctionBoxes []Point, maxConnections int) int {
	closestQueue := distanceQueue(junctionBoxes)

	clusters := map[int]map[int]struct{}{}
	for i := range len(junctionBoxes) {
		clusters[i] = map[int]struct{}{
			i: struct{}{},
		}
	}
	for _, closest := range closestQueue[:maxConnections] {
		// check if points are already together
		if cluster, ok := clusters[closest.P1]; ok {
			if _, ok := cluster[closest.P2]; ok {
				continue
			}
		}
		// join them
		cluster1, ok := clusters[closest.P1]
		if !ok {
			cluster1 = map[int]struct{}{}
		}
		cluster2, ok := clusters[closest.P2]
		if !ok {
			cluster2 = map[int]struct{}{}
		}

		merged := make(map[int]struct{})
		for p := range cluster1 {
			merged[p] = struct{}{}
		}
		for p := range cluster2 {
			merged[p] = struct{}{}
		}

		for p := range merged {
			clusters[p] = merged
		}
	}
	// get cluster sizes
	var clusterSizes []int
	visited := map[int]bool{}
	for _, cluster := range clusters {
		currentSlice := slices.Collect(maps.Keys(cluster))
		accountedFor := false
		for _, v := range currentSlice {
			if visited[v] {
				accountedFor = true
				break
			}
		}
		if accountedFor {
			continue
		}
		clusterSizes = append(clusterSizes, len(currentSlice))
		for _, v := range currentSlice {
			visited[v] = true
		}
	}

	slices.SortFunc(clusterSizes, func(a, b int) int {
		if a > b {
			return -1
		} else if a < b {
			return 1
		}
		return 0
	})

	threeLargestSize := 1
	for _, size := range clusterSizes[:3] {
		threeLargestSize *= size
	}
	return threeLargestSize
}

func hierarchicalClusteringFinal(junctionBoxes []Point) int {
	closestQueue := distanceQueue(junctionBoxes)

	clusters := map[int]map[int]struct{}{}
	for i := range len(junctionBoxes) {
		clusters[i] = map[int]struct{}{
			i: struct{}{},
		}
	}
	for _, closest := range closestQueue {
		// check if points are already together
		if cluster, ok := clusters[closest.P1]; ok {
			if _, ok := cluster[closest.P2]; ok {
				continue
			}
		}
		// join them
		cluster1, ok := clusters[closest.P1]
		if !ok {
			cluster1 = map[int]struct{}{}
		}
		cluster2, ok := clusters[closest.P2]
		if !ok {
			cluster2 = map[int]struct{}{}
		}

		merged := make(map[int]struct{})
		for p := range cluster1 {
			merged[p] = struct{}{}
		}
		for p := range cluster2 {
			merged[p] = struct{}{}
		}

		if len(merged) == len(junctionBoxes) {
			return junctionBoxes[closest.P1].X * junctionBoxes[closest.P2].X
		}

		for p := range merged {
			clusters[p] = merged
		}
	}
	return 0
}

func Day08() {
	file, err := os.Open("08.in")
	if err != nil {
		return
	}
	defer file.Close()
	fmt.Println("--- Day 8: Playground ---")

	var junctionBoxes []Point
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		splitRow := strings.Split(row, ",")
		if len(splitRow) != 3 {
			panic("len(splitRow) != 3")
		}
		x := StringToInt(splitRow[0])
		y := StringToInt(splitRow[1])
		z := StringToInt(splitRow[2])
		junctionBoxes = append(junctionBoxes, Point{X: x, Y: y, Z: z})
	}

	groups := hierarchicalClustering(junctionBoxes, 1000)
	fmt.Printf("Task 1: %d\n", groups)

	size := hierarchicalClusteringFinal(junctionBoxes)
	fmt.Printf("Task 2: %d\n", size)
}
