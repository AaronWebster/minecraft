#!/usr/bin/bash

REPOSITORY=/home/minecraft/snapshots.attic

/opt/attic/attic create --stats "${REPOSITORY}"::minecraft-`date +%m%d%Y%H%M%S` /opt/minecraft
/opt/attic/attic prune -v "${REPOSITORY}" --keep-hourly=24 --keep-daily=7 --keep-weekly=4 --keep-monthly=12
