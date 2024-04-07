from django.shortcuts import render


def index(request):
    if request.htmx:
        base_template = "partial.html"
    else:
        base_template = "base.html"
    return render(request, "website/home.html", {"base_template": base_template})


def projects(request):
    if request.htmx:
        base_template = "partial.html"
    else:
        base_template = "base.html"
    return render(request, "website/projects.html", {"base_template": base_template})
