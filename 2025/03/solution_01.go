package main

import ( "fmt" 
         "log"
         "strings"
         "bufio"
         "os"
         "strconv"
)

/* Goal: 

Each line of digits in the input is a bank of batteries, each labeled with its joltage rating (val from 1 to 9). 

The joltage produced by a bank is equal to the number formed by the digits on the *two* batteries you've turned on.
e.g. if you turn on batteries 2 and 4 in the bank 12345, bank would produce 24 jolts. 

Find the maximum joltage possible from each bank and return the total output joltage.

Solution for test input: 98 + 89 + 78 + 92 = 357.

*/

func max_joltage(batterybank string) int{

    // calculate max joltage for a given bank of batteries.

    // fmt.Println("Processing battery bank ",batterybank)

    max_joltage_val := 0
    l := len(batterybank)   //get number of batteries in bank

    // Find the first battery to turn on:
    // Find largest value battery, excluding the battery in last position (this can only be the 2nd battery).

    max_val := 0      // Max value found so far
    num_max := 0      // Number of occurences of current max value
    max_val_pos := 0  // Position of first occurence of the max value found so far

    for i := 0; i < l-1; i++ {
        battery_val_str := string(batterybank[i])
        if battery_val, err := strconv.Atoi(battery_val_str); err != nil {
            fmt.Println(err)
            log.Fatalf("Error converting battery value: ", err)
        } else if battery_val > max_val {  // We found a new max value. Reset the counter to 1 and record the position.
          max_val = battery_val
          num_max = 1
          max_val_pos = i
        } else if battery_val == max_val {
          num_max +=1
        }
    }
    fmt.Println("  Highest value found for 1st battery: ",max_val)

    // Switch on (1st if more than one) battery with the highest value:
    max_joltage_val = 10 * max_val

    final_val_str := string(batterybank[l-1])
    if final_val, err := strconv.Atoi(final_val_str); err != nil {
        fmt.Println(err)
        log.Fatalf("Error converting final battery value: ", err)
    } else {
        fmt.Println("  Value of battery in final position: ",final_val)

        if num_max > 1 {      // There's more than one battery with this value. 
            // if battery in final position has higher value, switch on final battery
            if final_val > max_val {
                max_joltage_val += final_val
            } else {    // switch on 2nd battery with same value as 1st
                max_joltage_val += max_val
            }
        } else {              // There's only one battery with this value. Find the 2nd battery to switch on.
            max_val = 0       // reset max_val
            // Start from the position to the right of the highest value battery and find the highest value to the right of it.
            for i := max_val_pos+1; i < l; i++ {
                battery_val_str := string(batterybank[i])
                if battery_val, err := strconv.Atoi(battery_val_str); err != nil {
                    fmt.Println(err)
                    log.Fatalf("Error converting battery value: ", err)
                } else if battery_val > max_val {  // We found a new max value.
                max_val = battery_val
                }
            }
            fmt.Println("  Highest value found for 2nd battery: ",max_val)
            max_joltage_val += max_val
        }
    }
    fmt.Println("  Max joltage for this battery bank: ",max_joltage_val)
    return max_joltage_val
}

func main() {

    total_joltage := 0


    // open the input file
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatalf("failed to open file: %s", err)
    }
    defer file.Close()

    // create a scanner to read the input file line by line
    scanner := bufio.NewScanner(file)

    // loop through input file
    for scanner.Scan() {
        batterybank := strings.TrimSpace(scanner.Text()) // get the line as a string and remove trailing whitespace
        total_joltage += max_joltage(batterybank)
    }
    fmt.Println(total_joltage)
}
