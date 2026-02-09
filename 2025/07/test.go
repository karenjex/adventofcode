package main

// Testing tree traversal methods

import "fmt"

type splitter_node struct { // Each splitter is a node in the tree
	node_id     int            // ID of the node
	node_coords [2]int         // coords of the node
	left_node   *splitter_node // ID of next node/splitter to the left
	right_node  *splitter_node // ID of next node/splitter to the right
}

// InOrderTraversal performs an in-order traversal of the binary tree starting from the root.
func InOrderTraversal(root *splitter_node) int {
	if root == nil { // we've traversed this branch - stop here
		return 1
	}

	var result int
	left := InOrderTraversal(root.left_node)
	right := InOrderTraversal(root.right_node)

	result += left
	result += right

	return result
}

func main() {

	// follow process used in solution_01 to get the tree - the splitters that the beam can hit.
	// use tree traversal to get the number of different paths from root to leaf, i.e. from line 0 to final line of input.

	// but first - practice with tree traversal algorithms.

	var splitter_tree []splitter_node

	node5 := splitter_node{node_id: 5, node_coords: [2]int{9, 7}}
	node4 := splitter_node{node_id: 4, node_coords: [2]int{7, 7}}
	node3 := splitter_node{node_id: 3, node_coords: [2]int{5, 7}}
	node2 := splitter_node{node_id: 2, node_coords: [2]int{8, 5}, left_node: *splitter_node{node4}, right_node: *splitter_node{node5}}
	node1 := splitter_node{node_id: 1, node_coords: [2]int{6, 5}, left_node: *splitter_node{node3}, right_node: *splitter_node{node4}}
	node0 := splitter_node{node_id: 0, node_coords: [2]int{7, 0}, left_node: *splitter_node{node1}, right_node: *splitter_node{node2}}

	splitter_tree = append(splitter_tree, node0)
	splitter_tree = append(splitter_tree, node1)
	splitter_tree = append(splitter_tree, node2)
	splitter_tree = append(splitter_tree, node3)
	splitter_tree = append(splitter_tree, node4)
	splitter_tree = append(splitter_tree, node5)

	fmt.Println(splitter_tree)

	traversalResult := InOrderTraversal(splitter_tree)

	for _, val := range traversalResult {
		fmt.Print(val, " ")
	}
	// Output: 1 3 2
}
