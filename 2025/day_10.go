package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"os/exec"
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

func (m Machine) FewestButtonPressesJoltage(z3 *Z3Proc) int {
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
	smt2String := createSMT2(A, b)
	minimum := z3.Call(smt2String)
	return minimum
}

func createSMT2(A [][]int, b []int) string {
	m := len(A)
	n := len(A[0])

	smt2String := "(set-logic QF_LIA)\n"

	// variables
	for j := 0; j < n; j++ {
		smt2String = fmt.Sprintf("%s(declare-fun x%d () Int)\n", smt2String, j)
		smt2String = fmt.Sprintf("%s(assert (>= x%d 0))\n", smt2String, j)
	}

	// Ax = b constraints
	for i := 0; i < m; i++ {
		smt2String = fmt.Sprintf("%s(assert (= (+", smt2String)
		for j := 0; j < n; j++ {
			if A[i][j] != 0 {
				smt2String = fmt.Sprintf("%s x%d", smt2String, j)
			}
		}
		smt2String = fmt.Sprintf("%s) %d))\n", smt2String, b[i])
	}

	// objectives
	smt2String = fmt.Sprintf("%s(minimize (+", smt2String)
	for j := 0; j < n; j++ {
		smt2String = fmt.Sprintf("%s x%d", smt2String, j)
	}
	smt2String = fmt.Sprintf("%s))\n(check-sat)\n(get-model)\n(get-objectives)\n", smt2String)

	return smt2String
}

func CheckDockerRunning() bool {
	cmd := exec.Command("docker", "info")
	err := cmd.Run()
	return err == nil
}

type Z3Proc struct {
	cmd    *exec.Cmd
	stdin  io.WriteCloser
	stdout io.ReadCloser
	reader *bufio.Reader
}

func InitZ3() *Z3Proc {
	cmd := exec.Command(
		"docker", "run", "--rm", "-i",
		"ghcr.io/z3prover/z3:ubuntu-20.04-bare-z3-sha-d66609e",
		"-in", "-smt2",
	)
	stdin, err := cmd.StdinPipe()
	if err != nil {
		panic(fmt.Sprintf("failed to open stdin: %v", err))
	}
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(fmt.Sprintf("failed to open stdout: %v", err))
	}
	if err := cmd.Start(); err != nil {
		panic(fmt.Sprintf("failed to start docker/z3: %v", err))
	}

	proc := &Z3Proc{
		cmd:    cmd,
		stdin:  stdin,
		stdout: stdout,
		reader: bufio.NewReader(stdout),
	}

	return proc
}

func (p *Z3Proc) Call(smt2String string) int {
	wrapped := fmt.Sprintf("(push 1)\n%s(echo \"__END__\")\n(pop 1)\n", smt2String)

	if _, err := p.stdin.Write([]byte(wrapped)); err != nil {
		panic(fmt.Sprintf("failed to write SMT to Z3: %v", err))
	}

	// read until "__END__"
	var sb strings.Builder
	for {
		line, err := p.reader.ReadString('\n')
		if err != nil {
			panic(fmt.Sprintf("failed reading Z3 output: %v", err))
		}
		if strings.Contains(line, "__END__") {
			break
		}
		sb.WriteString(line)
	}

	output := sb.String()
	solution := -1
	foundSolutionRow := false
	for _, row := range strings.Split(output, "\n") {
		if foundSolutionRow {
			//  ((+ x0 x1 ... xi) solution)
			splitRow := strings.Split(row, " ")
			solutionString := splitRow[len(splitRow)-1]                    // get "solution)"
			solution = StringToInt(solutionString[:len(solutionString)-1]) // remove last ")"
			break
		}
		if strings.Contains(row, "objectives") {
			foundSolutionRow = true
		}
	}
	return solution
}

func (p *Z3Proc) Close() {
	p.stdin.Close()
	if err := p.cmd.Process.Kill(); err != nil {
		panic(fmt.Sprintf("failed killing Z3 process: %v", err))
	}
	_, _ = p.cmd.Process.Wait()
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

	if !CheckDockerRunning() {
		return
	}
	z3 := InitZ3()
	totalButtonPresses = 0
	for _, machine := range machines {
		buttonPresses := machine.FewestButtonPressesJoltage(z3)
		totalButtonPresses += buttonPresses
	}
	z3.Close()
	fmt.Printf("Task 2: %d\n", totalButtonPresses)
}
