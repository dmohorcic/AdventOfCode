package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Node struct {
	Next      []string
	Prev      []string
	Score     int
	Evaluated bool
}

type Nodes map[string]Node

func (n *Node) Evaluate(nodes Nodes) {
	if n.Evaluated {
		return
	}
	for _, nodeId := range n.Prev {
		prevNode := nodes[nodeId]
		prevNode.Evaluate(nodes)
		n.Score += prevNode.Score
		nodes[nodeId] = prevNode
	}
	n.Evaluated = true
}

func (ns Nodes) Reset() {
	for nodeId, node := range ns {
		node.Score = 0
		node.Evaluated = false
		ns[nodeId] = node
	}
}

func (ns Nodes) Set(nodeId string, score int) {
	node := ns[nodeId]
	node.Score = score
	ns[nodeId] = node
}

func (ns Nodes) Get(nodeId string) int {
	node := ns[nodeId]
	return node.Score
}

func (ns Nodes) Evaluate() {
	for nodeId, node := range ns {
		node.Evaluate(ns)
		ns[nodeId] = node
	}
}

func Day11() {
	file, err := os.Open("day_11.in")
	if err != nil {
		return
	}
	defer file.Close()

	fmt.Println("--- Day 11: Reactor ---")

	nodes := Nodes{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := scanner.Text()
		splitRow := strings.Split(row, ": ")
		if len(splitRow) != 2 {
			panic("len(splitRow) != 2")
		}
		nodeString := splitRow[0]
		nextNodesRaw := strings.Split(splitRow[1], " ")
		node, ok := nodes[nodeString]
		if !ok {
			node = Node{
				Prev: []string{},
				Next: []string{},
			}
		}
		for _, nextNodeString := range nextNodesRaw {
			node.Next = append(node.Next, nextNodeString)
			nextNode, ok := nodes[nextNodeString]
			if !ok {
				nextNode = Node{
					Prev: []string{},
					Next: []string{},
				}
			}
			nextNode.Prev = append(nextNode.Prev, nodeString)
			nodes[nextNodeString] = nextNode
		}
		nodes[nodeString] = node
	}

	nodes.Set("you", 1)
	nodes.Evaluate()
	fmt.Printf("Task 1: %d\n", nodes.Get("out"))

	nodes.Reset()
	nodes.Set("svr", 1)
	nodes.Evaluate()
	// svr to fft and dac
	svrToFft := nodes.Get("fft")
	svrToDac := nodes.Get("fft")
	// fft to dac
	nodes.Reset()
	nodes.Set("fft", 1)
	nodes.Evaluate()
	fftToDac := nodes.Get("dac")
	// dac to fft
	nodes.Reset()
	nodes.Set("dac", 1)
	nodes.Evaluate()
	dacToFft := nodes.Get("fft")
	// one of fftToDac and dacToFft must be zero
	score := 0
	if fftToDac == 0 {
		nodes.Reset()
		nodes.Set("fft", 1)
		nodes.Evaluate()
		fftToOut := nodes.Get("out")
		score = svrToDac * dacToFft * fftToOut
	} else if dacToFft == 0 {
		nodes.Reset()
		nodes.Set("dac", 1)
		nodes.Evaluate()
		dacToOut := nodes.Get("out")
		score = svrToFft * fftToDac * dacToOut
	} else {
		panic("fftToDac != 0 and dacToFft != 0")
	}
	fmt.Printf("Task 2: %d\n", score)
}
