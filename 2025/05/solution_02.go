package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

/*
Goal: Find the number of (unique) ingredient IDs that are considered to be fresh.
Solution for test input: 14
*/

func main() {
	fresh_ingredient_count := 0

	var ingredient_ranges []struct {
		From_id int
		To_id   int
	}

	// Open File and create a scanner to read the input file line by line
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	// Process file line by line to get ranges as array of (from,to) pairs
	collect_ranges := true
	for scanner.Scan() {
		input_line := string(scanner.Text())
		var ingredient_range struct {
			From_id int
			To_id   int
		}
		if input_line == "" { // we've reached the end of the ranges list. Don't bother collecting the rest
			collect_ranges = false
		} else if collect_ranges {
			from_id := strings.SplitN(input_line, "-", 2)[0] // split the input on "-" to get the 2 values
			to_id := strings.SplitN(input_line, "-", 2)[1]   // split the input on "-" to get the 2 values

			from_id_int, err := strconv.Atoi(from_id)
			if err != nil {
				fmt.Println(err)
				log.Fatalf("Error converting range from ID: ", err)
			}

			to_id_int, err := strconv.Atoi(to_id)
			if err != nil {
				fmt.Println(err)
				log.Fatalf("Error converting range to ID: ", err)
			}
			ingredient_range.From_id = from_id_int
			ingredient_range.To_id = to_id_int
			ingredient_ranges = append(ingredient_ranges, ingredient_range)
		}
	}

	// Sort the list of ranges by From_id
	sort.SliceStable(ingredient_ranges, func(i, j int) bool {
		return ingredient_ranges[i].From_id < ingredient_ranges[j].From_id
	})
	// fmt.Println("Sorted list of ranges:\n", ingredient_ranges)

	var merged_ranges []struct { // merged version of the ranges
		From_id int
		To_id   int
	}

	for i, ingredient_range := range ingredient_ranges {
		if i == 0 {
			merged_ranges = append(merged_ranges, ingredient_range) // add first id_range to merged_ranges
		} else {
			// check if id_range overlaps with last range in the merged_ranges array
			merged_ingredient_range := merged_ranges[len(merged_ranges)-1]
			if ingredient_range.From_id <= merged_ingredient_range.To_id { // range overlaps previous range
				// merge the ranges - update final range in merged_ranges
				ingredient_range.From_id = merged_ingredient_range.From_id
				ingredient_range.To_id = max(ingredient_range.To_id, merged_ingredient_range.To_id)
				merged_ranges[len(merged_ranges)-1] = ingredient_range
			} else { // ranges does not overlap with previous range - append this range
				merged_ranges = append(merged_ranges, ingredient_range)
			}
		}
	}

	// fmt.Println("Merged list of ranges:\n", merged_ranges)

	for _, ingredient_range := range merged_ranges {
		// fmt.Println("range", ingredient_range.From_id, "to", ingredient_range.To_id)
		fresh_ingredient_count += ((ingredient_range.To_id + 1) - ingredient_range.From_id) // this gives number of IDs in a non-overlapping array.
	}
	fmt.Println(fresh_ingredient_count, "fresh ingredient IDs")
}
