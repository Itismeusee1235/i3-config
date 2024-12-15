#!/bin/bash

pkill eww
eww daemon --config /home/fenrir/.config/i3/eww/eww-bar &
eww open $1 --config /home/fenrir/.config/i3/eww/ --debug



