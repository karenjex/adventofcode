package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
)

/*
Goal: Find how many times the beam will be split.

The beam enters at the location marked S.
The beam(s) always move downward.
They pass freely through empty space (.).
If a beam encounters a splitter (^), the beam is stopped,
and a new tachyon beam continues from the immediate left and from the immediate right of the splitter.

Test input solution: The beam is split a total of 21 times.
*/

func main() {
	num_splits := 0
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
					num_splits += 1
				} else { // there's no splitter. Beam stays in same position
					new_beam_positions = append(new_beam_positions, beam_pos)
				}
			}
		}
		// Sort the list of beams and remove duplicates
		slices.Sort(new_beam_positions)
		new_beam_positions = slices.Compact(new_beam_positions)

		beam_positions = new_beam_positions
		line_num += 1
		// fmt.Println("Current beam positions:", beam_positions)
	}

	fmt.Println("Number of splits:", num_splits)
}
