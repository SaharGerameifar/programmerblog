# programmerblog

This project is an advanced news website.
Backend this project is written with Django and the template is made with Bootstrap, JavaScript, etc.
The user model in this project is completely personalized and users have different access levels after registering and receiving the activation email, and logging in to the site. The average user only reads regular articles. Special user who can read special articles by purchasing a special subscription package. Author user who generates or edits articles in his admin panel. Admin user who can be both an author and edit, delete or publish articles by other authors.

===========================================================

# Installation guide:
create virtualenv and activate

pip install -r requirements.txt

cp .env-sample .env

python manage.py runserver
