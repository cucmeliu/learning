#!/bin/sh

str='this is a string'

your_name='leo'

echo "Hello, your are \"${your_name}\"!\n"

greeting="Hello, "${your_name}"!"
greeting1="Hello, ${your_name}!"

echo $greeting $greeting1

# length of str
echo "Length of ${greeting} is: ${#greeting}"

# substr
echo "sub 1-4 of ${greeting} is: ${greeting:1:4}"

# search sub str
echo `expr index "${greeting}" leo`

