install:
	poetry install

start:
	python manage.py runserver

genmigrate:
	python manage.py makemigrations

migrate:
	python manage.py migrate

trans:
	django-admin makemessages -l ru

transsave:
	django-admin compilemessages

shell:
	python manage.py shell_plus --print-sql