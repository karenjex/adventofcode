package main

import ( "fmt" 
         "log"
         "bufio"
         "os"
)

/* 
Goal: Find number of rolls that can be accessed, i.e. that have fewer than 4 rolls in the 8 adjacent spaces.
Solution for test input: 13
*/

func num_accessible(row_len int, row_data string, row_above_data string, row_below_data string) int{
    // check each roll in given row and calculate number of accessible rolls for the entire row
    num_accessible := 0

    for i := 0; i < row_len; i++ { // Check each position in the row
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
            if i != row_len-1 {
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
            if num_rolls < 4 { num_accessible +=1 } // increment num_accessible if there are fewer than 4 rolls around it.
        }
    }
    return num_accessible
}

func main() {
    total_accessible := 0
    num_lines := 0

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
    row_length := len(map_lines[0])

    for y := 0; y < map_line_count; y++ {

        map_line := map_lines[y]   // get current line
        line_above := ""
        line_below := ""

        if y != 0 { line_above = map_lines[y-1] }               // get line above if it exists
        if y != map_line_count-1 { line_below = map_lines[y+1] } // get line below if it exists
        // fmt.Println("Line ",y)
        // fmt.Println("Line = ", map_line)
        // fmt.Println("Line above = ", line_above)
        // fmt.Println("Line below = " , line_below)
        total_accessible += num_accessible(row_length, map_line, line_above, line_below)
    }

    fmt.Println(total_accessible)
}