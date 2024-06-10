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


makefixtures:
  #!/usr/bin/env bash
  declare -a apps=(website project);
  cd src;
  for app in "${apps[@]}"; do
    mkdir -p apps/${app}/fixtures; python manage.py dumpdata --indent 2 -o apps/${app}/fixtures/${app}.json ${app};
  done