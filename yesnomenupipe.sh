#!/bin/bash
#the first CLi argument is the question that will be asked
#the second CLI argument is the command that will be executed after saying yes
selected=$(echo "yes
no" | rofi -dmenu -p "$1")


if [ $selected = yes  ]; then
	$2 | $3
else
	echo "he didnt accept :("
fi

