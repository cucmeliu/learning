#!/bin/sh

#  -b: block file
#  -c: character file
#  -d: directory
#  -f: is common file
#  -g: is SGID set
#  -k, -p, -u
#  -r: read access
#  -w: write access
#  -x: x access
#  -s: empty file
#  -e: exists

file="/var/www/abc.sh"

if [ -r $file ]
then
	echo "File has read access"
else
	echo "File does not have read acces"
fi
