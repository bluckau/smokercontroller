#!/bin/bash


cd `dirname $0`/..

python manage.py runserver 0:80
