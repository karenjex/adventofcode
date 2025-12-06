package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

/*
Goal: Return the grand total, found by adding together all of the answers to the individual problems.

The puzzle input consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.
Each problem's numbers are arranged vertically;
at the bottom of the problem is the symbol for the operation that needs to be performed.

Solution for test input: 33210 + 490 + 4243455 + 401 = 4277556.
*/

func solve_problem(input_line []string) int {
	problem_operator := input_line[len(input_line)-1]
	var running_total int
	if first_num, err := strconv.Atoi(input_line[0]); err != nil {
		fmt.Println(err)
		log.Fatalf("Error converting first number: ", err)
	} else {
		running_total = first_num
	}
	for i := 1; i < len(input_line)-1; i++ { // add or multiply 2nd and subsequent numbers, depending on operator
		if problem_operator == "+" {
			if next_num, err := strconv.Atoi(input_line[i]); err != nil {
				fmt.Println(err)
				log.Fatalf("Error converting number: ", err)
			} else {
				running_total += next_num
			}
		} else if problem_operator == "*" {
			if next_num, err := strconv.Atoi(input_line[i]); err != nil {
				fmt.Println(err)
				log.Fatalf("Error converting number: ", err)
			} else {
				running_total = running_total * next_num
			}
		}
	}
	return running_total
}

func main() {
	grand_total := 0

	// Open File
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	// create a scanner to read the input file line by line
	scanner := bufio.NewScanner(file)

	// Process file line by line to get problems
	var problem_list [][]string // Each element of problem_list is an array that contains the entries for a given problem.
	// For the test input: problem_list[0] = [123 45 6 *]
	//                     problem_list[1] = [328 64 98 +]
	//                     problem_list[2] = [51 387 215 *]
	//                     problem_list[3] = [64 23 314 +]]
	line_counter := 0
	for scanner.Scan() {
		input_line := string(scanner.Text())
		// split the input line into "words", each of which represents an element of a problem.
		input_line_words := strings.Fields(input_line) // split the input on white space
		if line_counter == 0 {                         // we're processing the first line. Create a new array for each word in the line - each represents a problem
			for _, word := range input_line_words {
				problem := []string{word}
				problem_list = append(problem_list, problem)
			}
		} else { // append each word to the relevant problem array
			for i, word := range input_line_words {
				// problem := []string{word}
				problem_list[i] = append(problem_list[i], word)
			}
		}
		line_counter += 1
	}

	for _, problem := range problem_list {
		grand_total += solve_problem(problem)
	}
	fmt.Println(problem_list)
	fmt.Println("Grand Total:", grand_total)
}
