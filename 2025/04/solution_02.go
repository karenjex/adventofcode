package main

import ( "fmt" 
         "log"
         "bufio"
         "os"
)

/* 
Goal: Find the total number of rolls that can be accessed and removed,
bearing in mind that once a roll has been removed, it may mean that other rolls can now be removed.
Solution for test input: 43
*/

/* 
Would be good to implement a more efficient method;
we're performing a lot of unecessary checks and repeating a lot of work.
*/

func num_removed(row_data string, row_above_data string, row_below_data string) (int, string) {
    // Check each roll in given row "row_data"
    // If roll is accessible, remove it.
    // Return number of rolls removed, along with string representing the new row

    removed_count := 0
    new_row_data := row_data

    for i := 0; i < len(row_data); i++ { // Check each position in the row
        if string(row_data[i])=="@" { // Only check for accessibility if there is a roll in this position
            num_rolls := 0
            // for each of the 8 positions around, check for a roll
            //   in row_above_data: i-1, i and i+1
            //   in row_data: i-1 and i+1
            //   in row_balow_data: i-1, i and i+1
            // Only check i-1 if we're not in the first position
            if i != 0 {
                if row_above_data!="" {
                    if string(row_above_data[i-1])=="@" { num_rolls +=1 }
                }
                if row_below_data!="" {
                    if string(row_below_data[i-1])=="@" { num_rolls +=1 }
                }
                if string(row_data[i-1])=="@" { num_rolls +=1 }
            }
            // Only check i+1 if we're not at the end of the row
            if i != len(row_data)-1 {
                if row_above_data!="" {
                    if string(row_above_data[i+1])=="@" { num_rolls +=1 }
                }
                if row_below_data!="" {
                    if string(row_below_data[i+1])=="@" { num_rolls +=1 }
                }
                if string(row_data[i+1])=="@" { num_rolls +=1 }
            }
            if row_above_data!="" {
                if string(row_above_data[i])=="@" { num_rolls +=1 }
            }
            if row_below_data!="" {
                if string(row_below_data[i])=="@" { num_rolls +=1 }
            }
            if num_rolls < 4 { // if the roll is accessible
                removed_count +=1 // increment number of rolls removed
                if i==0 {
                    new_row_data = "."+new_row_data[1:len(row_data)] // "remove" the roll
                } else if i==len(row_data)-1 {
                    new_row_data = new_row_data[0:len(row_data)-1]+"." // "remove" the roll
                } else {
                    new_row_data = new_row_data[0:i]+"."+new_row_data[i+1:len(row_data)] // "remove" the roll
                }
            } 
        }
    }
    return removed_count, new_row_data
}

func main() {
    total_removed := 0

    // Open File
    file, err := os.Open("input.txt")
    if err != nil { log.Fatalf("failed to open file: %s", err) }
    defer file.Close()

    var map_lines []string // array of strings, one string per line of the map input

    // create a scanner to read the input file line by line
    scanner := bufio.NewScanner(file)

    // Process file line by line to get map
    for scanner.Scan() {
        map_lines = append(map_lines,string(scanner.Text()))
    }

    map_line_count := len(map_lines)

// repeat the following until rows_removed == 0 :

for x := 1; x > 0 ; x=x { // keep passing through the map until we remove no rolls
        // fmt.Println("New pass through the map:")
        var new_map_lines []string  // var to store lines of map with rolls removed
        removed_this_time:=0 // rolls removed during this pass through the map
        for y := 0; y < map_line_count; y++ {

            map_line := map_lines[y]   // get current line
            line_above := ""
            line_below := ""

            if y != 0 { line_above = map_lines[y-1] }               // get line above if it exists
            if y != map_line_count-1 { line_below = map_lines[y+1] } // get line below if it exists
            // fmt.Println("  Line ",y)
            // fmt.Println("  ", map_line)
            rolls_removed, new_row := num_removed(map_line, line_above, line_below)
            new_map_lines = append(new_map_lines, new_row)
            // fmt.Println("  ",rolls_removed ," rolls removed from line")
            removed_this_time += rolls_removed
        }
        // fmt.Println(removed_this_time ," rolls removed this iteration")
        if removed_this_time==0 { 
            x = 0 
        } else { 
            total_removed += removed_this_time
            map_lines = new_map_lines // replace the old map with the new one before next iteration
        }
    }
    fmt.Println(total_removed)
}