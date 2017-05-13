#!/bin/bash
a=10
echo -e "Value of a is $a \n"

#command replace
DATE=`date`
echo "Date is $DATE"

USERS=`who | wc -l`
echo "Logged in users are $USERS"

UP=`date; uptime`
echo "Uptime is $UP"

