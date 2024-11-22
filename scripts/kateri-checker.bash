#!/bin/bash
if ! pgrep -f "kateri" > /dev/null
then
    /home/kateri/kateri.bash
fi
