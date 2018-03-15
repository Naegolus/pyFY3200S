#!/bin/sh

if [ ! -z "$1" ]; then
	dev=$1
else
	dev=/dev/ttyUSB0
fi

stty -F "$dev" 57600

echo ":r0c" > ${dev}
#cat -v < ${dev}
