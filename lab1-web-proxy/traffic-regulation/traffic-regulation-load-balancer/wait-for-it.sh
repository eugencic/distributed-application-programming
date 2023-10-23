#!/bin/bash
# wait-for-it.sh
# Waits for multiple services to be available before continuing.

for service in "$@"; do
  host_port=(${service//:/ })
  host=${host_port[0]}
  port=${host_port[1]}
  
  echo "Waiting for $host:$port to be available..."
  
  while ! nc -z "$host" "$port"; do
    sleep 1
  done
  
  echo "$host:$port is available!"
done

echo "All services are available."
