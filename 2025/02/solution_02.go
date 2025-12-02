package main

import ( "fmt" 
         "strconv"
         "log"
         "io/ioutil"
         "strings"
)

/* Goal: Find the total of all invalid IDs.
   The input contains a list of ranges, separated by commas.
   Each range gives its first ID and last ID separated by a dash (-).

   This time, an ID is invalid if it is made only of some sequence of digits repeated at least twice.

*/

func is_valid_id(val_to_check int64) bool {
    // determine whether or not given ID is valid, i.e. is not a repeated pattern.
    // takes in integer version of ID
    is_valid := true                    // Start by assuming this is a valid ID.

    val_to_check_str := strconv.FormatInt(val_to_check, 10) // get str format of ID. Using FormatInt to deal with int64 values

    l := len(val_to_check_str)

    // An invalid ID of length l could contain up to l repeated sequences of digits
    for r := 2; r <= l; r++ {   // start by looking for 2 repetitions, continue up to l repetitions
        looks_invalid := true       // Start by assuming this is not going to be valid, i.e. we will find only matching slices
        if l%r==0 {     // only check ID if length is divisible by number of repetitions
            // split string into r slices and compare them. As soon as we find one that doesn't match, we can stop.
            slice_1 := val_to_check_str[0:l/r]      // get first slice of ID
            for s := 2; s <= r; s++ { // compare remaining slices against slice_1. Continue until there's a slice that doesn't match.
                slice_s := val_to_check_str[ ((s-1)*l)/r : (s*l)/r ] //get slice s

                if slice_s != slice_1 { // stop here - we have not yet found this ID to be invalid. Move to next number of repetitions.
                    looks_invalid = false
                    break
                }
            }
            if looks_invalid {   // all r slices matched, so this is an invalid ID. No need to check for more repetitions. 
               is_valid = false
               break
           }
       }
    }
    return is_valid
}

func main() {

    var invalid_id_total int64 = 0

    // read input file
    input_data, err := ioutil.ReadFile("input_test.txt")
    if err != nil {
        log.Fatalf("failed to read file: %s", err)
    }

    // split the file content by comma to get list of ranges
    inputs := strings.Split(string(input_data),",")

    // check each value in each input range and add any invalid IDs to the running total
    for _, input := range inputs {

        // remove trailing whitespace from input
        input = strings.TrimSpace(input)


        start_val := strings.SplitN(input,"-", 2)[0]  // split the input on "-" to get the 2 values
        end_val := strings.SplitN(input,"-", 2)[1]
        
        var start_val_num int64
        var end_val_num int64

        // note: using ParseInt to specify int64 because Atoi won't process large enough numbers

        if s, err := strconv.ParseInt(start_val, 10, 64); err != nil { 
            fmt.Println("Problem converting ",start_val)
            panic(err) 
        } else { start_val_num = s }
        if e, err := strconv.ParseInt(end_val, 10, 64); err != nil { 
            fmt.Println("Problem converting ",end_val) 
            panic(err) 
        } else { end_val_num = e }
        fmt.Println("Processing range ",start_val," to ",end_val)
        for v := start_val_num; v < end_val_num+1; v++ {
            if v == start_val_num {
                fmt.Println("Processing range starting with ",start_val_num)
            }
            if !(is_valid_id(v)) { 
                invalid_id_total += v
//                fmt.Println("Invalid ID found: ",v) 
            } else {
//                fmt.Println("ID is valid: ",v) 
            }
	}
    }
    fmt.Println(invalid_id_total)
}
