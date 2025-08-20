#!/usr/bin/env bash

set -0 errexit


pip install -r requirements.txt


python manage.py cllectstatic --n0-input


python manage.py migrate