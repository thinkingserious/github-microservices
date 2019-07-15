#!/bin/sh

/usr/local/bin/gunicorn -w 2 -b :5000 app:app
