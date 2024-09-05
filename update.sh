#!/bin/bash
peyman="./CFscanners/peyman/install.sh"
if [ -e $peyman ]
then
echo "peyman exists"
source "$peyman"
else
echo "file does not exist"
echo "creating the file..".
fi
