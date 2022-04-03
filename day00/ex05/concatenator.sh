#!/bin/sh

curl -L "https://raw.githubusercontent.com/thehumit/py_scripts/master/concatenator.py" > concatenator.py
python3 concatenator.py
rm -rf concatenator.py
