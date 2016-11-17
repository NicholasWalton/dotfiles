#!/bin/bash

sigint_handler()
{
  kill $PID
  exit
}

trap sigint_handler SIGINT

while true; do
  $@ &
  PID=$!
#  gdb -p $PID
  inotifywait -e modify -e move -e create -e delete -r `pwd`
#  kill $PID
done
