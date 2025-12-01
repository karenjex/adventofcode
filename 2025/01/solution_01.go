package main

import ( "fmt" 	
         "strconv"
         "bufio"
         "os"
         "log"
)

// Goal: Find the password, i.e. the number of time the dial points at 0 after a rotation.
// Dial goes from 0 to 99 in a circle. Dial starts by pointing at 50
// Input: a sequence of rotations, one per line.
//        A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). 
//        Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
// Test input result: 3

func move_right(current_val int, dist int) int {
    return (current_val + dist)%100
}

func move_left(current_val int, dist int) int {
    return (current_val + (100 - dist))%100
 }

func main() {

    passwd := 0
    value := 50 // pointer starts at 0

    // open the input_test file
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatalf("failed to open file: %s", err)
    }
    defer file.Close()

    // create a scanner to read the input file line by line
    scanner := bufio.NewScanner(file)

    //    moves := [2]string{ "R10", "L20", }

    // loop through input file
    for scanner.Scan() {
        move := scanner.Text() // get the line as a string

        dir := move[0] // direction is 1st character of string

        // distance is integer value of 2nd and subsequent characters of the string
        if dist, err := strconv.Atoi(move[1:]); err == nil {
        if dir == 'R' { 
            value = move_right(value,dist) }
        if dir == 'L' { 
            value = move_left(value,dist) }
        }
        if value == 0 { passwd += 1 }  // increment password by 1 if the move lands the pointer on 0
    }
    fmt.Println(value, passwd)
}
