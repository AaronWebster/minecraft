#!/bin/bash
# Downloads the latest Minecraft server jar.

URL="$(wget -O - -q https://www.minecraft.net/en-us/download/server | grep "https.*server.jar" | sed -e s/.*href=\"// -e s/\".*//)"
wget -O /opt/minecraft/server.jar -q "${URL}"
