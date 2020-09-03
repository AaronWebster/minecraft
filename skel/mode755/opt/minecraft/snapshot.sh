#!/usr/bin/bash

REPOSITORY=/home/minecraft/snapshots.attic

/opt/attic/attic create --stats "${REPOSITORY}"::minecraft-`date +%m%d%Y%H%M%S` /opt/minecraft
/opt/attic/attic prune -v "${REPOSITORY}" --keep-hourly=24 --keep-daily=12 --keep-weekly=14 --keep-monthly=24
