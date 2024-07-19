#!/bin/sh -l

echo "Auth to DO registry"
doctl auth init -t $1

if [ $? -eq 1 ]; then
  echo "Authentication fail, Please check your token"
fi

echo "Start garbage collection cleaning"
doctl registry garbage-collection start $2 -f --include-untagged-manifests