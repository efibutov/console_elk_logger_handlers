#!/bin/sh
deactivate
rm -rf ./venv
python3 -m venv venv
source ./venv/bin/activate
which python
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip freeze > requirements.txt
