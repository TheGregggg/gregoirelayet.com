set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

default:
  just --list

#cd src; uvicorn --reload config.asgi_dev:app 
dev:
  cd src; python manage.py runserver