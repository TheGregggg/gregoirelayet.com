set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

default:
  just --list

#cd src; uvicorn --reload config.asgi_dev:app 
dev:
  cd src; python manage.py runserver

migrate:
  cd src; python manage.py migrate

makemigrations:
  cd src; python manage.py makemigrations

createsuperuser:
  cd src; python manage.py createsuperuser

makefixtures:
  #!/usr/bin/env bash
  declare -a apps=(website project);
  cd src;
  for app in "${apps[@]}"; do
    mkdir -p apps/${app}/fixtures; python manage.py dumpdata --natural-foreign --indent 2 -o apps/${app}/fixtures/${app}.json ${app};
  done
  mkdir -p fixtures; 
  python manage.py dumpdata --natural-foreign --indent 2 -o fixtures/base.json -a -e website -e project -e auth -e wagtailcore.pagelogentry -e contenttypes -e sessions -e wagtailcore.modellogentry -e wagtailcore.groupcollectionpermission -e wagtailcore.grouppagepermission;

loaddata:
  #!/usr/bin/env bash
  declare -a apps=(website project);
  cd src;
  python manage.py loaddata fixtures/base.json;
  for app in "${apps[@]}"; do
    python manage.py loaddata apps/${app}/fixtures/${app}.json;
  done

test:
  cd src; python manage.py test --keepdb --settings=config.settings.dev