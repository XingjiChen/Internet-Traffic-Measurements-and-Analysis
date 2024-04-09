#!/bin/bash
# generate random domain, most likely 
# 1) would not exists 
# 2) nobody has ever asked for that domain
# name has about 310 bits of entropy
dom=$1
echo Asking for host: $dom
dig $dom | fgrep time:
dig $dom | fgrep time:
