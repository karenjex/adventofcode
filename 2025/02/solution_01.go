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

   An ID is invalid if it is made only of some sequence of digits repeated twice.
*/

func is_valid_id(val_to_check int64) bool {
    // determine whether or not given ID is valid, i.e. is not a repeated pattern.
    // takes in integer version of ID
    is_valid := true                             // Start by aassuming this is a valid ID.

    val_to_check_str := strconv.FormatInt(val_to_check, 10) // get str format of ID. Using FormatInt to deal with int64 values
    // val_to_check_str := strconv.Itoa(val_to_check)  // get str format of ID. Not using Itoa because this doesn't cope with int64
    l := len(val_to_check_str)
    if l%2==0 {               // only check length is an even number.
        val_1 := val_to_check_str[0:l/2]       // get first half of ID
        val_2 := val_to_check_str[l/2:l]       // get second half of ID
        if val_2 == val_1 {            // 2 halves are same
            is_valid = false }
    }
    return is_valid
}

func main() {

    var invalid_id_total int64 = 0

    // read input file
    input_data, err := ioutil.ReadFile("input.txt")
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
