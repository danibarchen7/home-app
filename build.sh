#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input
python manage.py makemigrations  Customer  chat 
python manage.py migrate Customer Chat  
python manage.py makemigrations Favorites Images
python manage.py migrate Favorites Images
python manage.py makemigrations Property  Type
python manage.py migrate Property  Type
# Apply any outstanding database migrations
python manage.py migrate
