#!/bin/bash
if [ "$(id -u)" != "0" ]; then
    echo "You must run this as root, try sudo !!"
    exit 1
fi
pfctl -f $1
pfctl -e

echo "Please verify the following rules are correct"
pfctl -sn
