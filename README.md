# gregoirelayet.com

All rights reserved

My personal website V2

### 🏆 Goal

#### 👨‍💻 As a developper:

-   Dimple to host
-   Don't break easily
-   Fast to add feature
-   Beautiful and usable code

#### 🌐 As a user:

-   Simple to use as user and admin
-   Fast to load
-   Beautiful design

### Things used :

-   Django, Wagtail and PostgreSQL : rock solid stack and DB
-   HTMX for SPA-like fealing in page transition and infinite scroll capabilities
-   django-components and BEM css methodology for easy reusable component and styling
-   django-compress for single file css in production
-   automated script for easy life
-   automated tests for stress free development (WIP)

## Dev setup

create secrets files:

-   secrets/db_root_user_password
-   secrets/db_user_password
-   src/config/secrets/secret.txt

Launch db

```sh
docker compose up -d
```

Create Python env and install requirements.txt

Setup db (using the new Python env)

```sh
python setup_db.py
```

Migrate db

```sh
just migrate
```

Create super user

```sh
just createsuperuser
```

Start dev server

```sh
just dev
```

## Stack

Python 3.12.1  
Django 5.0  
Postgresql  
HTMX

## Legals

rx7 image : https://unsplash.com/fr/photos/porsche-911-blanche-garee-sur-un-terrain-dherbe-verte-K0mf6Hd3Ehc
