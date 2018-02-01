package main

import "fmt"

func main() {
	// bool 
	var flag bool = false
	fmt.Println("flag = ", flag)

	// int
	var i, j, k int
	i = 1
	j = 2
	k = 3
	fmt.Printf("i=%d j=%d k=%d\n", i, j, k)

	// var rune
	var r1, r2, r3 rune = 4, 5, 6
	fmt.Printf("r1=%d r2=%d r3=%d\n", r1, r2, r3)

	// var float32 & init
	var (
		f1 float32 = 2.1
		f2 float32 = 3.4
	)
	fmt.Printf("f1=%f f2=%f\n", f1, f2)

	// var string 
	var str1 string
	str1 = "leo"
	fmt.Println("Hello, ", str1)

	//:=
	str2 := "hello"
	fmt.Printf("str2 = %s \n", str2)

	///////////////////////////
	// pointer
	var intPointer *int
	var ii int = 100
	intPointer = &ii

	fmt.Println("value of ii [%d] address is [%x] \n", ii, &ii)
	fmt.Println("value of intPointer = ", intPointer)
	fmt.Println("value of var pointer to = ", *intPointer)

	/////////////////////////
	// array

	var intarr1 = [6]int{1,2,3,4,5,6}
	fmt.Println("intarr1 = ", intarr1)

	var strarr1 = []string{"this", "is", "a", "test"}
	fmt.Println("strarr1 = ", strarr1)

	////////////////////////
	// struct
	type person struct {
		id	int
		name	string
		country	string
	}
	
	//
	var leo person
	leo.id = 001
	leo.name = "leo"
	leo.country = "china"

	fmt.Println("leo=", leo)

	michael := person{1001, "michael", "PRC"}
	fmt.Println("michael=", michael)

}






