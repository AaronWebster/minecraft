#!/usr/bin/bash

chown -R minecraft:minecraft /opt/minecraft
find /opt/minecraft -type d -print0 | xargs -0 chmod 0775
find /opt/minecraft -type f -print0 | xargs -0 chmod 0664
find /opt/minecraft -type f -name "*.py" -print0 | xargs -0 chmod +x
find /opt/minecraft -type f -name "*.sh" -print0 | xargs -0 chmod +x

