#!/bin/sh

# =,  !=
# -z: string length is zero
# -n: string length is not zero
# str: whether the str is empty

a="abc"
b="efg"

if [ $a = $b ]
then
	echo "$a = $b: a is equal to b"
else
	echo "$a = $b: a is not equal to b"
fi

if [ $a ]
then 
	echo "$a: string is not empty"
else
	echo "$a: string is empty"
fi

