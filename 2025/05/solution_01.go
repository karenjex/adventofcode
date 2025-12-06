package main

import ( "fmt" 
         "log"
         "bufio"
         "os"
         "strings"
         "strconv"
)

/* 
Goal: Find the number of fresh ingredients.
The input consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. 
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. 
The ranges can also overlap; an ingredient ID is fresh if it is in any range.

Solution for test input: 3
*/

func main() {
    fresh_ingredient_count := 0
    var fresh_ranges []string
    var ingredients []int

    // Open File
    file, err := os.Open("input.txt")
    if err != nil { log.Fatalf("failed to open file: %s", err) }
    defer file.Close()

    // create a scanner to read the input file line by line
    scanner := bufio.NewScanner(file)

    // Process file line by line to get ranges and ingredients
    collect_ranges := true // start by collecting the ranges
    for scanner.Scan() {
        input_line := string(scanner.Text())
        if input_line == "" { // we've reached the end of the ranges list. Start collecting ingredients.
            collect_ranges = false
        } else if collect_ranges {
            fresh_ranges = append(fresh_ranges,input_line)
        } else { // this is an ingredient.
            if ingredient, err := strconv.Atoi(input_line); err != nil {
                fmt.Println(err)
                log.Fatalf("Error converting ingredient ID: ", err)
            } else { 
                ingredients = append(ingredients,ingredient) 
            }
        }
    }

    for _,ingredient := range ingredients {
        fmt.Println("Checking ingredient ",ingredient)
        is_fresh := false
        for _,fresh_range := range fresh_ranges {

            range_from_id := strings.SplitN(fresh_range,"-", 2)[0]  // split the input on "-" to get the 2 values
            range_to_id := strings.SplitN(fresh_range,"-", 2)[1]  // split the input on "-" to get the 2 values

            range_from_int, err := strconv.Atoi(range_from_id)
            if err != nil { 
                fmt.Println(err)
                log.Fatalf("Error converting range from ID: ", err)
            }

            range_to_int, err := strconv.Atoi(range_to_id)            
            if err != nil {
                fmt.Println(err)
                log.Fatalf("Error converting range to ID: ", err)
            }

            fmt.Println("Checking range",range_from_int, "to", range_to_int)

            if (ingredient >= range_from_int) && (ingredient <= range_to_int) { // ingredient is fresh
                is_fresh = true
                break
            }
        }
        if is_fresh { 
            fmt.Println(ingredient, " is fresh")
            fresh_ingredient_count +=1 
        }
    }
    fmt.Println(fresh_ingredient_count, "fresh ingredients")
}