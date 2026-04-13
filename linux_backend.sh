#!/bin/bash
source ../env-python/backend/bin/activate && cd backend && python manage.py makemigrations && python manage.py migrate
