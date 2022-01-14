#!/usr/bin/env bash

echo "Example: sudo bash nmap.sh 192.168.1.1"

COMMAND=$(cat nmap.txt | fzf)

$COMMAND 192.168.1.1