#!/bin/sh

curl -L "https://raw.githubusercontent.com/thehumit/py_scripts/master/counter.py" > counter.py
python3 counter.py
rm -rf counter.py
