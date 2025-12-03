package main

import ( "fmt" 
         "log"
         "strings"
         "bufio"
         "os"
         "strconv"
         "math"
)

/* Goal: 
Each line of digits in the input is a bank of batteries, each labeled with its joltage rating (val from 1 to 9). 
This time, the joltage produced by a bank is equal to the number formed by the digits on the *twelve* batteries you've turned on.
Find the maximum joltage possible from each bank and return the total output joltage.

Solution for test input: 
987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
*/

func max_joltage(batterybank string) int{
    // Calculate max joltage for a given bank of batteries.
    // Could make this more efficient - don't actually need to keep re-checking vals that have already been checked.

    max_joltage_val := 0
    l := len(batterybank)   //get number of batteries in bank
    current_pos := 0        // Position to check from (0 for first battery, position to rhs of previous battery for subsequent batteries)

    // Find each of the 12 batteries to switch on
    for x := 1; x <= 12; x++ { 

        max_val := 0      // Max value found so far
        max_val_pos := 0  // Position of first occurence of the max value found so far

        // Find largest battery from current_pos up to to battery in position (l-1)-(12-x)
        for i := current_pos; i < l-(12-x); i++ {
            battery_val_str := string(batterybank[i])
            if battery_val, err := strconv.Atoi(battery_val_str); err != nil {
                fmt.Println(err)
                log.Fatalf("Error converting battery value: ", err)
            } else if battery_val > max_val {  // We found a new max value. Record its value and position.
            max_val = battery_val
            max_val_pos = i
            }
        }
        fmt.Println("  Highest value found for ",x,"th battery: ",max_val)

        // Switch on (1st if more than one) battery with the highest value:
        max_joltage_val += (int(math.Pow10(12-x)) * max_val)
        current_pos = max_val_pos+1 // Check from this position for next battery
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