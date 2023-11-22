#!/bin/bash

#python3 ~/Desktop/UDS/tp.py

while [ true ] 
do
  #python3 ~/Desktop/UDS/tp_clear.py 
  #python3 ~/Desktop/UDS/tp_reset.py 
  echo "11 01" | isotpsend -p 00 -s 49a -d 49b can0
  echo "11 02" | isotpsend -p 00 -s 49a -d 49b can0
  echo "11 03" | isotpsend -p 00 -s 49a -d 49b can0
  echo "11 04" | isotpsend -p 00 -s 49a -d 49b can0
  sleep 0.5
done
