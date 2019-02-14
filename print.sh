#!/bin/bash

python3.7 injection_scheduler.py \
       | fmt -w 40 \
       | lp -o cpi=15 -o lpi=8
