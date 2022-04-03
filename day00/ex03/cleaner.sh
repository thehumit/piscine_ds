#!/bin/sh

curl -L "https://raw.githubusercontent.com/thehumit/py_scripts/master/cleaner.py" > cleaner.py
python3 cleaner.py
rm -rf cleaner.py

