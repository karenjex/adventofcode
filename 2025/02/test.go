package main

import ( "fmt" 
)

func main() {
    test_string := "123123"
    l := len(test_string)
    val_1 := test_string[0:l/2] //first half of string
    val_2 := test_string[l/2:l] //second half of string

    fmt.Println(test_string, len(test_string), val_1, val_2)
}
