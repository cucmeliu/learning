package main

import "fmt"
import "net/http"

func Hello(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "Hello, Welcome to go web programing..")
}

func main() {
	http.HandleFunc("/", Hello)
	http.ListenAndServe(":8080", nil)
}
