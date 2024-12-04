package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    content, err := io.ReadAll(file)
    if err != nil {
        fmt.Println("Error reading file:", err)
        return
    }

    total := parseMul(string(content))
	fmt.Println(total)
}

func parseMul(line string) int {
    total := 0
	re := regexp.MustCompile(`(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))`)
	matches := re.FindAllString(line, -1)

	enabled := 1
	for _, match := range matches {
		// Match is do()
		if match == "do()" {
			enabled = 1
		}
		// Match is don't()
		if match == "don't()" {
			enabled = 0
		}
		// Match is a mul
		if match != "do()" && match != "don't()" {
			nums := regexp.MustCompile(`\d+`).FindAllString(match, -1)
			num1, _ := strconv.Atoi(nums[0])
			num2, _ := strconv.Atoi(nums[1])
			if enabled == 1 {
				total += num1 * num2
			}
		}
	}
    return total
}