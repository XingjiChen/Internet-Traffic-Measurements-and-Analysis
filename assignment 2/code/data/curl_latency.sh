#!/bin/bash
dom=$1
export LANG=C
fmt="%{time_namelookup}, %{time_connect}, %{time_starttransfer}, %{time_total}\n"
curl -w "$fmt" -o /dev/null -T ./1K.bin -s $dom
