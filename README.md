Musical ear trainer

How to run project:
1) Check that you have python(3.8+) and poetry(1.4.2+)
2) Install Postgresql and create database   
3) Create venv by following command:```poetry update```
4) Create django migrations: ```poetry run python manage.py makemigrations```
5) Apply migrations: ```poetry run python manage.py migrate```
6) Copy ```config.json.example -> config.json``` and fill fields by your data
7) Create superuser for django admin: ```poetry run python manage.py createsuperuser```
8) Run project: ```poetry run python manage.py runserver```
9) Go to ```http://127.0.0.1:8000/admin/``` and use credentials of your superuser
10) Create tasks and exercises in admin panel
11) Enjoy!

   
