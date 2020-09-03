#!/usr/bin/bash

cd /home/minecraft/google_drive
export GOPATH=/home/minecraft/go
/home/minecraft/go/bin/drive push --no-prompt
/home/minecraft/go/bin/drive emptytrash --no-prompt
