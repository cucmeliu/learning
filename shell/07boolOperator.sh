#!/bin/sh

# !  -a -o
a=10
b=20

if [ $a != $b ]
then
	echo "$a != $b: a is not equal to b"
else
	echo "$a != $b: a is equal to b"
fi

if [ $a -lt 100 -a $b -gt 15 ]
then
	echo "$a -lt 100 -a $b -gt 15: return true"
else
	echo "$a -lt 100 -a $b -gt 15: return false"
fi


# -a   -o   
