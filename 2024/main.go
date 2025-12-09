package main

import "strconv"

func main() {
	Day01()
	Day02()
	Day03()
	Day04()
	Day05()
}

func StringToInt(str string) int {
	num, err := strconv.Atoi(str)
	if err != nil {
		panic(err)
	}
	return num
}
