#!/bin/sh
curl -L "https://raw.githubusercontent.com/thehumit/py_scripts/master/partitioner.py" > partitioner.py
python3 partitioner.py
rm -rf partitioner.py
