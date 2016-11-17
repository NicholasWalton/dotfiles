#!/bin/bash

sigint_handler()
{
  kill $PID
  exit
}

sigchild_handler()
{
  kill $!
}

trap sigint_handler SIGINT

trap sigchld_handler SIGCHLD

while true; do
  $@ </dev/stdin >/dev/stdout &
  PID=$!
#  gdb -p $PID
  inotifywait -e move_self -e close_write -e attrib -e delete_self $1
  kill $PID
  sleep 1
done
