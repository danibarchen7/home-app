#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input
python manage.py makemigrations  Customer  
python manage.py migrate Customer 
python manage.py makemigrations chat
python manage.py migrate chat
python manage.py makemigrations Favorites 
python manage.py migrate Favorites 
python manage.py makemigrations Images
python manage.py migrate Images
python manage.py makemigrations Property  
python manage.py migrate Property
python manage.py makemigrations Type
python manage.py migrate Property  Type
# Apply any outstanding database migrations
python manage.py migrate
