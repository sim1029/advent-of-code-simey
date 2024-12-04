package main

import (
    "bufio"
    "fmt"
    "os"
	"strings"
	"strconv"
	"sort"
	"math"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

	var left []int
	var right []int
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
		fields := strings.Fields(line)
		leftInt, _ := strconv.Atoi(fields[0])
		rightInt, _ := strconv.Atoi(fields[1])
		left = append(left, leftInt)
		right = append(right, rightInt)
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file:", err)
    }

	sort.Ints(left)
	sort.Ints(right)

	totalDiff := 0
    for i := 0; i < len(left); i++ {
        totalDiff += int(math.Abs(float64(left[i] - right[i])))
    }

	rightCount := make(map[int]int)
	for _, num := range right {
		rightCount[num]++
	}

	totalSim := 0
	for _, num := range left {
		totalSim += num * rightCount[num]
	}

	fmt.Println(totalDiff)
	fmt.Println(totalSim)
}