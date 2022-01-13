#!/usr/bin/env bash

COMMAND=$(cat nmap.txt | fzf)

$COMMAND 192.168.1.1