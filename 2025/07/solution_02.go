package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

/*
Goal: Find how many paths the beam could take.

Test input solution: The beam could take 40 different paths.
*/

/* Currently trying to brute force it using solution 1 but removing sorting and deduplication.
Need to use more efficient algorithm. Recursive function/tree traversal? */

func main() {
	num_paths := 1           // count number of splits, but this time, don't deduplicate the beam positions
	var beam_positions []int // current beam positions

	// Open File
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	// create a scanner to read the input file line by line
	scanner := bufio.NewScanner(file)

	line_num := 0
	for scanner.Scan() {
		var new_beam_positions []int
		line := string(scanner.Text())
		if line_num == 0 { // find start_position
			for i, char := range line {
				if string(char) == "S" {
					new_beam_positions = append(new_beam_positions, i)
				}
			}
		} else { // identify splitters and get new position of beam(s)
			for _, beam_pos := range beam_positions { // check each of the beams
				if string(line[beam_pos]) == "^" { // beam has hit a splitter
					new_beam_positions = append(new_beam_positions, beam_pos-1)
					new_beam_positions = append(new_beam_positions, beam_pos+1)
					num_paths += 1
				} else { // there's no splitter. Beam stays in same position
					new_beam_positions = append(new_beam_positions, beam_pos)
				}
			}
		}
		// Sort the list of beams (don't remove duplicates this time)
		// slices.Sort(new_beam_positions)
		// new_beam_positions = slices.Compact(new_beam_positions)

		beam_positions = new_beam_positions
		line_num += 1
		// fmt.Println("Current beam positions:", beam_positions)
	}

	fmt.Println("Number of splits:", num_paths)
}
