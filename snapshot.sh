#!/usr/bin/bash

if [ -z "$1" ]; then
  echo "Missing required world name"
  exit -1
fi 

SNAPSHOT_DIR="/opt/minecraft/snapshot"
WORLD="${1}"
tar --create --verbose --gzip --listed-incremental="${SNAPSHOT_DIR}/${WORLD}_incremental.snar" --file="${SNAPSHOT_DIR}/${WORLD}_$(date +%m%d%Y%H%M%S).tar.gz" "/opt/minecraft/${WORLD}"
