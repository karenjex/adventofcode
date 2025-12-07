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

The problems are written right-to-left in columns.
Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom.

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544

Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.
*/

func reverse(str string) (result string) {
	// get string in reverse order, character by character
	for _, v := range str {
		result = string(v) + result
	}
	return
}

func solve_problem(numbers []string, operator string) (result int) {
	if first_num, err := strconv.Atoi(strings.TrimSpace(numbers[0])); err != nil {
		fmt.Println(err)
		log.Fatalf("Error converting first number: ", err)
	} else {
		result = first_num
	}
	for i := 1; i < len(numbers); i++ { // add or multiply 2nd and subsequent numbers, depending on operator
		num := strings.TrimSpace(numbers[i])
		if operator == "+" {
			if next_num, err := strconv.Atoi(num); err != nil {
				fmt.Println(err)
				log.Fatalf("Error converting number: ", err)
			} else {
				result += next_num
			}
		} else if operator == "*" {
			if next_num, err := strconv.Atoi(num); err != nil {
				fmt.Println(err)
				log.Fatalf("Error converting number: ", err)
			} else {
				result = result * next_num
			}
		}
	}
	return
}

func main() {
	grand_total := 0

	type problem_type struct {
		Start_pos int      // position of first character of the problem
		End_pos   int      // position of final character of the problem
		Numbers   []string //  list of numbers to be added or multiplied - store as strings to make it easier to generate
		Operator  string   // "+" or "*" character representing operator
	}

	var problem_list []problem_type

	// Open File
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	// create a scanner to read the input file line by line
	scanner := bufio.NewScanner(file)

	var input_lines []string // get the input lines, reversed character by character, as an array.
	for scanner.Scan() {
		input_lines = append(input_lines, reverse(string(scanner.Text())))
	}

	// This time, the final line holds the key;
	// going from right to left (of the original line), a final line that contains a "+" or "*" indicates the end of a problem.
	final_line := input_lines[len(input_lines)-1]
	//iterate through chars in final_line to get start/end position of each problem and its operator.
	problem_num := 0
	var problem problem_type
	problem.Start_pos = 0 // the first problem starts at position 0
	problem_list = append(problem_list, problem)
	for i, char := range final_line {
		if (string(char) == "+") || (string(char) == "*") { // we're at the end of the current problem
			problem_list[problem_num].End_pos = i             // Record the end position for the problem
			problem_list[problem_num].Operator = string(char) // Record the operator
			if i < len(final_line)-1 {                        // if there are more characters to process, i.e. more problems to add
				var next_problem problem_type                     // create a var to store info about the next problem
				next_problem.Start_pos = i + 2                    // record its starting position (after the following space)
				problem_list = append(problem_list, next_problem) // add it to the list of problems
				problem_num += 1
			}
		}
	}

	// fmt.Println("Problems:", problem_list)

	for i, line := range input_lines {
		if i < len(input_lines)-1 { // process all lines other than the final line
			// fmt.Println(line)
			for pb, problem := range problem_list { // loop through list of problems and get numbers associated with each
				// fmt.Println("problem ", pb, "start:", problem.Start_pos, "end:", problem.End_pos)
				var problem_numbers []string
				if i > 0 { // this is not the first line, get the existing problem_numbers array
					problem_numbers = problem_list[pb].Numbers
				}
				problem_number_id := 0
				for pos := problem.Start_pos; pos <= problem.End_pos; pos++ {
					if i == 0 { // this is the first line, append val to problem_numbers array
						problem_numbers = append(problem_numbers, string(line[pos]))
					} else { // use string addition to add value to the string already in problem_number_id position
						problem_numbers[problem_number_id] = problem_numbers[problem_number_id] + string(line[pos])
					}
					problem_number_id += 1
				}
				problem_list[pb].Numbers = problem_numbers
			}
		}
	}
	// fmt.Println("Problem list:", problem_list)

	for _, problem := range problem_list {
		grand_total += solve_problem(problem.Numbers, problem.Operator)
	}
	fmt.Println("Grand Total:", grand_total)
}
