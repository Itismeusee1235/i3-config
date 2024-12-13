#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use 
polybar-msg cmd quit
# Otherwise you can use the nuclear option:
# killall -q polybar

CONFIG="$HOME/.config/i3/polybar/config.ini"

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar.log
polybar -c $CONFIG bar 2>&1 | tee -a /tmp/polybar1.log & disown

echo "Bars launched..."