# gregoirelayet.com

All rights reserved

My personal website V2

Goal : simple, reliable, fast, beautiful

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
