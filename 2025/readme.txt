2025: Using AoC to learn Go

For each day, go to the day's folder and run 
go mod init 2025/dd
create the solution.go file and run
go run .

--

Notes to self because I forget every year what I need to do to get set up:

1. Log in to https://adventofcode.com/yyyy via github
2. Get session cookie_id: right click on page, inspect, storage
3. Store cookie_id in ~/aoc_yyyy_cookie_id
4. Create folder per day: 01 .. 12 (12 days of puzzles starting from 2025)
5. Create get_input.sh file in each folder containing the following line (replace yyyy and dd as appropriate):
curl --cookie "session=$(cat ~/aoc_yyyy_cookie_id)" https://adventofcode.com/yyyy/day/dd/input > input.txt
6. On each day, run get_input.sh (just once!) to create input.txt
   (input.txt should be added to .git_ignore so it's not stored in my git repo)
7. Create an input_test.txt file containing the input given in the example solution for that day
8. Create solution_01.xx and solution_02.xx files (xx represents the programming language I'm using) 
9. Solve the day's puzzles!
