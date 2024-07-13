set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

default:
  just --list

#cd src; uvicorn --reload config.asgi_dev:app 
dev:
  cd src; pipenv run python manage.py runserver

migrate:
  cd src; pipenv run python manage.py migrate

makemigrations:
  cd src; pipenv run python manage.py makemigrations

createsuperuser:
  cd src; pipenv run python manage.py createsuperuser

makefixtures:
  #!/usr/bin/env bash
  declare -a apps=(website project blog);
  cd src;
  for app in "${apps[@]}"; do
    mkdir -p apps/${app}/fixtures; pipenv run python manage.py dumpdata --natural-foreign --natural-primary --indent 2 -o apps/${app}/fixtures/${app}.json ${app};
  done
  mkdir -p fixtures; 
  pipenv run python manage.py dumpdata --natural-foreign --natural-primary --indent 2 -o fixtures/base.json -a -e website -e blog -e project -e auth -e wagtailcore.pagelogentry -e contenttypes -e sessions -e wagtailcore.modellogentry -e wagtailcore.groupcollectionpermission -e wagtailcore.grouppagepermission;

loaddata:
  #!/usr/bin/env bash
  declare -a apps=(website project);
  cd src;
  pipenv run python manage.py loaddata fixtures/base.json;
  for app in "${apps[@]}"; do
    pipenv run python manage.py loaddata apps/${app}/fixtures/${app}.json;
  done

test:
  cd src; pipenv run python manage.py test --keepdb --settings=config.settings.dev