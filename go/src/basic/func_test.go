package basicfunc

import "testing"

func TestBasic(test *testing.T) {
	grade := GetGrade(40)
	if grade != "D" {
		test.Error("test case failed.")
	}
}

func TestAddfunc(test *testing.T) {
	sum := Add(1, 1)
	if sum == 2 {
		test.Log("Passed: 1+1 == 2 ")
	} else {
		test.Log("Failed: 1+1 == 2 ")
	}
}

func BenchmarkAddfunc(bmtest *testing.B) {
	for cnt := 0; cnt < bmtest.N; cnt++ {
		Add(1, 1)
	}
}

