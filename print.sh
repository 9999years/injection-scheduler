#!/bin/bash

export PATH="/usr/sbin:/sbin:/home/pi/.local/bin:/usr/local/bin:/usr/bin:/bin"

python3.7 injection_scheduler.py \
       | fmt -w 40 \
       | lp -o cpi=15 -o lpi=8
