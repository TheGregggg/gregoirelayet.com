# gregoirelayet.com

All rights reserved

This is my personal website, to showcase my projects and talk about stuff I'm interested in.

For this projects I have many goals.
Including the followings ones : 
- As a developper:
    -   Simple to host 
    -   Don't break easily 
    -   Fast to add feature
    -   Beautiful and usable code
- As a user:
    -   Simple to use as user and admin
    -   Fast to load
    -   Beautiful design

Initialy the website was a massive Django project, witch embrace 12 factors app techniques, testings, linter tools and pre commit checkings.

But the reality is different and for this type of website, juste a simple SSG is sufficient.
Thats why I decided to switch to Zola for making the website static.
It still check all the boxes and is even more simpler.

It's more optimized in ressource usage, it weight less on my vps cpu and storage.
I can also remove the postgres container i was running just for this website.
This allow me more flexibility and more efficient usage of my VPS ressources.

I choose Zola cause it's fast, and provided all the feature I wanted. Also it use Tera as a template language witch is 99% similare to Django template, so the conversion was very fast and the site look the same.


## Actual Tech stack:
- Zola as SSG
- Caddy as webserver

### Old version tech stack :
-   Django, Wagtail and PostgreSQL : rock solid stack and DB
-   HTMX for SPA-like fealing in page transition and infinite scroll capabilities
-   django-components and BEM css methodology for easy reusable component and styling
-   django-compress for single file css in production
-   automated script for easy life
-   automated tests for stress free development (WIP)

## Dev setup
You need to have Zola installed.
For building the site for production you also need lightningcss and gzip.
build site :
```sh
cd ssg
./build_min_comp.sh
```

develop site :
```sh
cd ssg
zola serve
```

If you have nix you can just creat a nix shell in the root with the following comand: 
```sh
nix-shell
```