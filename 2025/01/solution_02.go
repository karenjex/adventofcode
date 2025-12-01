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
//        Then, the rotation has a distance pointer_pos which indicates how many clicks the dial should be rotated in that direction.
// Test input result: 6

func rotate(current_pos int, dist int, dir byte) (int, int) {
    // take in current position, distance, and direction to rotate.

    // calculate new position and number of times we went past (or to) zero.
    new_pos := current_pos
    full_circuits := dist/100 // Integer division truncates result and therefore gives number of full circuits.
    times_past_zero := full_circuits  // We will pass (or land on) zero for each full circuit.
    final_circuit := dist%100 // Remainder gives number of positions to move into final position.
    if dir == 'R' { // move final_circuit positions clockwise, i.e. add to current_pos
        new_pos = (current_pos + final_circuit)%100
        if new_pos < current_pos { // we went past (or landed on) zero during the final part circuit
            times_past_zero += 1
        }
    } else if dir == 'L' { 
        new_pos = (current_pos + (100 - final_circuit))%100 
        if (new_pos > current_pos) && (current_pos != 0) { // we went past zero during the final part circuit
            times_past_zero += 1
        } else if new_pos == 0 {
            times_past_zero += 1
        } 
    }
    fmt.Println("Start position: ", current_pos, ", Direction: ",dir, ", Number of positions rotated: ",dist ,", Number of times past zero: ",times_past_zero)
    return new_pos, times_past_zero
 }

func main() {

    passwd := 0
    pointer_pos := 50 // pointer starts at 0

    // open the input file
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
        times_past_zero :=0

        move := scanner.Text() // get the line as a string
        dir := move[0] // direction is 1st character of string

        // distance is integer pointer_pos of 2nd and subsequent characters of the string
        if dist, err := strconv.Atoi(move[1:]); err == nil {
            pointer_pos, times_past_zero = rotate(pointer_pos,dist,dir)
        } else {
            log.Fatalf("failed to process input")
        }
        passwd += times_past_zero      // add times_past_zero to the password
    }
    fmt.Println(pointer_pos, passwd)
}
