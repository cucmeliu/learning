package main

import (
    "fmt"
    "math"
)

func add(x int, y int) int {
    return x + y
}

func main() {
    defer fmt.Println("hello world")
	fmt.Println(math.Pi)
	fmt.Println(add(42, 13))
}