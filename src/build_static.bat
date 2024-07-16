pipenv shell
python manage.py collectstatic --noinput -c --settings config.settings.build
python manage.py collectstatic --noinput -c --settings config.settings.whitenoise
python manage.py runserver --settings config.settings.dev
