#!/bin/bash

ewwDir=/home/fenrir/External\ Repos/eww/target/release/eww


pkill eww
"$ewwDir" daemon --config /home/fenrir/.config/i3/eww/
"$ewwDir" open $1 --config /home/fenrir/.config/i3/eww/



