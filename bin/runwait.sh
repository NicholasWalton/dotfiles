#!/bin/bash

while true; do
  $@
  inotifywait -e modify -e move -e create -e delete -r `pwd`
  sleep 1
done
