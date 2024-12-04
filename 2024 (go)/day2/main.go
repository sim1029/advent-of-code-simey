package main

import (
    "bufio"
    "fmt"
    "os"
	"strings"
	"strconv"
	"math"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

	safeReports := 0
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
		level := strings.Fields(line)
		if areLevelsValid(level[1:], -1) || areLevelsValid(level, 0) || areLevelsValid(level[:len(level)-1], -1) {
			safeReports++
		} else {
			for i := 0; i < len(level)-1; i++ {
				if areLevelsValid(level, i) {
					safeReports++
					break
				}
			}
		}
    }
	fmt.Println(safeReports)
}

func areLevelsValid(level []string, skip_idx int) bool {
	prev, valid := 0, true
	for i :=0; i < len(level)-1; i++ {
		if i+1 == skip_idx{
			valid, prev = validLevels(level[i], level[i+2], prev)
			i++
		} else {
			valid, prev = validLevels(level[i], level[i+1], prev)
		}
		if !valid {
			return false
		}
	}
	// fmt.Println(level, skip_idx)
	return true
}

func validLevels(left string, right string, prev int) (bool, int) {
	curr_num, _ := strconv.Atoi(left)
	prev_num, _ := strconv.Atoi(right)
	diff := curr_num - prev_num
	return !((diff > 0 && prev < 0) || (diff < 0 && prev > 0) || int(math.Abs(float64(diff))) == 0 || int(math.Abs(float64(diff))) > 3), diff
}