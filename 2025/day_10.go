package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

type Machine struct {
	Lights  []bool
	Buttons [][]int
	Joltage []int
}

func (m Machine) FewestButtonPressesLights() int {
	lights := make([]bool, len(m.Lights))
	copy(lights, m.Lights)
	min := m.fewestButtonPressesLights(0, 0, lights)
	return min
}

func (m Machine) fewestButtonPressesLights(idx, currentPresses int, lights []bool) int {
	allZero := true
	for _, l := range lights {
		if l {
			allZero = false
			break
		}
	}
	if allZero {
		return currentPresses
	}
	if idx >= len(m.Buttons) {
		return math.MaxInt
	}
	// don't press current button
	min_no := m.fewestButtonPressesLights(idx+1, currentPresses, lights)
	// press current button
	pressedLights := make([]bool, len(lights))
	copy(pressedLights, lights)
	for _, b := range m.Buttons[idx] {
		pressedLights[b] = !pressedLights[b]
	}
	min_yes := m.fewestButtonPressesLights(idx+1, currentPresses+1, pressedLights)
	return int(math.Min(float64(min_yes), float64(min_no)))
}

func (m Machine) FewestButtonPressesJoltage() int {
	// Integer Linear Programming
	A := make([][]int, len(m.Joltage))
	for i := range len(m.Joltage) {
		A[i] = make([]int, len(m.Buttons))
	}
	for i, button := range m.Buttons {
		for _, b := range button {
			A[b][i] = 1
		}
	}
	b := make([]int, len(m.Joltage))
	copy(b, m.Joltage)
	// x := make([]int, len(m.Buttons))
	// min x such that Ax = b and x >= 0
	return -1
}

func Day10() {
	file, err := os.Open("day_10.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 10: Factory ---")

	var machines []Machine
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		splitRow := strings.Split(row, " ")
		if len(splitRow) < 2 {
			panic("len(splitRow) < 2")
		}
		lightsRaw := strings.ReplaceAll(strings.ReplaceAll(splitRow[0], "[", ""), "]", "")
		lights := make([]bool, len(lightsRaw))
		for i, c := range lightsRaw {
			lights[i] = c == '#'
		}
		var buttons [][]int
		for _, buttonRaw := range splitRow[1 : len(splitRow)-1] {
			buttonRaw = strings.ReplaceAll(strings.ReplaceAll(buttonRaw, "(", ""), ")", "")
			buttonLights := strings.Split(buttonRaw, ",")
			var button []int
			for _, bl := range buttonLights {
				b := StringToInt(bl)
				button = append(button, b)
			}
			buttons = append(buttons, button)
		}
		joltageRaw := strings.Split(strings.ReplaceAll(strings.ReplaceAll(splitRow[len(splitRow)-1], "{", ""), "}", ""), ",")
		var joltage []int
		for _, jr := range joltageRaw {
			j := StringToInt(jr)
			joltage = append(joltage, j)
		}

		machines = append(machines, Machine{
			Lights:  lights,
			Buttons: buttons,
			Joltage: joltage,
		})
	}

	totalButtonPresses := 0
	for _, machine := range machines {
		buttonPresses := machine.FewestButtonPressesLights()
		totalButtonPresses += buttonPresses
	}
	fmt.Printf("Task 1: %d\n", totalButtonPresses)

	totalButtonPresses = 0
	for _, machine := range machines {
		buttonPresses := machine.FewestButtonPressesJoltage()
		totalButtonPresses += buttonPresses
	}
	fmt.Printf("Task 2: %d\n", totalButtonPresses)
}
