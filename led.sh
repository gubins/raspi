#!/bin/bash
source gpio
gpio mode 0 out
gpio mode 2 out
while true; do
gpio write 0 1
gpio write 2 0
sleep 0.5
gpio write 0 0
gpio write 2 1
sleep 0.5
done


